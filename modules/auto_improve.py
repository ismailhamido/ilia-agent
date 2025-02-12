import os
import file_manager

def improve_script(script_path):
    """Lit un script et propose une amélioration basique (ex: ajouter un commentaire)."""
    content = file_manager.read_file(script_path)
    if content:
        if "# Improved by Ilia" not in content:
            improved_content = "# Improved by Ilia\n" + content
            file_manager.write_file(script_path, improved_content)
            print("✅ Le script a été amélioré.")
        else:
            print("⚠️ Le script est déjà optimisé.")
    else:
        print("❌ Impossible de lire le script.")

# Exemple d'amélioration du script modifié
script_to_improve = "C:/Users/Utilisateurs4717/Auto-GPT/auto_gpt_workspace/script_to_be_modified.py"
improve_script(script_to_improve)
