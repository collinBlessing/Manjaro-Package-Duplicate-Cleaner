
# Manjaro Package Duplicate Cleaner

## Description

This Python script helps users of **Manjaro Linux** identify and remove duplicate package entries in the system’s package database (`/var/lib/pacman/local`). The script ensures that only the latest versions of packages are retained and old versions are moved to a backup folder (`/var/lib/pacman/OLD`), reducing package bloat and improving system efficiency.

## Features

- Automatically detects duplicate packages in `/var/lib/pacman/local`.
- Compares timestamps of packages and retains only the latest version.
- Moves older versions to a designated folder (`/var/lib/pacman/OLD`).
- Helps maintain a clean and optimized package database.

## Prerequisites

Before using the script, ensure you have the following:

- **Manjaro Linux** with `sudo` access.
- **Python 3.x** installed on your system.

## Installation

To install and use the script, follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/<your-username>/Manjaro-Package-Duplicate-Cleaner.git
cd Manjaro-Package-Duplicate-Cleaner
```

### 2. Make the script executable:

While Python scripts are usually executable directly, to ensure compatibility across systems, you can make the script executable as follows:

```bash
chmod +x r.py
```

### 3. Run the script with `sudo`:

To run the script and clean up old package versions, execute:

```bash
sudo python r.py
```

The script will scan the package folder (`/var/lib/pacman/local`) for duplicate packages, compare their timestamps, and move older packages to the `/var/lib/pacman/OLD` directory.

## Usage

The script will automatically handle package cleanup. Here is the basic usage:

```bash
sudo python r.py
```

### What it does:
1. Scans the `/var/lib/pacman/local` directory for duplicate packages.
2. Compares the timestamps of the packages to determine the newer version.
3. Moves the older versions of the package to the `/var/lib/pacman/OLD` folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

- **Permissions Issues**: Ensure you are running the script with `sudo` to have the necessary permissions for accessing system files.
- **Missing Old Packages**: If a package was previously deleted, the script might fail to move it. Make sure the package exists before running the cleanup.

## Contributions

Feel free to open an issue or a pull request if you find any bugs or wish to suggest improvements. Contributions are welcome!

## Disclaimer

This script should be used with caution. Always ensure you have backups of important data before modifying system files. The script is provided as-is and the authors are not responsible for any potential issues caused during its execution.
