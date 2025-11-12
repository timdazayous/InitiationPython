from os import walk as oswalk

PATH = r'.venv'
Nfiles = 0
Ndirs = 0


for root, dirnames, filenames in oswalk(PATH):
    Ndirs = Ndirs + len(dirnames)
    Nfiles += len(filenames)

print("Ndirs", Ndirs)
print("Nfiles", Nfiles)