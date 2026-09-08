# Random & Fun

A collection of small Python scripts, games, utilities, experiments, and generally unnecessary programs. This project is mostly about having fun with Python while experimenting with things like randomness, keyboard input, sounds, timers, games, APIs, and simple automation.

## Scripts

### Random & Games

* **coin_flip.py** - Plays a coin flip game with guesses, scores, streaks, and statistics
* **dice_roller.py** - Rolls dice from the terminal
* **random_name_picker.py** - Uses an API to randomly assign a name and country

  ```bash
  python3 -m pip install requests
  ```
* **fortune.py** - Gives random and questionable life advice
  > Note to self: Do not send to many requests or you will get rate-limited
  ```bash
    python3 -m pip install requests
  ```

* **compliment.py** - Randomly gives compliments
* **insult_generator.py** - Generates random insults
* **number_guessing_game.py** - Creates a simple number guessing game
* **rock_paper_scissors.py** - Plays Rock Paper Scissors against the computer

### Productivity

* **pomodoro.py** - Runs a simple productivity timer

### Generators

* **password_generator.py** - Generates random passwords

### Sound & Keyboard

* **fart_script.py** - Plays a fart sound when F is pressed
  
  ```bash
  python3 -m pip install pynput playsound3
  ```
* **bonk.py** - Plays a random sound when a key is pressed
  
  ```bash
  python3 -m pip install pynput playsound3
  ```
* **soundboard.py** - Maps keyboard keys to different sounds
  
  ```bash
  python3 -m pip install pynput playsound3
  ```
* **random_soundboard.py** - Plays random sounds from keyboard input
  
  ```bash
  python3 -m pip install pynput playsound3
  ```

### Chaos & Shenanigans

* **dramatic_button.py** - Does something unnecessarily dramatic when clicked
* **computer_gremlin.py** - Creates harmless random computer shenanigans
* **mouse_chaos.py** - Creates harmless random mouse shenanigans

---

## Requirements

Most scripts only require Python 3 and use the standard library. Scripts that require additional Python packages list the installation command directly under the script. For example:

```bash
python3 -m pip install requests
```

## Running a Script

From the project directory, run a script with:

```bash
python3 script_name.py
```

For example:

```bash
python3 coin_flip.py
```

---

## Project Structure

```text
Random & Fun/
├── bonk.py
├── coin_flip.py
├── compliment.py
├── computer_gremlin.py
├── dice_roller.py
├── dramatic_button.py
├── fart_script.py
├── fortune.py
├── insult_generator.py
├── mouse_chaos.py
├── number_guessing_game.py
├── password_generator.py
├── pomodoro.py
├── random_name_picker.py
├── random_soundboard.py
├── rock_paper_scissors.py
├── soundboard.py
└── README.md
```

---

## Notes

* Some scripts interact with the keyboard, mouse, audio system, or other parts of the operating system. Depending on the script and operating system, additional permissions or dependencies may be required.
* Scripts are intentionally small and independent, so each one can be run and experimented with on its own.
* This project is a collection of experiments rather than a single application. Some scripts are useful, some are games, and some exist mostly because they seemed funny at the time.
