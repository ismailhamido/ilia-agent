import psutil
import time
from datetime import datetime

# 📂 Fichier log de gestion des tâches
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/task_manager/task_log.txt"

# ✅ Fonction pour écrire dans le log
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Priorisation dynamique des tâches
def manage_tasks():
    log_message("🚀 Lancement de la gestion avancée des tâches...")

    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        log_message(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%")

        # Définition des priorités
        if cpu_usage > 80 or ram_usage > 95:
            log_message("⚠️ Charge critique ! Seules les tâches essentielles seront exécutées.")
            # Simuler la mise en pause de tâches secondaires
            time.sleep(10)
        elif cpu_usage > 60 or ram_usage > 90:
            log_message("⚡ Charge élevée, réduction des tâches secondaires...")
            time.sleep(7)
        else:
            log_message("✅ Charge normale, toutes les tâches fonctionnent normalement.")
            time.sleep(3)

# ✅ Exécution de la gestion des tâches
if __name__ == "__main__":
    manage_tasks()
