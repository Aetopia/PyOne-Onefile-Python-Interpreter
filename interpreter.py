# Modules [Import modules here.]

# Core
from sys import argv, exit
import os;os.system('')
from runpy import run_path

# Interpreter
def main():
    if len(argv) == 1: 
        print(f'\33[91mError: No file specified.\33[0m')
        exit(1)
    else:
        file = argv[1]; args = {}
        for index, arg in enumerate(argv[2:]): args[index] = arg
        run_path(file, init_globals=args, run_name='__main__')

if __name__ == '__main__':
    main()
