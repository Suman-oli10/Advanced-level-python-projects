import pyautogui
import pyperclip
import time

# Small delay so app becomes ready
time.sleep(2)

# Step 1: Click chrome icon at (1359, 1041)
pyautogui.click(1128, 1041)

# Wait for app/window to open
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(598, 281)
pyautogui.dragTo(1750, 901, duration=1, button='left')

# Small wait after selection
time.sleep(0.5)

# Step 3: Copy selected text (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')

# Wait for clipboard to update
time.sleep(0.5)

# Step 4: Store clipboard text in variable
copied_text = pyperclip.paste()

# Print result
print("Copied Text:")
print(copied_text)