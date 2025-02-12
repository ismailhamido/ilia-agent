import json
import os
import time
import subprocess

# 📂 Emplacement des fichiers et dossiers critiques
HISTORY_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/adaptive_system/cpu_ram_history.json"
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_optimizer/evolution_log.txt"
VISUALIZATION_SCRIPT = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/monitoring/visual_dashboard.py"
MONITORING_DIR = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/monitoring"

# ✅ Fonction pour écrire dans le log
def log_message(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Vérifie et crée le dossier monitoring s'il est manquant
def ensure_monitoring_folder():
    if not os.path.exists(MONITORING_DIR):
        os.makedirs(MONITORING_DIR)
        log_message("📂 Dossier 'monitoring/' créé automatiquement.")

# ✅ Vérifie si un module manque et génère le code si nécessaire
def check_for_missing_features():
    ensure_monitoring_folder()  # Vérifie que monitoring/ existe

    # Vérifier si l'affichage visuel est déjà en place
    if not os.path.exists(VISUALIZATION_SCRIPT):
        log_message("⚠️ Aucun tableau de bord visuel détecté. Génération automatique en cours...")
        generate_visualization_script()
        time.sleep(3)  # Pause pour éviter les conflits
        if os.path.exists(VISUALIZATION_SCRIPT):
            log_message("✅ Tableau de bord visuel généré avec succès !")
        else:
            log_message("❌ Échec de la création du tableau de bord.")

# ✅ Génère un script de visualisation si nécessaire
def generate_visualization_script():
    visualization_code = """
import json
import time
import matplotlib.pyplot as plt

HISTORY_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/adaptive_system/cpu_ram_history.json"

def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def display_graph():
    while True:
        history = load_history()
        times = list(history.keys())[-10:]  # Afficher les 10 dernières minutes
        cpu_values = [history[t]["cpu"] for t in times if "cpu" in history[t]]
        ram_values = [history[t]["ram"] for t in times if "ram" in history[t]]

        plt.clf()
        plt.plot(times, cpu_values, label="CPU Usage (%)", color="red")
        plt.plot(times, ram_values, label="RAM Usage (%)", color="blue")
        plt.xlabel("Temps")
        plt.ylabel("Utilisation (%)")
        plt.legend()
        plt.title("Surveillance CPU/RAM en temps réel")
        plt.pause(5)  # Rafraîchir toutes les 5s

display_graph()
"""
    with open(VISUALIZATION_SCRIPT, "w", encoding="utf-8") as file:
        file.write(visualization_code)
    
# ✅ Vérifie régulièrement si de nouvelles améliorations sont nécessaires
def evolution_loop():
    log_message("🚀 Lancement du moteur d'évolution automatique...")
    while True:
        check_for_missing_features()
        time.sleep(600)  # Vérification toutes les 10 minutes

# ✅ Exécution
if __name__ == "__main__":
    evolution_loop()
