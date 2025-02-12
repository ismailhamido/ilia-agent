import psutil

print("✅ Test de psutil réussi !")
print("Utilisation du CPU:", psutil.cpu_percent(), "%")
print("Utilisation de la RAM:", psutil.virtual_memory().percent, "%")
