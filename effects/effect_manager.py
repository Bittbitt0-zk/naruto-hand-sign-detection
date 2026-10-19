import cv2


class EffectManager:
    def __init__(self):
        self.video = cv2.VideoCapture("assets/sasuke.mp4")
        self.playing = False

    def trigger(self, name):
        if name == "Fireball Jutsu":
            print("🔥 Fireball Triggered!")

            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.playing = True

    def update(self, frame):
        if not self.playing:
            return frame

        ret, effect = self.video.read()

        if not ret:
            self.playing = False
            return frame

        effect = cv2.resize(effect, (300, 300))

        x = 100
        y = 100

        frame[y:y+300, x:x+300] = effect

        return frame