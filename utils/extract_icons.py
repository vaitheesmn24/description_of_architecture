from ultralytics import YOLO
import cv2
import os


def model(imagepath):
        model = YOLO(r"D:\architecture_description\models\best.pt")
        results = model.predict(source=imagepath, save=True, conf=0.25, classes=1)
        result = results[0]
        cor_b = result.boxes.xyxy
        tup = tuple(map(tuple, cor_b.tolist()))
        # print(tu)

        return tup

def get_image_name_from_path(file_path):
        return os.path.basename(file_path)

def crop_image( imagepath, bbox, u):
        img = cv2.imread(imagepath)

        x1, y1, x2, y2 = map(int, bbox)
        # x1, y1, x2, y2=bbox

        cropped_image = img[y1:y2, x1:x2]

        output = r"D:\architecture_description\icon_image"
        image_name = os.path.basename(imagepath)
        image_name = get_image_name_from_path(imagepath)
        image_name = image_name.split(".")[0]
        # print(image_name,'-------------------------------')
        
        filename = f"{image_name}"
        path = os.path.join(output, filename)

        if not os.path.exists(path):
            os.makedirs(path)

        cv2.imwrite(os.path.join(path, f"az_arch{u}.jpg"), cropped_image)

        return
    
def extract_image(image_path):
#     print(image_path,'--------------')
    img_coord = model(image_path)
#     print(img_coord,'=================')
    

    for u in range(len(img_coord)):
        # print('-----------------------------------------------------------------')
        crop_image(image_path, img_coord[u], u)

    return