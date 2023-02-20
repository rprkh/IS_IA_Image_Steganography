# IS IA1 - Image Steganography

### Contributors
- Uchit Mody: 16010120030
- Rahil Parikh: 16010120037
- Jai Rajani: 16010120041

### About Image Steganography
**Steganography**, which translates to "covered writing" or "hidden writing", is derived from the Greek terms `stegos` which means "to cover," and `grayfia`, which means "writing". Sensitive information can be hidden with steganography by being inserted into a text, audio, or video file. It is one of the methods used to defend sensitive or secret information against nefarious attacks. *Image Steganography* as the name suggests, steganography is the process of hiding data within an image file. The "cover picture" is the image selected for this purpose, while the "stego image" is the image that results from the steganography.

### Implementation Screenshots

![image](https://user-images.githubusercontent.com/75483881/220123698-87d67820-9b18-4cee-8bf3-569d76d7403d.png)

![image](https://user-images.githubusercontent.com/75483881/220123919-57a41a65-8d2a-4431-8605-b7ae0c1508eb.png)

![image](https://user-images.githubusercontent.com/75483881/220124060-50702de7-d839-49b2-8c21-72eb0f73ba1b.png)

![image](https://user-images.githubusercontent.com/75483881/220124133-06e6262e-3b07-4727-9eab-ae0e40daae42.png)

![image](https://user-images.githubusercontent.com/75483881/220124315-d45463d4-87f5-4668-9a7f-73c2efa4677f.png)

### Explanation
- We have utilized the Least Significant Bit Algorithm for this method.
- In Least Significant Bit Algorithm a secret key is appended to the data to be hidden in the image and the new data is converted to binary.
- Images are made up of pixels which usually refer to the color of that particular pixel.
- In an coloured image, these pixels are made up of three components (Red, Green, Blue) and each component is in the range 0-255.
- In this algorithm, we take the input text from user and using the secret key value we get the data message which we encode by converting it into binary format.
- The encoded string is then encrypted in the image bit by bit.
- On doing the same for every pixel, a new image matrix is created.
- The new image has negligible changes because only the least significant bits are changed.
- To decode, the least significant bit BGR components of pixels are extracted and concatenated in a string.
- Groups of 8 bits are formed and converted to corresponding character values and once the key is found at the end of the string the decryption stops and the message is returned without the key.


### Is Steganography a Safe Way to Communicate?
When steganography is used alone, it provides security through obscurity, which may result in the secret message being revealed. Combining steganography and cryptography is the most effective way to hide a message from adversaries while still protecting it if it is discovered.
