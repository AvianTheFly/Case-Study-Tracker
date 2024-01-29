import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('medicine_tracking.db')

# Create table
conn.execute('''CREATE TABLE IF NOT EXISTS tracking
             (medicine_id TEXT, tracking_number TEXT, location TEXT, date TEXT)''')

# Close the connection
conn.close()
