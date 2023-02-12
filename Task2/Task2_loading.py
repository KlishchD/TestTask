import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime, timedelta
import json 

def load_history(key: str, currencies: str, date_from: datetime) -> str:
	url = "https://api.freecurrencyapi.com/v1/historical"
	headers = {
		"apikey": key
	}
	params = {
		"currencies": currencies,
		"date_from": date_from.isoformat()
	}
	return requests.get(url, params=params, headers=headers).text

def write(data: dict, file_name: str = 'data.json') -> None:
	with open(file_name, 'w') as file:
		file.write(json.dumps(data, indent=2))


history = load_history("c33Kn6uEp0vRn9NGUqOaxq1Fixy7GGB5g1j9X8Un", "EUR", datetime.now() - timedelta(weeks=5))
write(json.loads(history))
