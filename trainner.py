import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
path='dataset'
def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
       faceImg=Image.open(imagePath).convert('L')
       faceNp=np.array(faceImg,'uint8')
       Id=int(os.path.split(imagePath)[-1].split(".")[1])
       faces.append(faceNp)
       print Id
       Ids.append(Id)
       cv2.imshow('trainer',faceNp)
       cv2.waitKey(10) 
    return Ids,faces
Ids ,faces= getImagesAndLabels('dataset')
recognizer.train(faces, np.array(Ids))
recognizer.save('train/trainner.yml')
cv2.destroyAllWindows()
