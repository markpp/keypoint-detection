# import package
import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "/media/aau3090/Storage/Datasets/teejet/DK/datasets/COCO/tmp/test/"

# set path for coco json to be saved
save_json_path = "/media/aau3090/Storage/Datasets/teejet/DK/datasets/COCO/tmp/test/"

# conert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)