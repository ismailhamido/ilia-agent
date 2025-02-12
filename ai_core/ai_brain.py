import os
import time
from datetime import datetime

# 📂 Fichier de logs de l'IA
log_file = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/ai_log.txt"

# 🔥 Seuils d'optimisation
CPU_HIGH_THRESHOLD = 80
RAM_HIGH_THRESHOLD = 85
ANALYSIS_INTERVAL = 30

def log_action(message):
    """Enregistre une action dans les logs avec un horodatage."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

def analyze_performance():
    """Analyse la charge CPU et RAM pour ajuster l'IA."""
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent

    log_action(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%")

    if cpu_usage > CPU_HIGH_THRESHOLD or ram_usage > RAM_HIGH_THRESHOLD:
        log_action("⚠️ Charge élevée détectée ! Passage en mode adaptatif.")
        adjust_settings(emergency=True)
    else:
        log_action("✅ Charge normale. Ajustement optimal.")
        adjust_settings(emergency=False)

def adjust_settings(emergency=False):
    """Ajuste les paramètres d'analyse selon la charge détectée."""
    global ANALYSIS_INTERVAL
    if emergency:
        ANALYSIS_INTERVAL = min(ANALYSIS_INTERVAL * 2, 120)
    else:
        ANALYSIS_INTERVAL = max(ANALYSIS_INTERVAL / 1.5, 15)

    log_action(f"🔄 Nouvel intervalle d'analyse : {ANALYSIS_INTERVAL} secondes.")

if __name__ == "__main__":
    log_action("🚀 Lancement de l'IA Ilia...")
    while True:
        analyze_performance()
        time.sleep(ANALYSIS_INTERVAL)
