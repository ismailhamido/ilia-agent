import psutil
import time
import os
from datetime import datetime

# 📂 Fichier log de gestion des processus
LOG_FILE = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/process_manager/process_log.txt"

# ✅ Fonction pour écrire dans le log
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Détection des processus gourmands
def find_heavy_processes():
    processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
        try:
            cpu_usage = proc.info['cpu_percent']
            if cpu_usage > 10:  # Processus utilisant plus de 10% CPU
                processes.append((proc.info['pid'], proc.info['name'], cpu_usage))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return sorted(processes, key=lambda x: x[2], reverse=True)  # Trier par usage CPU

# ✅ Mettre en pause un processus
def pause_process(pid):
    try:
        os.kill(pid, 19)  # Signal SIGSTOP (pause)
        log_message(f"⏸️ Processus {pid} mis en pause.")
    except Exception as e:
        log_message(f"❌ Impossible de mettre en pause {pid}: {str(e)}")

# ✅ Reprendre un processus
def resume_process(pid):
    try:
        os.kill(pid, 18)  # Signal SIGCONT (reprise)
        log_message(f"▶️ Processus {pid} repris.")
    except Exception as e:
        log_message(f"❌ Impossible de reprendre {pid}: {str(e)}")

# ✅ Gestion dynamique des processus en fonction de la charge CPU
def manage_processes():
    log_message("🚀 Lancement du gestionnaire de processus...")

    paused_processes = set()

    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        log_message(f"📊 CPU : {cpu_usage}%, RAM : {ram_usage}%")

        if cpu_usage > 80 or ram_usage > 95:
            log_message("⚠️ Charge critique ! Mise en pause des processus non essentiels...")
            heavy_processes = find_heavy_processes()
            for pid, name, usage in heavy_processes:
                if pid not in paused_processes:
                    pause_process(pid)
                    paused_processes.add(pid)

        elif cpu_usage < 50 and ram_usage < 85:
            log_message("✅ Charge normale détectée. Reprise des processus en pause.")
            for pid in list(paused_processes):
                resume_process(pid)
                paused_processes.remove(pid)

        time.sleep(5)  # Pause de 5s avant nouvelle analyse

# ✅ Exécution du gestionnaire de processus
if __name__ == "__main__":
    manage_processes()
