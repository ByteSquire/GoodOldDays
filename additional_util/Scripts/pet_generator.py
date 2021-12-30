import os
import sys
import re

arguments=sys.argv

if len(arguments) != 3:
    print("ERROR: Please specifiy exactly two arguments:")
    print("arg1: filepath to pet file, arg2: directory path to pet directory")
    sys.exit(1)

pet_file_path=arguments[1]
pet_dir_path=arguments[2]

def append_value_to_dict(line_dict, key, value):
    if key in line_dict.keys():
        line_dict[key] = line_dict[key] + ";" + value
    else:
        line_dict[key] = value

def write_godpet_file(pet_file, line_dict):
    for key in line_dict.keys():
        value = line_dict[key]
        if ";" in value:
            values = value.split(";")
            if all(i == values[0] for i in values):
                value = values[0]
        pet_file.write(key + "," + value)
        pet_file.write(',\n')
    pet_file.close()

def write_pet_files(pet_file_path, num_files, line_dict, epic_line_dict, legendary_line_dict):   
    for i in range(num_files):
        pet_file = open(pet_file_path.replace(".dbr", f"_{str(i+1).zfill(2)}.dbr"), "w")
        pet_file.close()
    
    for key in line_dict.keys():
        value = line_dict[key]
        if key in epic_line_dict.keys():
            epic_value = epic_line_dict[key]
        else:
            epic_value = value
        if key in legendary_line_dict.keys():
            legendary_value = legendary_line_dict[key]
        else:
            legendary_value = value

        values = None
        if ";" in value:
            values = value.split(";")
            if all(i == values[0] for i in values):
                value = values[0]
        
        epic_values = None
        if ";" in epic_value:
            epic_values = epic_value.split(";")
            if all(i == epic_values[0] for i in epic_values):
                epic_value = epic_values[0]
        
        legendary_values = None
        if ";" in legendary_value:
            legendary_values = legendary_value.split(";")
            if all(i == legendary_values[0] for i in legendary_values):
                legendary_value = legendary_values[0]

        for i in range(num_files):
            pet_file = open(pet_file_path.replace(".dbr", f"_{str(i+1).zfill(2)}.dbr"), "a")
            if values is not None:
                try:
                    value = values[i]
                except IndexError:
                    print(f"WARNING: Normal difficulty value missing for {key} at level {i+1}")
            if epic_values is not None:
                try:
                    epic_value = epic_values[i]
                except IndexError:
                    print(f"WARNING: Epic difficulty value missing for {key} at level {i+1}")
            if legendary_values is not None:
                try:
                    legendary_value = legendary_values[i]
                except IndexError:
                    print(f"WARNING: Legendary difficulty value missing for {key} at level {i+1}")
            
            pet_file.write(key + "," + value)
            if value != epic_value:
                pet_file.write(";" + epic_value)
                pet_file.write(";" + legendary_value)
            pet_file.write(',\n')
            pet_file.close()

if os.path.isfile(pet_file_path):
    if os.path.isdir(pet_dir_path):
        if len(os.listdir(pet_dir_path)) > 0:
            print(f"WARNING: Pet directory {pet_dir_path} is not empty, continue? [y/n]")
            if input().lower() != "y":
                sys.exit(0)
        line_dict = {"templateName": "database\Templates\Pet.tpl"}
        epic_line_dict = {"templateName": "database\Templates\Pet.tpl"}
        legendary_line_dict = {"templateName": "database\Templates\Pet.tpl"}
        
        pet_file=open(pet_file_path, "r")
        for i,line in enumerate(pet_file):
            key = line.split(",")[0]
            value = line.split(",")[1]
            if key == "templateName":
                if "pet.tpl" not in value.lower():
                    print(f"ERROR: Pet file is using template {value} instead of pet, please change")
                    sys.exit(1)
                continue
            
            if ";" in value:
                values = value.split(";")
                num_files= len(values)
            append_value_to_dict(line_dict, key, value)
        pet_file.close()
            
        pet_file=open(pet_file_path.replace("normal", "epic"), "r")
        for i,line in enumerate(pet_file):
            key = line.split(",")[0]
            value = line.split(",")[1]
            if key == "templateName":
                if "pet.tpl" not in value.lower():
                    print(f"ERROR: Pet file is using template {value} instead of pet, please change")
                    sys.exit(1)
                continue
            
            if ";" in value:
                values = value.split(";")
                num_files= len(values)
            append_value_to_dict(epic_line_dict, key, value)
        pet_file.close()
            
        pet_file=open(pet_file_path.replace("normal", "legendary"), "r")
        for i,line in enumerate(pet_file):
            key = line.split(",")[0]
            value = line.split(",")[1]
            if key == "templateName":
                if "pet.tpl" not in value.lower():
                    print(f"ERROR: Pet file is using template {value} instead of pet, please change")
                    sys.exit(1)
                continue
            
            if ";" in value:
                values = value.split(";")
                num_files= len(values)
            append_value_to_dict(legendary_line_dict, key, value)
        pet_file.close()

        write_pet_files(os.path.join(pet_dir_path, os.path.basename(pet_dir_path) + ".dbr"), num_files, line_dict, epic_line_dict, legendary_line_dict)
    else:
        print (f"ERROR: Pet directory {pet_dir_path} not found!")
        sys.exit(1)
else:
    print(f"Pet file: {pet_file_path} not found!")
    print(f"Do you want to create it from the files in the directory {pet_dir_path}? [y/n]")
    if input().lower() == "y":
        if os.path.isdir(pet_dir_path):
            if len(os.listdir(pet_dir_path)) > 0:
                line_dict = {"templateName": "database\Templates\Pet.tpl"}
                epic_line_dict = {"templateName": "database\Templates\Pet.tpl"}
                legendary_line_dict = {"templateName": "database\Templates\Pet.tpl"}
                for filename in os.listdir(pet_dir_path):
                    if not filename.endswith(".dbr"):
                        continue
                    filepath = os.path.join(pet_dir_path, filename)
                    file = open(filepath, "r")
                    skip_file = False
                    tmp_line_dict = {}
                    tmp_epic_line_dict = {}
                    tmp_legendary_line_dict = {}
                    for i,line in enumerate(file):
                        key = line.split(",")[0]
                        value = line.split(",")[1]
                        if key == "templateName":
                            if "pet.tpl" not in value.lower():
                                print(f"WARNING: Pet file {filepath} is using template {value} instead of pet, please change")
                                skip_file = True
                                break
                            continue

                        keys_to_ignore = ["characterRacialProfile", "monsterMesh", "specialAttack[0-9]Range"]
                        regex_from_list = temp = '(?:% s)' % '|'.join(keys_to_ignore)
                        if ";" in value and not re.match(regex_from_list, key):
                            values = value.split(";")
                            if len(values) != 3:
                                print(f"WARNING: Pet file {filepath} contains {len(values)} entries for variable {key} instead of 3, please fix!")
                                append_value_to_dict(tmp_line_dict, key, value)
                                append_value_to_dict(tmp_epic_line_dict, key, value)
                                append_value_to_dict(legendary_line_dict, key, value)
                            else:
                                append_value_to_dict(tmp_line_dict, key, values[0])
                                append_value_to_dict(tmp_epic_line_dict, key, values[1])
                                append_value_to_dict(tmp_legendary_line_dict, key, values[2])
                        else:
                            append_value_to_dict(tmp_line_dict, key, value)
                            append_value_to_dict(tmp_epic_line_dict, key, value)
                            append_value_to_dict(tmp_legendary_line_dict, key, value)

                    if skip_file:
                        print(f"INFO: File {filepath} skipped!")
                        continue
                    else:
                        for key in tmp_line_dict.keys():
                            append_value_to_dict(line_dict, key, tmp_line_dict[key])
                        for key in tmp_epic_line_dict.keys():
                            append_value_to_dict(epic_line_dict, key, tmp_epic_line_dict[key])
                        for key in tmp_legendary_line_dict.keys():
                            append_value_to_dict(legendary_line_dict, key, tmp_legendary_line_dict[key])
                    file.close()

                write_godpet_file(open(pet_file_path.replace(".dbr", "_normal.dbr"), "w"), line_dict)
                
                write_godpet_file(open(pet_file_path.replace(".dbr", "_epic.dbr"), "w"), epic_line_dict)
                
                write_godpet_file(open(pet_file_path.replace(".dbr", "_legendary.dbr"), "w"), legendary_line_dict)
            else:
                print(f"ERROR: Pet directory {pet_dir_path} is empty!")
                sys.exit(1)
        else:
            print (f"ERROR: Pet directory {pet_dir_path} not found!")
            sys.exit(1)
    sys.exit(1)
