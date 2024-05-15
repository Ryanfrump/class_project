import psycopg2
import random

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="class_project",
    user="postgres",
    password="Packers0192!",
    host="localhost"
)

# Create a cursor object using the connection
cur = conn.cursor()

# Execute the SQL query
cur.execute("SELECT * FROM workout WHERE workout.muscle_group_id=2")

# Fetch all rows into a list
rows = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

# Choose 3 random rows from the list
random_rows = random.sample(rows,3)

# Now you have a variable 'random_rows' containing 3 randomly chosen rows from the result set
for row in random_rows:
    print(row[1])