import cv2
import os
from glob import glob


class PNGPlayer:

    def __init__(self, folder):

        self.files = sorted(glob(os.path.join(folder, "*.png")))

        self.frames = []

        for f in self.files:
            img = cv2.imread(f, cv2.IMREAD_UNCHANGED)

            if img is not None:
                self.frames.append(img)

        self.index = 0
        self.playing = False

    def play(self):
        self.index = 0
        self.playing = True

    def update(self):

        if not self.playing:
            return None

        if self.index >= len(self.frames):
            self.playing = False
            return None

        frame = self.frames[self.index]
        self.index += 1

        return frame