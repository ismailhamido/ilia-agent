import os
import subprocess
import sys
sys.path.append("C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/modules")  # Ajoute le dossier des modules au chemin d'import

import file_manager
import auto_improve
from datetime import datetime

# Nom du fichier à modifier et fichier de logs
script_to_modify = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/script_to_be_modified.py"
log_file = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/log.txt"

def log_action(message):
    """Écrit une action dans le fichier log avec un horodatage."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_manager.append_to_file(log_file, f"[{timestamp}] {message}")

def modify_and_execute():
    """Modifie, améliore et exécute le script."""
    print("\n🛠 Amélioration du script...\n")
    auto_improve.improve_script(script_to_modify)  # Applique des améliorations

    print("\n🚀 Exécution du script modifié...\n")
    result = subprocess.run(["python", script_to_modify], text=True, capture_output=True)
    log_action(f"Exécution du script :\n{result.stdout}")

    print("\n📜 Journal des actions :")
    print(file_manager.read_file(log_file))

# Lancer l'amélioration et l'exécution
modify_and_execute()
