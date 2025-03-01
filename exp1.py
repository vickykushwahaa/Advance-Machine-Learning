import sqlite3

# Connect to the database

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

# Execute a query to retrieve data

cursor.execute('SELECT * FROM example_table')

rows = cursor.fetchall() # Fetch all rows returned by the query

# Process the retrieved data

for row in rows:

print(row) # You can access the columns in the row using row[0], row[1], etc.

# Close the database connection

conn.close()
