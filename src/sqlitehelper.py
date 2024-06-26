import sqlite3
from datetime import datetime

# Generate the database file name based on the current datetime
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
db_file = f"mqtt_dump_{current_time}.db"
whole_path_global = "a"
# Define the SQL statement to create the table
create_table_sql = """
CREATE TABLE IF NOT EXISTS messages (
    lp INTEGER PRIMARY KEY,
    received_time DATETIME,
    message TEXT,
    topic TEXT
)
"""

# Function to insert a message into the database
def insert_message(message, topic):
    global whole_path_global
    received_time = datetime.now()
    conn = sqlite3.connect(whole_path_global)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (received_time, message, topic) VALUES (?, ?, ?)", (received_time, message, topic))
    conn.commit()
    conn.close()


# Create the database and table if they don't exist
def init_db(path):
    print(path)
    # print(whole_path)
    whole_path = path+db_file
    global whole_path_global
    whole_path_global = whole_path
    print(f"Create file: whole_path:")
    print(whole_path_global)
    conn = sqlite3.connect(whole_path)
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.close()

# Example usage: Insert a message into the database
# received_time = datetime.now()
# message = "Hello, world!"
# topic = "test/topic"
# insert_message(received_time, message, topic)
