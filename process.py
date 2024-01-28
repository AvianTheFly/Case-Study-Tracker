import json

def create_tracking_data(file_path):
    tracking_data = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                entry = json.loads(line.strip())
                track_number = entry['tracking_number']

                if track_number not in tracking_data:
                    tracking_data[track_number] = []

                tracking_data[track_number].append({
                    'medicine_id': entry['medicine_id'],
                    'location': entry['location'],
                    'timestamp': entry['date']
                })

    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")

    return tracking_data

def query_by_tracking_number(data, tracking_number):
    return data.get(tracking_number, "No history found for this tracking number.")

def main():
    file_path = 'data.txt'
    data = create_tracking_data(file_path)

    tracking_number = input("Enter a tracking number to get history: ")
    history = query_by_tracking_number(data, tracking_number)
    print(json.dumps(history, indent=4))

if __name__ == "__main__":
    main()
