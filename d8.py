def read_data(filepath, width, height):
    line = ""
    with open(filepath) as fp:
        line = fp.readline()
        print line
        print len(line)

    img_size = len(line)
    layer_size = width * height
    print "layer size is " + str(layer_size)
    layers = img_size / layer_size
    img = {}
    layer = 0
    zeros, ones, twos = 0, 0, 0
    min_layer, min_zeros = -1, 10000000
    pixels_in_layer = []

    for pixelIdx in range(img_size):
        pixel = line[pixelIdx]
        pixels_in_layer.append(pixel)
        if pixel == '0':
            zeros += 1
            # print "zero found in layer " + str(layer)
        if pixel == '1':
            ones += 1
        if pixel == '2':
            twos += 1

        if ((pixelIdx + 1) % layer_size == 0) and pixelIdx != 0:
            print "New layer at pixel " + str(pixelIdx)
            img[layer] = (zeros, ones, twos)
            if zeros < min_zeros:
                min_zeros = zeros
                min_layer = layer

            layer = layer + 1
            zeros, ones, twos = 0, 0, 0

    print min_zeros
    print img
    print img[min_layer]
    print img[min_layer][1] * img[min_layer][2]


def decode(filepath, width, height):
    raw_image = ""
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            raw_image += line.strip()
            line = fp.readline()
    img_size = len(raw_image)
    layer_size = width * height
    print "layer size is " + str(layer_size)
    layers = img_size / layer_size
    img = {}
    layer = 0
    pixels_in_layer = []

    for pixelIdx in range(img_size):
        pixel = raw_image[pixelIdx]
        pixels_in_layer.append(pixel)

        if ((pixelIdx + 1) % layer_size == 0) and pixelIdx != 0:
            # print "New layer at pixel " + str(pixelIdx)
            img[layer] = pixels_in_layer
            layer = layer + 1
            pixels_in_layer = []

    img[layer] = pixels_in_layer + ['2'] * (width * height - len(pixels_in_layer))

    print img
    for layer in img:
        print str("") +  ": " + str(img[layer])


    decoded = []
    for pixel_number in range(layer_size):
        pixel = 2
        layer_idx = 0
        while layer_idx < layers:
            # print "Checking layer " + str(layer_idx) + " for pixel_nb " + str(pixel_number)
            if img[layer_idx][pixel_number] == `1`:
                pixel = `1`
                break
            if img[layer_idx][pixel_number] == `0`:
                pixel = `0`
                break
            layer_idx += 1
        decoded.append(pixel)


    print ": " + str(decoded)
    result = ""

    pidx = 0
    row =""
    for l in range (height):
        print row
        row = ""
        for c in range (width):
            p = decoded[pidx]
            if p == '1':
                row+="$"
            else:
                row+=" "
            pidx+=1

    print row
    print
    print


    print "result = " + result
    print "result len = " + str(len(result))


decode("input/d7.txt", 25, 6)
#decode("input/d7_short.txt", 2, 2)
