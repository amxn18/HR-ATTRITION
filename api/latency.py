import time 
class LatencyTimer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        end_time = time.time()
        return round((end_time - self.start_time)*1000, 2) # Latency in m/s