import os
print ("Starting script1")
os.system("pip install -r requirements.txt")
print ("script1 ended")
print ("Starting script2")
os.system("python yaml2json.py")
print ("script2 ended")
print ("Starting script3")
os.system("python convert.py")
print ("script3 ended")
print ("Starting script4")
os.system("python merge.py")
print ("script4 ended")
print ("Starting script5")
os.system("python train.py")
print ("script5 ended")