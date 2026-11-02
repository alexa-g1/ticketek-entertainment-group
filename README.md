# ticketek-entertainment-group

Data Engineer take-home for TEG. Pipeline and notes are in `DE_Take_Home_Assessment.ipynb`.

Used PySpark because Spark is required from the job description. Pandas could be used for such a small data set, I wanted to show my Spark capabilities for a simple pipeline.

Put schemas in separate files for easier readability and easier to update.

Used T-SQL for the SQL tasks because it is required for task 6.

## How to run

Needs Python 3, Java 11 or 17, and PySpark.

```
pip install pyspark jupyter
```

Open the notebook from the repo root so the data paths work (`Data/Raw/...`):

```
jupyter notebook DE_Take_Home_Assessment.ipynb
```

Run the Spark cells in order (tasks 1–2). The SQL cells (tasks 3, 4, 6) are T-SQL for SQL Server / SSRS, not for the notebook kernel.

ERD is in `Data/ERD/ERD.png`.

## Assumptions

- sale_date is a string in the read schema because the formats are different and need transformation first.
- Missing product_id is already null when using Spark so nothing extra is needed there.
- Used distinct instead of dropDuplicates because there is no need to specify keys, the whole row is duplicated.
- Dates in the sample data are one of `yyyy-MM-dd`, `MM/dd/yyyy`, or `yyyy/MM/dd`.
- Last 30 days in the reporting query is relative to the latest sale_date in the data, not today's date, so it still works on this small sample.
- Task 5 assumes Databricks on AWS, files landing in S3, and Airflow for scheduling.
