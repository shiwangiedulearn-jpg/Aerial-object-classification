from pathlib import Path
from PIL import Image
folder= Path("data")
sub_folders= list(folder.iterdir())
total_count=0
for sub in sub_folders:     #sub is a Path object test, train etc
    folder_count=0
    print(sub.name)
    sub_folder= folder / sub.name
    contents= list(sub_folder.iterdir())
    for file in contents: # file is folder bird or drone
        print("  ",file.name)
        img= list(file.iterdir())
        count=0
        for item in img:
            if item.suffix==".jpg":
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
first_size= first_image.size
same_count=0
diff_count=0
for i in range(len(img)):
    opened_img=Image.open(img[i])
    opened_size= opened_img.size
    if opened_size==first_size:
        same_count+=1
    else:
        diff_count+=1
print(same_count)
print(diff_count)

