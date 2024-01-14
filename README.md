Save any text into an image and decode it back.

How it works:

The program uses Alpha (translaprency) colour channel of image's pixels to save binary values of symbols the text is made of. Every pixel saves 1 bit of information (Alpha==255 -> 0, Alpha==254 -> 1, Alpha==253 -> No data). The first pixel's Alpha value will always be 253 to check if the image may have an text saved into it.

How to use: 

Follow instructions displayed by the program.
