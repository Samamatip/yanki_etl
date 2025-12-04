# Yanki E-Commerce ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline for processing Yanki e-commerce data. This pipeline extracts raw e-commerce transaction data, transforms it into normalized tables, and loads the processed data into CSV files organized by date.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Installation](#installation)
- [Usage](#usage)
- [Pipeline Components](#pipeline-components)
- [Data Download](#data-download)
- [Output](#output)

## Overview

This ETL pipeline automates the processing of e-commerce transaction data by:

1. **Extracting** raw data from CSV files
2. **Transforming** the data by:
   - Cleaning missing values
   - Converting date formats
   - Normalizing data into separate dimensional tables
3. **Loading** processed data into date-stamped directories

The pipeline follows a modular architecture with separate modules for extraction, transformation, and loading operations.

## Project Structure

```
Yanki-e-commerce/
│
├── main.py                     # Entry point for the ETL pipeline
│
├── ETL/
│   └── ETL.py                  # Main ETL orchestration logic
│
├── extract/
│   └── extract.py              # Data extraction module
│
├── transformation/
│   └── transform.py            # Data transformation and normalization
│
├── Load/
│   └── load.py                 # Data loading module
│
├── utilities/
│   └── utility.py              # Helper functions for file I/O and data processing
│
├── raw-data/
│   └── yanki_ecommerce.csv     # Raw input data (download separately)
│
├── processed-data/             # Output directory (auto-created)
│   └── YYYY-MM-DD/             # Date-stamped subdirectories
│       ├── Customer.csv
│       ├── Product.csv
│       ├── Order.csv
│       ├── Payment.csv
│       └── Shipping.csv
│
└── README.md                   # This file
```

## Data Model

The pipeline transforms a single denormalized e-commerce dataset into five normalized tables:

### 1. **Customer Table**
- `Customer_ID` (Primary Key)
- `Customer_Name`
- `Email`
- `Phone_Number`

### 2. **Product Table**
- `Product_ID` (Primary Key)
- `Product_Name`
- `Brand`
- `Category`
- `Price`

### 3. **Shipping Table**
- `Shipping_ID` (Primary Key, auto-generated)
- `Shipping_Address`
- `City`
- `State`
- `Country`
- `Postal_Code`

### 4. **Orders Table**
- `Order_ID` (Primary Key)
- `Customer_ID` (Foreign Key)
- `Product_ID` (Foreign Key)
- `Quantity`
- `Order_Date`

### 5. **Payment Table**
- `Order_ID` (Primary Key)
- `Payment_Method`
- `Transaction_Status`
- `Total_Price`

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository** (or download the project):
   ```bash
   git clone <repository-url>
   cd Yanki-e-commerce
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Windows (Command Prompt)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. **Install required packages**:
   ```bash
   pip install pandas
   ```

## Usage

### Running the Pipeline

1. **Download the raw data** (see [Data Download](#data-download) section)

2. **Place the CSV file** in the `raw-data/` directory:
   ```
   raw-data/yanki_ecommerce.csv
   ```

3. **Run the pipeline**:
   ```bash
   python main.py
   ```

4. **Check the output** in the `processed-data/` directory:
   ```
   processed-data/YYYY-MM-DD/
   ```

### Expected Output

Upon successful execution, you should see:
Assuming Today's date is 2024-12-04

```
Saved Customer to processed-data\2024-12-04\Customer.csv
----------------------------------------
Completed loading data to CSV files.
Saved Product to processed-data\2024-12-04\Product.csv
----------------------------------------
Completed loading data to CSV files.
Saved Order to processed-data\2024-12-04\Order.csv
----------------------------------------
Completed loading data to CSV files.
Saved Payment to processed-data\2024-12-04\Payment.csv
----------------------------------------
Completed loading data to CSV files.
Saved Shipping to processed-data\2024-12-04\Shipping.csv
----------------------------------------
Completed loading data to CSV files.
ETL process completed successfully. Processed data saved to: processed-data\2024-12-04
```

## Pipeline Components

### 1. Extract (`extract/extract.py`)

Reads raw data from CSV files using the utility function `extract_from()`.

**Key Features:**
- Supports CSV and Excel formats
- Error handling for missing or unsupported file formats

### 2. Transform (`transformation/transform.py`)

Performs data cleaning and normalization:

**Data Cleaning:**
- Removes rows with missing `Order_ID` or `Customer_ID`
- Converts `Order_Date` to datetime format

**Data Normalization:**
- Creates five normalized tables
- Removes duplicates from each table
- Generates `Shipping_ID` as an auto-incrementing identifier

### 3. Load (`Load/load.py`)

Saves transformed data to CSV files:

**Key Features:**
- Creates date-stamped directories automatically
- Uses the first column name to determine output filename
- Saves data without index columns

### 4. Utilities (`utilities/utility.py`)

Provides reusable helper functions:

- `extract_from()`: Load data from CSV/Excel files
- `save_data()`: Save DataFrames to various formats (CSV, Excel, Parquet, JSON)
- `clean_data_and_create_sub_tables()`: Extract columns and remove duplicates
- `make_directory_if_not_exists()`: Create directories with parent paths

## Data Download

Download the raw sample data from Google Drive:

**Download Link:** [Yanki E-Commerce Dataset](https://drive.google.com/file/d/1lPmrM-4EJLfM14E_3pWF2aLl_Y7HsoHa/view?usp=sharing)

After downloading:
1. Place the file in the `raw-data/` directory
2. Ensure the filename is `yanki_ecommerce.csv`

## Output

The pipeline generates five CSV files in a date-stamped directory:

```
processed-data/
└── 2024-12-04/
    ├── Customer.csv    # Customer information
    ├── Product.csv     # Product catalog
    ├── Order.csv       # Order transactions
    ├── Payment.csv     # Payment details
    └── Shipping.csv    # Shipping addresses
```

Each file contains clean, deduplicated data ready for analysis or database loading.

## Error Handling

The pipeline includes comprehensive error handling:

- **Missing Data:** Automatically removes rows with missing critical IDs
- **File Errors:** Clear error messages for missing or unsupported file formats
- **Pipeline Failures:** Detailed error messages with traceback information

If the pipeline fails, check:
1. The raw data file exists in `raw-data/yanki_ecommerce.csv`
2. The CSV file is properly formatted
3. Required packages (pandas) are installed in your virtual environment

## Troubleshooting

### Import Errors

If you see `Import "pandas" could not be resolved`:
- Ensure your virtual environment is activated
- Install pandas: `pip install pandas`
- Restart VS Code or reload the window

### File Not Found

If the pipeline can't find the data file:
- Verify the file path in `main.py` matches your actual file location
- Ensure the file is named `yanki_ecommerce.csv`
- Check that the file is in the `raw-data/` directory

## Author

Developed by Samson {github.com/samamatip} for 10Alytics e-commerce data processing.

---

**Last Updated:** December 2025