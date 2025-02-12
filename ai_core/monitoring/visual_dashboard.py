
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
