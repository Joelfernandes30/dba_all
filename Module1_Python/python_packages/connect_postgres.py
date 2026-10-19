
import psycopg2

try:
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Joel@123",
        host="localhost"
    )

    print("Connection established successfully!")

    # Create a cursor
    cursor = conn.cursor()

    # SQL query to create the table
    sql_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        email VARCHAR(50)
    )
    """

    # Execute the query
    cursor.execute(sql_query)

    # Save the changes
    conn.commit()

    print("Table created successfully!")

except Exception as e:
    print("Error:", e)

finally:
    # Close resources if they were created
    if 'cursor' in locals():
        cursor.close()

    if 'conn' in locals() and not conn.closed:
        conn.close()
        print("Database connection closed.")
