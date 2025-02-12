import os
import re
import time
import json
import subprocess
from datetime import datetime

# 📂 Chemins des fichiers
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/evolution_log.txt"
REPAIR_LOG = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_repair/repair_log.txt"
KNOWN_ERRORS_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_repair/known_errors.json"
AUTO_FIXER = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_repair/auto_fixer.py"

# ✅ Chargement sécurisé des erreurs connues
def load_known_errors():
    if os.path.exists(KNOWN_ERRORS_FILE):
        try:
            with open(KNOWN_ERRORS_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                if not data:  # Vérifier si le fichier est vide
                    raise ValueError("Le fichier JSON est vide.")
                return data
        except json.JSONDecodeError:
            print("⚠️ ERREUR : Fichier known_errors.json corrompu. Restauration des valeurs par défaut.")
            default_errors = {
                "can’t open file": "Vérifie que le chemin du fichier est correct et accessible.",
                "ModuleNotFoundError": "pip install psutil",
                "Permission denied": "Essaie d’exécuter le script en administrateur.",
                "Restart Required": "Restart"
            }
            with open(KNOWN_ERRORS_FILE, "w", encoding="utf-8") as file:
                json.dump(default_errors, file, indent=4)
            return default_errors
    else:
        print("⚠️ ERREUR : Fichier known_errors.json introuvable. Création d’un fichier vierge.")
        with open(KNOWN_ERRORS_FILE, "w", encoding="utf-8") as file:
            json.dump({}, file, indent=4)
        return {}

# ✅ Enregistrement des erreurs détectées
def log_error(error_message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPAIR_LOG, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] ERREUR DÉTECTÉE: {error_message}\n")
    print(f"⚠️ [ALERTE] Erreur détectée : {error_message}")

# ✅ Vérification si l'erreur est toujours présente après correction
def verify_error_correction():
    with open(LOG_FILE, "r", encoding="utf-8") as log_file:
        log_lines = log_file.readlines()
    for line in log_lines:
        if "ERREUR DÉTECTÉE" in line:
            print("❌ L'erreur persiste après correction !");
            return True
    return False

# ✅ Détection des erreurs dans les logs et correction automatique
def detect_and_fix_errors():
    known_errors = load_known_errors()
    
    with open(LOG_FILE, "r", encoding="utf-8") as log_file:
        log_lines = log_file.readlines()

    for line in log_lines:
        for error_pattern, solution in known_errors.items():
            if re.search(error_pattern, line):
                log_error(line.strip())
                print(f"🔍 Erreur détectée : {error_pattern}")
                print(f"💡 Suggestion de correction : {solution}")
                
                # ✅ Lancer auto_fixer.py pour correction automatique
                subprocess.run(f"python {AUTO_FIXER}", shell=True, check=False)
                
                # Vérifier si l'erreur est toujours présente
                if verify_error_correction():
                    print("⚠️ L'erreur persiste, une action manuelle peut être nécessaire.")
                else:
                    print("✅ Erreur corrigée avec succès !")
                return
    
    print("✅ Aucun problème détecté.")

# ✅ Surveillance en temps réel des logs et correction automatique
def monitor_logs():
    print("🛠️ Surveillance et auto-correction des logs en temps réel...")
    while True:
        detect_and_fix_errors()
        time.sleep(5)  # Vérification toutes les 5 secondes

# ✅ Exécution du module
if __name__ == "__main__":
    monitor_logs()


