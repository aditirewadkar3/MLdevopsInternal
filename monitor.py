
import pandas as pd
from evidently import Dataset, DataDefinition, Report
from evidently.presets import DataDriftPreset

# Reference data: the baseline
reference_df = pd.DataFrame({
    "age": [22, 25, 28, 30, 32, 35],
    "income": [20000, 25000, 28000, 30000, 32000, 35000]
})

# Current data: the incoming data
current_df = pd.DataFrame({
    "age": [40, 42, 45, 48, 50, 55],
    "income": [50000, 52000, 55000, 58000, 60000, 65000]
})

schema = DataDefinition(
    numerical_columns=["age", "income"]
)

reference = Dataset.from_pandas(
    reference_df,
    data_definition=schema
)

current = Dataset.from_pandas(
    current_df,
    data_definition=schema
)

report = Report([
    DataDriftPreset()
])

result = report.run(current, reference)
result.save_html("evidently_report.html")

print("Monitoring completed.")
print("Report saved as evidently_report.html")
