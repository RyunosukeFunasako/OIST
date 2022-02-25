"""
Function to plot a circle on the extracted image using the coordinate data.
The first argument is the extracted coordinate data.
The second argument is the path to the images extracted from the original video.
The third argument is the path to save the plotted images.
The fourth, fifth, and sixth arguments are the color elements of the circle to be plotted.
"""
def circle_draw(xy_position, path_to_read_image, path_to_write_image, figure_R, figure_G, figure_B):
    import cv2

    #as long as the coordinate data is available, the circle is plotted on the specified image and saved in the specified path with the name corresponding to the frame number
    for i in range(len(xy_position)):
        #plot a circle on a specified image
        image_name_to_be_read = path_to_read_image + '/image%03d.png' % i
        image = cv2.imread(image_name_to_be_read)
        cv2.circle(image, (int(xy_position[i][0]), int(xy_position[i][1])), 8, (figure_R, figure_G, figure_B), thickness = 1, lineType = cv2.LINE_AA)

        #save the image to the specified path with the name corresponding to the frame number
        image_name_to_be_write = path_to_write_image + '/image'
        cv2.imwrite(image_name_to_be_write + str(i).zfill(3) + '.png', image)

        #get the size of the image
        global height, width
        height, width = image.shape[:2]

"""
Function to plot a square on the extracted image using the coordinate data.
The first argument is the extracted coordinate data.
The second argument is the path to the images extracted from the original video.
The third argument is the path to save the plotted images.
The fourth, fifth, and sixth arguments are the color elements of the square to be plotted.
"""
def square_draw(xy_position, path_to_read_image, path_to_write_image, figure_R, figure_G, figure_B):
    import cv2

    #as long as the coordinate data is available, the circle is plotted on the specified image and saved in the specified path with the name corresponding to the frame number
    for i in range(len(xy_position)):
        #plot a square on a specified image
        image_name_to_be_read = path_to_read_image + '/image%03d.png' % i
        image = cv2.imread(image_name_to_be_read)
        cv2.rectangle(image, (int(xy_position[i][0] - 8), int(xy_position[i][1] + 8)), (int(xy_position[i][0] + 8), int(xy_position[i][1] - 8)), (figure_R, figure_G, figure_B), thickness = 1, lineType = cv2.LINE_AA)

        #save the image to the specified path with the name corresponding to the frame number
        image_name_to_be_write = path_to_write_image + '/image'
        cv2.imwrite(image_name_to_be_write + str(i).zfill(3) + '.png', image)

        #get the size of the image
        global height, width
        height, width = image.shape[:2]