import json
import numpy as np
from datetime import datetime

HISTORICAL_DATA_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/performance_tracker.json"

def load_historical_data():
    try:
        with open(HISTORICAL_DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"history": []}

def analyze_trends():
    data = load_historical_data()
    history = data["history"][-10:]

    if len(history) < 5:
        return "normal"

    cpu_values = np.array([entry["cpu"] for entry in history])
    ram_values = np.array([entry["ram"] for entry in history])

    avg_cpu = np.mean(cpu_values)
    avg_ram = np.mean(ram_values)

    # Détection des tendances critiques
    if avg_cpu > 70 and avg_ram > 80:
        return "urgence"
    elif avg_cpu > 50 or avg_ram > 75:
        return "attention"
    else:
        return "normal"

def decide_action():
    trend = analyze_trends()

    if trend == "urgence":
        log_action("🚨 Urgence détectée ! Activation du mode de réduction d'activité.")
        return "réduction"
    elif trend == "attention":
        log_action("⚠️ Attention : Charge élevée, optimisation nécessaire.")
        return "optimisation"
    else:
        log_action("✅ Charge normale, aucun ajustement requis.")
        return "stable"

if __name__ == "__main__":
    decision = decide_action()
    log_action(f"🔍 Décision prise : {decision}")

