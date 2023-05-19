import os, sys, re, argparse
from PIL import Image

# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

def convert2jpg():
    for infile in sys.argv[1:]:
        f, e = os.path.splitext(infile)
        outfile = f + ".jpg"
        if infile != outfile:
            try:
                with Image.open(infile) as im:
                    im.save(outfile)
            except OSError:
                print("cannot convert", infile)

def remove_exif(path:str, replace:bool = False):
    """
    suppprted extensions include: [ jpg, jpeg, png, raw ]
    """
    
    files = os.listdir(path)
    extensions = re.compile(r"[\w\-. ]+\.(jpg|jpeg|png|raw)", re.IGNORECASE)
    image_files = [file for file in files if extensions.match(file)]
    
    for image_file in image_files:
        image_path = path + "/" + image_file
        if os.path.exists(image_path) and os.path.getsize(image_path) > 0:
            with Image.open(image_path) as image:
                stripped = Image.new(image.mode, image.size)
                stripped.putdata(list(image.getdata()))
                
                os.remove(image_path) # remove original
                if replace:
                    stripped.save(image_path)
                    print("Succesfully removed metadata and replaced file:", image_file)
                else:
                    stripped.save(path + "/New_" + image_file)
                    print("Succesfully removed metadata from file:", image_file)
    
    uncleaned_files = [file for file in files if file not in image_files]
    if len(uncleaned_files) > 0:
        print("Failed to process the following files:", uncleaned_files)
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
                    prog='ImageProcess',
                    description="""
                        Removes exif data from images and replaces them. 
                        Suppprted extensions include: [ jpg, jpeg, png, raw ]
                    """,
                    epilog="""
                        -r, --replace will replace the image. Otherwise it will
                        be saved with the tag "New_" inserted into the filename.
                    """)
    
    parser.add_argument('filename')
    parser.add_argument('-r', '--replace')
    args = parser.parse_args()
    
    if not bool(args.replace):
        raise ValueError(
            f"""
                Error: --replace accepts a boolean (True | False),
                recieved {type(args.replace)}
            """)
        
    replace = False if args.replace.lower() == "false" else True
    remove_exif(args.filename, replace)