# ⚡ Spark Data Pipeline

This project demonstrates a simple data pipeline built with PySpark, simulating a real-world data processing workflow.

---

## 🚀 Project Overview

The goal of this project is to:

- Ingest raw data from a CSV source
- Perform data transformations
- Aggregate data for analysis
- Store processed results for downstream use

---

## 🧠 Technologies Used

- Python
- PySpark
- Apache Spark
- CSV (data source)

---

## 📊 Dataset

The dataset simulates user activity events, including:

- User interactions (click, view, purchase)
- Associated values
- Timestamped records

---

## 🏗️ Pipeline Architecture

1. **Data Ingestion**
   - Load CSV data using Spark

2. **Data Transformation**
   - Cast and clean data types

3. **Aggregation**
   - Group data by action
   - Calculate total values per action

4. **Data Output**
   - Save aggregated results to output directory

---

## ⚙️ How to Run

1. Install dependencies:

```bash
pip install pyspark
```

2. Run the pipeline:

```bash
python src/main.py
```

---

## 📈 Future Improvements
- Integration with cloud storage (AWS S3 / Azure Data Lake)
- Use of Delta Lake
- Real-time streaming with Spark Structured Streaming
- Orchestration with Airflow

---
## 📌 Motivation

This project was created to strengthen my practical experience with data pipelines and Spark, focusing on real-world data processing scenarios.
