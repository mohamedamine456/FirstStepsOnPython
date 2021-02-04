from pathlib import Path

# Absolute Path
# c:\Program Files\Microsoft
# /usr/local/bin

# Relative Path
path = Path("ecommerce")
print(path.exists())

path2 = Path("ecommerce1")
print(path2.exists())

# create directory
path3 = Path("emails")
path3.mkdir()

# delete directory
path3.rmdir()

# access files in directory
# search for file
# Path() return actual path
path4 = Path()
for file in path4.glob("*"):
    print(file)