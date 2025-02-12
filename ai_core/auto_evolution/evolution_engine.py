import psutil  # Ajouté pour éviter l'erreur NameError
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import time
import json
from datetime import datetime
import threading
import subprocess
from ai_core.auto_evolution.decision_engine import decide_action  # ✅ Ajout du moteur de décision

# ✅ Lancement des modules en parallèle
def start_module(module_path):
    subprocess.run(f"python {module_path}", shell=True, check=False)

if __name__ == "__main__":
    log_action("🚀 Démarrage du moteur d'auto-évolution...")
    
    # Lancer la surveillance CPU/RAM
    threading.Thread(target=start_module, args=("C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/performance_monitor.py",)).start()
    
    # Lancer l'ajustement dynamique des cycles
    threading.Thread(target=start_module, args=("C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/auto_adjuster.py",)).start()

# 📂 Définition des chemins des fichiers
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/evolution_log.txt"
PERFORMANCE_TRACKER = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/performance_tracker.json"

# 📊 Seuils d’alerte CPU et RAM
HIGH_RAM_THRESHOLD = 85  # Seuil critique RAM
NORMAL_RAM_THRESHOLD = 75  # Retour à la normale
HIGH_CPU_THRESHOLD = 80  # Seuil critique CPU
NORMAL_CPU_THRESHOLD = 50  # Retour à la normale

# 🔄 Paramètres dynamiques
ANALYSIS_INTERVAL = 30  # Temps entre chaque analyse (secondes)
MAX_INTERVAL = 240  # Intervalle max en mode urgence
MIN_INTERVAL = 15  # Intervalle minimum

# 🔍 Stockage des charges CPU/RAM
history = []

def log_action(message):
    """Écrit une action dans les logs avec un timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")
    log_action(message)

def save_performance(cpu, ram):
    """Sauvegarde l’historique des performances pour analyse future."""
    history.append({"cpu": cpu, "ram": ram, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    if len(history) > 10:  # Garde seulement les 10 dernières entrées
        history.pop(0)
    with open(PERFORMANCE_TRACKER, "w", encoding="utf-8") as file:
        json.dump({"history": history}, file, indent=4)

def optimize_memory():
    """Libère la RAM en fermant les processus inutiles."""
    for process in psutil.process_iter(attrs=['pid', 'name', 'memory_percent']):
        if process.info['memory_percent'] > 5:  # Si un processus consomme plus de 5% de RAM
            log_action(f"🛑 Processus gourmand détecté : {process.info['name']} (PID: {process.info['pid']}), arrêt en cours...")
            try:
                p = psutil.Process(process.info['pid'])
                p.terminate()
                log_action(f"✅ {process.info['name']} arrêté avec succès.")
            except Exception as e:
                log_action(f"⚠️ Erreur en fermant {process.info['name']} : {e}")

def adjust_interval(cpu, ram):
    """Ajuste l'intervalle d'analyse en fonction de la charge et de la décision IA."""
    global ANALYSIS_INTERVAL

    # 📌 Utilisation du moteur de décision
    decision = decide_action()

    if decision == "réduction":
        log_action("🔻 Mode de réduction activé : diminution des analyses pour alléger la charge.")
        ANALYSIS_INTERVAL = min(ANALYSIS_INTERVAL * 1.5, MAX_INTERVAL)

    elif decision == "optimisation":
        log_action("⚡ Mode optimisation activé : ajustement pour réduire la charge CPU.")
        ANALYSIS_INTERVAL = max(ANALYSIS_INTERVAL * 0.8, MIN_INTERVAL)

    else:
        log_action("✅ Charge normale, maintien du cycle actuel.")

    if cpu > HIGH_CPU_THRESHOLD or ram > HIGH_RAM_THRESHOLD:
        log_action(f"⚠️ Charge élevée ! Augmentation de l'intervalle à {ANALYSIS_INTERVAL:.2f} sec.")
        optimize_memory()
    elif cpu < NORMAL_CPU_THRESHOLD and ram < NORMAL_RAM_THRESHOLD:
        log_action(f"✅ Charge normale. Réduction de l'intervalle à {ANALYSIS_INTERVAL:.2f} sec.")

def analyze_performance():
    """Analyse la charge CPU et RAM et ajuste l’intervalle d’analyse."""
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    save_performance(cpu_usage, ram_usage)

    log_action(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%. Prochain scan dans {ANALYSIS_INTERVAL:.2f} sec.")
    adjust_interval(cpu_usage, ram_usage)

def main():
    """Boucle principale du moteur d’évolution automatique."""
    log_action("🚀 Démarrage du moteur d'évolution automatique...")

    while True:
        analyze_performance()
        # Remplacé pour optimisation
ANALYSIS_INTERVAL)

if __name__ == "__main__":
    main()

