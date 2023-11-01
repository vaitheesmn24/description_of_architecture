from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import StudentForm
import os
from utils.main import jpg_description, docx_description, pdf_description
import shutil
# Create your views here.
import time
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from numba import njit


def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
      
            
def uploadImage(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            uploaded_file = request.FILES["files"]
            file_name = uploaded_file.name

            request.session["file_name"] = file_name

            return redirect("success")
    else:
        form = StudentForm()
    return render(request, "index.html", {"form": form})


def uploadok(request):
    # print('------------------------------')
    start=time.time()
    file_name = request.session.get("file_name")
    media = r"D:\architecture_description\media"
    file_path = os.path.join(media, file_name)
    
    format_name = file_name.split(".")[1]

    descripted = ""
    image_path=""
    # print(file_path,'--------------')
    # image_path=f"media/{file_name}"
    # print(image_path,'---------')
    
    try:
        # assert format_name in file_format, "file is invalid"

        if format_name == "pdf":
            descripted,file_path1= pdf_description(file_path=file_path)
            descripted+=descripted
            # file_path1=descripted[1]
            for folder_path,folder_names,files in os.walk(file_path1):
                if ".jpg" in files[0]:
                    shutil.copy(os.path.join(file_path1,files[0]),media)
                image_path+=f"media/{files[0]}"
        elif format_name == "docx":
            descripted,file_path1 = docx_description(file_path=file_path)
            descripted+=descripted
            # file_path1=descripted[1]
            for folder_path,folder_names,files in os.walk(file_path1):
                if ".jpg" in files[0]:
                    shutil.copy(os.path.join(file_path1,files[0]),media)
                image_path+=f"media/{files[0]}"
            

        elif format_name in ["jpg", "png"]:
            descripted += jpg_description(file_path=file_path)
            print(descripted,'---------') 
            
            image_path+=f"media/{file_name}"
    
    
     
        

    except Exception as ep:
        print(ep)
        
    finally:
        # delete_files_in_folder('media/')
        pass
    context={
         "imagepath": image_path, "file_name": descripted
    }
    # print(time.time()-start,'-----------------------------------------------------------')
    
    return render(
        request, "result.html",context
    )






























































