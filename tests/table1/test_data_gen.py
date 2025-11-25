from faker import Faker
import csv

# Initialize faker
fake = Faker()

# Number of records you want
num_records = 20   # change as needed

# CSV file name
filename = "s3"+'/'+"customers_{date}.csv"

# Header
header = ["CustomerID", "Name", "Email", "Phone", "City"]

# Generate data
data = [header]
for i in range(1, num_records + 1):
    customer_id = i
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    city = fake.city()

    data.append([customer_id, name, email, phone, city])

# Write CSV file
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Dynamic CSV '{filename}' created with {num_records} customer rows!")
