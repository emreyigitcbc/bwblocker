import pyautogui, json, os
from pynput.keyboard import Key, Listener, Controller

keyList = []
badWords = []
maxLen = 0
if not os.path.isfile("./badword_config.json"):
    with open("badword_config.json", "w") as file:
        badWords = ["fuck", "shit", "bitch"]
        maxLen = len(max(badWords, key=len))
        json.dump({"bad_words": badWords}, file)
else:
    with open("badword_config.json", "r") as file:
        jsonFile = json.load(file)
        badWords = jsonFile["bad_words"]
        maxLen = len(max(badWords, key=len))
        
def detectKey(key):
    try:
        keyList.append(key.char)
    except: 
        keyList.append("N")
    
    lastWord = "".join(keyList[-maxLen:])
    detected = [bw for bw in badWords if bw == lastWord[-len(bw):]]

    for bw in detected:
        pyautogui.press("backspace", presses=len(bw))
        
with Listener(on_press = detectKey) as listener:
    print("=" * 20)
    print("=", "BWBlocker v1.0")
    print("=", "Author: Emre Cebeci")
    print("=", "Loaded BW Count:", len(badWords))
    print("=", "Longest BW:", maxLen, "chars long")
    print("=" * 20)
    listener.join()