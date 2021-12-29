import os
import sys

arguments=sys.argv

if len(arguments) != 3:
    print("Please specifiy exactly two arguments:")
    print("arg1: filepath to pet file, arg2: directory path to pet directory")
    exit(1)

pet_file_path=arguments[1]
pet_dir_path=arguments[2]

if os.path.exists(pet_file_path):
    if os.path.exists(pet_dir_path):
        pet_file=open(pet_file_path, "r")
        for i,line in enumerate(pet_file):
            pass
    else:
        print (f"Pet directory {pet_dir_path} not found!")
else:
    print(f"Pet file: {pet_file_path} not found!")
    exit(1)