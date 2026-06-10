import requests

# The URL to your local server
URL = "http://127.0.0.1:8000/api/v1/speedtester/run"

# Attach your API Key directly to the headers
headers = {
    "X-API-Key": "pn_key_keQCnbDsjfv9kCqdTwadY3hGm-s05gxkNBuXcnIdLZs" # Replace with your actual API key
}

print("🤖 Machine is connecting to the Philippine Navy API...")

# Send the request bypassing the login screen
response = requests.post(URL, headers=headers)

if response.status_code == 200:
    print("✅ Success! Here is the data:")
    print(response.json())
else:
    print(f"❌ Failed! Status Code: {response.status_code}")
    print(response.json())