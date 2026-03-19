# ============================================================
#  Excel / CSV Data Cleaner — Sample Script
#  Author  : @jgauravpy (Fiverr)
#  Purpose : Demonstrates automated data cleaning with Python
# ============================================================

import pandas as pd
import os

def clean_data(input_file: str, output_file: str = None):
    """
    Cleans an Excel or CSV file automatically:
      - Removes duplicate rows
      - Strips extra spaces from text columns
      - Standardises date columns
      - Removes completely empty rows/columns
      - Saves a clean output file
    """

    # ── 1. Load the file ────────────────────────────────────
    ext = os.path.splitext(input_file)[1].lower()
    if ext == ".csv":
        df = pd.read_csv(input_file)
    elif ext in (".xlsx", ".xls"):
        df = pd.read_excel(input_file)
    else:
        raise ValueError("Only .csv, .xlsx, or .xls files are supported.")

    print(f"✅ Loaded '{input_file}'  →  {df.shape[0]} rows, {df.shape[1]} columns")

    # ── 2. Remove completely empty rows & columns ───────────
    before = df.shape[0]
    df.dropna(how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)
    print(f"🗑️  Removed {before - df.shape[0]} fully empty rows")

    # ── 3. Remove duplicate rows ────────────────────────────
    before = df.shape[0]
    df.drop_duplicates(inplace=True)
    print(f"🗑️  Removed {before - df.shape[0]} duplicate rows")

    # ── 4. Strip whitespace from all text columns ───────────
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())
    print(f"✂️  Stripped whitespace from {len(str_cols)} text column(s): {list(str_cols)}")

    # ── 5. Auto-detect & convert date columns ───────────────
    date_cols_converted = []
    for col in str_cols:
        try:
            converted = pd.to_datetime(df[col], infer_datetime_format=True, errors="raise")
            df[col] = converted.dt.strftime("%Y-%m-%d")
            date_cols_converted.append(col)
        except Exception:
            pass
    if date_cols_converted:
        print(f"📅 Converted date columns: {date_cols_converted}")

    # ── 6. Reset index ───────────────────────────────────────
    df.reset_index(drop=True, inplace=True)

    # ── 7. Save output ───────────────────────────────────────
    if output_file is None:
        name, _ = os.path.splitext(input_file)
        output_file = f"{name}_cleaned.xlsx"

    df.to_excel(output_file, index=False)
    print(f"\n🎉 Clean file saved → '{output_file}'")
    print(f"📊 Final size: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


# ── Run it ───────────────────────────────────────────────────
if __name__ == "__main__":
    # 👇 Change this to your actual file name
    clean_data("your_file.xlsx")
