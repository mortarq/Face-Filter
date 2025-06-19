import cv2 # OpenCV is a library for computer vision (face detection, etc.)
from PIL import Image # Pillow is a library we will use to handle images (overlaying, etc.)

# Input and Overlay images
input_path = "geeked.jpg"       
overlay_path = "wasted2.png" #PNG so that it supports transparency for the wasted-bar

cv_image = cv2.imread(input_path) # Reads the input image, so that we can process it with OpenCV
if cv_image is None: # If we could't read the image, it prints out an error
    raise FileNotFoundError(f"Could not load image: {input_path}")

# Face recognition using the cv2 library
gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) #Face detection requires grayscale images (so we convert it)
face_cascade = cv2.CascadeClassifier( # Load the pre-trained Haar Cascade model for our face detection 
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# We convert the OpenCV (BGR) into Pillow (RBG) for easy overlaying
# Pillow uses RGBA so we can handle transparency
input_pil = Image.fromarray(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)) 
overlay = Image.open(overlay_path).convert("RGBA")

# Now we paste the overlay on each detected face
# We get the coordinates of each face and resize the overlay for each one
# Then we paste the overlay on the input image

for (x, y, w, h) in faces: # -> coordinates (x, y) and size of the face (w, h)
    resized_overlay = overlay.resize((w, h))
    input_pil.paste(resized_overlay, (x, y), resized_overlay)

# Now we save the image with the overlays applied
output_path = "output.jpg" 
input_pil.save(output_path)
input_pil.show()
# It displays the image immediately

# Extra we will also print out how many faces were detected and where the image was saved to
print(f"Found {len(faces)} face(s), saved to {output_path}")
