import os
import json
import time
from datetime import datetime

# 📂 Fichier de suivi des performances
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/evolution_log.txt"
PERFORMANCE_TRACKER = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/performance_tracker.json"

# 📊 Seuils d'optimisation dynamique
THRESHOLD_CPU_HIGH = 85  # Si CPU dépasse 85%, ralentir l’analyse
THRESHOLD_CPU_LOW = 50   # Si CPU < 50%, accélérer l’analyse
THRESHOLD_RAM_HIGH = 90  # Si RAM dépasse 90%, ralentir l’analyse
THRESHOLD_RAM_LOW = 60   # Si RAM < 60%, accélérer l’analyse

# ⏳ Intervalle d’analyse dynamique
ANALYSIS_INTERVAL = 30  # Par défaut, 30 secondes

def log_action(message):
    """Enregistre une action dans le fichier log avec un timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

def save_performance(cpu, ram):
    """Sauvegarde les performances actuelles pour analyse future."""
    performance_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu": cpu,
        "ram": ram
    }
    with open(PERFORMANCE_TRACKER, "w", encoding="utf-8") as file:
        json.dump(performance_data, file, indent=4)

def analyze_performance():
    """Analyse les performances actuelles et ajuste dynamiquement les paramètres."""
    global ANALYSIS_INTERVAL

    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    log_action(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%")

    # 📈 Ajustement dynamique
    if cpu_usage > THRESHOLD_CPU_HIGH or ram_usage > THRESHOLD_RAM_HIGH:
        log_action("⚠️ Charge élevée détectée ! Ralentissement du cycle d’analyse.")
        ANALYSIS_INTERVAL = min(ANALYSIS_INTERVAL * 1.5, 120)  # Augmente jusqu’à max 120s
    elif cpu_usage < THRESHOLD_CPU_LOW and ram_usage < THRESHOLD_RAM_LOW:
        log_action("✅ Charge basse détectée ! Accélération du cycle d’analyse.")
        ANALYSIS_INTERVAL = max(ANALYSIS_INTERVAL / 1.5, 15)  # Diminue jusqu’à min 15s

    log_action(f"🔄 Nouvel intervalle d’analyse : {ANALYSIS_INTERVAL} secondes.")
    save_performance(cpu_usage, ram_usage)

if __name__ == "__main__":
    log_action("🚀 Démarrage du moteur d’auto-optimisation...")

    while True:
        analyze_performance()
        # Remplacé pour optimisation
ANALYSIS_INTERVAL)
