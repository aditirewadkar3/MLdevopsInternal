
from sklearn import datasets
from evidently import Report
from evidently.presets import DataDriftPreset

# Load the built-in Iris dataset
iris = datasets.load_iris(as_frame=True)
iris_df = iris.frame

print("Iris dataset loaded successfully")
print("Dataset shape:", iris_df.shape)
print(iris_df.head())

# Reference data and current data
reference_data = iris_df.iloc[60:120].copy()
current_data = iris_df.iloc[:60].copy()

# Generate a data drift report
report = Report([
    DataDriftPreset()
])

result = report.run(
    current_data=current_data,
    reference_data=reference_data
)

# Save report
result.save_html("iris_drift_report.html")

print("\nEvidently monitoring completed!")
print("Report saved as iris_drift_report.html")
