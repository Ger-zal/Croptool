import cv2
import	os


if __name__== "__main__":

	path="Images/"
	input_dir= os.listdir(path)
	print input_dir
	for directory in input_dir :
		s = str(directory)
		s = path + s + "/"
		names = os.listdir(s)
		print directory + "  " + str(names)
		for name in names:
			print name
			img = cv2.imread(os.path.join(path, directory , name),1)
			os.remove(path+directory+"/"+name)
			# save as JPEG
			name=name[0:(len(name)-5)]
			cv2.imwrite(path+directory+"/"+name+ ".jpg", img)
print("end")
