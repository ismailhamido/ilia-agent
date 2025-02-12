import json
import time
import psutil
from datetime import datetime, timedelta

# 📂 Fichiers pour les données
HISTORY_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/adaptive_system/cpu_ram_history.json"
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/predictive_system/anomaly_log.txt"

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

# ✅ Sauvegarde des nouvelles données
def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

# ✅ Détection des anomalies sur la charge CPU/RAM
def detect_anomaly():
    history = load_history()
    current_time = datetime.now().strftime("%H:%M")
    previous_time = (datetime.now() - timedelta(minutes=1)).strftime("%H:%M")

    if previous_time in history:
        actual_cpu = psutil.cpu_percent(interval=1)
        actual_ram = psutil.virtual_memory().percent

        prev_cpu = history[previous_time]["cpu"]
        prev_ram = history[previous_time]["ram"]

        cpu_variation = abs(actual_cpu - prev_cpu)
        ram_variation = abs(actual_ram - prev_ram)

        if cpu_variation > 20:  # Si le CPU change de plus de 20% en 1 min
            log_message(f"⚠️ Anomalie CPU détectée : {cpu_variation}% de variation en 1 min !")
            history[current_time] = {"cpu": round(prev_cpu * 0.7 + actual_cpu * 0.3, 1), "ram": prev_ram}
            save_history(history)

        if ram_variation > 15:  # Si la RAM change de plus de 15% en 1 min
            log_message(f"⚠️ Anomalie RAM détectée : {ram_variation}% de variation en 1 min !")
            history[current_time] = {"cpu": prev_cpu, "ram": round(prev_ram * 0.7 + actual_ram * 0.3, 1)}
            save_history(history)

# ✅ Boucle de détection des anomalies
def anomaly_detection_loop():
    log_message("🚀 Activation de la détection des anomalies CPU/RAM...")
    while True:
        detect_anomaly()
        time.sleep(30)  # Vérification toutes les 30 secondes

# ✅ Exécution
if __name__ == "__main__":
    anomaly_detection_loop()
