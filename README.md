# mvm - Mobius Version Manager for Testing Environments

Mobius Version Manager (MVM) allows users to manage, switch,
and run different Mobius builds within a testing environment. It
supports uploading new versions, switching between versions, and
managing Mobius server/client instances.

## Features
- Upload new Mobius builds
- Automatic processing of various Mobius release formats
- List available versions
- Switch between different builds
- Start and stop Mobius instances
- Prepare Server and MMM packages
- Store unused builds in compressed format

## Usage
`mvm [command] [options]`

### Commands: 
| Command           | Description                                                   |
|-------------------|---------------------------------------------------------------|
| `--upload <file>` | Upload a new Mobius version (ZIP file).                       |
| `--list`          | List all available Mobius versions.                           |
| `--switch <ver>`  | Switch to a specified Mobius version.                         |
| `--start <ver>`   | Start the specified Mobius version.                           |
| `--stop`          | Stop the currently running Mobius version.                    |
| `--delete <ver>`  | Delete a specified Mobius version.                            |
| `--current`       | Show the currently active Mobius version.                     |
| `--server`        | Create compressed server package for upload to server machine |
| `--mmm`           | Create compressed mmm package for upload to ICC tablets       |
| `--help`          | Show this help message.                                       |

---
**Copyright 2024 by Kolter Saurey. Licensed under the MIT License**
