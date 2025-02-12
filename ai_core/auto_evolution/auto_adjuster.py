import json
import time

# 📂 Chemins des fichiers
HISTORICAL_DATA_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/historical_data.json"

# ✅ Chargement des données historiques
def load_historical_data():
    try:
        with open(HISTORICAL_DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"history": []}

# ✅ Analyse et ajustement des intervalles
def adjust_analysis_cycle():
    log_action("🔄 Analyse des performances pour ajustement...")
    historical_data = load_historical_data()
    if not historical_data["history"]:
        log_action("⚠️ Pas encore assez de données pour ajuster.")
        return 30  # Intervalle par défaut

    last_5 = historical_data["history"][-5:]  # Dernières 5 entrées
    avg_cpu = sum(entry["cpu"] for entry in last_5) / len(last_5)
    avg_ram = sum(entry["ram"] for entry in last_5) / len(last_5)

    # 🔧 Ajustement dynamique de l'intervalle
    if avg_cpu > 75 or avg_ram > 80:
        interval = 10  # Haute charge, intervalle réduit
    elif avg_cpu < 30 and avg_ram < 40:
        interval = 60  # Charge faible, intervalle augmenté
    else:
        interval = 30  # Situation normale

    log_action(f"📊 CPU Moyenne: {avg_cpu}%, RAM Moyenne: {avg_ram}% → Nouvel intervalle : {interval} sec.")
    return interval

# ✅ Exécution du module
if __name__ == "__main__":
    while True:
        cycle = adjust_analysis_cycle()
        # Remplacé pour optimisation
cycle)  # Attente selon le cycle défini
