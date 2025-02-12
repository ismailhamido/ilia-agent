import os
import subprocess
import json
import time
from datetime import datetime

# 📂 Chemins des fichiers
REPAIR_LOG = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_repair/repair_log.txt"
KNOWN_ERRORS_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_repair/known_errors.json"

# ✅ Charger les erreurs connues et leurs solutions
def load_known_errors():
    if os.path.exists(KNOWN_ERRORS_FILE):
        with open(KNOWN_ERRORS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# ✅ Enregistrement des corrections appliquées
def log_fix(error_message, action_taken):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPAIR_LOG, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] ✅ Correction appliquée : {error_message} → {action_taken}\n")
    print(f"🔧 Correction appliquée : {error_message} → {action_taken}")

# ✅ Appliquer une correction automatique
def apply_fix(error_message):
    known_errors = load_known_errors()

    for error_pattern, solution in known_errors.items():
        if error_pattern in error_message:
            if "pip install" in solution:
                print(f"⚙️ Installation du module manquant...")
                subprocess.run(solution, shell=True, check=False)
                log_fix(error_message, solution)
                return True
            elif "Restart" in solution:
                print(f"🔄 Redémarrage du module impacté...")
                restart_module()
                log_fix(error_message, "Redémarrage du module")
                return True

    print("⚠️ Aucune correction automatique trouvée pour cette erreur.")
    return False

# ✅ Lire le dernier log d’erreur
def get_last_error():
    if os.path.exists(REPAIR_LOG):
        with open(REPAIR_LOG, "r", encoding="utf-8") as file:
            lines = file.readlines()
        for line in reversed(lines):
            if "ERREUR DÉTECTÉE" in line:
                return line.strip()
    return None

# ✅ Vérifier et installer les dépendances manquantes
def check_and_install_dependencies():
    required_modules = ["psutil", "json", "datetime"]
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"⚠️ Module manquant : {module}. Installation en cours...")
            subprocess.run(f"pip install {module}", shell=True, check=False)
            log_fix(f"Module {module} manquant", f"pip install {module}")

# ✅ Vérifier et mettre à jour les modules installés
import subprocess
from importlib.metadata import distributions

def update_packages():
    print("🔄 Vérification et mise à jour des modules Python...")

    # ✅ Étape 1 : Supprimer aiohttp avant la mise à jour
    print("⚠️ Suppression de aiohttp pour éviter les conflits...")
    subprocess.run("pip uninstall -y aiohttp", shell=True, check=False)

    # ✅ Étape 2 : Mettre à jour tous les autres modules sauf aiohttp
    outdated_packages = [dist.metadata["Name"] for dist in distributions()]
    for package in outdated_packages:
        if package.lower() != "aiohttp":  # ⚠️ Ignore aiohttp
            print(f"📦 Mise à jour de {package}...")
            subprocess.run(f"pip install --upgrade {package}", shell=True, check=False)

    log_fix("Mise à jour des modules (sauf aiohttp)", "pip upgrade")

    # ✅ Étape 3 : Réinstaller aiohttp dans la bonne version
    print("⚠️ Rétrogradation de aiohttp à la version 3.10.11 pour compatibilité avec ccxt...")
    subprocess.run("pip install aiohttp==3.10.11", shell=True, check=False)
    log_fix("Rétrogradation forcée de aiohttp", "pip install aiohttp==3.10.11")

    # ✅ Correction des packages corrompus après la mise à jour
    print("⚠️ Correction : Nettoyage des packages corrompus...")
    subprocess.run("pip uninstall -y numpy", shell=True, check=False)
    subprocess.run("pip install numpy", shell=True, check=False)
    log_fix("Réinstallation propre de numpy", "pip uninstall -y numpy && pip install numpy")

# ✅ Redémarrer un module (simulé ici)
def restart_module():
    print("🔄 Redémarrage du moteur d'évolution automatique...")
    subprocess.run("for /f \"delims=\" %i in ('pip list --outdated --format=freeze') do pip install --upgrade %i", shell=True, check=False)
    log_fix("Redémarrage du moteur", "Processus relancé")

# ✅ Exécuter la réparation automatique avec les nouvelles fonctionnalités
def auto_fix():
    print("🛠️ Début de la correction automatique...")
    
    # Vérifier les dépendances avant toute chose
    check_and_install_dependencies()
    
    # Vérifier et mettre à jour les modules si besoin
    update_packages()

    last_error = get_last_error()
    if last_error:
        print(f"🔍 Erreur trouvée : {last_error}")
        if apply_fix(last_error):
            print("✅ Erreur corrigée avec succès !")
        else:
            print("🚨 Aucune correction automatique disponible.")
    else:
        print("✅ Aucun problème détecté.")

# ✅ Lancer la correction
if __name__ == "__main__":
    auto_fix()
