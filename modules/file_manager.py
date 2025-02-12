import os

def read_file(filepath):
    """Lit et retourne le contenu d'un fichier."""
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    return None

def write_file(filepath, content):
    """Écrit du contenu dans un fichier (écrase le contenu existant)."""
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

def append_to_file(filepath, content):
    """Ajoute du contenu à un fichier sans écraser les données existantes."""
    with open(filepath, "a", encoding="utf-8") as file:
        file.write("\n" + content)

def file_exists(filepath):
    """Vérifie si un fichier existe."""
    return os.path.exists(filepath)
