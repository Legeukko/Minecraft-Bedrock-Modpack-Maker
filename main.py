import os, subprocess, shutil, time
from zipfile import ZipFile
print("To use this you must seperate the BP and RP packs into new .mcpacks if they are in one pack!")
profName = input("What is the name of your linux profile? This script needs this for commands, and such.")
profName = "mcpack-maker"
fileBlacklist = ['main.py', 'RPmanifest.json', 'README.md', 'BPmanifest.json', 'backup', 'RP', 'BP']
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
  if i[-7:] == '.mcpack' or i[-3:] == '.py' or i[-5:] == '.json' or i[-3:] == '.md' or i == 'backup':
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
  if i not in fileBlacklist:
    fileBlacklist.append(i)
    with ZipFile(i, 'r') as zipObj:
      print("Just opeed zip file, getting cwd")
      i = i.replace(" ", "_") #Replaces whitespace
      i = i[:-7] #Gets rid of .mcpack so we dont get mkdir error
      os.system("cd -") #cds into main dir
      os.system("mkdir a" + i) #makes directory
      print("made dir", i) 
      zipObj.extractall('a' + i)
     #bigger packs
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
            print("Checking subpacks: Manifest.json not found. CDing up a level...")
            print(strtolst(x))
            os.chdir(j)
      tokeep3 = os.getcwd()
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
              tokeep = p # Not sure why this is here but im too lazy to change it
              for l in strtolst(subprocess.check_output(['ls']).decode()):
                if l != p:
                  os.system('rm -rf ' + l) #delete subpack if the user answered y
              print("Kept!")
              os.chdir(tokeep)
              tokeep2 = os.getcwd()
              print(tokeep2)
              
              for b in strtolst(subprocess.check_output(['ls']).decode()): #Go into subpack
                os.chdir(tokeep2)
                for h in strtolst(subprocess.check_output(['ls']).decode()): #Loop through files and CD into them
                  
                  os.chdir(tokeep2)
                  if os.path.isdir(h):
                    print("LINE 89")
                    os.chdir(h)
                    for a in strtolst(subprocess.check_output(['ls']).decode()): #Loop through files and CD into them again
                      print("CDd into", h)
                      
                      os.system('mv ' + a  + ' ' + tokeep3 + '/' + b) #Finnaly move them with a tokeep variable that stores the path of the current pack directory
                  print(h)
              break
            else:
              pass


#Create RP
os.chdir("/")
os.chdir("/home/runner/" + profName)
os.system('mkdir RP')
os.system('cp RPmanifest.json RP/manifest.json')
countOfLoopedThrough = 0
for x in strtolst(subprocess.check_output(['ls']).decode()):
  print(x)
  if x not in fileBlacklist: #Makes sure file is not readme/this script
    countOfLoopedThrough = 1
    os.chdir("/")
    os.chdir("/home/runner/" + profName)
    os.system('ls')
    os.chdir(x)
    g = subprocess.check_output(['ls -a'], shell=True)
    g = g.decode()
    print("LINE 99", g)
    if 'manifest.json' not in strtolst(g): #CHeckng if the program needs to cd up a level
      print('X + ' + g)
      for j in strtolst(g):
        if '.' != j and '..' != j: #Random dots? IDK why 
          print("Mainifest.json not found in CWD. CDing up 1 level.")
          print("Old level was:", os.getcwd())
          os.chdir(j)
    if countOfLoopedThrough == 1:
      currentcd = os.getcwd() #need this for later
      for k in strtolst(subprocess.check_output(['ls']).decode()):
        print("LINE 114: ", k)
        os.chdir(currentcd) #CD into the directory after every iteration so we dnt get stuck in one
        if os.path.isdir('/home/runner/' + profName + '/RP/' + k):
          print("Attempted to move files, but they already exist! CDing into directory...")
          os.chdir(k)
          print("CDd into directory", k)
          for f in strtolst(subprocess.check_output(['ls']).decode()):
            print("Moving:", f)
            os.system('mv ' + f + ' /home/runner/' + profName + '/RP/' + k)
          
          
        else:
          if os.path.isdir(k): #Make sure k is an actual directory so we dont cd into a file
            print('Moving: ' + k)
            os.system('mv ' + k + ' /home/runner/' + profName + '/RP') #Finally move files.
      
        
        
    
