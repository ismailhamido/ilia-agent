import os
import re
import time
import json
from datetime import datetime

# 📂 Chemins des fichiers
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/evolution_log.txt"
REPAIR_LOG = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_repair/repair_log.txt"
KNOWN_ERRORS_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_repair/known_errors.json"

# ✅ Chargement des erreurs connues
def load_known_errors():
    if os.path.exists(KNOWN_ERRORS_FILE):
        with open(KNOWN_ERRORS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# ✅ Enregistrement des erreurs détectées
def log_error(error_message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPAIR_LOG, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] ERREUR DÉTECTÉE: {error_message}\n")
    log_action(f"⚠️ [ALERTE] Erreur détectée : {error_message}")

# ✅ Détection des erreurs dans les logs
def detect_errors():
    known_errors = load_known_errors()
    with open(LOG_FILE, "r", encoding="utf-8") as log_file:
        log_lines = log_file.readlines()

    for line in log_lines:
        for error_pattern, solution in known_errors.items():
            if re.search(error_pattern, line):
                log_error(line.strip())
                return error_pattern, solution

    return None, None

# ✅ Surveillance en temps réel des logs
def monitor_logs():
    log_action("🛠️ Surveillance des logs en temps réel...")
    while True:
        error_pattern, solution = detect_errors()
        if error_pattern:
            log_action(f"🔍 Erreur détectée : {error_pattern}")
            log_action(f"💡 Suggestion de correction : {solution}")
            # ✅ Ici, on pourra appeler auto_fixer.py pour corriger
        # Remplacé pour optimisation
5)  # Vérification toutes les 5 secondes

# ✅ Exécution du module
if __name__ == "__main__":
    monitor_logs()
