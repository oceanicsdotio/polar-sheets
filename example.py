#!/usr/bin/env python3
"""
Example script demonstrating how to pull data from a Google Sheets link
into a Polars DataFrame.

This example uses gspread to access Google Sheets and converts the data
to a Polars DataFrame for efficient data processing.
"""

import polars as pl
import gspread
from gspread import Client


def get_google_sheets_data(sheet_url: str, worksheet_name: str = None) -> pl.DataFrame:
    """
    Fetch data from a Google Sheets URL and return as a Polars DataFrame.
    
    Args:
        sheet_url: The URL of the Google Sheets document
        worksheet_name: Optional name of specific worksheet. If None, uses first sheet.
    
    Returns:
        A Polars DataFrame containing the sheet data
    """
    # Initialize gspread client (uses default authentication)
    # This will look for credentials in standard locations
    gc = gspread.service_account()
    
    # Open the spreadsheet by URL
    spreadsheet = gc.open_by_url(sheet_url)
    
    # Get the worksheet (first sheet by default)
    if worksheet_name:
        worksheet = spreadsheet.worksheet(worksheet_name)
    else:
        worksheet = spreadsheet.sheet1
    
    # Get all values from the worksheet
    data = worksheet.get_all_records()
    
    # Convert to Polars DataFrame
    df = pl.DataFrame(data)
    
    return df


def main():
    """
    Main example demonstrating Google Sheets to Polars DataFrame conversion.
    """
    # Example Google Sheets URL
    # Replace this with your own public or accessible Google Sheets URL
    # For testing, you can use a public Google Sheets document
    sheet_url = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"
    
    print("=" * 60)
    print("Google Sheets to Polars DataFrame Example")
    print("=" * 60)
    print()
    print("NOTE: Before running this example, you need to:")
    print("1. Set up Google Service Account credentials")
    print("2. Download the JSON key file")
    print("3. Save it as 'service_account.json' in this directory")
    print("4. Share your Google Sheet with the service account email")
    print("5. Replace 'YOUR_SHEET_ID' in this script with your actual Sheet ID")
    print()
    print("For authentication setup, see:")
    print("https://docs.gspread.org/en/latest/oauth2.html#service-account")
    print()
    print("=" * 60)
    print()
    
    # Example: If you have a valid sheet URL and credentials set up:
    # Uncomment the following lines to test with your own sheet
    
    # try:
    #     # Fetch data from Google Sheets
    #     df = get_google_sheets_data(sheet_url)
    #     
    #     # Display basic information about the DataFrame
    #     print("DataFrame shape:", df.shape)
    #     print("\nColumn names:", df.columns)
    #     print("\nFirst few rows:")
    #     print(df.head())
    #     
    #     # Example: Perform some Polars operations
    #     print("\nData types:")
    #     print(df.dtypes)
    #     
    #     print("\nExample complete!")
    #     
    # except Exception as e:
    #     print(f"Error: {e}")
    #     print("\nMake sure you have:")
    #     print("- Valid service account credentials")
    #     print("- Shared the sheet with your service account")
    #     print("- Correct sheet URL")


if __name__ == "__main__":
    main()
