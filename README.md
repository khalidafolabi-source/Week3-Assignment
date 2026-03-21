# 📊 DATA CLEANING PIPELINE – FINANCIAL TRANSACTIONS

## 📌 Project Overview
This project focuses on building a *data cleaning pipeline* using *Python* and *Pandas* to transform a messy financial transactions dataset into a clean, structured, and analysis-ready format.

In real-world data engineering, raw datasets often contain inconsistencies, missing values, and errors. This project demonstrates how to systematically clean and prepare such data for reporting, analytics, and machine learning.

---

## 🎯 Objective
The main goal of this project is to:

- Load and inspect a raw dataset  
- Clean and standardize inconsistent data  
- Handle missing and incorrect values  
- Perform feature engineering  
- Export a clean dataset  
- Build a reusable data cleaning function  

---

## 📂 Dataset Description
The dataset used: financial_transactions.csv

### Columns:
- transaction_id
- transaction_date
- customer_id
- product_name
- quantity
- price
- payment_method
- transaction_status

⚠️ The dataset contains:
- Missing values  
- Incorrect data types  
- Negative values  
- Inconsistent text formatting  
- Duplicate records  

---

## ⚙️ Technologies Used
- Python 🐍  
- Pandas 🧮  
- Jupyter Notebook / Python Script  

---

## 🧹 Data Cleaning Process

### 1. Load Dataset
- Imported dataset using Pandas  
- Displayed initial rows for preview  

### 2. Inspect Dataset
- Checked shape (rows & columns)  
- Reviewed data types  
- Identified missing values  

### 3. Standardize Column Names
- Converted all column names to *snake_case*  

### 4. Handle Missing Values
- Identified null values  
- Applied appropriate filling strategies  

### 5. Clean Price Column
- Removed currency symbols  
- Converted to numeric type  
- Converted negative values to positive  
- Filled missing values using median  

### 6. Clean Quantity Column
- Converted negative values to positive  

### 7. Standardize Text Columns
Applied to:
- product_name  
- payment_method  
- transaction_status  

Steps:
- Removed extra spaces  
- Converted to lowercase  
- Fixed inconsistent labels  

### 8. Clean Date Column
- Converted transaction_date to datetime format  

### 9. Remove Duplicates
- Identified and removed duplicate records  

---

## 🧠 Feature Engineering

### 🔹 total_value
- quantity × price

### 🔹 order_size
- bulk → quantity ≥ 100  
- regular → quantity < 100  

### 🔹 transaction_year
- Extracted from transaction date  

### 🔹 transaction_month
- Extracted from transaction date  

### 🔹 high_value_transaction
- True → total_value > 2000  
- False → otherwise  

---

## 🚀 Bonus Features (Optional)

### 🔹 revenue_category
- low → total_value < 500  
- medium → 500 ≤ total_value ≤ 2000  
- high → total_value > 2000  

### 🔹 transaction_weekday
- Extracted day of the week from transaction date  

---

## 💾 Output
- Cleaned dataset saved as:  
  *clean_transactions.csv*

- Index column excluded during export  

---

## 🔁 Reusable Pipeline Function

```python
def clean_transaction_data(file_name)

## Function Features
- Loads Dataset
- Performs all cleaning steps
- Returns cleaned DataFrame
- Automatically saves cleaned file

## Repository Structure
 data-cleaning-pipeline
 ┣ 📜 clean_transactions.csv
 ┣ 📜 financial_transactions.csv
 ┣ 📜 data_cleaning_script.py
 ┗ 📜 README.md

## Key Learnings
	•	Data cleaning is a critical step in data engineering
	•	Handling missing and inconsistent data improves data quality
	•	Feature engineering adds business value
	•	Writing reusable functions improves efficiency
