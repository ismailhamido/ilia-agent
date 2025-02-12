import os
import json
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# 📂 Chemins des fichiers
LEARNING_LOG = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/learning_log.txt"
KNOWLEDGE_DB = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/ai_core/auto_evolution/knowledge_base.json"

# 🔍 Sources de documentation
LEARNING_SOURCES = [
    "https://realpython.com/", 
    "https://www.geeksforgeeks.org/python-programming-language/", 
    "https://dev.to/t/python"
]

# ✅ Chargement des connaissances existantes
def load_knowledge():
    if os.path.exists(KNOWLEDGE_DB):
        with open(KNOWLEDGE_DB, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# ✅ Sauvegarde des nouvelles connaissances
def save_knowledge(knowledge):
    with open(KNOWLEDGE_DB, "w", encoding="utf-8") as file:
        json.dump(knowledge, file, indent=4)

# ✅ Enregistrement des cycles d’apprentissage
def log_learning(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LEARNING_LOG, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

# ✅ Scraping des articles et extraction des bonnes pratiques
def fetch_articles():
    print("🔍 Recherche de nouvelles optimisations...")
    knowledge = load_knowledge()
    
    for source in LEARNING_SOURCES:
        try:
            response = requests.get(source, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                titles = [title.get_text() for title in soup.find_all("h2")]
                
                for title in titles:
                    if title not in knowledge:
                        knowledge[title] = source
                        log_learning(f"📚 Nouvelle optimisation détectée : {title}")
        except Exception as e:
            log_learning(f"⚠️ Erreur en scrappant {source} : {e}")
    
    save_knowledge(knowledge)

# ✅ Boucle principale d’apprentissage
def self_learn():
    print("🚀 Lancement du moteur d’apprentissage autonome...")
    while True:
        fetch_articles()
        # Remplacé pour optimisation
60)  # Vérification et apprentissage toutes les 60 secondes

# ✅ Exécution du module
if __name__ == "__main__":
    self_learn()

