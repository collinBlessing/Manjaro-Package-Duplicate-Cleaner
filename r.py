#!/usr/bin/env python

import os
import re
import shutil

# Directory where packages are stored
d = '/var/lib/pacman/local'
# Folder to move old versions of duplicates
old_pkg_dir = '/var/lib/pacman/OLD'

# Ensure the old packages directory exists
if not os.path.exists(old_pkg_dir):
    os.makedirs(old_pkg_dir)

# List all package folders in the directory
packages = os.listdir(d)
packages.sort()

# Regular expression to capture package name and version
pkgname_search = re.compile(r'^(.*?)-(\d+(\.\d+)*)')

old_packages = []

# Iterate through each package folder
for pkg1 in packages:
    if pkg1 in old_packages:
        continue

    # Get package name and version
    match1 = pkgname_search.match(pkg1)
    if not match1:
        continue
    pkgname = match1.group(1)

    # Look for duplicates
    for pkg2 in packages:
        if pkg2 == pkg1 or pkg2 in old_packages:
            continue

        match2 = pkgname_search.match(pkg2)
        if not match2:
            continue
        pkgname2 = match2.group(1)

        # If both packages are the same
        if pkgname == pkgname2:
            # Get the paths of both packages
            path1 = os.path.join(d, pkg1)
            path2 = os.path.join(d, pkg2)

            # Ensure both paths exist before comparing timestamps
            if not os.path.exists(path1) or not os.path.exists(path2):
                print(f"Warning: One of the packages {pkg1} or {pkg2} does not exist. Skipping comparison.")
                continue

            # Compare the modification times
            if os.stat(path1).st_mtime > os.stat(path2).st_mtime:
                old_package = pkg2
            else:
                old_package = pkg1

            # Mark the old package
            old_packages.append(old_package)

            # Move the old package to the backup folder
            oldpath = os.path.join(d, old_package)
            target = os.path.join(old_pkg_dir, old_package)

            # Check if the old package still exists before moving
            if os.path.exists(oldpath):
                print(f"Moving old package {old_package} to {old_pkg_dir}")
                try:
                    shutil.move(oldpath, target)
                except Exception as e:
                    print(f"Error moving package {old_package}: {e}")
            else:
                print(f"Error: Old package {old_package} does not exist at {oldpath}. Skipping move.")
