from tokenize import Double


class Pitch():
	def __init__(self, frequency) -> None:
		self.frequency = frequency

	def __str__(self):
		return str(self.frequency)

	#Frequency ratios:
	#Unison 1:1
	#Minor second 15:16
	#Major second 8:9
	#Minor third 5:6
	#Major third 4:5
	#Fourth 3:4
	#Tritone 32:45
	#Fifth 2:3
	#Minor sixth 5:8
	#Major sixth 3:5
	#Minor seventh 5:9
	#Major seventh 8:15
	#Octave 1:2