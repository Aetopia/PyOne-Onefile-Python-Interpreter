# Onefile Python Interpreter
Make your application's python runtime compact and easy to maintain.                  
This is aimed toward people who want to keep/have their python application to run as scripts and not a compiled executable.


## How do we make a python interpreter onefile?        

To simply put we take advantage of the way how python scripts are compiled by tools like Nuitka or PyInstaller.        

A compiled python script contains the following:          
1. Scripts
2. Data/Files
3. Python Installation it is was compiled with.          

So we compile this specific base code for every onefile python interpreter.      

```py
from sys import argv, exit
from runpy import run_path
if len(argv) == 1: exit()
file = argv[1]; args = {}
for index, arg in enumerate(argv[2:]): args[index] = arg
run_path(file, init_globals=args)
```
We take advantage of `runpy.run_path` to execute our python scripts.

## Advantages of making my own "Onefile Interpreter"
**Note: These are advantages when you are dealing with only `.py` files and not python zipapps.**

1. Single/One file executable that can be used as your application's python interpreter.         
2. Add pip packages easily into your runtime by just importing them. (Compare this against, embedded python's method of including pip packages.)
3. Easy to maintain.

## Limitations
Onefile python interpreters have some limitations in regards with how executed scripts parse command-line arguments.                        
This all boils down to how `runpy.run_path` passes `init_globals` to the script that has to be executed.

Say:        
```
example.exe file.py -a -b -c
```
is executed via the command-line.

Now in our compiled onefile interpreter sees the following:      
`['example.exe', 'file.py', '-a', '-b', '-c']`        
          
What our executed script sees:         
`['file.py', 'file.py', '-a', '-b', '-c']`      

We have a duplicate filepath entry.            
Thus, this can mess with any scripts that deal with `sys.argv` or `argparse`.       

### Workarounds
Its actually easy to fix/workaround these limitations.

1. Fixing duplicate filepath entires.        
   Add the following at the beginning your script.
   
   ```py
   from sys import argv # Imports sys.argv
   if argv[0] is argv[1]: argv = argv[1:]
   ```
   
   OR
   
   ```py
   import sys
   if sys.argv[0] is sys.argv[1]: sys.argv = sys.argv[1:]
   ```
2. Fixing parsing issues with `argparse`.                  
   `argparse` doesn't respect the first workaround directly so we will need to explictly tell what arguments to parse.
   
   1. Add the first workaround for `sys.argv`.
   2. Find the `.parse_args()` function in your code and add the following argument:
   
      ```py
      .parse_args(argv[2:])
      ```
      OR
      ```py
      .parse_args(sys.argv[2:])
      ```
## Adding in PIP Packages/User Made Modules
Its actually really easy!     

Just import them into the base code:

```py
import package1
import module1

from sys import argv, exit
from runpy import run_path
if len(argv) == 1: exit()
file = argv[1]; args = {}
for index, arg in enumerate(argv[2:]): args[index] = arg
run_path(file, init_globals=args)
```

and just compile the script!

## Compiling the Onefile Python Interpreter
To compile your onefile python interpreter, do the following.

1. Install the following PIP packages.
   ```bat
   pip install nuitka zstandard ordered-set
   ```
2. Run `build.bat` and you are good to go!   
