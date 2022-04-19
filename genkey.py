import numpy, cv2, random, sys, getopt

target_name = "imgs/generated.png"
target_height, target_width, target_channel = (0,0,3)

opts, args = getopt.getopt(sys.argv[1:], 'r:w:h:c:')
for opt, arg in opts:
	if opt == '-r':
		target_name = arg
		target = cv2.imread(target_name)
		target_height, target_width, target_channel = target.shape
	elif opt == '-w':
		target_width = int(arg)
	elif opt == '-h':
		target_height = int(arg)
	elif opt == '-c':
		target_channel = int(arg)

target = numpy.zeros((target_height, target_width, 3))

print("PixelSeed")
print(f"Status: Generating { target_width }x{ target_height } key")

for h in range(target_height):
	for w in range(target_width):
		for c in range(target_channel):
			target[h][w][c] = random.randint(0, 255)

output_file = target_name.split('.')
output_file[-1] = f"-key.{ output_file[-1] }"
output_file = ''.join(output_file)

print("Status: Key generated")
print(f"Output file: { output_file }")

cv2.imwrite(output_file, target)