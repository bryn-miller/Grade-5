import os

if not os.path.exists("c:\\temp"):
    os.makedirs("c:\\temp")

outFile = open('c:\\temp\\hellow.txt', 'w')
outFile.write(' It is fun to play with Pinkie Pie.')
outFile.close()

print("done!")
