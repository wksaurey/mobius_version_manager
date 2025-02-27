#!/usr/bin/env python3

import argparse

import unpacker


# Example function to handle uploading a file
def upload_version(file_location):
    print(f"Uploading and extracting version from: {file_location}")
    # Here you would add your unzip, rename, and configure logic
    unpacker.unpack(file_location)


# Main CLI handler
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mobius Version Manager (MVM)")

    # Add commands (like --upload, --list, --switch)
    parser.add_argument("-u", "--upload", help="Upload a new version", type=str)

    args = parser.parse_args()

    if args.upload:
        upload_version(args.upload)
    else:
        parser.print_help()
