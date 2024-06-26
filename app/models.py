import time
import requests
from zapv2 import ZAPv2

zap_url = "http://127.0.0.1:8080"
api_key = "3vra30d326kr9csl8bj6hsvmd9"
zap = ZAPv2(apikey=api_key)

scan_id_list = []


def add_id(id_scan):
    scan_id.append({"id_scan": id_scan})
    

def get_list_scan_models():
    return scan_id_list


def start_scan_models(target_url):
    scan_url = f"{zap_url}/JSON/ascan/action/scan/?url={target_url}&apikey={api_key}"
    response = requests.get(scan_url)
    scan_id = response.json().get("scan")
    scan_id_list.append({"scan_id": scan_id})
    return scan_id_list


def get_scan_status():
    status_url = f"{zap_url}/JSON/ascan/view/status/?scanId={scan_id}"
    response = requests.get(status_url)
    status = response.json().get("status")
    return status


def get_scan_results(target_url):
    results_url = f"{zap_url}/JSON/core/view/alerts/?baseurl={target_url}&apikey={api_key}"
    response = requests.get(results_url)
    return response.json()


if __name__ == "__main__":

    scan_id = start_scan_models(target_url)
    print(f"Iniciando varredura no alvo: {target_url}, ID da varredura: {scan_id}")
    
    results = get_scan_results()
    print("Resultados da varredura:")
    for alert in results.get("alerts", []):
        print(
            f"Alerta:{alert.get('alert')},Severidade:{alert.get('risk')}, Descrição:{alert.get('description')}"
        )
