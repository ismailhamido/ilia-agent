import os
import ast
import re
from datetime import datetime

# 📂 Dossier contenant le code à optimiser
CODE_PATH = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/"
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_optimizer/optimizer_log.txt"

# ✅ Fonction pour enregistrer les optimisations
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Suppression des imports inutiles
def remove_unused_imports(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Rechercher les imports inutiles
        imports_to_remove = []
        for line in lines:
            match = re.match(r"^\s*import (\S+)", line)
            if match and match.group(1) == "psutil":
                imports_to_remove.append(line)

        # Supprimer les lignes inutiles
        if imports_to_remove:
            new_lines = [line for line in lines if line not in imports_to_remove]
            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(new_lines)
            log_message(f"✅ Import inutile supprimé dans {file_path} : psutil")
        else:
            log_message(f"✅ Aucun import inutile trouvé dans {file_path}.")

    except Exception as e:
        log_message(f"❌ Erreur de correction dans {file_path}: {str(e)}")

# ✅ Optimisation automatique des fichiers Python
def optimize_codebase():
    log_message("🚀 Lancement de l'optimisation du code...")
    for root, _, files in os.walk(CODE_PATH):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                remove_unused_imports(file_path)
    log_message("✅ Optimisation terminée.")

# ✅ Exécution de l'optimisation
if __name__ == "__main__":
    optimize_codebase()
