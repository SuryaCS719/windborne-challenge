import requests
from shapely.geometry import Point, Polygon

# ------------------------
# Step 1: Fetch Balloon Positions
# ------------------------

# Fetch WindBorne balloon data
balloon_url = "https://a.windbornesystems.com/treasure/00.json"
balloon_response = requests.get(balloon_url)
balloon_data = balloon_response.json()

balloon_positions = []

# Extract [latitude, longitude, altitude] triples
if isinstance(balloon_data, list):
    for entry in balloon_data:
        if isinstance(entry, list) and len(entry) == 3:
            latitude, longitude, altitude = entry
            balloon_positions.append((latitude, longitude))

print(f"Fetched {len(balloon_positions)} balloon positions.\n")

# ------------------------
# Step 2: Fetch NOAA Alerts
# ------------------------

# Fetch NOAA alerts
noaa_url = "https://api.weather.gov/alerts/active"
headers = {
    "User-Agent": "WindBorneChallengeSurya/1.0 (suvalava@ucsc.edu)"
}
noaa_response = requests.get(noaa_url, headers=headers)
noaa_data = noaa_response.json()

alerts = noaa_data.get("features", [])

print(f"Fetched {len(alerts)} active weather alerts.\n")

# ------------------------
# Step 3: Match Balloons to Alerts
# ------------------------

# For each alert with geometry, check for nearby balloons
for alert in alerts:
    properties = alert.get("properties", {})
    event = properties.get("event", "Unknown Event")
    severity = properties.get("severity", "Unknown Severity")
    urgency = properties.get("urgency", "Unknown Urgency")

    geometry = alert.get("geometry")
    if geometry and geometry.get("type") == "Polygon":
        coords = geometry.get("coordinates", [[]])[0]  # Get the first polygon
        polygon = Polygon(coords)

        # Check each balloon
        for lat, lon in balloon_positions:
            point = Point(lon, lat)  # Notice: Shapely expects (x=longitude, y=latitude)
            if polygon.contains(point):
                print("🚨 Match Found!")
                print(f"Balloon at (lat={lat}, lon={lon}) is inside a danger zone!")
                print(f"Event: {event}, Severity: {severity}, Urgency: {urgency}")
                print("-" * 50)


