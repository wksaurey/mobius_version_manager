#!/usr/bin/env python3

import argparse
import unpacker

# Example function to handle uploading a file
def upload_version(file_location):
    print(f"Uploading and extracting version from: {file_location}")
    # Here you would ad your unzip, rename, and configure logic
    unpacker.unpack(file_location)

# Example function to handle listing available versions
def list_versions():
    print("Listing all available versions...")
    # Logic for listing versions

# Example function to handle switching versions
def switch_version(version):
    print(f"Switching to version: {version}")
    # Logic for switching versions

# Main CLI handler
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mobius Version Manager (MVM)")

    # Add commands (like --upload, --list, --switch)
    parser.add_argument("-u", "--upload", help="Upload a new version", type=str)
    parser.add_argument("-l", "--list", help="List available versions", action="store_true")
    parser.add_argument("-s", "--switch", help="Switch to a specific version", type=str)

    args = parser.parse_args()

    if args.upload:
        upload_version(args.upload)
    elif args.list:
        list_versions()
    elif args.switch:
        switch_version(args.switch)
    else:
        parser.print_help()
