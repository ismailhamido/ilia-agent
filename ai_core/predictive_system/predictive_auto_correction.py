import json
import time
import psutil
from datetime import datetime, timedelta

# 📂 Fichiers pour les données
HISTORY_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/adaptive_system/cpu_ram_history.json"
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/predictive_system/auto_correction_log.txt"

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

# ✅ Sauvegarde des nouvelles données
def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

# ✅ Fonction de correction des prédictions
def correct_predictions():
    history = load_history()
    current_time = datetime.now().strftime("%H:%M")
    previous_time = (datetime.now() - timedelta(minutes=1)).strftime("%H:%M")

    if previous_time in history:
        actual_cpu = psutil.cpu_percent(interval=1)
        actual_ram = psutil.virtual_memory().percent

        predicted_cpu = history[previous_time].get("cpu", None)
        predicted_ram = history[previous_time].get("ram", None)

        if predicted_cpu and predicted_ram:
            error_cpu = abs(predicted_cpu - actual_cpu)
            error_ram = abs(predicted_ram - actual_ram)

            log_message(f"🔍 Comparaison {previous_time} : Prédit CPU {predicted_cpu}%, Réel {actual_cpu}% → Écart {error_cpu}%")
            log_message(f"🔍 Comparaison {previous_time} : Prédit RAM {predicted_ram}%, Réel {actual_ram}% → Écart {error_ram}%")

            if error_cpu > 10 or error_ram > 10:
                log_message("⚠️ Erreur détectée, correction des pondérations...")
                correction_factor = 0.8  # Réduction de 20% pour s'ajuster
                history[previous_time]["cpu"] = round(predicted_cpu * correction_factor + actual_cpu * (1 - correction_factor), 1)
                history[previous_time]["ram"] = round(predicted_ram * correction_factor + actual_ram * (1 - correction_factor), 1)
                save_history(history)
                log_message(f"✅ Correction appliquée : CPU {history[previous_time]['cpu']}%, RAM {history[previous_time]['ram']}%")

# ✅ Boucle d'auto-correction
def auto_correction_loop():
    log_message("🚀 Activation de l'auto-correction des prédictions...")
    while True:
        correct_predictions()
        time.sleep(60)  # Vérification toutes les minutes

# ✅ Exécution
if __name__ == "__main__":
    auto_correction_loop()
