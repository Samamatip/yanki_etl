from extract.extract import extract
from transformation.transform import transform_data
from Load.load import load_data_to_csv

def run_etl_process(data_path):
    try:
        # Extract
        raw_data = extract(data_path)

        # Transform
        transformed_data = transform_data(raw_data)

        # Load
        dest_dir = load_data_to_csv(transformed_data)
        
        print(f"ETL process completed successfully. Processed data saved to: {dest_dir}")
    except Exception as e:
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print(f"ETL process failed: {e}")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        SystemExit(1)