import pandas as pd

def extract_from(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        if not file_path:
            print("File path is empty")
            raise ValueError("Missing file format")
        raise ValueError("Unsupported file format")


def save_data(df, file_path, targetFormat='csv', index=False):
    if targetFormat == 'csv':
        df.to_csv(file_path, index=index)
    elif targetFormat == 'xlsx':
        df.to_excel(file_path, index=index)
    elif targetFormat == 'parquet':
        df.to_parquet(file_path, index=index)
    elif targetFormat == 'json':
        df.to_json(file_path, index=index)
    else:
        if not file_path:
            print("File path is empty")
            # raise an error for wrong file destination path
        if not targetFormat:
            print("Target format is missing")
            raise ValueError("Missing target format")
        raise ValueError("Unsupported target format")
    

def clean_data_and_create_sub_tables(df, array_of_columns):
    df_cleaned = df[array_of_columns].copy().drop_duplicates().reset_index(drop=True)
    return df_cleaned

def make_directory_if_not_exists(directory_path):
    import pathlib # create directory path
    dest_dir = pathlib.Path(directory_path) # create pathlib object
    dest_dir.mkdir(parents=True, exist_ok=True) # create directory if not exists
    return dest_dir