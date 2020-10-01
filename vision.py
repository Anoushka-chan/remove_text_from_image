from google.cloud import vision
import io
import cv2
import numpy as np

client = vision.ImageAnnotatorClient()
path = 'Bath1.png'
# path = 'OCRImg/Bath2.jpg'
with io.open(path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')
outputFile = ''
for text in texts:
	print('\n"{}"'.format(text.description))

	vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])

	print('bounds: {}'.format(','.join(vertices)))


##---------Fill Color START-----------
	i = 1
	x1 = 0
	y1 = 0
	x2 = 0
	y2 = 0

	for vert in text.bounding_poly.vertices:
		print('vertxxxxx::::',vert.x)
		print('vertyyyyy::::',vert.y)
		if outputFile=='':
			img = cv2.imread(path)
		else:
			img = cv2.imread("output.jpg")
		img = np.array(img)
		# color = (0, 0, 0)
		print(img)
		if i == 1:
			x1 = vert.x
			y1 = vert.y
		if i == 3:
			x2 = vert.x
			y2 = vert.y
		if i == 4:  

			print('one two::::---',x1, y1, x2, y2)
			cv2.rectangle(img, (x1,y1), (x2,y2),(0, 0, 0),-1)
			outputFile = "output.jpg"
			cv2.imwrite(outputFile,img)
		i = i+1
##---------Fill Color END-----------


##--------Logo START---------
responseLogo = client.logo_detection(image=image)
logos = responseLogo.logo_annotations
print('Logos:')
for logo in logos:
    print(logo.description)
##--------Logo END---------


##--------Object START---------
objects = client.object_localization(
        image=image).localized_object_annotations

print('Number of objects found: {}'.format(len(objects)))
for object_ in objects:
    print('\n{} (confidence: {})'.format(object_.name, object_.score))
    print('Normalized bounding polygon vertices: ')
    for vertex in object_.bounding_poly.normalized_vertices:
        print(' - ({}, {})'.format(vertex.x, vertex.y))
##--------Object END---------

if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            response.error.message))

#################Img Text ENT ##################