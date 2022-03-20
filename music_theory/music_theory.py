from keyboard import Keyboard

keyboard = Keyboard()
for pitch in keyboard.get_keyboard_pitches():
	print(pitch)