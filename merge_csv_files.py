import pandas as pd
import glob
import os

def merge_csv_files(folder_path, output_file='merged_output.csv'):
    """
    Merges all CSV files in a folder into one single file.

    Parameters:
        folder_path (str): Path to folder containing your CSV files
        output_file (str): Name of the merged output file

    Example:
        merge_csv_files('my_folder', 'merged.csv')
    """

    # Find all CSV files in the folder
    all_files = glob.glob(os.path.join(folder_path, "*.csv"))

    if not all_files:
        print("No CSV files found in the folder!")
        return

    print(f"Found {len(all_files)} CSV files:")
    for f in all_files:
        print(f"  - {os.path.basename(f)}")

    # Read and merge all files
    dataframes = []
    for file in all_files:
        df = pd.read_csv(file)
        df['source_file'] = os.path.basename(file)  # track which file each row came from
        dataframes.append(df)
        print(f"Loaded {len(df)} rows from {os.path.basename(file)}")

    # Combine all into one
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save the merged file
    merged_df.to_csv(output_file, index=False)

    print(f"\nDone! Merged {len(merged_df)} total rows")
    print(f"Saved as: {output_file}")


# ---- HOW TO USE ----
# 1. Put all your CSV files into one folder
# 2. Change 'your_folder' to your actual folder path
# 3. Run the script

if __name__ == "__main__":
    merge_csv_files('your_folder', 'merged_output.csv')
