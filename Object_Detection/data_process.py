import numpy as np
import random
from DataAugmentationForObjectDetection.data_aug.data_aug import *
from DataAugmentationForObjectDetection.data_aug.bbox_util import *
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
import pickle as pkl

def data_aug():
	input_file = open("./pascal_voc_training_data.txt", 'r')

	output_name = './augmented_' + aug + '_data.txt'
	output_file = open(output_name, 'w')

	for line in input_file:
		line = line.strip()
		line = line.split(" ")
		filename = line[0]
		obj_num = len(line)//5
		obj_list = []

		for i in range(obj_num):
			obj_list.append(line[(i*5+1):(i*5+6)])

		obj_np = (np.array(obj_list)).astype('int')

		img = cv2.imread("./VOCdevkit_train/VOC2007/JPEGImages/" + filename)[:,:,::-1]

		seq = Sequence([RandomShear(0.2)])
		img_, bboxes_ = seq(img.copy(), bboxes.copy())
		cv2.imwrite("/home/yuan65536/kaggle02/augumented_Shear_test/"+"augmented_Rotate_"+filename, img_)

		output_file.write("augmented_Shear_" + filename)
		bboxes_ = bboxes_.astype('int')
		for item in bboxes_:
			for detail in item:
				output_file.write(' ')
				output_file.write(str(detail))

		output_file.write("\n")
	output_file.close()

def merge_img(path):
	dir_path = os.listdir(path)

	for i in len(dir_path):
		if os.path.isdir(dir_path[i]):
			img_dir = os.path.join(path, dir_path[i]) + '/'
			imgs = os.path.listdir(img_dir)

			for img in imgs:

def merge_text(path):
	dir_path = os.listdir(path)

	output_file = open('./all_training_data.txt','w')

	for i in len(dir_path):
		if os.path.isfile(dir_path[i]):
			text = dir_path[i]
			input_file = open(os.path.join(path, text), 'r')

			for line in input_file:
				output_file.writelines(line)

	output_file.close()
	print('merge txt done')

if __name__ == '__main__':
	if not os.path.isdir('./augmented/train'):
		os.mkdir('./augmented')

	merge_text()