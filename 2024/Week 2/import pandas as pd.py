import pandas as pd

# Read the input CSV files
df1 = pd.read_csv(r"C:\Users\OlivierNewman\Documents\Prepin data\2024\Week 2\PD 2024 Wk 1 Output Flow Card.csv")
df2 = pd.read_csv(r"C:\Users\OlivierNewman\Documents\Prepin data\2024\Week 2\PD 2024 Wk 1 Output Non-Flow Card.csv")

def PD_Week2_2024(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # Concatenate the DataFrames
    unioned_df = pd.concat([df1, df2], ignore_index=True, axis=0)
    
    # Ensure the 'Date' column is of datetime type (if there are any errors, 'coerce' will handle them)
    unioned_df['Date'] = pd.to_datetime(unioned_df['Date'], errors='coerce')
    
    # Extract the quarter from the 'Date' column
    unioned_df['Quarter'] = unioned_df['Date'].dt.quarter
    
    return unioned_df

# Call the function PD_Week2_2024 to concatenate and process the DataFrames
final_df = PD_Week2_2024(df1, df2)

def PD_Week2_2024_Median(final_df: pd.DataFrame) -> pd.DataFrame:
    # Convert the 'Price' column to numeric, coercing errors to NaN (if any)
    final_df["Price"] = pd.to_numeric(final_df['Price'], errors='coerce')
    
    # Group by 'Quarter', 'Flow Card?', and 'Class', then calculate the median of 'Price'
    median_prices = final_df.groupby(["Quarter", "Flow Card?", "Class"])["Price"].median().reset_index()
    
    # Pivot the table to spread 'Class' into new columns
    median_prices_pivoted = median_prices.pivot_table(index=['Flow Card?', "Quarter"], columns='Class', values='Price')
    
    return median_prices_pivoted

final_median = PD_Week2_2024_Median(final_df)
print(final_median)

def PD_Week2_2024_Max(final_df: pd.DataFrame) -> pd.DataFrame:
    # Convert the 'Price' column to numeric, coercing errors to NaN (if any)
    final_df["Price"] = pd.to_numeric(final_df['Price'], errors='coerce')
    
    # Group by 'Quarter', 'Flow Card?', and 'Class', then calculate the max of 'Price'
    max_prices = final_df.groupby(["Quarter", "Flow Card?", "Class"])["Price"].max().reset_index()
    
    # Pivot the table to spread 'Class' into new columns
    max_prices_pivoted = max_prices.pivot_table(index=['Flow Card?', "Quarter"], columns='Class', values='Price')
    
    return max_prices_pivoted

final_max = PD_Week2_2024_Max(final_df)
#print(final_max)

def PD_Week2_2024_Min(final_df: pd.DataFrame) -> pd.DataFrame:
    # Convert the 'Price' column to numeric, coercing errors to NaN (if any)
    final_df["Price"] = pd.to_numeric(final_df['Price'], errors='coerce')
    
    # Group by 'Quarter', 'Flow Card?', and 'Class', then calculate the min of 'Price'
    min_prices = final_df.groupby(["Quarter", "Flow Card?", "Class"])["Price"].min().reset_index()
    
    # Pivot the table to spread 'Class' into new columns
    min_prices_pivoted = min_prices.pivot_table(index=['Flow Card?', "Quarter"], columns='Class', values='Price')
    
    return min_prices_pivoted

final_min = PD_Week2_2024_Min(final_df)
#print(final_min)

def PD_Week2_2024_final(final_median: pd.DataFrame, final_min: pd.DataFrame, final_max: pd.DataFrame) -> pd.DataFrame:
    # Concatenate the min, max, and median DataFrames
    unioned_results = pd.concat([final_min, final_max, final_median], ignore_index=False, axis=0)

    # Reset the index and keep the columns (Flow Card?, Quarter, Class)
    unioned_results = unioned_results.reset_index(drop=False)

    # Ensure columns like 'Flow Card?' and 'Quarter' are not lost when you reset the index
    # Unioned results should have Flow Card? and Quarter as columns

    # Optionally, rename columns if needed (ensure the columns are correct before renaming)
    unioned_results.rename(columns={
        "Economy": "First", 
        "First Class": "Economy", 
        "Business Class": "Premium", 
        "Premium Economy ": "Business"
    }, inplace=True)
    
    return unioned_results

final_unions = PD_Week2_2024_final(final_median, final_min, final_max)
print(final_unions)

output_path = r"C:\Users\OlivierNewman\Documents\Prepin data\2024\Week 2\Processed_PD_Week2_2024.csv"
final_unions.to_csv(output_path, index=False)

# Print confirmation
print(f"Processed data saved to {output_path}")

