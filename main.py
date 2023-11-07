from rembg import remove
import easygui 
from PIL import Image
import os

inputPath = easygui.fileopenbox(title="Select image file")
outputPath = easygui.filesavebox(title="Save file to...")

input = Image.open(inputPath)
output = remove(input)

file_extension = os.path.splitext(outputPath)[-1].lower()

#Ensure the file extension is valid and add one if missing
if not file_extension:
    outputPath += ".png"  #Default to PNG format

output.save(outputPath)