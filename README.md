# Warframe CopyPaste Fixer

**Author:** Slxrdd

---

## Overview

This application is a simple desktop tool designed to fix copy-paste issues in Warframe.  
It allows you to send a predefined "thank you" message and paste clipboard content with custom hotkeys.

---

## Features

- Set custom hotkeys to send a thank-you message.
- Set custom hotkeys to paste clipboard content.
- GUI interface with a stylish background.
- Logs actions in real-time.
- Open your social networks with one click.

---

## Requirements

- **Python 3.7+** installed on your system.  
  You can download Python from [python.org](https://www.python.org/downloads/).

- Required Python packages (can be installed via pip):

tkinter
pillow
pynput
pyperclip
keyboard




> Note: `tkinter` is usually included with Python installations on Windows.  
> On some Linux distributions, you may need to install it separately.

---

## Installation

1. **Install Python**

 Download and install the latest Python 3 version from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. **Install required packages**

 Open a terminal or command prompt and run the following commands:

 ```bash
 pip install pillow pynput pyperclip keyboard

If you encounter permission issues, try:

bash
Copier
Modifier
python -m pip install --user pillow pynput pyperclip keyboard


Download the release executable (optional)

If you don't want to run the script directly, check the latest releases for a compiled executable version.

How to Run
Running from source:

bash
Copier
Modifier
python WarframeFixer.py
Using the GUI

The app window opens with fields to set your hotkeys:

Key for the thank-you message (default: -)

Key to paste clipboard content (default: 8)

Click "Apply" to register the hotkeys.

Use your hotkeys in any active window to trigger actions.


Additional Notes
The thank-you message is hardcoded in the script but can be modified inside the send_fixed_message() method.

The "Mes réseaux" button opens your webpage at https://guns.lol/slxrdd.

If you want to customize or extend the tool, feel free to edit the source code.

Troubleshooting
Tkinter errors:
Ensure tkinter is installed. On Ubuntu/Debian:

bash
Copier
Modifier
sudo apt-get install python3-tk
Permission denied when installing packages:
Use --user flag with pip or run the terminal as Administrator.

Hotkeys not working:
Some hotkeys might be reserved by your OS or other applications. Try different keys.

License
This script is provided "as-is" without any warranty. Use it responsibly.

Contact
For any questions or suggestions, visit https://guns.lol/slxrdd.
