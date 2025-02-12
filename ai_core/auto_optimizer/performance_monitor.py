import os
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

# ✅ Analyse de la consommation CPU/RAM
def analyze_performance():
    log_message("🚀 Lancement de l'analyse de performance...")
    
    for _ in range(5):  # Test sur 5 cycles
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        log_message(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%")
        
        time.sleep(2)  # Pause entre les analyses

    log_message("✅ Analyse de performance terminée.")

# ✅ Exécution de l'analyse
if __name__ == "__main__":
    analyze_performance()
