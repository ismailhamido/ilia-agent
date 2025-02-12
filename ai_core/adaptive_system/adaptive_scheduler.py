import time
import psutil
from datetime import datetime
import json

# 📂 Fichier log de planification
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/adaptive_system/schedule_log.txt"
HISTORY_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/adaptive_system/cpu_ram_history.json"

# ✅ Fonction pour écrire dans le log
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Sauvegarde des données CPU/RAM pour l’analyse des tendances
def save_usage(cpu_usage, ram_usage):
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history = {}

    hour = datetime.now().strftime("%H:%M")
    history[hour] = {"cpu": cpu_usage, "ram": ram_usage}

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

# ✅ Mode Adaptatif : Ajustement des intervalles d'analyse
def adaptive_analysis():
    log_message("🚀 Lancement de l'analyse adaptative...")

    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        save_usage(cpu_usage, ram_usage)

        log_message(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%")

        # Détection des tendances
        if cpu_usage > 80 or ram_usage > 95:
            log_message("⚠️ Charge critique ! Augmentation de l’intervalle à 10s.")
            time.sleep(10)
        elif cpu_usage > 60 or ram_usage > 90:
            log_message("⚡ Charge élevée, intervalle à 7s.")
            time.sleep(7)
        else:
            log_message("✅ Charge normale, intervalle à 3s.")
            time.sleep(3)

# ✅ Exécution de l’analyse adaptative
if __name__ == "__main__":
    adaptive_analysis()
