# -*- coding: utf-8 -*-
import os
import time
import json
from datetime import datetime
from ai_predictor import collect_data, predict_next_interval

# Chemins des fichiers
log_file = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/ai_log.txt"

def log_action(message):
    """Enregistre une action dans le fichier log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

def adaptive_analysis():
    """Gère l'auto-adaptation de l'IA en ajustant la fréquence d'analyse."""
    log_action("🚀 Démarrage du moteur d'auto-adaptation...")
    interval = 15  # Intervalle de base

    while True:
        cpu_usage, ram_usage = collect_data()
        interval = predict_next_interval()
        
        log_action(f"🔄 Ajustement dynamique : CPU {cpu_usage}%, RAM {ram_usage}%, Nouvel Intervalle : {interval}s")
        time.sleep(interval)

if __name__ == "__main__":
    adaptive_analysis()
