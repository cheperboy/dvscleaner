# Gérénrer l'IHM
IHM basé sur le programme pi2exe
sourceforge.net/projects/py2exe/files/py2exe/0.6.9/

ligne de commande pour générer l'exe:
python setup.py py2exe

Un sous répertoire nommé dist est créé.
Il contient le fichier exécutable Concat_documents.exe
(source : http://fsincere.free.fr/isn/python/cours_python_py2exe.php)


# fichiers
## setup.py
fichier appelé pour générer l'ihm.

## Concat_documents.py
code de l'ihm basé sur librairie Tkinter.

## Concat_documents.py
code de l'ihm basé sur librairie Tkinter.

## dvscleaner.py
scrit principal, implémentation des fonctions de lecture et écriture de fichiers
### fonction init
charge le contenu de regexes_keep_first.txt dans la variable regexes_keep_first
idem pour regexes_delete_all

regexes_delete_all : expressions régulières pour identifier les lignes qui ne seront pas conservées dans les fichiers de sortie
regexes_keep_first : expressions régulières pour identifier les lignes qui ne seront pas conservées dans les fichiers de sortie sauf la première occurence (en-tête de table)

### fonction find_files
récupère les fichiers d'un dossier sur la base d'une expression régulière sans tenir compte de la casse (exemple: tous les fichier du type *dvs*.tab* ou *DVS*.TAB*)

### fonction filter
source_file : ouvert en lecture seule.
destination_file : ouvert en écriture pour y copier le contenu de source_file sauf les lignes qui match les expressions régulières

### fonction main_function
crée le dossier de destination dans le même répertoire que le dossier source. le dossier de destination est nommé comme le répertoire source et suffixé d'un timestamp.

pour chaque fichier ".tab" du dossier source, crée un fichier ".tab" dans le dossier de destination puis nettoie le fichier créé en appelant la fonction filter qui exploite les expressions régulières pour supprimer les lignes inutiles.

le fichier ".pre" est recopié dans le dossier de destination sans modification.

création d'un fichier concaténé nommé comme le dossier de destination et portant l'extention ".TXT" contenant le fichier ".pre" puis les fichiers ".tab"

# Limitations
Le répertoire source ne doit contenir qu'UN seul type de fichier (DVS ou DCO ou DVP)

l'appel du script en ligne de commande avec en paramètre le dossier source à traiter n'est pas prévu. il faut indiquer en dur dans le script le chemin du dossier source à traiter. (pas de limitation si utilisé via ihm).