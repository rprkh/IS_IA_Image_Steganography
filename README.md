# IS IA1 - Image Steganography

### Contributors
- Uchit Mody: 16010120030
- Rahil Parikh: 16010120037
- Jai Rajani: 16010120041

### About Image Steganography
**Steganography**, which translates to "covered writing" or "hidden writing", is derived from the Greek terms `stegos` which means "to cover," and `grayfia`, which means "writing". Sensitive information can be hidden with steganography by being inserted into a text, audio, or video file. It is one of the methods used to defend sensitive or secret information against nefarious attacks. *Image Steganography* as the name suggests, steganography is the process of hiding data within an image file. The "cover picture" is the image selected for this purpose, while the "stego image" is the image that results from the steganography.


###Explanation
-We have utilized the Least Significant Bit Algorithm for this method.
-In Least Significant Bit Algorithm a secret key is appended to the data to be hidden in the image and the new data is converted to binary.
-Images are made up of pixels which usually refer to the color of that particular pixel.
-In an coloured image, these pixels are made up of three components (Red, Green, Blue) and each component is in the range 0-255.
-In this algorithm, we take the input text from user and using the secret key value we get the data message which we encode by converting it into binary format.
-The encoded string is then encrypted in the image bit by bit.
-On doing the same for every pixel, a new image matrix is created.
-The new image has negligible changes because only the least significant bits are changed.
-To decode, the least significant bit BGR components of pixels are extracted and concatenated in a string.
-Groups of 8 bits are formed and converted to corresponding character values and once the key is found at the end of the string the decryption stops and the message is returned without the key.
