# -*- coding: UTF-8 -*-
from fnmatch import translate
from datetime import datetime
from shutil import copy2
from re import compile, match, IGNORECASE
from os import path, listdir, makedirs

regexes_delete_all_file = 'regexes_delete_all.txt'
regexes_keep_first_file = 'regexes_keep_first.txt'
regexes_keep_first = []
regexes_delete_all = []

# vérifie qu'un seul type de fichier (dvs, dco ou dvp) est présent dans le dossier source
def check_one_file_type():
    pass

# charge le contenu du fichier de paramétrage regex.txt dans une variable globale
def init():
    regfile = open(regexes_delete_all_file, 'r')
    for line in regfile.readlines():
        if not (line[0] == '#') :
            regexes_delete_all.append(line)
    regfile.close()
    regfile = open(regexes_keep_first_file, 'r')
    for line in regfile.readlines():
        if not (line[0] == '#') :
            regexes_keep_first.append(line)
    regfile.close()

# recherche des fichiers présents dans un répertoire par expression régulière avec option IGNORECASE
# which : expression régulière our identifier les fichiers à récupérer
# where : dossier source
def findfiles(which, where='.'):
    rule = compile(translate(which), IGNORECASE)
    return [name for name in listdir(where) if rule.match(name)]

#copie le contenu de source vers destination sauf les lignes qui match une des regex
def filtrer(source_file, destination_file):
    #open destination_file to copy source in it and work with regex from the begining of the file. do not copy any occurence that match regexes_delete_all.
    source = open(source_file, "r")
    out = source.readlines()
    source.close()
    for line in range(len(out)):
        combined_regex = "(" + ")|(".join(regexes_delete_all) + ")"
        if (match( combined_regex, out[line])) : out[line] = ''
#    print out
    #reopen destination_file to work with regex from the begining of the file. do not copy any occurence that match regexes_keep_first except the first occurence.
    for regex in regexes_keep_first:
        first_occ = True
        for line in range(len(out)):
            if ((match( regex, out[line])) and (first_occ == True)): 
                first_occ = False
            elif ((match( regex, out[line])) and (first_occ == False)): out[line] = ''
            elif not (match( regex, out[line])): pass
    
    destination = open(destination_file, "a")
    for line in range(len(out)):
        destination.write("%s"% out[line])
    destination.close()

def main_function(sourcedir):
    init()
    concat_file_name = path.basename(sourcedir) + '_CONCAT.TXT'
# create destination directory
    dest = path.basename(sourcedir) + '_' + datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    destdir = path.join(path.abspath(sourcedir),'..', dest)
    makedirs(destdir)
#find all .tab in source dir, copy in dest dir, clean the copy
    tabfiles = findfiles('*.tab*', sourcedir)
    for file in tabfiles:
        source_file = path.join(sourcedir, path.basename(file))
        destination_file = path.join(destdir, path.basename(file))
        filtrer(source_file, destination_file)
#copy file ".pre" without any modification in dest dir
    otherfiles = findfiles('*.pre*', sourcedir)
    for file in otherfiles:
        copy2(path.join(sourcedir, path.basename(file)), path.join(destdir, path.basename(file)))

#create DVS_CONCAT.txt in dest dir
    allfiles = findfiles('*', destdir)
    concat = open(path.join(destdir, path.basename(concat_file_name)), 'a')
    for file in allfiles:
        filein = open(path.join(destdir, path.basename(file)), "r")
        for line in filein.readlines():
            concat.write("%s"% line)
            filein.close()
    concat.close()
    return (destdir)

if __name__ == '__main__':
    print (main_function(sourcedir = '../dvscleaner_tests/dco'))

