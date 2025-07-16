import requests
import time
import json
from utils import send_telegram_message
from constants import LOCATIONS, CHECK_INTERVAL, HEARTBEAT_INTERVAL
from datetime import datetime

url = "https://trouverunlogement.lescrous.fr/api/fr/search/41"

payload = {
    "idTool": 41,
    "need_aggregation": True,
    "page": 1,
    "pageSize": 24,
    "sector": None,
    "occupationModes": ["alone", "couple", "house_sharing"],
    "location": [
        {"lon": 3.0532561, "lat": 45.8183838},
        {"lon": 3.1721761, "lat": 45.7556941}
    ],
        
    "residence": None,
    "precision": 6,
    "equipment": [],
    "price": {"max": 10000000},
    "area": {"min": 0},
    "toolMechanism": "residual",
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/ld+json, application/json",
    "User-Agent": "Mozilla/5.0"
}



def check_crous(place: str, location: list):
    try:


        now = datetime.now()
        formatted_string = now.strftime("%Y-%m-%d %H:%M:%S")

        payload['location'] = location
        response = requests.post(url, headers=headers,
                                 data=json.dumps(payload))
        response.raise_for_status()

        data = response.json()
        total = data.get('results', {}).get("total", {}).get('value', 0)

        print(f'Checked {place} : {total} logements at {formatted_string}  ...')

        if total > 0:
            send_telegram_message(
                f'🚨 {total} logements disponibles in {place} !\n👉 https://trouverunlogement.lescrous.fr/')
    except Exception as e:
        send_telegram_message(
            f"❌ Erreur lors de la vérification des logements : {e}")


def check_all_crous():
    for place, location in LOCATIONS.items():
        check_crous(place, location)




def main():
    last_heartbeat = time.time()

    while True:
        check_all_crous()

        # Check if it's time to send a heartbeat message
        if time.time() - last_heartbeat >= HEARTBEAT_INTERVAL:
            send_telegram_message("✅ Le bot fonctionne toujours")
            last_heartbeat = time.time()

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
