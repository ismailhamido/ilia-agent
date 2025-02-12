import psutil
import json
import time
from datetime import datetime

# 📂 Chemins des fichiers
HISTORICAL_DATA_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/historical_data.json"

# ✅ Chargement des données historiques
def load_historical_data():
    try:
        with open(HISTORICAL_DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"history": []}

# ✅ Sauvegarde des performances
def save_historical_data(data):
    with open(HISTORICAL_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# ✅ Surveillance avancée du CPU et RAM
def monitor_performance():
    log_action("🚀 Lancement de la surveillance avancée des performances...")
    historical_data = load_historical_data()

    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 📊 Enregistrement des données
        historical_data["history"].append({"timestamp": timestamp, "cpu": cpu_usage, "ram": ram_usage})
        save_historical_data(historical_data)

        log_action(f"📊 CPU: {cpu_usage}%, RAM: {ram_usage}% - Données enregistrées.")

        # Remplacé pour optimisation
10)  # Vérification toutes les 10 secondes

# ✅ Exécution du module
if __name__ == "__main__":
    monitor_performance()
