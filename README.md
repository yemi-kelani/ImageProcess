
#### Description
---
Removes exif data from images and optionally replaces them. Suppprted extensions include: [ jpg, jpeg, png, raw ]
-r, --replace will replace the image,. Otherwise it will be saved with the tag "New_" inserted into the filename.

#### Usage
---

`pip install -r requirements.txt`

`python3 process_image.py <PATH_TO_IMAGE_FOLDER>`
`python3 process_image.py <PATH_TO_IMAGE_FOLDER> -r <True | False>`
`python3 process_image.py <PATH_TO_IMAGE_FOLDER> --replace <True | False>`