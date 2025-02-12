import threading
import time
import os

# 📂 Emplacements des scripts
PREDICTIVE_DASHBOARD = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/predictive_system/predictive_dashboard.py"
AUTO_CORRECTION = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/predictive_system/predictive_auto_correction.py"
ANOMALY_DETECTOR = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/predictive_system/predictive_anomaly_detector.py"
PREVENTION = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/predictive_system/predictive_prevention.py"

# ✅ Fonction pour démarrer un script en thread
def run_script(script_path):
    os.system(f"python {script_path}")

# ✅ Lancer les modules en parallèle
def start_ai_system():
    print("🚀 Lancement du système d'auto-adaptation IA...")
    
    # Démarrer chaque module sur un thread séparé
    threading.Thread(target=run_script, args=(PREDICTIVE_DASHBOARD,), daemon=True).start()
    threading.Thread(target=run_script, args=(AUTO_CORRECTION,), daemon=True).start()
    threading.Thread(target=run_script, args=(ANOMALY_DETECTOR,), daemon=True).start()
    threading.Thread(target=run_script, args=(PREVENTION,), daemon=True).start()

    while True:
        time.sleep(60)  # Vérification toutes les minutes

# ✅ Exécution
if __name__ == "__main__":
    start_ai_system()
