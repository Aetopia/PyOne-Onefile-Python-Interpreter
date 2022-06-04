# Onefile Python Interpreter
Make your application's python runtime compact and easy to maintain. 
This is aimed toward people who want to keep/have their python application to run as scripts and not a compiled executable.


# How do we make a python interpreter onefile?

To simply put we take advantage of the way how python scripts are compiled by tools like Nuitka or PyInstaller.

A compiled python script contains the following:
1. Scripts
2. Data/File
3. Python Installation it is was compiled with.

# Advantages of making my own "Onefile Interpreter"
**Note: These are advantages when you are dealing with only `.py` files and not python zipapps.**

1. Single/One file executable that can be used as your application's python interpreter.
2. Add pip packages easily into your runtime by just importing them. (Compare this against, embedded python's method of including pip packages.)
3. Easy to maintain.

