import sys
import os
sys.path.append(os.path.abspath("C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/self_optimizer"))
import self_optimizer
import time
from datetime import datetime

# 📂 Fichier de logs d'Ilia
log_file = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/self_optimizer/optimizer_log.txt"

# 📊 Seuils d'alerte CPU et RAM
THRESHOLD_CPU = 80  # % d'utilisation CPU critique
THRESHOLD_RAM = 85  # % d'utilisation RAM critique
ANALYSIS_INTERVAL = 30  # Temps entre chaque analyse (secondes)
HYSTERESIS_CYCLES = 3  # Nombre de cycles consécutifs avant activation du mode urgence

# 🛑 Historique des charges CPU/RAM pour éviter les changements brutaux
history = []

def log_action(message):
    """Enregistre une action dans les logs avec un timestamp en UTF-8."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

def save_history(cpu, ram):
    """Ajoute une nouvelle mesure dans l'historique, avec un max de 5 entrées."""
    history.append((cpu, ram))
    if len(history) > HYSTERESIS_CYCLES:
        history.pop(0)  # Supprime les entrées les plus anciennes

def analyze_performance():
    """Analyse les performances CPU et RAM et ajuste les paramètres d'Ilia."""
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    save_history(cpu_usage, ram_usage)

    log_action(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%")

    high_load_count = sum(1 for c, r in history if c > THRESHOLD_CPU or r > THRESHOLD_RAM)
    
    if high_load_count >= HYSTERESIS_CYCLES:
        log_action("⚠️ Charge élevée détectée 3 fois de suite ! Activation du mode d'urgence.")
        adjust_settings(emergency=True)
    else:
        log_action("✅ Charge normale. Ajustement optimal des paramètres.")
        adjust_settings(emergency=False)

def adjust_settings(emergency=False):
    """Ajuste les paramètres d'analyse en fonction de la charge système."""
    global ANALYSIS_INTERVAL

    if emergency:
        ANALYSIS_INTERVAL = min(ANALYSIS_INTERVAL * 1.5, 120)  # Augmenter graduellement
    else:
        ANALYSIS_INTERVAL = max(ANALYSIS_INTERVAL / 1.3, 15)  # Réduire progressivement

    log_action(f"🔄 Nouvel intervalle d'analyse : {round(ANALYSIS_INTERVAL, 2)} secondes.")

if __name__ == "__main__":
    log_action("🚀 Lancement du moteur d'auto-adaptation d'Ilia...")

    while True:
        analyze_performance()
        time.sleep(ANALYSIS_INTERVAL)
