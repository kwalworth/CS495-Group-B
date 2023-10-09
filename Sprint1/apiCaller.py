import requests, json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['BamaBasketball']
collection = db['players']

api1_url = 'https://cloud.hawkindynamics.com/api/dev/athletes'

bearer_token = 'bearer_token_here'

headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'  # Adjust content type as needed
}

response1 = requests.get(api1_url, headers=headers)

try:
    data = response1.json()
    if not data:
        print("API response is empty.")
    else:
        # Deserialize the JSON data into a Python dictionary
        json_data = json.loads(json.dumps(data))

        print(json_data)

        for entry in json_data['data']:
            player_data = {
                'name': entry['name'],
                'Training Impulse': 'temp',
                'Training Status': 'temp',
                'Calories': 'temp',
                'Duration': 'temp',
                'Accumulated Acceleration Load': 'temp',
                'Accumulated Acceleration/min': 'temp',
                'Total Distance for session (miles)': 'temp',
                'Total Distance for week (miles)': 'temp',
                'Max Speed (mph)': 'temp',
                'Max Jump Height (inches)': 'temp',
                'Jump Count': 'temp',
                'Changes of Orientation': 'temp',
                'Jump Height': 'temp',
                'RSI': 'temp',
                'Time to Takeoff': 'temp',
                'Breaking Phase': 'temp',
                'Peak Relative Propulsive Power': 'temp',
                'Braking Power': 'temp',
                'Braking Net Impulse': 'temp',
                'Propulsive Net Impulse': 'temp',
                'L\R Avg. Braking Force': 'temp'
            }

        # Insert the Python dictionary into the MongoDB collection
            collection.insert_one(player_data)

        print("Data inserted successfully.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

client.close()