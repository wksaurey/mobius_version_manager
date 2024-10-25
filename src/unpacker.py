import os
from zipfile import ZipFile

def get_build_name(file_location):
    filename = os.path.basename(file_location)
    name_segments = filename.split()
    build_name = [name_segments[i] for i in [0, 4, 5, 8]]

    # modify sections of the name
    build_name[0] = build_name[0].capitalize()
    build_name[2] = build_name[2].lower()
    build_name[3] = build_name[3].split('.')[-2]

    build_name = ' '.join(build_name)
    # print(build_name)
    return build_name

def unpack(file_location):

    build_name = get_build_name(file_location)
    extract_path = f'bin/temp_build/{build_name}'
    with ZipFile(file_location, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    print(f'Extracted contents to {extract_path}')
    convert_file_structure_from_windows(extract_path)

def convert_file_structure_from_windows(dir_location):
    # converting windows garbage

    # Loop through each file in the directory
    for filename in os.listdir(dir_location):
        
        if '\\' in filename:
            # Create the new filename by replacing backslashes with forward slashes
            new_filename = filename.replace('\\', '/')
            
            # Create full paths for renaming
            old_file_path = os.path.join(dir_location, filename)
            new_file_path = os.path.join(dir_location, new_filename)
            
            # build file structure
            new_dir_path = os.path.dirname(new_file_path)
            if not os.path.exists(new_dir_path):
                print(f'Making dir {new_dir_path}')
                os.makedirs(new_dir_path)

            if not os.path.isdir(new_file_path):
                # Rename the file
                print(f'Renaming: {old_file_path} -> {new_file_path}')
                os.rename(old_file_path, new_file_path)
            else:
                # delete {old_file_path
                print(f'Deleting {old_file_path}')
                os.remove(old_file_path)
        else:
            print(f'No backslash found in: {filename}')

    print("All files have been processed.")

if __name__ == "__main__":
    pass