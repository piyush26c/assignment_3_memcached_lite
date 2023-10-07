import sys
import json
import string
import random
import os
import shutil

def generate_random_string(size):
    # Define the characters you want to use
    characters = string.ascii_letters  # Contains both uppercase and lowercase letters

    # Generate the random string by selecting characters randomly
    random_string = ''.join(random.choice(characters) for _ in range(size))

    return random_string


if __name__ == '__main__':
    if len(sys.argv) == 6:
        number_of_kv_pairs = int(sys.argv[1])
        min_key_size = int(sys.argv[2])
        max_key_size = int(sys.argv[3])
        min_val_size = int(sys.argv[4])
        max_val_size = int(sys.argv[5])
        
        file_name = "key_value_" + str(number_of_kv_pairs) + ".json"
        with open(file_name, 'w') as f:
                json.dump({}, f)

        data = None
        # read json file
        with open(file_name, 'r') as file:
                data = json.load(file)
        
        for indx in range(number_of_kv_pairs):
            key = generate_random_string(random.randint(min_key_size, max_key_size))
            value = generate_random_string(random.randint(min_val_size, max_val_size))

            data[key] = value
        
        # save data to json file and write it on disk
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

        # logic to copy file in one directory above and delete generated file in current directory.
        file_path = os.getcwd() + "/" + file_name
        os.chdir("..")
        folder_path = os.getcwd()
        shutil.copy(file_path, folder_path)
        os.remove(file_path)
        
    else:
        print("Inappropriate number of arguments. (python3 data_generator.py <number_of_key_value_pairs> <minimum_key_size> <maximum_key_size> <minimum_value_size> <maximum_value_size>")




