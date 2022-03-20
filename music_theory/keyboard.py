from pitch import Pitch

class Keyboard():
	def __init__(self) -> None:
		self.notes = self.get_keyboard_pitches()

	def get_keyboard_pitches(self, a4_frequency:float=440.0) -> list:
		"""
		Returns the list of pitches that make up an 88 key keyboard, given
		the A4 tuning frequency. 

		Result is a list, ordered from lowest pitch to highest.
		"""

		keyboard_pitches = []

		current_frequency = a4_frequency/16.0 #Down 4 octaves (TODO refactor)

		semitone_ratio = 2.0**(1.0/12.0)
		for key in range(88): #TODO expand for variable num_keys
			current_pitch = Pitch(current_frequency)
			keyboard_pitches.append(current_pitch)
			current_frequency *= semitone_ratio

		return keyboard_pitches