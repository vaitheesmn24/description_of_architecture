from .cos_icons import main
from .extract_icons import extract_image,get_image_name_from_path
from .upload_file import pdf_to_jpg, docx_pdf_jpg

import os
import shutil
# from classification.classify import classifi
import tensorflow as tf
from keras.models import load_model
# from keras_preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
from .ai_description import description_prompt
from numba import njit



def delete_all_subfolders(parent_folder):
    try:
        # List all subdirectories in the parent folder
        subfolders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, f))]

        for subfolder in subfolders:
            subfolder_path = os.path.join(parent_folder, subfolder)
            shutil.rmtree(subfolder_path)
            
    except Exception as e:
        print(f"An error occurred: {e}")

def classifi(file_path):
    loaded_model = tf.keras.models.load_model(r'D:\architecture_description\models\BI_model.h5')
    
    a=''
    # image_path= r"D:\azure_arch\MicrosoftTeamsaz.png"
    # image_path= r"D:\CV\Flowchart\Binary_Classification\Dataset\test\Content\40.png"
    img = cv2.imread(file_path)
    resize = tf.image.resize(img, (150,150))
    # plt.imshow(img)
    img = np.expand_dims(resize, axis=0)
    result=loaded_model.predict(img)
    if result[0][0]== 1.0:
        a+='Architecture'
    elif result[0][1]== 1.0:
        a+='Content'
    
    return a



origin_dir=os.getcwd()
# azure_service_icon=r"D:\architecture_description\Icons"
azure_service_icon=r"D:\architecture_description\Icons"
file_format=['jpg','pdf','docx','png']
# file_path=r'D:\azure_arch\MicrosoftTeamsaz.pdf'
# file_path=r"D:\azure_arch\MicrosoftTeamsaz.png"
arch_folder=r"D:\architecture_description\architecture"


# base_name=os.path.basename(file_path)
# base_name=base_name.split('.')

# file_name=base_name[0]
# format_name=base_name[1]


    



       
def pdf_description(file_path):
    print('entered pdf')
    base_name=os.path.basename(file_path)
    base_name=base_name.split('.')

    file_name=base_name[0]
    # print(file_name,'------------------------------------------------')
    format_name=base_name[1]
    
    
    pdf_image_list=[]
    
    
    pdf_to_jpg(file_path)
    
    img_path=r"D:\architecture_description\image"
    os.chdir(img_path)
    for foldername in os.listdir(img_path):
        folder_path = os.path.join(img_path, foldername)
        if os.path.isdir(folder_path):  # Check if it's a subfolder
            pass

# Loop through files in the subfolder
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.jpg')):
                    image_path = os.path.join(folder_path, filename)
                    pdf_image_list.append(image_path)
                    

    for u in range(len(pdf_image_list)):
        # print(pdf_image_list[u],'---------------------------')
        classification=classifi(pdf_image_list[u])
        print(classification)
        img_pathh=''
        # classification='Architecture'
        if classification=='Architecture':
            subfolder_path = os.path.join(arch_folder, file_name)
            # print(subfolder_path)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
            shutil.copy(pdf_image_list[u],subfolder_path)
        else:
            pass                      
        
    # image_arch_file=r"D:\azure_arch\architecture"
    img_full_path=os.path.join(arch_folder,file_name)
    file_paths = []
    for root, dirs, files in os.walk(img_full_path):
        for filename in files:
            file_paths.append(os.path.join(root, filename))    

    for i in range(len(file_paths)):
        extract_image(file_paths[i])
    # os.chdir(cwd)
   

    folder_path=r"D:\architecture_description\icon_image"
    img_des=[]
    # os.chdir(folder_path)
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            img_des.append(os.path.join(root, filename))
    service_list=[]          
    for u in range(len(img_des)):
        servicename=main(azure_service_icon,img_des[u])
        service_list.append(servicename)
        # description=azure_description(servicename)
    
    delete_all_subfolders(folder_path)
    
    description=description_prompt(set(service_list))
    
        
    return description,subfolder_path


def docx_description(file_path):
    base_name=os.path.basename(file_path)
    base_name=base_name.split('.')

    file_name=base_name[0]
    format_name=base_name[1]
    print('entered docx')
    docx_output=docx_pdf_jpg(filename=file_path)
    pdf_to_jpg(docx_output)
    pdf_image_list=[]
    # img_path=r"D:\azure_arch\image"
    img_path=r"D:\architecture_description\image"
    
    os.chdir(img_path)
    for foldername in os.listdir(img_path):
        folder_path = os.path.join(img_path, foldername)
        if os.path.isdir(folder_path):  # Check if it's a subfolder
            pass

# Loop through files in the subfolder
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.jpg')):
                    image_path = os.path.join(folder_path, filename)
                    pdf_image_list.append(image_path)
                    

    for u in range(len(pdf_image_list)):
        # classification=classify(pdf_image_list[u])
        classification=classifi(pdf_image_list[u])
        print(classification)
        # classification='Architecture'
        if classification=='Architecture':
            subfolder_path = os.path.join(arch_folder, file_name)
            # print(subfolder_path)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
            shutil.copy(pdf_image_list[u],subfolder_path)
        else:
            pass                      
        
    # image_arch_file=r"D:\azure_arch\architecture"
    img_full_path=os.path.join(arch_folder,file_name)
    file_paths = []
    for root, dirs, files in os.walk(img_full_path):
        for filename in files:
            file_paths.append(os.path.join(root, filename))    

    for i in range(len(file_paths)):
        extract_image(file_paths[i])
    
    
    

    folder_path=r"D:\architecture_description\icon_image"
    img_des=[]
    # os.chdir(folder_path)
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            img_des.append(os.path.join(root, filename))
   
    
    service_list=[]           
    for u in range(len(img_des)):
        servicename=main(azure_service_icon,img_des[u])
        # description=azure_description(servicename)
        service_list.append(servicename)
    delete_all_subfolders(folder_path)    
    
    description=description_prompt(set(service_list))
    
    
    
    return description,subfolder_path


def jpg_description(file_path):
    print('entered jpg')
    # print(file_path,'-----------------')
    base_name=os.path.basename(file_path)
    base_name=base_name.split('.')

    file_name=base_name[0]
    format_name=base_name[1]
    
    os.chdir(origin_dir)
    # print('eeeeeeeeeeeeeeeeeeeeeeee')
    extract_image(file_path)
    croped_images_path = os.path.join(origin_dir, f"icon_image\{file_name}")
    if not os.path.exists(croped_images_path):
        os.makedirs(croped_images_path)
    
    list_images = os.listdir(croped_images_path)
    folder_path=r"D:\architecture_description\icon_image"
    
    
    service_list=[]           
    
    for img in list_images:
        
        
        file_to_test = os.path.join(croped_images_path, img)

        # service_name = azs.extract_and_cosine(file_to_test)
        servicename=main(azure_service_icon,file_to_test)
        service_list.append(servicename)
    
    delete_all_subfolders(folder_path)
    # description = azure_description(servicename)
    
    # for service in service_list:
    description=description_prompt(set(service_list))
        # des.write(f"{description}\n")
    
    # print(service_list,'-----------------------')
    return description
    
        
