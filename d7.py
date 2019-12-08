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

    for pixelIdx in range(img_size):
        pixel = line[pixelIdx]
        if pixel == '0':
            zeros += 1
            #print "zero found in layer " + str(layer)
        if pixel == '1':
            ones += 1
        if pixel == '2':
            twos += 1

        if ((pixelIdx+1) % layer_size == 0) and pixelIdx != 0:
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



read_data("input/d7.txt", 25, 6)
