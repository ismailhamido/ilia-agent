import random
import time

def simulate_impact(optimization_type):
    log_action(f"🔄 Simulation de l'impact de l'optimisation : {optimization_type}...")

    simulated_cpu = random.uniform(10, 60)
    simulated_ram = random.uniform(30, 80)

    # Remplacé pour optimisation
2)

    log_action(f"📊 Résultat simulé : CPU {simulated_cpu:.2f}%, RAM {simulated_ram:.2f}%")

    if simulated_cpu < 50 and simulated_ram < 70:
        log_action("✅ Optimisation validée, application en cours...")
        return True
    else:
        log_action("❌ Optimisation annulée, impact négatif détecté.")
        return False

if __name__ == "__main__":
    simulate_impact("Ajustement des cycles d'analyse")
