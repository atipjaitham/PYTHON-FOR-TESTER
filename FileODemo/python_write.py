# Manual Steps to write to a File
# 1. Open notepad and create File
# 2. Write in the file
# 3. Closr the file

# Mode
# Read Mode : r
# Write Mode : w
# Append mode : a
# Read / Write : r+

# f = open("c:/Users/atipj/Documents/Portfolio/SELENIUM PYTHON/PYTHON FOR TESTER/FileODemo/wrtiedemo.txt","w")
# f.write("This is first line")
# f.close()

f = open("c:/Users/atipj/Documents/Portfolio/SELENIUM PYTHON/PYTHON FOR TESTER/FileODemo/wrtiedemo.txt","a")
l = [65, 78, 989, 877, 8787]
for items in l:
    f.write(str(items)+"\n")
f.close()