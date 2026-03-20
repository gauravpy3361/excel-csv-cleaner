import argparse
from auto_format_excel import auto_format_excel
from merge_csv_files import merge_csv_files
from remove_duplicates import remove_duplicates
from sample_data_cleaner import clean_data


def main():
    parser = argparse.ArgumentParser(description="Excel/CSV Automation Toolkit")

    parser.add_argument("--task", required=True,
                        choices=["format", "dedupe", "merge", "clean"],
                        help="Task to perform")

    parser.add_argument("--input", help="Input file path")
    parser.add_argument("--folder", help="Folder path (for merge)")
    parser.add_argument("--output", help="Output file (optional)")

    args = parser.parse_args()

    if args.task == "format":
        auto_format_excel(args.input, args.output)

    elif args.task == "dedupe":
        remove_duplicates(args.input, args.output)

    elif args.task == "merge":
        merge_csv_files(args.folder, args.output or "merged.csv")

    elif args.task == "clean":
        clean_data(args.input, args.output)


if __name__ == "__main__":
    main()