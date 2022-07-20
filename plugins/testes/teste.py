
import requests 

apiKey = "5ae2e3f221c38a28845f05b6615597c527436941cc468e6bf42eaaf7"

url = f"http://api.opentripmap.com/0.1/en/places/xid/Q372040?apikey={apiKey}"

response = requests.request("GET", url=url).json()

print(response)