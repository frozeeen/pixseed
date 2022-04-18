# PixSeed 🌱
Encrypt your image using another image. (Not suitable for all images)

![PixSeed (github)](https://user-images.githubusercontent.com/40148013/163804800-3156c810-dbb4-4af0-80a2-7f697f529862.png)

### How does it work?
It uses the `key image` (another image) to generate a `seed`, and the seed will be used by the target image to encrypt or decrypt.

### How to use
```sh
# Generate key
python genkey.py <image-reference>

# Encryption
python app.py E <image-to-encrypt> <image-key>

# Decryption
python app.py D <image-to-decrypt> <image-key>
```

### Is it secure?
Not really, this is just for fun and some simple experimentation.
