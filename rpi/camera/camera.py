import time
import picamera
import io
import threading
import detection

class ImageProcessor(therading.Thread):
	def __init__(self):
		super(ImageProcessor, self).__init__()
		self.stream = io.BytesIO()
		self.event = threading.Event()
		self.terminated = False
		self.start()
	
	def run(self):
		global done
		while not self.terminated:
			if self.event.wait(1):
				try:
					self.stream.seek(0)
					image = Image.open(self.stream)
					with detection.DetectionProcessor() as dp:
						dp.process(image)
				finally:
					self.stream.seek(0)
					self.stream.truncate()
					self.event.clear()
					with lock:
						pool.append(self)

def streams():
    while not done:
        with lock:
            if pool:
                processor = pool.pop()
            else:
                processor = None
        if processor:
            yield processor.stream
            processor.event.set()
        else:
            # When the pool is starved, wait a while for it to refill
            time.sleep(0.1)

			
with picamera.PiCamera() as camera:
	pool = [ImageProcessor() for i in range(4)]
	camera.resolution = (640, 480)
	camera.framerate = 30
	camera.start_preview()
	time.sleep(2)
	camera.capture_sequence(streams(), use_video_port=True)

while pool:
    with lock:
        processor = pool.pop()
    processor.terminated = True
    processor.join()
