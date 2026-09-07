# Fart Script

A simple Python script that plays a fart sound whenever the F key is pressed

## Requirements
* Python 3
* pynput
* playsound3

Install the dependencies with

```bash
python3 -m pip install pynput playsound3
```

## Setup
Place `fart-with-reverb.mp3` in the same folder as `fart_script.py`. The folder should look like:
```text
fart-script/
├── fart_script.py
├── fart-with-reverb.mp3
└── README.md
```

## Usage
Run the script with:
```bash
python3 fart_script.py
```

Then:
* Press F to play the sound
* Press ESC to exit

## macOS Setup
This script listens for keyboard input globally, so macOS requires Accessibility permission

1. Go to System Settings → Privacy & Security → Accessibility
2. Add and enable the application you are using to run the script

For example, this could be

- Terminal
- Visual Studio Code
- PyCharm
- Another application you use to run Python

After enabling the permission, completely quit and reopen the application before running the script again

## Troubleshooting

### F key does nothing
If the script starts but pressing F does not trigger the sound, check that the application running the script has Accessibility permission. You may see:
```text
This process is not trusted! Input event monitoring will not be possible until it is added to accessibility clients
```
This means macOS has not granted the required permission. Enable Accessibility access and restart the application

### ModuleNotFoundError
If you see an error such as:
```text
ModuleNotFoundError: No module named 'pynput'
```
or:
```text
ModuleNotFoundError: No module named 'playsound3'
```
Install the dependencies with:
```bash
python3 -m pip install pynput playsound3
```
> Note: The original version of this script used the `keyboard` package, but it did not work correctly on macOS, so `pynput` is used instead.

### can't open file
If Python says it cannot find `fart_script.py`, make sure your terminal is in the correct folder

Check your current directory with:
```bash
pwd
```
Check the files in the directory with:
```bash
ls
```
Then run the script using the correct filename:
```bash
python3 fart_script.py
```

## Notes
* The script uses `pynput` to listen for keyboard input
* `playsound3` is used to play the audio file
* The F key listener works globally while the script is running
* macOS Accessibility permission is required for global keyboard input
