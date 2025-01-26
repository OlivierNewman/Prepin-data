import pandas as pd

# Read the input CSV file
df = pd.read_csv(r"C:\Users\OlivierNewman\Documents\Prepin data\2024\Week 1\PD 2024 Wk 1 Input.csv")

def PD_Week1_2024(df: pd.DataFrame) -> pd.DataFrame:
    # Create a copy of the DataFrame to prevent modifying the original data
    df_processed = df.copy()
    
    # Replace 0 and 1 with 'No' and 'Yes' in the 'Flow Card?' column
    df_processed['Flow Card?'] = df_processed['Flow Card?'].replace({0: 'No', 1: 'Yes'})
    
    # Split 'Flight Details' into separate columns and limit the number of splits to avoid excess columns
    flight_details = df_processed['Flight Details'].str.split('/', expand=True, n=9)
    
    # Rename the new columns for clarity (e.g., Flight Detail Part 1, 2, etc.)
    flight_details.columns = [f'Flight Detail {i+1}' for i in range(flight_details.shape[1])]
    
    # Concatenate the split columns back to the original DataFrame
    df_final = pd.concat([df_processed, flight_details], axis=1)
    
    # Rename specific columns for clarity
    df_final = df_final.rename(columns={'Flight Detail 1': 'Date',
                                        'Flight Detail 3': 'Flight_Number',
                                        'Flight Detail 5': 'OD_Pair',
                                        'Flight Detail 7': 'Class',
                                        'Flight Detail 9': 'Price'}).drop(['Flight Details'], axis=1)[['Date','Flight_Number','OD_Pair','Class','Price','Flow Card?']]
    
    # Split the 'OD_Pair' column into 'Origin' and 'Destination'
    df_final[['Origin', 'Destination']] = df_final['OD_Pair'].str.split('-', expand=True)
    
    # Drop the 'OD_Pair' column
    df_final = df_final.drop(['OD_Pair'], axis=1)

    # Convert 'Date' to datetime using pd.to_datetime() to ensure proper conversion
    df_final['Date'] = pd.to_datetime(df_final['Date'], errors='coerce').dt.date

    # Print the data types of the DataFrame columns
    print("Data Types of Columns:")
    print(df_final.dtypes)  # This will display the data types of each column
    
    # Optionally print the final processed DataFrame to verify the changes
    print("\nProcessed DataFrame:")
    print(df_final)  # This will print the entire DataFrame

    return df_final

# Process the DataFrame using the function
df_processed = PD_Week1_2024(df)

# Save the resulting DataFrame to a new CSV file
output_path = r"C:\Users\OlivierNewman\Documents\Prepin data\2024\Week 1\Processed_PD_Week1_2024.csv"
df_processed.to_csv(output_path, index=False)

# Print confirmation
print(f"Processed data saved to {output_path}")
