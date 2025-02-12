import os
import ast
import time
from datetime import datetime

# 📂 Dossier contenant le code à analyser
CODE_PATH = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/"
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_optimizer/optimizer_log.txt"

# ✅ Fonction pour écrire dans le log
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Fonction d’analyse du code Python
def analyze_code(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read(), filename=file_path)

        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 20:
                    issues.append(f"⚠️ Fonction {node.name} trop longue ({len(node.body)} lignes).")
            if isinstance(node, ast.Import):
                if node.names[0].name not in ["os", "sys", "subprocess", "json", "time", "datetime"]:
                    issues.append(f"⚠️ Import inutile détecté : {node.names[0].name}")

        if issues:
            log_message(f"📌 Problèmes détectés dans {file_path}:")
            for issue in issues:
                log_message(issue)
        else:
            log_message(f"✅ Aucun problème détecté dans {file_path}.")

    except Exception as e:
        log_message(f"❌ Erreur d'analyse dans {file_path}: {str(e)}")

# ✅ Parcourir tous les fichiers `.py` dans le dossier CODE_PATH
def scan_codebase():
    log_message("🚀 Lancement de l'analyse du code...")
    for root, _, files in os.walk(CODE_PATH):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                analyze_code(file_path)
    log_message("✅ Analyse terminée.")

# ✅ Exécution du scanner
if __name__ == "__main__":
    scan_codebase()
