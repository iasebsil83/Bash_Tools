# ---------------- IMPORTATIONS ----------------
import os








# ---------------- DEFINITIONS ----------------

#show devices already there ?
print_old_devices = False








# ---------------- GET DEVICE LIST BEFORE ----------------

#user info
print("Please ensure that the device to detect is not connected.\nThen press ENTER")
input()

#get dev list BEFORE connection
os.system("ls /dev > devList.tmp")
f = open("devList.tmp", "r")
oldData = f.read().split("\n")
f.close()








# ---------------- GET DEVICE LIST AFTER ----------------

#user info
print("Now connect the device.\nThen press ENTER")
input()

#get dev list AFTER connection
os.system("ls /dev > devList.tmp")
f = open("devList.tmp", "r")
newData = f.read().split("\n")
f.close()
os.remove("devList.tmp")








# ---------------- COMPARISON ----------------

#compare the 2 lists
newDevNbr = 0
print("Here is the difference :")
for d in range(len(newData)):
	foundInOld = False
	for o in oldData:
		if o == newData[d]:
			foundInOld = True
	if not foundInOld:
		newDevNbr += 1
		print("NEW DEVICE    :", newData[d])
	else:
		if print_old_devices:
			print("Already there :", newData[d])

print("Total : {} new device(s).".format(newDevNbr))
