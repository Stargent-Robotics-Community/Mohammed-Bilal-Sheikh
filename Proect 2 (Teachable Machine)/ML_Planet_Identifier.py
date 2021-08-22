import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
#python file for Tkinter code
from tkinter import *
# loading Python Imaging Library
from PIL import ImageTk, Image
# To get the dialog box to open when required 
from tkinter import filedialog

#functions
def open_img(file_name):
    # Select the Imagename  from a folder 
    x = file_name
  
    # opens the image
    img = Image.open(x)
      
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)
  
    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)
   
    # create a label
    panel = Label(root, image = img)
      
    # set the image as img 
    panel.image = img
    panel.grid(row = 2)

def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title ='"pen')
    return filename

def predict_now(prediction_list,tkinter_root):
    i=np.argmax(prediction_list[0], axis=0)
    text = Text(tkinter_root, height = 5, width = 15)
    text.grid(row = 4)
    text.insert(END, "" + lables[i])


# Create a window
root = Tk()
  
# Set Title as Image Loader
root.title("Image Loader")
  
# Set the resolution of window
root.geometry("%dx%d+%d+%d" % (550,300,300,150))
  
# Allow Window to be resizable
root.resizable(width = True, height = True)

#getting file name
img_file_name = openfilename()

#display selected img
open_img(img_file_name)

'''
# Create a button and place it into the window using grid layout
#btn = Button(root, text ='open image', command = open_img).grid(row = 1, columnspan = 4)
'''




# Lables for returning the name of the planet
lables = ['Jupiter','Saturn','Earth','Mars']

# Disable scientific notations for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model(r'C:\Users\user\Desktop\Web Dev\VS-Code\Random\keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(4, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image1 = Image.open(""+img_file_name)


#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image1 = ImageOps.fit(image1, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array1 = np.asarray(image1)

# Normalize the image
normalized_image_array1 = (image_array1.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array1

# run the inference
prediction = model.predict(data)

#button for prediction
btn = Button(root, text ='Prediction', command = predict_now(prediction,root)).grid(row = 3, columnspan = 4)



'''
#print(prediction)
#print("="*100)
#print("\nThe Result of prediction is: \n")
#print(i)
#print("\nThe image: " + str(k) + "\nIs a: " + lables[i])

'''


root.mainloop()
