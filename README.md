# BackUpSoftware

A Python Project Where backup of Selected files are stored in the same directory.

## Project Overview

BackUpSoftware is a simple Python project designed to create backups of selected files in the same directory. It aims to help users easily store copies of their important files.

## Setup Instructions

### Prerequisites

- Python 3.x
- PyInstaller (for creating the executable)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Aryan01b/BackUpSoftware.git
   cd BackUpSoftware
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Creating the Executable

To create an executable using PyInstaller, follow these steps:

1. Install PyInstaller if you haven't already:
   ```sh
   pip install pyinstaller
   ```

2. Navigate to the project directory and run the following command to create the executable:
   ```sh
   pyinstaller --onefile backup.py
   ```

3. The executable will be created in the `dist` directory.

## User Manual

### Usage Instructions

1. Run the executable:
   ```sh
   ./dist/backup
   ```

2. Follow the on-screen instructions to select the files you want to back up.

### Example

Here's an example of how to use BackUpSoftware:

```sh
./dist/backup
```

Follow the prompts to select the files you wish to back up. The selected files will be copied to the same directory with a timestamp appended to their names.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to modify this draft to better fit your project's specifics. Let me know if you need any further changes!
