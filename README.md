# polar-sheets

Testing Google Sheets to Polar Dataframe developer experience.

This repository demonstrates how to use [Pixi](https://pixi.sh) for Python environment management and provides an example of pulling data from Google Sheets into a [Polars](https://pola.rs) DataFrame.

## Prerequisites

- [Pixi](https://pixi.sh) installed on your system
  - Installation: `curl -fsSL https://pixi.sh/install.sh | bash`
  - Or see [Pixi installation docs](https://pixi.sh/latest/#installation)

## Getting Started

### 1. Install Dependencies

Pixi will automatically install all required dependencies specified in `pixi.toml`:

```bash
pixi install
```

This will create a virtual environment with:
- Python 3.10+
- Polars (for efficient DataFrame operations)
- gspread (for Google Sheets API access)
- pandas (for data compatibility)

### 2. Set Up Google Sheets Authentication

To access Google Sheets, you need to set up a Google Service Account:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Enable the Google Sheets API
4. Create a Service Account:
   - Navigate to "IAM & Admin" > "Service Accounts"
   - Click "Create Service Account"
   - Give it a name and click "Create"
   - Click "Done" (no roles needed for basic access)
5. Create and download a JSON key:
   - Click on your new service account
   - Go to "Keys" tab
   - Click "Add Key" > "Create new key"
   - Choose "JSON" format
   - Save the file as `service_account.json` in this directory
6. Share your Google Sheet with the service account email (found in the JSON file)

For more details, see [gspread authentication documentation](https://docs.gspread.org/en/latest/oauth2.html#service-account).

### 3. Run the Example

Run the example script using Pixi:

```bash
pixi run example
```

Or activate the environment and run directly:

```bash
pixi shell
python example.py
```

## Example Code

The `example.py` script demonstrates:

- Connecting to Google Sheets using a URL
- Fetching data from a worksheet
- Converting the data to a Polars DataFrame
- Basic DataFrame operations

## Modifying the Example

To use your own Google Sheet:

1. Open `example.py`
2. Replace `YOUR_SHEET_ID` in the `sheet_url` with your actual Google Sheets document ID
3. Uncomment the try/except block in the `main()` function
4. Make sure your sheet is shared with your service account email
5. Run the script: `pixi run example`

## Detailed Guide

For comprehensive instructions including authentication setup, troubleshooting, and advanced use cases, see [USAGE.md](USAGE.md).

## Development

### Adding Dependencies

To add more Python packages:

```bash
pixi add <package-name>
```

### Running Other Python Scripts

```bash
pixi run python your_script.py
```

### Updating Dependencies

```bash
pixi update
```

## About Pixi

Pixi is a modern package management tool that:
- Provides fast, reproducible environments
- Works across platforms (Linux, macOS, Windows)
- Uses conda-forge packages
- Manages both Python and system dependencies
- Creates isolated environments automatically

## About Polars

Polars is a blazingly fast DataFrame library that:
- Offers better performance than pandas for large datasets
- Uses Apache Arrow for memory efficiency
- Provides a clean, expressive API
- Supports lazy evaluation for query optimization

## License

See [LICENSE](LICENSE) file for details.
