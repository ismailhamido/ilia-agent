import time
import multiprocessing
import numpy as np

# ✅ Fonction pour stresser la CPU avec des calculs inutiles
def stress_cpu():
    print("🚀 Stress CPU en cours...")
    while True:
        np.random.rand(1000, 1000) @ np.random.rand(1000, 1000)  # Multiplication de matrices énormes

# ✅ Fonction pour remplir la RAM avec des données temporaires
def stress_ram():
    print("🚀 Stress RAM en cours...")
    data = []
    while True:
        data.append(np.random.rand(1000000))  # Ajoute 1 million de nombres flottants à chaque itération
        time.sleep(0.5)

# ✅ Lancer les tests en parallèle
if __name__ == "__main__":
    print("🔥 Démarrage du Stress Test CPU & RAM...")
    
    cpu_process = multiprocessing.Process(target=stress_cpu)
    ram_process = multiprocessing.Process(target=stress_ram)

    cpu_process.start()
    ram_process.start()

    cpu_process.join()
    ram_process.join()
