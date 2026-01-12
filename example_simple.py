#!/usr/bin/env python3
"""
Simple example demonstrating Polars DataFrame creation and basic operations.
This example simulates Google Sheets data without requiring authentication.
"""

import polars as pl


def create_sample_data() -> pl.DataFrame:
    """
    Create a sample DataFrame that simulates data from a Google Sheet.
    
    Returns:
        A Polars DataFrame with sample data
    """
    # Sample data that would typically come from a Google Sheet
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "Age": [25, 30, 35, 28, 32],
        "Department": ["Engineering", "Marketing", "Sales", "Engineering", "HR"],
        "Salary": [75000, 65000, 70000, 80000, 60000],
        "Years_Experience": [3, 7, 10, 5, 8],
    }
    
    return pl.DataFrame(data)


def main():
    """
    Demonstrate basic Polars operations on sample data.
    """
    print("=" * 60)
    print("Polars DataFrame Example (Simulating Google Sheets Data)")
    print("=" * 60)
    print()
    
    # Create sample DataFrame
    df = create_sample_data()
    
    # Display basic information
    print("📊 DataFrame Shape:", df.shape)
    print(f"   ({df.shape[0]} rows × {df.shape[1]} columns)")
    print()
    
    print("📋 Column Names:", df.columns)
    print()
    
    print("🔍 Data Types:")
    for col, dtype in zip(df.columns, df.dtypes):
        print(f"   {col}: {dtype}")
    print()
    
    print("📄 Full DataFrame:")
    print(df)
    print()
    
    # Demonstrate some Polars operations
    print("=" * 60)
    print("Example Polars Operations")
    print("=" * 60)
    print()
    
    # 1. Filter data
    print("1️⃣  Employees in Engineering:")
    engineering_df = df.filter(pl.col("Department") == "Engineering")
    print(engineering_df)
    print()
    
    # 2. Sort data
    print("2️⃣  Employees sorted by salary (descending):")
    sorted_df = df.sort("Salary", descending=True)
    print(sorted_df)
    print()
    
    # 3. Select specific columns
    print("3️⃣  Name and Salary columns only:")
    selected_df = df.select(["Name", "Salary"])
    print(selected_df)
    print()
    
    # 4. Add calculated column
    print("4️⃣  Adding calculated column (Salary per Year of Experience):")
    with_calc_df = df.with_columns(
        (pl.col("Salary") / pl.col("Years_Experience")).alias("Salary_per_Year")
    )
    print(with_calc_df)
    print()
    
    # 5. Group by and aggregate
    print("5️⃣  Average salary by department:")
    agg_df = df.group_by("Department").agg(
        pl.col("Salary").mean().alias("Avg_Salary"),
        pl.col("Name").count().alias("Employee_Count")
    ).sort("Avg_Salary", descending=True)
    print(agg_df)
    print()
    
    # 6. Statistics
    print("6️⃣  Salary statistics:")
    stats_df = df.select(
        pl.col("Salary").mean().alias("Mean"),
        pl.col("Salary").median().alias("Median"),
        pl.col("Salary").min().alias("Min"),
        pl.col("Salary").max().alias("Max"),
        pl.col("Salary").std().alias("Std_Dev")
    )
    print(stats_df)
    print()
    
    print("=" * 60)
    print("✅ Example complete!")
    print()
    print("💡 To connect to a real Google Sheet:")
    print("   1. See example.py for Google Sheets integration")
    print("   2. Set up service account authentication")
    print("   3. Use gspread to fetch data from your sheet")
    print("=" * 60)


if __name__ == "__main__":
    main()
