import cv2

class LifeGameCamera():
    def get_frame(self):
        image = self.draw_image()  # OpenCVを使って描画
        _, encimg = cv2.imencode('.jpg', image)
        return encimg.tobytes()