from datetime import datetime
import os

# Generate the database file name based on the current datetime
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
db_file = f"mqtt_dump_{current_time}.csv"
whole_path_global = "a"

def check_path(path):
    if not os.path.exists(path):
        # Create the directory if it does not exist
        os.makedirs(path)
        print(f'>>> [csv helper] Directory {path} created.')
    else:
        print(f'>>> [csv helper] Directory {path} already exists.')


# Create the database and table if they don't exist
def init_db(path):
    whole_path = path+db_file
    global whole_path_global
    whole_path_global = whole_path
    print(f">>> [csv helper] Create file: path, whole_path_global, whole_path:")
    print(path)
    print(whole_path_global)
    print(whole_path)
    # Create the CSV file if it does not exist
    if not os.path.exists(whole_path):
        with open(whole_path, "w") as f:
            f.write("timestamp;topic;message\n")
        print(f">>> [csv helper] CSV file created: {whole_path}")
    else:
        print(f">>> [csv helper] CSV file already exists: {whole_path}")
    

def insert_message(message, topic):
    # Remove tabs and newlines from message
    clean_message = message.replace('\n', '').replace('\r', '').replace('\t', '')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(whole_path_global, "a") as f:
        f.write(f"{timestamp};{topic};{clean_message}\n")