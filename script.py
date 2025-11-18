from os import walk as oswalk

PATH = r'.venv'
Nfiles = 0
Ndirs = 0

# oswalk(path) parcourt recursivement le dossier .venv
# root = chemin du dossier en cours / dirnames = liste des sous dossiers dans ce dossier / filenames = liste des fichiers dans ce dossier
for root, dirnames, filenames in oswalk(PATH):
    Ndirs = Ndirs + len(dirnames)
    Nfiles += len(filenames)

print("Ndirs", Ndirs)
print("Nfiles", Nfiles)


