import numpy, cv2, random, sys

target_name = sys.argv[1]
target = cv2.imread(target_name)
target_height, target_width, target_channel = target.shape
target = numpy.zeros((target_height, target_width, 3))

print("PixelSeed")
print(f"Status: Generating { target_height }x{ target_width } key")

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