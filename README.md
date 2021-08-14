
#   Summary

This program was made for a Lab homework assignment to make a program 
that can read given barcodes. Since I used made the program in Python, 
the bar code reading part was easy to implement trough an external 
library (pyzbar, which also reads QR codes), so of course to make it
a bit more challenging I also made a basic image viewer around it.

As a note:
- no matter how clear the code might be represented in the image, 
there is a minimum resolution that pybar will be able to read;
- the way I implemented the zoom in function in this program is rather 
"brute forced" (it scales up the image), which means under certain 
conditions it tends to get pretty resource intensive for the thing it is 
actually doing.
- at some point in the future I'd like to fix these issues and also add a 
Drag and Drop feature to the program.
