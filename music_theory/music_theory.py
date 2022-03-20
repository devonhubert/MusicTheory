from keyboard import Keyboard
from note import Note

def get_keyboard_pitches(a4_frequency:float) -> list:
	keyboard = Keyboard(a4_frequency)
	keyboard_pitches = keyboard.get_keyboard_pitches()

	#"""
	for pitch in keyboard_pitches:
		print(pitch)
	#"""

	return keyboard_pitches

def get_semitone_ratio() -> float:
	return 2.0**(1.0/12.0)

def get_interval(first_note:Note, second_note:Note):
	frequencies = [first_note.pitch.frequency, second_note.pitch.frequency]
	frequencies.sort()

	lower_frequency = float(frequencies[0])
	higher_frequency = float(frequencies[1])

	#TODO, OR just go based on index
	num_semitones = 0
	while lower_frequency < higher_frequency:
		lower_frequency *= get_semitone_ratio()
		num_semitones += 1

	print(num_semitones)

	if num_semitones == 0:
		return "Perfect Unison"
	elif num_semitones == 1:
		return "Minor Second"
	elif num_semitones == 2:
		return "Major Second"
	elif num_semitones == 3:
		return "Minor Third"
	elif num_semitones == 4:
		return "Major Third"
	elif num_semitones == 5:
		return "Perfect Fourth"
	elif num_semitones == 6:
		return "Tritone"
	elif num_semitones == 7:
		return "Perfect Fifth"
	elif num_semitones == 8:
		return "Minor Sixth"
	elif num_semitones == 9:
		return "Major Sixth"
	elif num_semitones == 10:
		return "Minor Seventh"
	elif num_semitones == 11:
		return "Major Seventh"
	elif num_semitones == 12:
		return "Octave"
	else:
		return "More than an Octave"
	
def get_chord(notes:list):
	notes.sort()

	if len(notes) == 3:
		return get_triad(notes)

def get_triad(notes:list):
	pass

keyboard_pitches = get_keyboard_pitches(440.0)
a0 = Note(keyboard_pitches[50])
c1 = Note(keyboard_pitches[56])

print(get_interval(a0, c1))