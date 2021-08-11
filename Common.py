from pathlib import Path
import cv2

class Common(object):

    @staticmethod
    def getImagePath():
        path = Path("images")
        return path
      
    @staticmethod
    def get_images(imgNum):
      filename = "images/Snap" + imgNum + "a.png"
      gt_filename = "images/Snap" + imgNum + "m.png"
      img = cv2.imread(filename)
      gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
      gt = cv2.imread(gt_filename)
      gt = cv2.cvtColor(gt,cv2.COLOR_BGR2GRAY)
      return gray, gt, img