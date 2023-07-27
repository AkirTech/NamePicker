from PIL import Image
from pystray import Icon, Menu, MenuItem

def convert_to_ico(jpg_path, ico_path):
    # Open the JPEG image using Pillow
    image = Image.open(jpg_path)

    # Resize the image to multiple sizes required for the ICO file
    sizes = [256, 128, 64, 32, 16]
    icons = [image.resize((size, size), Image.ANTIALIAS) for size in sizes]

    # Save the resized images as ICO file using pystray's ico module
    icons[0].save(ico_path, format='ICO', sizes=[(size, size) for size in sizes], quality=90)
    print(f"Converted '{jpg_path}' to '{ico_path}' successfully.")

# Specify the paths to your JPEG and desired ICO files
jpg_path = 'G:\\PS-Project\\17-logo-v2.jpg'
ico_path = 'G:\\PS-Project\\17-logo-v2.ico'

# Convert the JPEG image to ICO
convert_to_ico(jpg_path, ico_path)
