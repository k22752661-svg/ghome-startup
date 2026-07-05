import json
import urllib.request

# Change this to your RAW GitHub config.json link
CONFIG_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/ghome-startup/main/config.json"

def get_config():
    try:
        response = urllib.request.urlopen(CONFIG_URL, timeout=10)
        data = response.read().decode("utf-8")
        return json.loads(data)
    except Exception:
        return None
