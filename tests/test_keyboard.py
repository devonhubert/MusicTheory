from music_theory.keyboard import Keyboard

def test_get_keyboard_pitches():
	keyboard_pitches = Keyboard.get_keyboard_pitches()
	for pitch in keyboard_pitches:
		print(pitch)