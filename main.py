import os, subprocess, shutil, time
from zipfile import ZipFile
print("To use this you must seperate the BP and RP packs into new .mcpacks if they are in one pack!")
profName = input("What is the name of your linux profile? This script needs this for commands, and such.")
profName = "mcpack-maker"
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
  os.chdir("/")
  os.chdir("/home/runner/" + profName)
  if i not in ['main.py']:
    with ZipFile(i, 'r') as zipObj:
      print("Just opeed zip file, getting cwd")
      print(os.getcwd())
      i = i.replace(" ", "_") #Replaces whitespace
      i = i[:-7] #Gets rid of .mcpack so we dont get mkdir error
      os.system("cd -") #cds into main dir
      os.system("mkdir a" + i) #makes directory
      print("made dir", i) 
      os.system("ls")
      zipObj.extractall('a' + i)
      time.sleep(2) #bigger packs
      #Check for subpacks
      os.chdir('a' + i)
      
      x = subprocess.check_output(['ls -a'], shell=True)
      print("Got LS, is", x.decode())
      x = x.decode()
      print("Checking for subpacks")
      if 'manifest.json' not in strtolst(x): #See if program needs to cd up again
        for j in strtolst(x):
          print(j)
          if '.' != j and '..' != j: #Random dots? IDK why 
            print("manifest not found")
            print(strtolst(x))
            os.chdir(j)
      print(os.getcwd())
      os.system('ls')
      x = subprocess.check_output(['ls']) #Get ls for subpacks
      x = x.decode()
      for g in strtolst(x):
        if g == "subpacks": #Check for subpack folder
          print("Subpack detected!")
          os.chdir('subpacks') #CD in
          print("subpacks are: \n \n")
          os.system('ls')
          for p in strtolst(subprocess.check_output(['ls']).decode()):
            print(p)
            if input("Would you like to keep this subpack? Y/N").upper() == 'Y': #Ask if they want to keep it
              tokeep = p
              for l in strtolst(subprocess.check_output(['ls']).decode()):
                if l != p:
                  os.system('rm -rf ' + l)
              print("Kept!")
              break
            else:
              pass
            

            
          
      
      
