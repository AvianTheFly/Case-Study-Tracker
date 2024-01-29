import sqlite3

def connect_db():
    return sqlite3.connect('medicine_tracking.db')

def read_records(tracking_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT medicine_id, location, date FROM tracking WHERE tracking_number = ?", (tracking_number,))
    records = cursor.fetchall()
    conn.close()
    return records

def delete_record(medicine_id, tracking_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tracking WHERE medicine_id = ? AND tracking_number = ?", (medicine_id, tracking_number))
    conn.commit()
    conn.close()

def display_history(records, tracking_number):
    if records:
        print(f"Tracking History for Tracking Number: {tracking_number}:")
        for record in records:
            medicine_id, location, date = record
            print(f" - {date}: {location} (Medicine ID: {medicine_id})")
    else:
        print("No records found for this tracking number.")

def display_all_records():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT medicine_id, tracking_number, location, date FROM tracking")
    records = cursor.fetchall()
    conn.close()

    if records:
        print("All Records in Database:")
        for record in records:
            medicine_id, tracking_number, location, date = record
            print(f" - Medicine ID: {medicine_id}, Tracking Number: {tracking_number}, Location: {location}, Date: {date}")
    else:
        print("No records in the database.")

def main():
    print("Medicine Tracking Operations")
    print("1: Read Records, 2: Delete Record, 3: Display All Records")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        tracking_number = input("Enter Tracking Number to read: ")
        records = read_records(tracking_number)
        display_history(records, tracking_number)
    elif choice == '2':
        medicine_id = input("Enter Medicine ID to delete: ")
        tracking_number = input("Enter Tracking Number to delete: ")
        delete_record(medicine_id, tracking_number)
        print("Record deleted successfully.")
    elif choice == '3':
        display_all_records()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
