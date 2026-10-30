# Image Pixel Calculator
width = int(input("Enter width: "))
height = int(input("Enter height: "))
pixels = width * height
megapixels = pixels / 1000000
print("Total pixels:", pixels)
print("Megapixels:", round(megapixels, 2), "MP")
