import sqlite3
import random

def connect_db():
    return sqlite3.connect('medicine_tracking.db')

def add_record(medicine_id, tracking_number, location, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tracking (medicine_id, tracking_number, location, date) VALUES (?, ?, ?, ?)",
                   (medicine_id, tracking_number, location, date))
    conn.commit()
    conn.close()

def get_records(tracking_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tracking WHERE tracking_number = ?", (tracking_number,))
    records = cursor.fetchall()
    conn.close()
    return records

def delete_records(tracking_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tracking WHERE tracking_number = ?", (tracking_number,))
    conn.commit()
    conn.close()

def test_tracking_system():
    # Generate a random tracking number for testing
    tracking_number = str(random.randint(1000, 9999))

    # Step 1: Add two records with the same tracking number
    add_record("Med1", tracking_number, "Location1", "2024-01-01")
    add_record("Med2", tracking_number, "Location2", "2024-01-02")

    # Step 2: Retrieve and print the records
    records = get_records(tracking_number)
    print(f"Records retrieved for tracking number {tracking_number}:")
    for record in records:
        print(record)

    # Step 3: Delete the records
    delete_records(tracking_number)
    print(f"Records with tracking number {tracking_number} have been deleted.")

    # Verify deletion
    records_post_deletion = get_records(tracking_number)
    if not records_post_deletion:
        print("Deletion successful.")
    else:
        print("Deletion failed.")

if __name__ == "__main__":
    test_tracking_system()
