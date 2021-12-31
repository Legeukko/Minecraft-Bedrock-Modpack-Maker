import os, subprocess, shutil
from zipfile import ZipFile
def strtolst(inp): #Turns str with newlines into list
  out = []
  buff = []
  for c in inp:
    if c == '\n':
        out.append(''.join(buff))
        buff = []
    else:
        buff.append(c)
  return out
  
x = subprocess.check_output(['ls']) #Gets ls output to see what packs were added
x = x.decode()
#First lists through and purges all files that do not have mcpack ending
for i in strtolst(x):
  if i[-7:] == '.mcpack' or i[-3:] == '.py':
    print("Found mcpack file!")
  else:
    print("Purging file", i)
    try: #Try to rmove directory
      shutil.rmtree(i)
    except: #Must be file
      os.system('rm ' + '"' + i + '"') #Delete file with whitespace also


  
#Actual Program
x = subprocess.check_output(['ls'])
x = x.decode()
for i in strtolst(x): #Loops through ls check
  if i not in ['main.py']:
    with ZipFile(i, 'r') as zipObj:
      i = i.replace(" ", "_") #Replaces whitespace
      i = i[:-7] #Gets rid of .mcpack so we dont get mkdir error
      os.system("cd -") #cds into main dir
      os.system("mkdir " + i) #makes directory
      print("made dir", i) 
      zipObj.extractall(i)
