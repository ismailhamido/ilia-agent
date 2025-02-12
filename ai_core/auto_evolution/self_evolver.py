import os
import json
import time
import subprocess
from datetime import datetime

# 📂 Chemins des fichiers
CODE_BASE_PATH = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/"
EVOLUTION_LOG = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/evolution_log.txt"
CONFIG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/adaptive_config.json"

# ✅ Chargement de la configuration
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            config = json.load(file)
            if "evolution_cycles" not in config:
                config["evolution_cycles"] = 0
            return config
    return {"cpu_threshold": 80, "ram_threshold": 85, "adjustment_factor": 1.2, "evolution_cycles": 0}

# ✅ Sauvegarde de la configuration mise à jour
def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)

# ✅ Évolution dynamique du code
def evolve_code():
    print("🔄 Analyse et évolution du code...")
    config = load_config()
    config["evolution_cycles"] += 1
    
    for file_name in os.listdir(CODE_BASE_PATH):
        if file_name.endswith(".py") and file_name not in ["self_evolver.py"]:
            file_path = os.path.join(CODE_BASE_PATH, file_name)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # 📌 Auto-optimisation : remplacer time.sleep() par une attente conditionnelle
            if "time.sleep(" in content:
                content = content.replace("time.sleep(", "# Remplacé pour optimisation\n")
                print(f"✅ Optimisation appliquée : {file_name}")
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
    
    save_config(config)
    log_action("Evolution cycle : " + str(config["evolution_cycles"]))

# ✅ Enregistrement des cycles d'évolution
def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(EVOLUTION_LOG, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Boucle principale d’auto-évolution
def self_evolve():
    print("🚀 Lancement du moteur d’auto-évolution avancée...")
    while True:
        evolve_code()
        time.sleep(20)  # Vérification et évolution toutes les 20 secondes

# ✅ Exécution du module
if __name__ == "__main__":
    self_evolve()

