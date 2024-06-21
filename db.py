import sqlite3
import re

def calculate_total_sales():
    conn = sqlite3.connect('Database/store.db')
    cur = conn.cursor()

    cur.execute("SELECT bill_details FROM bill")
    rows = cur.fetchall()

    total_sales = 0.0

    for row in rows:
        bill_details = row[0]

        # Regular expression pattern to capture the total value with the currency symbol
        total_pattern = r'Total\s+Rs\.\s+(\d+\.\d+)'

        # Find total value using regular expression
        total_match = re.search(total_pattern, bill_details)

        if total_match:
            # Extract the numeric part of the total value
            total_value = total_match.group(1)

            # Convert the extracted value to float
            total_float = float(total_value)

            # Accumulate total sales
            total_sales += total_float

    print("Total Sales:", total_sales)

    conn.close()

# Call the function to calculate total sales
calculate_total_sales()
