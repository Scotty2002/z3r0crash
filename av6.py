import os
from fnmatch import fnmatch

root = 'c:\\'
 
pattern = "*.*"

for path, subdirs, files in os.walk(root):
    for name in files:
       if fnmatch(name, pattern):
             os.path.join(path, name)
file1 = open("C:\Users\joebl\Desktop\Programming\Virus Soruce Codes\Virus Research\VirusSignaturesDB.txt", "r")
file2 = open(os.path.join(path, name), "r") 
list1 = file1.readlines()
list2 = file2.readlines()


try:    
    for i in list1:
        for j in list2:
           if i == j: 
            print("Virus is found :",i)
            fclose()
            break
           else:   
            print("Firus not Found")
            fclose()
            break

except Exception: 
  pass

def fclose():
   print("Good Bye")
