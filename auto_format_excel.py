import pandas as pd

def auto_format_excel(input_file, output_file=None):
    """
    Automatically cleans and formats an Excel or CSV file:
    - Strips extra spaces from text columns
    - Fixes date column formatting
    - Capitalizes names properly
    - Removes completely empty rows
    - Standardizes column headers

    Parameters:
        input_file (str): Path to your Excel or CSV file
        output_file (str): Path to save formatted file (optional)

    Example:
        auto_format_excel('messy_data.xlsx', 'clean_data.xlsx')
    """

    # Load the file
    print(f"Loading: {input_file}")
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_excel(input_file)

    print(f"Rows loaded: {len(df)}")

    # Step 1 — Clean column headers
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    print("✓ Column headers cleaned")

    # Step 2 — Remove completely empty rows
    df = df.dropna(how='all')
    print("✓ Empty rows removed")

    # Step 3 — Strip spaces from all text columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
    print("✓ Extra spaces stripped")

    # Step 4 — Capitalize name columns properly
    name_cols = [col for col in df.columns if 'name' in col]
    for col in name_cols:
        df[col] = df[col].str.title()
    print(f"✓ Name columns capitalized: {name_cols}")

    # Step 5 — Fix date columns
    date_cols = [col for col in df.columns if 'date' in col]
    for col in date_cols:
        try:
            df[col] = pd.to_datetime(df[col]).dt.strftime('%Y-%m-%d')
            print(f"✓ Date column formatted: {col}")
        except:
            print(f"  Skipped date column (unreadable): {col}")

    # Save output
    if output_file is None:
        name, ext = input_file.rsplit('.', 1)
        output_file = f"{name}_formatted.{ext}"

    if output_file.endswith('.csv'):
        df.to_csv(output_file, index=False)
    else:
        df.to_excel(output_file, index=False)

    print(f"\nDone! Formatted file saved as: {output_file}")


# ---- HOW TO USE ----
# 1. Put your file in the same folder as this script
# 2. Change 'your_file.xlsx' to your actual filename
# 3. Run the script

if __name__ == "__main__":
    auto_format_excel('your_file.xlsx', 'formatted_output.xlsx')
