import os
import json
import time
import subprocess
import psutil
from datetime import datetime

# 📂 Chemins des fichiers
CONFIG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/adaptive_config.json"
PERFORMANCE_TRACKER = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/performance_tracker.json"

# ✅ Chargement de la configuration adaptative
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {"cpu_threshold": 80, "ram_threshold": 85, "adjustment_factor": 1.2}

# ✅ Sauvegarde de la configuration mise à jour
def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)

# ✅ Analyse des performances et adaptation dynamique
def adaptive_adjustment():
    print("🔄 Adaptation en fonction des performances...")
    config = load_config()
    
    if os.path.exists(PERFORMANCE_TRACKER):
        with open(PERFORMANCE_TRACKER, "r", encoding="utf-8") as file:
            data = json.load(file)
            if "history" in data and data["history"]:
                latest = data["history"][-1]
                cpu_usage, ram_usage = latest["cpu"], latest["ram"]
                
                if cpu_usage > config["cpu_threshold"] or ram_usage > config["ram_threshold"]:
                    print("⚠️ Charge élevée détectée, ajustement des paramètres...")
                    config["cpu_threshold"] *= config["adjustment_factor"]
                    config["ram_threshold"] *= config["adjustment_factor"]
                else:
                    print("✅ Charge normale, optimisation stable.")
    
    save_config(config)

# ✅ Boucle principale d’adaptation
def self_adapt():
    print("🚀 Lancement du moteur d’adaptation intelligente...")
    while True:
        adaptive_adjustment()
        # Remplacé pour optimisation
10)  # Vérification toutes les 10 secondes

# ✅ Exécution du module
if __name__ == "__main__":
    self_adapt()

