import pico2d from*

def update(self, frame_time):
    self.life_time += frame_time
    distance = FreeBoy.RUN_SPEED_PPS * frame_time
    self.total_frames