import os
import json
import time
from datetime import datetime

# 📂 Chemin absolu du fichier de suivi
TRACKER_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/performance_tracker.json"

# ⏳ Paramètres d'analyse
ANALYSIS_INTERVAL = 30
HIGH_LOAD_THRESHOLD = 85  # Seuil RAM pour mode urgence
EMERGENCY_INTERVAL = 120  # Intervalle en mode urgence
MAX_HISTORY = 100  # Nombre max d'entrées

def initialize_tracker():
    """📝 Vérifie et initialise le fichier JSON s'il est inexistant ou vide."""
    if not os.path.exists(TRACKER_FILE) or os.path.getsize(TRACKER_FILE) == 0:
        data = {"history": [], "timestamp": "", "cpu": 0, "ram": 0}
        with open(TRACKER_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

def update_performance_tracker(cpu, ram, interval):
    """📊 Met à jour le fichier JSON de suivi des performances."""
    initialize_tracker()

    # 🔍 Lecture du fichier JSON
    with open(TRACKER_FILE, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = {"history": []}

    # ✅ Vérification et correction de la clé "history"
    if "history" not in data or not isinstance(data["history"], list):
        data["history"] = []

    # 📝 Ajout de la nouvelle entrée
    data["history"].append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu": cpu,
        "ram": ram
    })

    # 🗑️ Limite l'historique à 100 entrées max
    data["history"] = data["history"][-MAX_HISTORY:]

    # 💾 Sauvegarde du fichier JSON
    with open(TRACKER_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def analyze_performance():
    """📡 Analyse CPU/RAM et ajuste les paramètres en conséquence."""
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    if ram_usage > HIGH_LOAD_THRESHOLD:
        interval = EMERGENCY_INTERVAL
        log_action(f"⚠️ Charge élevée détectée ! Mode urgence activé : {interval}s.")
    else:
        interval = ANALYSIS_INTERVAL

    log_action(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%. Prochain scan dans {interval} sec.")

    update_performance_tracker(cpu_usage, ram_usage, interval)

    return interval

def main():
    """🚀 Boucle principale du moteur d'évolution automatique."""
    log_action("🔥 Démarrage du moteur d'évolution automatique...")

    while True:
        interval = analyze_performance()
        # Remplacé pour optimisation
interval)

if __name__ == "__main__":
    main()
