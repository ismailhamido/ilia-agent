# -*- coding: utf-8 -*-
import os
import time
import json
from datetime import datetime
from ai_core.auto_evolution.adaptive_learning import analyze_trends

# 📂 Chemins des fichiers
script_dir = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution"
log_file = os.path.join(script_dir, "evolution_log.txt")
performance_tracker = os.path.join(script_dir, "performance_tracker.json")

# 🔧 Seuils d'évolution
ADAPTIVE_THRESHOLD_CPU = 75  # Seuil d'alerte CPU pour adaptation
ADAPTIVE_THRESHOLD_RAM = 80  # Seuil d'alerte RAM pour adaptation
ANALYSIS_INTERVAL = 30  # Intervalle d'analyse en secondes

def log_action(message):
    """Enregistre une action dans les logs avec un timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

def track_performance():
    """Analyse et enregistre la performance actuelle de l'IA."""
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    log_action(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%")

    performance_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu": cpu_usage,
        "ram": ram_usage
    }

    with open(performance_tracker, "w", encoding="utf-8") as file:
        json.dump(performance_data, file, indent=4)

    return cpu_usage, ram_usage

def adapt_evolution():
    """Adapte les paramètres d'évolution en fonction des performances et des tendances détectées."""
    cpu_usage, ram_usage = track_performance()
    analyze_trends(cpu_usage, ram_usage)

    if cpu_usage > ADAPTIVE_THRESHOLD_CPU or ram_usage > ADAPTIVE_THRESHOLD_RAM:
        log_action("⚠️ Charge élevée détectée, ajustement des paramètres d'évolution...")
        return max(ANALYSIS_INTERVAL * 2, 120)  # Augmentation de l'intervalle pour alléger la charge
    else:
        log_action("✅ Charge stable, maintien des paramètres d'évolution.")
        return max(ANALYSIS_INTERVAL / 1.5, 15)  # Accélération si la charge est basse

if __name__ == "__main__":
    log_action("🚀 Lancement du moteur d'évolution automatique...")

    while True:
        next_interval = adapt_evolution()
        log_action(f"⏳ Prochain cycle d'analyse dans {next_interval} secondes.")
        # Remplacé pour optimisation
next_interval)
