import time
import os

# Chemin des fichiers de configuration et logs
log_file = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/self_optimizer/optimizer_log.txt"
config_file = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/self_optimizer/config.py"

# Seuils de déclenchement
HIGH_CPU_THRESHOLD = 85.0
HIGH_RAM_THRESHOLD = 90.0

# Fonction pour modifier dynamiquement la configuration
def modifier_configuration(nouvel_intervalle):
    with open(config_file, "w", encoding="utf-8") as f:
        f.write(f"INTERVALLE_ANALYSE = {nouvel_intervalle}\n")
    print(f"⚙️ Configuration mise à jour : INTERVALLE_ANALYSE = {nouvel_intervalle}")
    os.system(f"echo '[CONFIG] INTERVALLE_ANALYSE mis à {nouvel_intervalle} secondes' >> {log_file}")

# Actions selon l’état du système
def activer_mode_urgence():
    print("⚠️ Mode urgence activé : Limitation des processus.")
    modifier_configuration(120)

def optimiser_taches():
    print("🔄 Réorganisation des tâches...")
    modifier_configuration(15)

# Fonction principale
def analyse_logs_et_action():
    while True:
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_usage = psutil.virtual_memory().percent

            print(f"📌 CPU: {cpu_usage}%, RAM: {ram_usage}%")

            # Ajustement automatique
            if cpu_usage > HIGH_CPU_THRESHOLD or ram_usage > HIGH_RAM_THRESHOLD:
                activer_mode_urgence()
            else:
                optimiser_taches()

            time.sleep(15)

        except Exception as e:
            print(f"❌ Erreur dans le moteur décisionnel: {e}")

if __name__ == "__main__":
    analyse_logs_et_action()
