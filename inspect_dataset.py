from pathlib import Path
from PIL import Image
import numpy as np

folder= Path("data")
sub_folders= list(folder.iterdir())
total_count=0
for sub in sub_folders:     #sub is a Path object test, train etc
    folder_count=0
    print(sub.name)
    sub_folder= folder / sub.name
    contents= list(sub_folder.iterdir())
    for cl_fol in contents: # file is folder bird or drone
        print("  ",cl_fol.name)
        img= list(cl_fol.iterdir())
        count=0
        for item in img:
            if item.suffix.lower() in {".jpg", ".jpeg"}:
                count+=1
        print("  ",count)
        folder_count+=count
        total_count+=count
    print(f"{sub.name} total: ",folder_count)
print("total images: ",total_count)


#IMAGE DIMENSIONS------------------------

fol= Path("data/train/bird")
img= list(fol.iterdir())
first_image=Image.open(img[0])
num_img= np.array(first_image)
normalized_img= num_img / 255
print("Array representation of image: ", num_img.shape)
print("RGB value of top left pixel: ",num_img[0][0])
print("Normalized array of top left pixel: ",normalized_img[0][0])
print("data type: ",num_img.dtype)
print("mode of image: ",first_image.mode)
print("format of image: ",first_image.format)
print(normalized_img.dtype)
print(normalized_img.min())
print(normalized_img.max())
first_size= first_image.size
same_count=0
diff_count=0
jpg_image_count=0
for i in range(len(img)):
    opened_img=Image.open(img[i])
    opened_size= opened_img.size
    img_array= np.array(opened_img)
    if img_array.shape != (416, 416, 3):
        print("Unmatched images: ",img[i].name, img_array.shape)
    if img[i].suffix==".jpg":
        jpg_image_count+=1
    if opened_size==first_size:
        same_count+=1
    else:
        diff_count+=1
print("No of jpg images: ",jpg_image_count)
print("same dimension images count: ",same_count)
print("different dimension images count: ",diff_count)


data_folder= Path("data")
sub_fol= list(data_folder.iterdir())
for sub in sub_fol:
    print(sub.name)
    content= list(sub.iterdir())
    for class_fol in content:
        print("  ",class_fol.name)
        img= list(class_fol.iterdir())
        for i in range(len(img)):
            opened_img= Image.open(img[i])
            num_img= np.array(opened_img)
            trans_arr=np.transpose(num_img,(2,0,1)) #converting for pytorch as it expects CHW channel, height , width from HWC
            if num_img.shape != (416,416,3):
                print(img[i].name, num_img.shape)
