from utilities.utility import make_directory_if_not_exists
from datetime import datetime


def load_data_to_csv(dfs):
    today_date = datetime.today().strftime('%Y-%m-%d')
    dest_dir = make_directory_if_not_exists(f'processed-data/{today_date}/')
    
    for df in dfs:
        df_name = df.columns[0].split('_')[0]  # get the first column name and use it as df name
        file_path = dest_dir / f'{df_name}.csv'
        df.to_csv(file_path, index=False)
        print(f"Saved {df_name} to {file_path}")
        print('----------------------------------------')
        print('Completed loading data to CSV files.')
    return dest_dir