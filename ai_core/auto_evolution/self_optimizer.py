import os
import json
import time
from datetime import datetime

# 📂 Chemins des fichiers
KNOWLEDGE_DB = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/knowledge_base.json"
CODE_BASE_PATH = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/"
OPTIMIZATION_LOG = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/optimization_log.txt"

# ✅ Chargement des connaissances acquises
def load_knowledge():
    if os.path.exists(KNOWLEDGE_DB):
        with open(KNOWLEDGE_DB, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# ✅ Enregistrement des optimisations
def log_optimization(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(OPTIMIZATION_LOG, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Application des optimisations sur le code source
def apply_optimizations():
    print("🔧 Application des optimisations basées sur l'apprentissage...")
    knowledge = load_knowledge()
    
    for file_name in os.listdir(CODE_BASE_PATH):
        if file_name.endswith(".py") and file_name not in ["self_optimizer.py", "self_learning.py"]:
            file_path = os.path.join(CODE_BASE_PATH, file_name)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            for title, source in knowledge.items():
                if "print(" in content and "logging" in title.lower():
                    content = content.replace("print(", "logging.info(")
                    log_optimization(f"✅ Optimisation appliquée sur {file_name} : remplacement de print() par logging")
            
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
    
# ✅ Boucle principale d’optimisation
def self_optimize():
    print("🚀 Lancement du moteur d’auto-optimisation...")
    while True:
        apply_optimizations()
        # Remplacé pour optimisation
120)  # Appliquer les optimisations toutes les 2 minutes

# ✅ Exécution du module
if __name__ == "__main__":
    self_optimize()

    self_optimize()

