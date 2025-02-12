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

def predict_performance():
    data = load_historical_data()
    history = data["history"][-10:]

    if len(history) < 5:
        log_action("⚠️ Pas assez de données pour une prédiction fiable.")
        return None

    cpu_values = np.array([entry["cpu"] for entry in history])
    ram_values = np.array([entry["ram"] for entry in history])

    avg_cpu = np.mean(cpu_values)
    avg_ram = np.mean(ram_values)

    trend_cpu = "hausse" if cpu_values[-1] > avg_cpu else "baisse"
    trend_ram = "hausse" if ram_values[-1] > avg_ram else "baisse"

    prediction = {
        "cpu": avg_cpu,
        "ram": avg_ram,
        "tendance_cpu": trend_cpu,
        "tendance_ram": trend_ram
    }

    log_action(f"📊 Prédiction : CPU {trend_cpu}, RAM {trend_ram}")
    return prediction

if __name__ == "__main__":
    predict_performance()
