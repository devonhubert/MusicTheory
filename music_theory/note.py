from pitch import Pitch

class Note():
	def __init__(self, pitch:Pitch) -> None:
		self.pitch = pitch
		#self.duration = None #duration derived from rhythm context