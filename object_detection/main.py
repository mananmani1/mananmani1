import cv2


from gui_buttons import Buttons
import numpy as np

#intialize button

# button = Buttons()
# button.add_button("Person", 20, 20)



#openCv DNN
net = cv2.dnn.readNet("D:\object_detection\dnn_model\yolov4-tiny.weights","D:\object_detection\dnn_model\yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size = (320,320),scale = 1/255)

classes = []
with open("D:\object_detection\dnn_model\classes.txt","r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
print(classes)





#initialize camera

cap = cv2.VideoCapture(r"D:\object_detection\video.mp4")
# setting a resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


while True:
    #get frames
    
    ret,frame = cap.read()
    #object detection
    (class_ids, scores, bboxes) = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        cv2.rectangle(frame,(x,y),(x + w,y + h),(200,10,50),3)
        class_name = classes[class_id]
        cv2.putText(frame, (class_name),(x,y-10),cv2.FONT_HERSHEY_PLAIN,2,(200,10,50),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(200,10,50),3)
    print('classs',class_ids)
    print('scores',scores)
    print('bboxes',bboxes) 
    
    # button.display_buttons(frame) 
                   



    cv2.imshow("Frame",frame)    
    key = cv2.waitKey(10)
    
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
    


# cv2.putText(frame,"Hello World!!!", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)


 









