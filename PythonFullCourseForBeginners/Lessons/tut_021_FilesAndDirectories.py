from pathlib import Path


# set the base to the parent folder of the python file.
# So in this case its PythonFullCourseForBeginners
base = Path(__file__).parent.parent

path = base / Path("ecommerce")
print(path.exists())

path = base / Path("notexisting")
print(path.exists())

# with this code, the folder creating_folder gets created
path = base / Path("creating_folder")
print(path.mkdir())

# and with this code, it gets deleted
path = base / Path("creating_folder")
print(path.rmdir())

# there will be created a map object which could be iterated in a loop
path = base / Path() / 'Lessons'
print(path.glob('*.py'))

# iterate the map object and print all files
for file in path.glob('*.py'):
    print(file)
