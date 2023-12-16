import urllib.request
import json
import pymysql

# Function to perform the API request
def perform_api_request():
    url = "https://geo.api.gouv.fr/communes/"
    params = {"fields": "population"}

    try:
        # Create the full URL with parameters
        full_url = f"{url}?{urllib.parse.urlencode(params)}"

        # Perform the GET request
        with urllib.request.urlopen(full_url) as response:
            # Check if the request was successful (status code 200)
            if response.getcode() == 200:
                data = json.load(response)
                return data
            else:
                print(f"Error during API request: {response.getcode()} {response.read().decode('utf-8')}")
                return None

    except urllib.error.URLError as e:
        print(f"Error during API request: {e}")
        return None

# API data
api_data = perform_api_request()

# Database connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="IntegrationDatabase"  # Replace with your actual database name
)

# Create a cursor
cursor = connection.cursor()

# Iterate over API data and update the database
for entry in api_data:
    code_postal = entry.get("codePostal", "")
    population_info = entry.get("population", 0)

    # Update query
    update_query = "UPDATE COMMUNES SET Code_postal = %s WHERE Code_postal = %s"
    cursor.execute(update_query, (population_info, code_postal))

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()