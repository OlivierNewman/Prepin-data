Steps Performed:
Loading the Data:

The script reads a CSV file containing flight-related data into a pandas DataFrame.
Flow Card Status Transformation:

The script converts the Flow Card? column values from numeric (0 and 1) to categorical strings ('No' and 'Yes').
Splitting and Renaming Flight Details:

The Flight Details column, which contains multiple values separated by slashes (/), is split into separate columns.
These columns are renamed to improve clarity (e.g., Flight Detail 1 becomes Date, Flight Detail 3 becomes Flight_Number).
OD Pair (Origin-Destination) Split:

The OD_Pair column (representing the origin and destination of a flight) is split into two separate columns: Origin and Destination.
Date Conversion:

The Date column is converted to a datetime64[ns] format to ensure that the dates are properly recognized and handled as date objects.
Final DataFrame:

The script retains only relevant columns (e.g., Date, Flight_Number, Origin, Destination, Price, etc.), and outputs a cleaned and well-structured DataFrame.
Saving Processed Data:

After processing the data, the script saves the cleaned DataFrame to a new CSV file for further use or analysis.
Output:
The script outputs the processed data as a CSV file (Processed_PD_Week1_2024.csv), ensuring that the data is clean, well-formatted, and ready for use.
Dependencies:
pandas (for data manipulation and conversion)
Usage:
Simply modify the file paths in the script and run it to process your flight data CSV file. The processed data will be saved to the specified output path.
