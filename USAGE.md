# Usage Guide

This guide provides detailed instructions for using polar-sheets to work with Google Sheets data in Polars DataFrames.

## Quick Start

### 1. Install Pixi

If you haven't already, install Pixi:

**Linux/macOS:**
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

**Windows:**
```powershell
iwr -useb https://pixi.sh/install.ps1 | iex
```

For more options, see [Pixi installation](https://pixi.sh/latest/#installation).

### 2. Clone and Setup

```bash
git clone https://github.com/oceanicsdotio/polar-sheets.git
cd polar-sheets
pixi install
```

### 3. Run the Demo

Try the simple demo that doesn't require authentication:

```bash
pixi run demo
```

This demonstrates various Polars operations on sample data.

## Working with Google Sheets

### Option 1: Service Account (Recommended for automation)

1. **Create a Google Cloud Project**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing

2. **Enable Google Sheets API**
   - In the project, go to "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click "Enable"

3. **Create Service Account**
   - Go to "IAM & Admin" > "Service Accounts"
   - Click "Create Service Account"
   - Provide a name (e.g., "polar-sheets-reader")
   - Click "Create and Continue"
   - Skip role assignment (click "Continue")
   - Click "Done"

4. **Generate Key**
   - Click on your newly created service account
   - Go to "Keys" tab
   - Click "Add Key" > "Create new key"
   - Select "JSON" format
   - Save the downloaded file as `service_account.json` in your project directory

5. **Share Your Sheet**
   - Open the `service_account.json` file
   - Copy the `client_email` value
   - Open your Google Sheet
   - Click "Share" button
   - Paste the service account email
   - Give at least "Viewer" permissions
   - Click "Send"

6. **Update Example Script**
   - Open `example.py`
   - Replace `YOUR_SHEET_ID` with your actual Google Sheets ID
     - The ID is in the URL: `https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit`
   - Uncomment the try/except block in the `main()` function

7. **Run the Example**
   ```bash
   pixi run example
   ```

### Option 2: OAuth2 (For interactive use)

For personal use with your own Google account, you can use OAuth2:

```python
import gspread
from google.oauth2.service_account import Credentials

# Use OAuth2 flow
gc = gspread.oauth()

# Rest of the code remains the same
spreadsheet = gc.open_by_url(sheet_url)
# ...
```

## Example Use Cases

### 1. Basic Data Import

```python
import polars as pl
import gspread

gc = gspread.service_account()
sheet = gc.open_by_url("YOUR_SHEET_URL")
data = sheet.sheet1.get_all_records()
df = pl.DataFrame(data)
print(df)
```

### 2. Data Analysis Pipeline

```python
# Fetch data
df = get_google_sheets_data(sheet_url)

# Clean and transform
df_clean = (
    df
    .filter(pl.col("Amount") > 0)
    .with_columns([
        pl.col("Date").str.to_date(),
        pl.col("Amount").cast(pl.Float64)
    ])
    .sort("Date")
)

# Aggregate
summary = (
    df_clean
    .group_by("Category")
    .agg([
        pl.col("Amount").sum().alias("Total"),
        pl.col("Amount").mean().alias("Average"),
        pl.count().alias("Count")
    ])
)

print(summary)
```

### 3. Multiple Sheets

```python
# Access multiple worksheets from same spreadsheet
spreadsheet = gc.open_by_url(sheet_url)

# Get data from different sheets
sales_df = pl.DataFrame(spreadsheet.worksheet("Sales").get_all_records())
inventory_df = pl.DataFrame(spreadsheet.worksheet("Inventory").get_all_records())

# Join the dataframes
merged_df = sales_df.join(inventory_df, on="ProductID", how="left")
```

### 4. Writing Back to Sheets (Optional)

```python
# Convert Polars DataFrame back to list of lists
data_to_write = df.to_numpy().tolist()

# Update sheet
worksheet.update("A1", data_to_write)
```

## Troubleshooting

### Authentication Issues

**Error: "Unable to find credentials"**
- Make sure `service_account.json` exists in your project directory
- Check that the file path is correct
- Verify the JSON file is valid

**Error: "The caller does not have permission"**
- Ensure you've shared the Google Sheet with the service account email
- Check that the service account has at least "Viewer" permission
- Verify you're using the correct Sheet ID

### API Issues

**Error: "API has not been used in project"**
- Go to Google Cloud Console
- Navigate to "APIs & Services" > "Library"
- Search for "Google Sheets API" and enable it

### Data Type Issues

**Numbers imported as strings:**
```python
# Cast columns to correct types
df = df.with_columns([
    pl.col("Amount").cast(pl.Float64),
    pl.col("Quantity").cast(pl.Int64)
])
```

**Date parsing issues:**
```python
# Parse dates from various formats
df = df.with_columns([
    pl.col("Date").str.to_date("%Y-%m-%d")
])
```

## Performance Tips

1. **Use lazy evaluation for large datasets:**
   ```python
   df_lazy = pl.LazyFrame(data)
   result = df_lazy.filter(...).group_by(...).collect()
   ```

2. **Limit data fetched:**
   ```python
   # Get only specific range
   data = worksheet.get("A1:E100")
   ```

3. **Batch operations:**
   ```python
   # Update multiple cells at once
   cell_list = worksheet.range("A1:A5")
   for i, cell in enumerate(cell_list):
       cell.value = values[i]
   worksheet.update_cells(cell_list)
   ```

## Additional Resources

- [Polars Documentation](https://pola-rs.github.io/polars-book/)
- [gspread Documentation](https://docs.gspread.org/)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [Pixi Documentation](https://pixi.sh/latest/)

## Getting Help

- Create an issue in the repository
- Check the examples in `example.py` and `example_simple.py`
- Refer to the main README for basic setup instructions
