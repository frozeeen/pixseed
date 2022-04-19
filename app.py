import cv2, numpy, sys, math, getopt

# Read target and key
type = ""
target_name = ""
key_name = ""

opts, args = getopt.getopt(sys.argv[1:], 't:i:k:')
for opt, arg in opts:
	if opt == '-t':
		type = arg
	elif opt == '-i':
		target_name = arg
		target = cv2.imread(target_name)
		target_height, target_width, target_channel = target.shape
	elif opt == '-k':
		key_name = arg
		key_image = cv2.imread(key_name)
		key_height, key_width, key_channel = key_image.shape

print("PixelSeed")
print(f"Target image: { target_name }")
print(f"Key image: { key_name }")

if type.lower() == "e":
	print("ENCRYPTING")
else:
	print("DECRYPTING")

# Tiling
if target_height != key_height or target_width != key_width:
	missing = math.ceil( target_height / key_width )
	key_image = numpy.tile(key_image, (missing, missing, 1))
	key_image = cv2.resize(key_image, (target_height, target_width))

# Seed generators
def getRowSeed():
	hseed = ""
	for x in range(target_height):
		hseed += str(key_image[x][0][0])
	return int(hseed) % (2 ** 32)

def getColumnSeed(h):
	wseed = ""
	for x in range(target_width):
		wseed += ''.join(str(x1) for x1 in key_image[h][x])
	return int(wseed) % (2 ** 32)

def getPixelSeed(h, w):
	return int(''.join(str(x) for x in key_image[h][w])) % (2 ** 32)

# Main program
if type == "E":

	# Shuffle rows
	numpy.random.seed(getRowSeed())
	numpy.random.shuffle(target)
	for h in range(target_height):
		
		# Shuffle columns
		numpy.random.seed(getColumnSeed(h))
		numpy.random.shuffle(target[h])
		for w in range(target_width):
			# Generate seed for every pixels
			numpy.random.seed(getPixelSeed(h, w))
			numpy.random.shuffle(target[h][w])

else:

	# Restore pixels
	if True:
		for h in range(target_height):
			for w in range(target_width):
				pixelList = list(range(target_channel))
				numpy.random.seed(getPixelSeed(h, w))
				numpy.random.shuffle(pixelList)

				newPixelList = [0] * target_channel
				for i, oi in enumerate(pixelList):
					newPixelList[oi] = target[h][w][i]
				target[h][w] = newPixelList
	
	# Restore columns
	if True:
		for h in range(target_height):
			columnList = list(range(target_width))
			numpy.random.seed(getColumnSeed(h))
			numpy.random.shuffle(columnList)

			newColumnList = [0] * target_width
			for i, oi in enumerate(columnList):
				newColumnList[oi] = target[h][i]

			target[h] = numpy.array(newColumnList)
	
	# Restore pixels
	if True:
		rowList = list(range(target_height))
		numpy.random.seed(getRowSeed())
		numpy.random.shuffle(rowList)
		
		newRowList = [0] * target_height
		for i, oi in enumerate(rowList):
			newRowList[oi] = target[i]

		target = newRowList

target = numpy.array(target)

print("Status: Done")

output_file = target_name.split('.')
output_file[-1] = f"-{ type }.{ output_file[-1] }"
cv2.imwrite(''.join(output_file), target)