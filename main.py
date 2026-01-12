#!/usr/bin/env python3
"""
Example script demonstrating how to pull data from a Google Sheets link
into a Polars DataFrame.

This example uses gspread to access Google Sheets and converts the data
to a Polars DataFrame for efficient data processing.
"""

from os import getenv
from polars import DataFrame
from gspread import api_key


def get_google_sheets_data(
    sheets_api_key: str,
    sheets_source_key: str,
    worksheet_name: str | None = None
) -> DataFrame:
    """
    Fetch data from a Google Sheets URL and return as a Polars DataFrame.
    
    Args:
        sheet_url: The URL of the Google Sheets document
        worksheet_name: Optional name of specific worksheet. If None, uses first sheet.
    
    Returns:
        A Polars DataFrame containing the sheet data
    """
    spreadsheet = api_key(sheets_api_key).open_by_key(sheets_source_key)
    if worksheet_name:
        worksheet = spreadsheet.worksheet(worksheet_name)
    else:
        worksheet = spreadsheet.sheet1

    data = worksheet.get_all_records()
    return DataFrame(data)


def main():
    """
    Main example demonstrating Google Sheets to Polars DataFrame conversion.
    """

    # This will look for the credentials.json file in the default location
    # and handle the authorization flow
    _api_key = getenv("SHEETS_API_KEY", "")
    # Open a spreadsheet by name or URL
    _source_key = getenv("SOURCE_KEY", "")

    # Fetch data from Google Sheets
    df = get_google_sheets_data(
        sheets_api_key=_api_key,
        sheets_source_key=_source_key,
        worksheet_name=None
    )

    # Display basic information about the DataFrame
    print("DataFrame shape:", df.shape)
    print("\nColumn names:", df.columns)
    print("\nFirst few rows:")
    print(df.head())

    # Example: Perform some Polars operations
    print("\nData types:")
    print(df.dtypes)


if __name__ == "__main__":
    main()
