from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('medicine_tracking.db')

# Function to check if the record exists in the database
def record_exists(tracking_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tracking WHERE tracking_number = ?", (tracking_number,))
    records = cursor.fetchall()
    conn.close()
    return len(records) > 0

# Function to delete test records from the database
def delete_test_records(tracking_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tracking WHERE tracking_number = ?", (tracking_number,))
    conn.commit()
    conn.close()

# Path to WebDriver and URL of your index.html
driver_path = "path/to/your/webdriver"
url = "http://localhost/path/to/index.html"

# Start a browser session
driver = webdriver.Chrome(driver_path)
driver.get(url)

# Fill out and submit the form twice with the same tracking number
for i in range(2):
    medicine_id_field = driver.find_element_by_id("medicine_id")
    tracking_number_field = driver.find_element_by_id("tracking_number")
    location_field = driver.find_element_by_id("location")

    medicine_id_field.send_keys("TestMed" + str(i))
    tracking_number_field.send_keys("Test1234")
    location_field.send_keys("TestLocation" + str(i))

    location_field.submit()
    time.sleep(2)  # Wait for the form to submit

# Verify if the records were added
if record_exists("Test1234"):
    print("Test records were added successfully.")
else:
    print("Test records were not found in the database.")

# Clean up: delete the test records
delete_test_records("Test1234")
print("Test records deleted.")

# Close the browser
driver.quit()
