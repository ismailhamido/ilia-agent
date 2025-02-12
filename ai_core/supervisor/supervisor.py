import sys
import os
import os
import sys
import time
from datetime import datetime

# 📂 Définition des chemins absolus des modules
BASE_DIR = os.path.abspath("C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core")
SELF_OPTIMIZER_PATH = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/self_optimizer/self_optimizer.py"
AUTO_ADAPT_PATH = os.path.join(BASE_DIR, "auto_adapt.py")

# 📂 Fichier de logs du superviseur
LOG_FILE = os.path.join(BASE_DIR, "supervisor", "supervisor_log.txt")

def log_action(message):
    """Enregistre une action dans les logs avec un timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

def check_system_status():
    """Vérifie l'état actuel du CPU et de la RAM."""
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    log_action(f"📊 État système : CPU {cpu_usage}%, RAM {ram_usage}%")
    return cpu_usage, ram_usage

def run_module(module_path, module_name):
    """Exécute un module en vérifiant s'il existe et gère les erreurs éventuelles."""
    if os.path.exists(module_path):
        log_action(f"✅ Exécution du module : {module_name}")
        os.system(f"python {module_path}")
    else:
        log_action(f"⚠️ Module introuvable : {module_name}")

def supervisor_loop():
    """Boucle principale du superviseur qui surveille et exécute les modules IA."""
    log_action("🚀 Démarrage du superviseur IA...")

    while True:
        check_system_status()

        # Vérification et exécution des modules
        run_module(SELF_OPTIMIZER_PATH, "Self-Optimizer")
        run_module(AUTO_ADAPT_PATH, "Auto-Adapt")

        log_action("🔄 Supervision en cours, prochaine analyse dans 60 secondes...")
        time.sleep(60)

if __name__ == "__main__":
    supervisor_loop()
