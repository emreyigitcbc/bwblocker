# Bad Word Blocker for Windows/Linux/MacOS
Is it really a blocker? No, it stores every pressed key in a list and compares last `n` key with some bad word and sends `length of badword` `backspace` signal to OS.

### Usage
It needs 2 modules, type `pip install -r requirements.txt` to install them automatically or type `pip install pynput` and `pip install pyautogui`.
Then you just need to start the script by using `python main.py`.

Just close the `shell` or `command console` to quit.

### Editing Bad Words
In first start It creates `badword_config.json` file so you can edit, add or delete bad words as you wish. It doesn't update its own bad words, so after editing file you have to re-start the script.
