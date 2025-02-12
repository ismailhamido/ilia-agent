import json
import time
import psutil
import pandas as pd
from datetime import datetime, timedelta

# 📂 Fichiers pour l'historique et les logs
HISTORY_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/adaptive_system/cpu_ram_history.json"
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/predictive_system/dashboard_log.txt"

# ✅ Fonction pour écrire dans le log
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Chargement de l'historique CPU/RAM
def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# ✅ Pondération des dernières valeurs pour améliorer la précision
def weighted_prediction(history, future_time):
    times = list(history.keys())
    times.sort()

    recent_cpu = []
    recent_ram = []
    weights = [1, 2, 3, 4, 5]  # Plus on est proche, plus la valeur est pondérée

    for i, time_point in enumerate(times[-5:]):  # Prendre les 5 dernières minutes
        if time_point in history:
            recent_cpu.append(history[time_point]["cpu"] * weights[i])
            recent_ram.append(history[time_point]["ram"] * weights[i])

    if recent_cpu and recent_ram:
        cpu_pred = sum(recent_cpu) / sum(weights)
        ram_pred = sum(recent_ram) / sum(weights)
        return round(cpu_pred, 1), round(ram_pred, 1)

    return "N/A", "N/A"

# ✅ Génération des prévisions sur les 5 prochaines minutes
def generate_predictions():
    history = load_history()
    future_predictions = {}

    for i in range(1, 6):  # Prévision sur les 5 prochaines minutes
        future_time = (datetime.now() + timedelta(minutes=i)).strftime("%H:%M")
        cpu_pred, ram_pred = weighted_prediction(history, future_time)
        future_predictions[future_time] = {"cpu": cpu_pred, "ram": ram_pred}

    return future_predictions

# ✅ Affichage des prévisions CPU/RAM sous forme de tableau
def display_dashboard():
    log_message("🚀 Affichage des prévisions CPU/RAM avec pondération avancée...")
    while True:
        predictions = generate_predictions()
        df = pd.DataFrame(predictions).T
        df.columns = ["Prédiction CPU (%)", "Prédiction RAM (%)"]

        print("\n📊 **PRÉVISIONS CPU/RAM SUR LES 5 PROCHAINES MINUTES**")
        print(df)
        log_message(f"📊 Tableau mis à jour :\n{df}")

        time.sleep(60)  # Met à jour les prévisions toutes les minutes

# ✅ Exécution du tableau de bord prédictif
if __name__ == "__main__":
    display_dashboard()
