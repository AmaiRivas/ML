import cv2
import mediapipe as mp
import time

class FaceMeshDetector():
    def __init__(self, staticImage = False, maxFaces = 5, redefineLms = False, minDetectionCon = 0.5, minTrackingCon = 0.5 ) :
        self.staticImage = staticImage
        self.maxFaces = maxFaces
        self.redefineLms = redefineLms
        self.minDetectionCon = minDetectionCon
        self.minTrackingCon = minTrackingCon

        self.mpDraw = mp.solutions.drawing_utils
        self.drawSpecs = self.mpDraw.DrawingSpec(color = (0, 255, 0), thickness = 1, circle_radius = 1)
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticImage, self.maxFaces, self.redefineLms, self.minDetectionCon, self.minTrackingCon)


    def findFaceMesh(self, img, draw = True) :
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.faceMesh.process(imgRGB)

        faces = []

        if self.results.multi_face_landmarks :
            for faceLms in self.results.multi_face_landmarks:
                if draw :
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpecs, self.drawSpecs)

                face = []
                for id, lm in enumerate(faceLms.landmark) :
                    ih, iw, ic = img.shape

                    x, y = int(lm.x*iw), int(lm.y*ih)
                    face.append([x, y])
                
                faces.append(face)
        return img, faces
    

def main():
    pTime = 0
    cap = cv2.VideoCapture(0)
    
    detector = FaceMeshDetector()

    while True:
        success, img = cap.read()
        
        img, faces = detector.findFaceMesh(img)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime=cTime

        cv2.putText(img, f'fps : {int(fps)}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

        cv2.imshow("Video", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()