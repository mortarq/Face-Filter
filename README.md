# Face-Filter
-- Face Filter project, uses AI to find faces and overlay a chosen image over it

With the original code I also provided two example photos, one is a jpg, which will be the one
used as a base (it's also the one where the AI tries to find faces) and a png, which is an 
exaple overlay (I made a wasted filter inspired by GTAIV with photoshop). It's imporant the
overlay is a png if you are working with transparency.

The pre-trained AI model might not be the most accurate one, but it's easier to work 
with. This specific AI is trained on data to look for human faces, so do not be surprised if it
doesn't work for animals etc. IF you want to change that, you can also use another model.

The AI finds the faces in the photo and gives us 4 vectors. Two are for the position of the face
x, y and the other two are for the size of the face w (for width) h (for height). Basically what
we do is with the overlay is adjust our png to the faces and stitch it over, I explained it more
concrete in FILTER.py, where you can also see the actual code.


This code is free to use to anyone interested
