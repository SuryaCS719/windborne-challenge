import requests

# URL of WindBorne live data
url = "https://a.windbornesystems.com/treasure/00.json"

# Fetch the data
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Check if the outermost data is a list
if isinstance(data, list):
    for entry in data:
        if isinstance(entry, list) and len(entry) == 3:
            latitude = entry[0]
            longitude = entry[1]
            altitude = entry[2]

            print(f"Balloon Position: Latitude = {latitude}, Longitude = {longitude}, Altitude = {altitude} meters")
        else:
            print("Skipping invalid entry:", entry)
else:
    print("Warning: Unexpected data format from API:", data)

