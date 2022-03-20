from pitch import Pitch

class Keyboard():
	def __init__(self, a4_frequency:float=440.0) -> None:
		self.notes = self.get_keyboard_pitches(a4_frequency)

	def get_semitone_ratio(self) -> float:
		return 2.0**(1.0/12.0)

	def get_keyboard_pitches(self, a4_frequency:float=440.0) -> list:
		"""
		Returns the list of pitches that make up an 88 key keyboard, given
		the A4 tuning frequency. 

		Result is a list, ordered from lowest pitch to highest.
		"""

		keyboard_pitches = []

		current_frequency = a4_frequency/16.0 #Down 4 octaves (TODO refactor)

		semitone_ratio = self.get_semitone_ratio()
		for key in range(88): #TODO expand for variable number of keys
			current_pitch = Pitch(current_frequency)
			keyboard_pitches.append(current_pitch)
			current_frequency *= semitone_ratio

		return keyboard_pitches