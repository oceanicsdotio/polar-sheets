# polar-sheets

Testing Google Sheets to Polars DataFrame developer experience.

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

### 2. Set Up Google Sheets Authentication

To access Google Sheets, you need to set up a Google Service Account:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Enable the Google Sheets API
4. Create an API Key
5. Make your Google Sheet publicly visible

For more details, see [gspread authentication documentation](https://docs.gspread.org/en/latest/oauth2.html#service-account).

### 3. Run the Example

Run the example script using Pixi:

```bash
pixi run main
```

## Example Code

The `main.py` script demonstrates:

- Connecting to Google Sheets using a URL
- Fetching data from a worksheet
- Converting the data to a Polars DataFrame
- Basic DataFrame operations

## About Pixi

Pixi is a modern package management tool that:
- Provides fast, reproducible environments
- Works across platforms (Linux, macOS, Windows)
- Uses conda-forge packages
- Manages both Python and system dependencies
- Creates isolated environments automatically

## About Polars

Polars is a fast DataFrame library that:
- Offers better performance than pandas for large datasets
- Uses Apache Arrow for memory efficiency
- Provides a clean, expressive API
- Supports lazy evaluation for query optimization

## License

See [LICENSE](LICENSE) file for details.
