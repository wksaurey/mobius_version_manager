import os
import re
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile


def get_build_name(file_location):
    # naming examples
    # Mining 4.2 rc5 45584
    # MINING MOBIUS 24-10-18 Release 4.1.1 RC1 Mobius Version 7.40.54645.43961
    # MINING MOBIUS 24-08-15 Release 4.1 RC13 Mobius Version 7.39.54469.42812
    filename = os.path.basename(file_location).lower().removesuffix('.zip')

    # print(filename)  # debug

    # possible markets
    markets = ['mining']
    # find all market matches from markets in filename
    market_matches = []
    for market in markets:
        if market in filename:
            market_matches.append(market)
    market = verify_one_match(
        market_matches,
        'market'
    )

    # matches to any number as long as it is followed
    # by one or more number seperated by a period
    # as long as the following characters are exactly ' rc'
    # This is to exclude the build id on the end
    version_number = verify_one_match(
        re.findall(r'[0-9]+(?:\.[0-9])+(?= rc)', filename),
        'version_number'
    )

    # possible build_types
    build_types = ['rc', 'tb']
    # find all build type matches from build_types in filename
    build_type_matches = []
    for build_type in build_types:
        if build_type in filename:
            build_type_matches.append(build_type)
    build_type = verify_one_match(
        build_type_matches,
        'build_type'
    )

    # matches the number following 'rc'
    build_number = verify_one_match(
        re.findall(r'(?<=rc)[0-9]+', filename),
        'build_number'
    )

    # matches any number that is at the end of the filename
    # checks for at least one match
    build_id = verify_one_match(
        re.findall(r'[0-9]+$', filename),
        'build_id'
    )

    build_info = {
        'market': market,
        'version_number': version_number,
        'build_type': build_type,
        'build_number': build_number,
        'build_id': build_id
    }

    return build_info


# verify that only one match was found from filename parsing
# otherwise print an error message and quit
def verify_one_match(matches, name_segment):
    # print(f'{name_segment} matches: {matches}') # debug
    if len(matches) == 0:
        print(f'No matches found for {name_segment}')
        sys.exit(1)  # loop back to user input?
    if len(matches) > 1:
        print(f'Matches found for {name_segment}: {matches}')
        print('Unable to process filenames with multiple matches')
        sys.exit(1)  # loop back to user input
    return matches[0]


class Build:
    def __init__(self, file_location):
        build_info = get_build_name(file_location)
        self.market = build_info['market']
        self.version_number = build_info['version_number']
        self.build_type = build_info['build_type']
        self.build_number = build_info['build_number']
        self.build_id = build_info['build_id']
        self.name = self.generate_build_name()

    def generate_build_name(self):
        return f'{self.market.capitalize()} {self.version_number} {self.build_type}{self.build_number} {self.build_id}'


# entry point
def unpack(file_location):

    # generate build info
    build = Build(file_location)
    extract_path = f'bin/temp_build/{build.name}'
    with ZipFile(file_location, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    print(f'Extracted contents to {extract_path}')
    convert_file_structure_from_windows(extract_path)
    unpack_software(extract_path, build)


def convert_file_structure_from_windows(dir_location):
    # converting windows garbage

    print('Converting from Windows to unix filesystem')

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
                # print(f'Making dir {new_dir_path}')
                os.makedirs(new_dir_path)

            if not os.path.isdir(new_file_path):
                # Rename the file
                # print(f'Renaming: {old_file_path} -> {new_file_path}')
                os.rename(old_file_path, new_file_path)
            else:
                # delete {old_file_path
                # print(f'Deleting {old_file_path}')
                os.remove(old_file_path)
        else:
            print(f'No backslash found in: {filename}')


def unpack_software(software_path, build):

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

    modify_configurations(software_path, build)


def modify_configurations(software_path, build):

    for client_dir in os.listdir(software_path):
        config_path = f'bin/temp_build/{build.name}/Software/{client_dir}/Mobius.dll.config'

        if 'Server' in client_dir:
            client_type = 'Server'
            config_path = f'bin/temp_build/{build.name}/Software/{client_dir}/MobiusServer.dll.config'
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
            "InterfaceAddress": "https://+:18080/",
            "CertificateFile": "C:\\Certificates\\durability_10_10_253_130.pfx",
            'ServerAddress': 'https://10.10.253.130:18080',
            'AllowMultipleInstances': 'True'
        }

        tree = ET.parse(config_path)
        root = tree.getroot()

        for element in root.findall("./appSettings/add"):
            for value in config_modifications:
                if element.attrib.get('key') == value:
                    element.set('value', config_modifications[value])

        tree.write(config_path, encoding='utf-8', xml_declaration=True)


if __name__ == "__main__":
    pass
