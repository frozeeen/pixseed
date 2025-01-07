# PixSeed 🌱

Encrypt your image using another image. (Not suitable for all images)

![PixSeed (github)](https://user-images.githubusercontent.com/40148013/163804800-3156c810-dbb4-4af0-80a2-7f697f529862.png)

### How does it work?

It uses the `key image` (another image) to generate a `seed`, and the seed will be used by the target image to encrypt or decrypt.

### How to use

```sh
# Generate key
python genkey.py -r <key-image-name> -w <width> -h <height> -r <channel>

Arguments:
  -r (optional)   Key file name
  -w (required)   Key image width
  -h (required)   Key image height
  -r (optional)   Key image channel

---

# Encryption
python app.py -t E -i <image-to-encrypt> -k <image-key>

Arguments:
  -t (required)   Type(E|D)
  -i (required)   Target Image
  -k (required)   Key Image

---

# Decryption
python app.py -t D -i <image-to-decrypt> -k <image-key>

Arguments:
  -t (required)   Type
  -i (required)   Target Image
  -k (required)   Key Image
```

### Is it secure?

Not really, this is just for fun and some simple experimentation.
