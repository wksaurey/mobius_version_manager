Help-page for Mobius Version Manager (MVM)
MVM 1 "October 2024" "Version 1.0" "Mobius Version Manager"

mvm - Mobius Version Manager for Testing Environments (MVM)

mvm [command] [options]

The Mobius Version Manager (MVM) allows users to manage, switch,
and run different Mobius builds within a testing environment. It
supports uploading new versions, switching between versions, and
managing Mobius server/client instances.

mvm --upload file_path
Upload a new version by providing the file path to a zip file.

mvm --list
List all available Mobius versions.

mvm --switch version
Switch to a specified Mobius version.

mvm --start version
Start the specified Mobius version.

mvm --stop
Stop the currently running Mobius version.

mvm --delete version
Delete the specified Mobius version from the system.

mvm --current
Show the currently active Mobius version.

mvm --help
Show this help message.

--upload file_path
Upload a new Mobius version.

--list
List all available versions.

--switch version
Switch to a specified version.

--start version
Start a specified version of Mobius.

--stop
Stop the currently running Mobius instance.

--delete version
Delete a Mobius version from the system.

--current
Display the currently active version.

--help
Display the help message.

Copyright 2024 by Kolter Saurey. Licensed under the MIT Lic
