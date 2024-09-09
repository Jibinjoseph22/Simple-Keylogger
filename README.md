
### README.md

# Simple Keylogger

## Description
This project is a **Simple Keylogger** implemented in Python. It records and logs keystrokes to a text file (`key_log.txt`). The keylogger captures both regular characters (letters, numbers, etc.) and special keys (like `Enter`, `Space`, `Tab`). This tool should only be used for educational and authorized purposes. Unauthorized use of keyloggers is illegal and can have serious legal consequences.

**Important**: Ensure you have permission to use this tool on any system where it will be deployed. This tool is designed for ethical purposes, such as monitoring one's own system or auditing user inputs with consent.

## Features
- Logs all keystrokes to `key_log.txt`.
- Captures special keys such as `Enter`, `Space`, and `Tab`.
- Stops logging when `Esc` key is pressed.
- Simple and lightweight, running in the background.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jibinjoseph22/simple-keylogger.git
   ```

2. Navigate into the project directory:
   ```bash
   cd simple-keylogger
   ```

3. Install the required dependencies:
   ```bash
   pip install pynput
   ```

4. Run the keylogger:
   ```bash
   python simple_keylogger.py
   ```

## Requirements

- Python 3.x
- `pynput` library (install using `pip install pynput`)

## Usage

Once the script is running, it will start recording all key presses and save them in `key_log.txt` in the same directory.

To stop the keylogger, press the **Esc** key.

## Disclaimer

This project is for **educational purposes only**. Do not use this keylogger on any system without **explicit permission** from the owner. Unauthorized use is illegal and unethical.

