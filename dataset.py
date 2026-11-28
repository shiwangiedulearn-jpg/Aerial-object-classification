from torch.utils.data import Dataset
from pathlib import Path
from PIL import Image
import numpy as np

class AerialDataset(Dataset):
    def __init__(self):
        self.folder = Path("data/train")
        self.path_fol= []
        contents = list(self.folder.iterdir())
        for content in contents:
            images= list(content.iterdir())
            for i in range(len(images)):
                if content.name=="bird":
                    img_tup=(0,images[i])
                else:
                    img_tup=(1, images[i])
                
                self.path_fol.append(img_tup)

    def __len__(self):
        return len(self.path_fol)
    def __getitem__(self, index):
        label= self.path_fol[index][0]
        image_path= self.path_fol[index][1]
        img= Image.open(image_path)
        img= img.convert("RGB")
        num_img= np.array(img)
        trans_img=np.transpose(num_img, (2,0,1))
        return (label,trans_img)
    
dataset= AerialDataset()
print(len(dataset))
print(dataset[0])
label= dataset[0][0]
trans_img= dataset[0][1]
print(trans_img.shape)
norm_img= trans_img/255
print(norm_img.shape)
print(norm_img.dtype)
print(norm_img.min())
print(norm_img.max())