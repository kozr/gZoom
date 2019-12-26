import tldetection
import signdetection
from enum import Enum

class ENABLE_FLAGS(Enum):
	ENABLE_TRAFFIC_LIGHT_DETECTION = 0
	ENABLE_SIGN_DETECTION = 1
	
class DetectionProcessor:
	def __init__(self, flags=[ENABLE_FLAGS.TRAFFIC_LIGHT_DETECTION, ENABLE_FLAGS.ENABLE_SIGN_DETECTION]):
		self.flags = flags
		
	def process(self, image):
		if ENABLE_FLAGS.ENABLE_TRAFFIC_LIGHT_DETECTION in flags:
			tldetection.process(image)
		if ENABLE_FLAGS.ENABLE_SIGN_DETECTION in flags:
			signdetection.process(image)