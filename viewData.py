import os
import zipfile
import pandas as pd

def print_csv_heads_from_zip(data_folder):
    # List all files in the data folder
    all_files = os.listdir(data_folder)

    if len(all_files) < 1:
        print("No dataset found in the Data folder.\nDownload the zip from the top right of https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks?resource=download\nThen place the zip file in the data folder and run this script again.")

    # Filter for zip files
    zip_files = [f for f in all_files if f.endswith('.zip')]

    # Process each zip file
    for zip_file in zip_files:
        print(f"Processing zip file: {zip_file}")
        with zipfile.ZipFile(os.path.join(data_folder, zip_file), 'r') as z:
            # List csv files in the zip archive
            csv_files = [f for f in z.namelist() if f.endswith('.csv')]

            # Process each csv file
            for csv_file in csv_files:
                
                # Extract and load the CSV file
                with z.open(csv_file) as f:
                    df = pd.read_csv(f)

                    # Print the head of the dataset and its shape
                    print("~-"*30)
                    print(f"{csv_file} from {zip_file}")
                    print(df.head())
                    print(f"Number of attributes (rows): {df.shape[0]}")
                    print(f"Number of features (columns): {df.shape[1]}")
                    print("-~"*30)
                print("\n")

# Print all datasets found in the zip files of the Data folder
print_csv_heads_from_zip("Data")