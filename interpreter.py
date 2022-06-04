# PIP Packages [Import PIP Packages Here.]

# Core
from sys import argv, exit
from runpy import run_path
if len(argv) == 1: exit()
file = argv[1]; args = {}
for index, arg in enumerate(argv[2:]): args[index] = arg
run_path(file, init_globals=args)