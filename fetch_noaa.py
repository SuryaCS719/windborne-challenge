import requests

# NOAA Weather Alerts API endpoint
url = "https://api.weather.gov/alerts/active"

# Set headers (NOAA requires a "User-Agent" header!)
headers = {
    "User-Agent": "WindBorneChallengeSurya/1.0 (suvalava@ucsc.edu)"
}

# Fetch the data
response = requests.get(url, headers=headers)

# Parse the JSON response
data = response.json()

# Extract the alerts
alerts = data.get("features", [])

print(f"Found {len(alerts)} active weather alerts.\n")

# Print basic info for each alert
for alert in alerts[:10]:  # Only first 10 alerts for now
    properties = alert.get("properties", {})
    event = properties.get("event", "Unknown Event")
    area_desc = properties.get("areaDesc", "Unknown Area")
    severity = properties.get("severity", "Unknown Severity")
    urgency = properties.get("urgency", "Unknown Urgency")
    headline = properties.get("headline", "No Headline")

    print(f"Event: {event}")
    print(f"Area: {area_desc}")
    print(f"Severity: {severity}, Urgency: {urgency}")
    print(f"Headline: {headline}")
    print("-" * 40)

