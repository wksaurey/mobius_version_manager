from os import path, makedirs
from zipfile import ZipFile

def get_build_name(file_location):
    filename = path.basename(file_location)
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
    zip_ref = ZipFile(file_location, 'r')
    zip_ref.extract(file_location, f'bin/temp_build/{build_name}')

if __name__ == "__main__":
    pass