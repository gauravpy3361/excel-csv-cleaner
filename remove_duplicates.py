import pandas as pd
import os

def remove_duplicates(input_file, output_file=None):
    """
    Removes duplicate rows from a CSV or Excel file.
    
    Parameters:
        input_file (str): Path to your input CSV or Excel file
        output_file (str): Path to save the cleaned file (optional)
    
    Example:
        remove_duplicates('my_data.csv', 'clean_data.csv')
    """

    # Load the file
    print(f"Loading file: {input_file}")
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(input_file)
    else:
        print("Error: Please provide a .csv or .xlsx file")
        return

    # Count before
    before = len(df)
    print(f"Total rows before cleaning: {before}")

    # Remove duplicates
    df = df.drop_duplicates()

    # Count after
    after = len(df)
    print(f"Total rows after cleaning: {after}")
    print(f"Duplicates removed: {before - after}")

    # Save output
    if output_file is None:
        name, ext = os.path.splitext(input_file)
        output_file = f"{name}_cleaned{ext}"

    if output_file.endswith('.csv'):
        df.to_csv(output_file, index=False)
    else:
        df.to_excel(output_file, index=False)

    print(f"Clean file saved as: {output_file}")


# ---- HOW TO USE ----
# 1. Put your file in the same folder as this script
# 2. Change 'your_file.csv' to your actual filename
# 3. Run the script

if __name__ == "__main__":
    remove_duplicates('your_file.csv', 'cleaned_output.csv')
