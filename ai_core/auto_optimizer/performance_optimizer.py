import os
import psutil
import time
from datetime import datetime

# 📂 Fichier log de performance
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_optimizer/performance_log.txt"

# ✅ Fonction pour écrire dans le log
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Mode Économie avancé : Ajustement dynamique de la charge
def low_power_mode():
    log_message("⚡ Mode Économie activé : Réduction progressive des tâches non essentielles...")
    interval = 5  # Délai de base
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        if cpu_usage > 80 or ram_usage > 95:
            interval = 10  # Charge critique, on ralentit fortement
        elif cpu_usage > 60 or ram_usage > 90:
            interval = 7  # Charge élevée, on ralentit modérément
        elif cpu_usage < 50 and ram_usage < 85:
            log_message("✅ Charge normale détectée. Reprise du fonctionnement habituel.")
            break  # On sort du mode économie

        log_message(f"⏳ Pause de {interval}s pour réduire la charge...")
        time.sleep(interval)  # Ajustement dynamique

# ✅ Optimisation dynamique des performances
def optimize_performance():
    log_message("🚀 Lancement de l'optimisation des performances...")

    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        log_message(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%")

        # Activation du Mode Économie amélioré
        if cpu_usage > 60 or ram_usage > 90:
            low_power_mode()
        else:
            time.sleep(2)  # Analyse normale

# ✅ Exécution de l'optimisation
if __name__ == "__main__":
    optimize_performance()
