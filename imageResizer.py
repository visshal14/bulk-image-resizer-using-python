from PIL import Image

Image.MAX_IMAGE_PIXELS = None
import glob

# imagesToResize is name of relative directory path in which image are stores
images = glob.glob("imagesToResize/*.jpg")

if not images:
    print("Error!No Image Found")
    exit()
  
# width of resized image in pixels
basewidth = 600   #height will set according to aspect ratio
for x in images:
    name = "./" + x
    img = Image.open(name)
    print(x)
    wpercent = basewidth / float(img.size[0])
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    tempName = name.split("/")
    nameResize = "./resizedImages/new" + tempName[2]
    img.save(nameResize)
