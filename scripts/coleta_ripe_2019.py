import requests
import json

ases = ['58224', '44244', '57218', '16322', '197207']

start_time = "2019-11-15T00:00"
end_time = "2019-11-27T23:59"

def fetch_bgp_updates(as_number, start, end):
    print(f"Coletando dados de BGP Updates para AS{as_number}...")
    url = f"https://stat.ripe.net/data/bgp-update-activity/data.json?resource=AS{as_number}&starttime={start}&endtime={end}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        filename = f"bgp_updates_AS{as_number}_2019.json"
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Dados salvos com sucesso em {filename}")
    else:
        print(f"Erro na coleta do AS{as_number}: {response.status_code}")

for asn in ases:
    fetch_bgp_updates(asn, start_time, end_time)