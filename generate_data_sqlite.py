from faker import Faker
import random
import sqlite3
from datetime import datetime, timedelta

fake = Faker()

# Function to generate random birth dates
def generate_birth_date():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2005, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

# Function to generate sample data
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        birth_day = generate_birth_date()
        email_address = fake.email()
        local_address = fake.address()
        data.append((first_name, last_name, birth_day, email_address, local_address))
    return data

# Create SQLite database and table
conn = sqlite3.connect('sample_data.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS persons (
                person_id INTEGER PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                birth_day DATE,
                email_address VARCHAR(150) UNIQUE NOT NULL,
                local_address VARCHAR(200)
                )''')

# Generate and insert sample data
sample_data = generate_data(100)

for row in sample_data:
    cursor.execute('''INSERT INTO persons (first_name, last_name, birth_day, email_address, local_address) 
                      VALUES (?, ?, ?, ?, ?)''', row)

conn.commit()
conn.close()
print("Sample data generated and inserted into the database.")
