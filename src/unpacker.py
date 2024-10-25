import os
from zipfile import ZipFile
import xml.etree.ElementTree as ET

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
    unpack_software(extract_path)

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

def unpack_software(software_path):

    software_path = f'{software_path}/Software'
    for filename in os.listdir(software_path):
        file_path = f'{software_path}/{filename}'
        extract_path = f'{file_path}'.removesuffix('.zip')

        if 'Server' in filename:
            clientType = 'Server'
        elif 'loader' in filename:
            clientType = 'Loader'
        elif 'survey' in filename:
            clientType = 'Survey'
        elif 'cab' in filename:
            clientType = 'ICC'
        else:
            clientType = 'Control'
        print(f'Extracting {clientType} client to {extract_path}')

        os.makedirs(extract_path)

        with ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

    print("Cleaning up zip files...")
    for filename in os.listdir(software_path):
        if filename.endswith('.zip'):
            os.remove(f'{software_path}/{filename}')

    modify_configurations(software_path)

def modify_configurations(software_path):

    for client_dir in os.listdir(software_path):
        config_path = f'bin/temp_build/Mining 4.1 rc13 42812/Software/{client_dir}/Mobius.dll.config'

        if 'Server' in client_dir:
            client_type = 'Server'
            print('Skipping Server')
            continue
        elif 'loader' in client_dir:
            client_type = 'Loader'
        elif 'survey' in client_dir:
            client_type = 'Survey'
        elif 'cab' in client_dir:
            client_type = 'ICC'
        else:
            client_type = 'Control'
        print(f'Modifying {client_type} config values')

        config_modifications = {
            'ServerAddress': 'https://10.10.253.130:18080',
            'AllowMultipleInstances': 'True'
        }

        tree=ET.parse(config_path)
        root = tree.getroot()

        for element in root.findall("./appSettings/add"):
            for value in config_modifications:
                if element.attrib.get('key') == value:
                    element.set('value', config_modifications[value])

        tree.write(config_path, encoding='utf-8', xml_declaration=True)


if __name__ == "__main__":
    modify_configurations()