import os
from datetime import datetime

# 📂 Fichier de feedback sur la performance
feedback_file = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/self_optimizer/performance_feedback.txt"

def log_feedback(message):
    """Enregistre un feedback sur la performance avec un horodatage."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(feedback_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

def analyze_feedback(cpu_usage, ram_usage):
    """Analyse les performances et génère un feedback pour ajustement."""
    if cpu_usage > 80 or ram_usage > 85:
        log_feedback("⚠️ Charge critique détectée. Recommandation : Réduction des processus secondaires.")
    elif cpu_usage < 30 and ram_usage < 50:
        log_feedback("✅ Charge faible détectée. Recommandation : Augmentation des cycles d'analyse.")
    else:
        log_feedback("🔄 Charge stable. Aucun ajustement nécessaire.")

if __name__ == "__main__":
    print("📊 Module de feedback sur la performance prêt à être intégré.")
