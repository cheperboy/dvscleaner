# -*- coding: UTF-8 -*-
import re, glob, os, datetime, fnmatch
import shutil
regexes_delete_all_file = 'regexes_delete_all.txt'
regexes_keep_first_file = 'regexes_keep_first.txt'
regexes2 = [
    "^Ansaldo.+$",
    "^DOSSIER DE .+$",
    "^SEI_TVM300 -.+$",
    "^(\||_)*$", #lignes du type "|______|_____|"
    "^(\||\s)*$", #lignes du type "|   |    |    |"
    "^\W*$",
    "^\|\s+TABLEAU.+\|$",
    "^\|\s+NOM\sDE\sLA\sFONCTION.+\|$",
    "^[|]$",
    "^((\|\s*))+(_*)((\|\s*))*$",
    "^(\|\s*)+TYPE(\s*\|*\s*)*VALEUR(\s*\|*\s*)*$",
    "^\s_+\s+$",
    "^(\|\s*)NOM\sDU\sTYPE.*$",
    "^(\|\s*)*NOM\sENUMERE.*$",
    "^(\|\s*)*DOMAINE.*$"
    ]  
regexes_keep_first = []
regexes_delete_all = []

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

# recherche des fichiers présents dans un répertoire par expression régulière
def findfiles(which, where='.'):
    rule = re.compile(fnmatch.translate(which), re.IGNORECASE)
    return [name for name in os.listdir(where) if rule.match(name)]

#copie le contenu de source vers destination sauf les lignes qui match une des regex
def filtrer(source_file, destination_file):
    #open destination_file to copy source in it and work with regex from the begining of the file
    source = open(source_file, "r")
    out = source.readlines()
    source.close()
    for line in range(len(out)):
        combined_regex = "(" + ")|(".join(regexes_delete_all) + ")"
        if (re.match( combined_regex, out[line])) : out[line] = ''
#    print out
    #reopen destination_file to work with regex from the begining of the file
    for regex in regexes_keep_first:
        first_occ = True
        for line in range(len(out)):
            if ((re.match( regex, out[line])) and (first_occ == True)): 
                first_occ = False
            elif ((re.match( regex, out[line])) and (first_occ == False)): out[line] = ''
            elif not (re.match( regex, out[line])): pass
    
    destination = open(destination_file, "a")
    for line in range(len(out)):
        destination.write("%s"% out[line])
    destination.close()

def main_function(sourcedir):
    init()
    concat_file_name = os.path.basename(sourcedir) + '_CONCAT.TXT'
# create destination directory
    dest = os.path.basename(sourcedir) + '_' + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    destdir = os.path.join(os.path.abspath(sourcedir),'..', dest)
    os.makedirs(destdir)
#find all .tab in source dir, copy in dest dir, clean the copy
    tabfiles = findfiles('*.tab*', sourcedir)
    for file in tabfiles:
        source_file = os.path.join(sourcedir, os.path.basename(file))
        destination_file = os.path.join(destdir, os.path.basename(file))
        filtrer(source_file, destination_file)
#copy .pre & .del in dest dir
    otherfiles = findfiles('*.pre*', sourcedir)
    for file in otherfiles:
        shutil.copy2(os.path.join(sourcedir, os.path.basename(file)), os.path.join(destdir, os.path.basename(file)))

#create DVS_CONCAT.txt in dest dir
    allfiles = findfiles('*', destdir)
    concat = open(os.path.join(destdir, os.path.basename(concat_file_name)), 'a')
    for file in allfiles:
        filein = open(os.path.join(destdir, os.path.basename(file)), "r")
        for line in filein.readlines():
            concat.write("%s"% line)
            filein.close()
    concat.close()
    return (destdir)

if __name__ == '__main__':
    print (main_function(sourcedir = 'dvp'))

