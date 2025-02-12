import os
import subprocess
import json
from datetime import datetime

# 📂 Chemins des fichiers
CODE_BASE_PATH = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/"
TEST_RESULTS_LOG = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/test_results.json"

# ✅ Exécuter les scripts et vérifier s'ils tournent sans erreur
def run_test(file_path):
    try:
        subprocess.run(["python", file_path], check=True, capture_output=True, text=True)
        return "✅ Test réussi"
    except subprocess.CalledProcessError as e:
        return f"❌ Erreur détectée: {e.stderr}"

# ✅ Tester tous les fichiers Python
def test_code():
    print("🚀 Lancement des tests automatiques...")
    results = {}
    for file_name in os.listdir(CODE_BASE_PATH):
        if file_name.endswith(".py") and file_name not in ["self_tester.py"]:
            file_path = os.path.join(CODE_BASE_PATH, file_name)
            print(f"🔍 Test de {file_name} en cours...")
            results[file_name] = run_test(file_path)
            print(f"📝 Résultat: {results[file_name]}")
    return results

# ✅ Enregistrement des résultats
def save_test_results(results):
    with open(TEST_RESULTS_LOG, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

# ✅ Boucle principale d’auto-test
def self_test():
    print("🔎 Début des tests automatiques...")
    results = test_code()
    save_test_results(results)
    print("✅ Tous les tests sont enregistrés dans test_results.json")

# ✅ Exécution du module
if __name__ == "__main__":
    self_test()
