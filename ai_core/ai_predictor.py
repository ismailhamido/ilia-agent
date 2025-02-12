# -*- coding: utf-8 -*-
import os
import json
from datetime import datetime

# Chemins des fichiers
workspace_dir = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core"
history_file = os.path.join(workspace_dir, "resource_history.json")
log_file = os.path.join(workspace_dir, "ai_log.txt")

# Vérifie et crée le fichier d'historique si nécessaire
if not os.path.exists(history_file):
    with open(history_file, "w") as f:
        json.dump([], f)

def log_action(message):
    """Enregistre une action dans le fichier log avec horodatage."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

def collect_data():
    """Collecte les données CPU et RAM et met à jour l'historique."""
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_action(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%")

    # Charge l'historique
    with open(history_file, "r") as f:
        history = json.load(f)

    # Ajoute les nouvelles données
    history.append({"timestamp": timestamp, "cpu": cpu_usage, "ram": ram_usage})

    # Limite à 50 entrées max pour éviter surcharge
    if len(history) > 50:
        history.pop(0)

    # Sauvegarde l'historique
    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)

    return cpu_usage, ram_usage

def predict_next_interval():
    """Analyse l'historique et ajuste l'intervalle d'analyse."""
    with open(history_file, "r") as f:
        history = json.load(f)

    if len(history) < 5:
        return 15  # Valeur par défaut si pas assez de données

    avg_cpu = sum(d["cpu"] for d in history[-5:]) / 5
    avg_ram = sum(d["ram"] for d in history[-5:]) / 5

    if avg_cpu > 75 or avg_ram > 85:
        log_action("⚠️ Charge élevée détectée, allongement de l'intervalle.")
        return 120
    elif avg_cpu < 30 and avg_ram < 50:
        log_action("✅ Charge faible, raccourcissement de l'intervalle.")
        return 10
    else:
        log_action("🔄 Charge stable, maintien de l'intervalle.")
        return 30

if __name__ == "__main__":
    log_action("🚀 Lancement du moteur de prédiction AI...")
    collect_data()
    next_interval = predict_next_interval()
    log_action(f"⏳ Nouvel intervalle prédit : {next_interval} secondes.")
