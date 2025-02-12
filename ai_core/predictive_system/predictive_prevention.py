import json
import time
import psutil
from datetime import datetime, timedelta

# 📂 Fichiers pour les données
HISTORY_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/adaptive_system/cpu_ram_history.json"
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/predictive_system/prevention_log.txt"

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

# ✅ Mode prévention en cas de surcharge CPU/RAM
def prevention_mode():
    history = load_history()
    current_time = datetime.now().strftime("%H:%M")
    actual_cpu = psutil.cpu_percent(interval=1)
    actual_ram = psutil.virtual_memory().percent

    if actual_cpu > 80:
        log_message(f"⚠️ Alerte : CPU élevé ({actual_cpu}%) - Activation du Mode Économie...")
        history[current_time] = {"cpu": actual_cpu * 0.8, "ram": actual_ram}
        save_history(history)
        time.sleep(10)  # Pause de 10s pour laisser souffler le système

    if actual_ram > 90:
        log_message(f"⚠️ Alerte : RAM saturée ({actual_ram}%) - Désactivation temporaire de certaines tâches.")
        history[current_time] = {"cpu": actual_cpu, "ram": actual_ram * 0.8}
        save_history(history)
        time.sleep(10)

    if actual_cpu > 85 and actual_ram > 95:
        log_message("🚨 CRITIQUE : Surcharge CPU/RAM - Arrêt temporaire des processus non essentiels.")
        time.sleep(15)  # Pause plus longue en cas de surcharge totale

# ✅ Boucle de surveillance proactive
def prevention_loop():
    log_message("🚀 Activation du mode prévention CPU/RAM...")
    while True:
        prevention_mode()
        time.sleep(30)  # Vérification toutes les 30 secondes

# ✅ Exécution
if __name__ == "__main__":
    prevention_loop()
