import json
import time
import psutil
from datetime import datetime, timedelta

# 📂 Fichiers pour l'historique et les logs
HISTORY_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/adaptive_system/cpu_ram_history.json"
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/predictive_system/prediction_log.txt"

# ✅ Fonction pour écrire dans le log
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Chargement de l'historique CPU/RAM
def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# ✅ Prédiction de la charge future
def predict_future_load():
    history = load_history()
    future_time = (datetime.now() + timedelta(minutes=1)).strftime("%H:%M")

    if future_time in history:
        predicted_cpu = history[future_time]["cpu"]
        predicted_ram = history[future_time]["ram"]
        log_message(f"📈 Prédiction pour {future_time} → CPU : {predicted_cpu}%, RAM : {predicted_ram}%")

        return predicted_cpu, predicted_ram
    else:
        log_message(f"⚠️ Aucune donnée historique pour {future_time}, pas de prédiction possible.")
        return None, None

# ✅ Ajustement dynamique basé sur la prédiction
def adaptive_prediction():
    log_message("🚀 Lancement du gestionnaire prédictif...")

    while True:
        predicted_cpu, predicted_ram = predict_future_load()

        if predicted_cpu and predicted_ram:
            if predicted_cpu > 80 or predicted_ram > 95:
                log_message("⚠️ PRÉDICTION : Charge élevée détectée, activation du Mode Économie anticipé.")
                time.sleep(10)
            elif predicted_cpu > 60 or predicted_ram > 90:
                log_message("⚡ PRÉDICTION : Charge modérée attendue, ajustement en cours...")
                time.sleep(7)
            else:
                log_message("✅ PRÉDICTION : Charge normale prévue, fonctionnement standard.")
                time.sleep(3)
        else:
            time.sleep(5)

# ✅ Exécution du gestionnaire prédictif
if __name__ == "__main__":
    adaptive_prediction()
