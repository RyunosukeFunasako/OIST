"""
Function to plot a trajectory on the extracted image using the coordinate data.
This function is used for the first time for the type of trajectory disappearance ('disappear').
The first argument is the path to the image extracted one frame at a time from the original video.
The second argument is the number of images extracted from the original video one frame at a time.
The third argument is the extracted coordinate data.
The fourth argument is the path to the image where the shape is plotted.
The fifth argument is the path to save the plotted images.
The sixth, seventh, and eighth arguments are the color elements of the trajectory to be plotted.
"""
def trajectory_draw_disappear_1(original_images_path, number_of_frame, xy_position, path_to_read_image, path_to_write_image, trajectory_R, trajectory_G, trajectory_B):
    import cv2

    #as long as the coordinate data is available, the trajectory is plotted on the specified image and saved in the specified path with the name corresponding to the frame number
    for i in range(number_of_frame):
        #as long as there is an image with the figure plotted, use it
        if i < len(xy_position):
            image_name_to_be_read = path_to_read_image + '/image%03d.png' % i
            #plot a trajectory on a specified image
            image = cv2.imread(image_name_to_be_read)
            frame_number = i
            while frame_number - 1 >= 0:
                cv2.line(image, (int(xy_position[frame_number-1][0]), int(xy_position[frame_number-1][1])), (int(xy_position[frame_number][0]), int(xy_position[frame_number][1])), (trajectory_R, trajectory_G, trajectory_B), thickness=1, lineType=cv2.LINE_8)
                frame_number -= 1

        #if there is no image with the figure plotted, use the original image
        elif len(xy_position) <= i < number_of_frame:
            image_name_to_be_read = original_images_path + '/image%03d.png' % i
            #plot a trajectory on a specified image
            image = cv2.imread(image_name_to_be_read)
            
        #save the image to the specified path with the name corresponding to the frame number
        image_name_to_be_write = path_to_write_image + '/image'
        cv2.imwrite(image_name_to_be_write + str(i).zfill(3) + '.png', image)

"""
Function to plot a trajectory on the extracted image using the coordinate data.
This function is used for the first time for the type of trajectory keeping ('keep').
The first argument is the path to the image extracted one frame at a time from the original video.
The second argument is the number of images extracted from the original video one frame at a time.
The third argument is the extracted coordinate data.
The fourth argument is the path to the image where the shape is plotted.
The fifth argument is the path to save the plotted images.
The sixth, seventh, and eighth arguments are the color elements of the trajectory to be plotted.
"""
def trajectory_draw_keep_1(original_images_path, number_of_frame, xy_position, path_to_read_image, path_to_write_image, trajectory_R, trajectory_G, trajectory_B):
    import cv2

    #as long as the coordinate data is available, the trajectory is plotted on the specified image and saved in the specified path with the name corresponding to the frame number
    for i in range(number_of_frame):
        #as long as there is an image with the figure plotted, use it
        if i < len(xy_position):
            image_name_to_be_read = path_to_read_image + '/image%03d.png' % i
            #plot a trajectory on a specified image
            image = cv2.imread(image_name_to_be_read)
            frame_number = i
            while frame_number - 1 >= 0:
                cv2.line(image, (int(xy_position[frame_number-1][0]), int(xy_position[frame_number-1][1])), (int(xy_position[frame_number][0]), int(xy_position[frame_number][1])), (trajectory_R, trajectory_G, trajectory_B), thickness=1, lineType=cv2.LINE_8)
                frame_number -= 1
        
        #if there is no image with the figure plotted, continue plotting the last state of the trajectory on the original image
        elif len(xy_position) <= i < number_of_frame:
            image_name_to_be_read = original_images_path + '/image%03d.png' % i
            #plot a trajectory on a specified image
            image = cv2.imread(image_name_to_be_read)
            frame_number = len(xy_position) - 1
            while frame_number - 1 >= 0:
                cv2.line(image, (int(xy_position[frame_number-1][0]), int(xy_position[frame_number-1][1])), (int(xy_position[frame_number][0]), int(xy_position[frame_number][1])), (trajectory_R, trajectory_G, trajectory_B), thickness=1, lineType=cv2.LINE_8)
                frame_number -= 1
            
        #save the image to the specified path with the name corresponding to the frame number
        image_name_to_be_write = path_to_write_image + '/image'
        cv2.imwrite(image_name_to_be_write + str(i).zfill(3) + '.png', image)

"""
Function to plot a trajectory on the extracted image using the coordinate data.
This function is used for the second and subsequent times for the type of trajectory disappearance ('disappear').
The first argument is the extracted coordinate data.
The second argument is the path to the image where the shape is plotted.
The third argument is the path to save the plotted images.
The fourth, fifth, and sixth arguments are the color elements of the trajectory to be plotted.
"""
def trajectory_draw_disappear_2(xy_position, path_to_read_image, path_to_write_image, trajectory_R, trajectory_G, trajectory_B):
    import cv2

    #as long as there is an image with the figure plotted, use it
    for i in range(len(xy_position)):
        image_name_to_be_read = path_to_read_image + '/image%03d.png' % i
        #plot a trajectory on a specified image
        image = cv2.imread(image_name_to_be_read)
        frame_number = i
        while frame_number - 1 >= 0:
            cv2.line(image, (int(xy_position[frame_number-1][0]), int(xy_position[frame_number-1][1])), (int(xy_position[frame_number][0]), int(xy_position[frame_number][1])), (trajectory_R, trajectory_G, trajectory_B), thickness=1, lineType=cv2.LINE_8)
            frame_number -= 1
            
        #save the image to the specified path with the name corresponding to the frame number
        image_name_to_be_write = path_to_write_image + '/image'
        cv2.imwrite(image_name_to_be_write + str(i).zfill(3) + '.png', image)

"""
Function to plot a trajectory on the extracted image using the coordinate data.
This function is used for the second and subsequent times for the type of trajectory keeping ('keep').
The first argument is the number of images extracted from the original video one frame at a time.
The second argument is the extracted coordinate data.
The third argument is the path to the image where the shape is plotted.
The fourth argument is the path to save the plotted images.
The fifth, sixth, and seventh arguments are the color elements of the trajectory to be plotted.
"""
def trajectory_draw_keep_2(number_of_frame, xy_position, path_to_read_image, path_to_write_image, trajectory_R, trajectory_G, trajectory_B):
    import cv2

    #as long as the coordinate data is available, the trajectory is plotted on the specified image and saved in the specified path with the name corresponding to the frame number
    for i in range(number_of_frame):
        #as long as there is an image with the figure plotted, use it
        if i < len(xy_position):
            image_name_to_be_read = path_to_read_image + '/image%03d.png' % i
            #plot a trajectory on a specified image
            image = cv2.imread(image_name_to_be_read)
            frame_number = i
            while frame_number - 1 >= 0:
                cv2.line(image, (int(xy_position[frame_number-1][0]), int(xy_position[frame_number-1][1])), (int(xy_position[frame_number][0]), int(xy_position[frame_number][1])), (trajectory_R, trajectory_G, trajectory_B), thickness=1, lineType=cv2.LINE_8)
                frame_number -= 1
        
        #if there is no image with the figure plotted, continue plotting the last state of the trajectory on the original image
        elif len(xy_position) <= i < number_of_frame:
            image_name_to_be_read = path_to_read_image + '/image%03d.png' % i
            #plot a trajectory on a specified image
            image = cv2.imread(image_name_to_be_read)
            frame_number = len(xy_position) - 1
            while frame_number - 1 >= 0:
                cv2.line(image, (int(xy_position[frame_number-1][0]), int(xy_position[frame_number-1][1])), (int(xy_position[frame_number][0]), int(xy_position[frame_number][1])), (trajectory_R, trajectory_G, trajectory_B), thickness=1, lineType=cv2.LINE_8)
                frame_number -= 1
            
        #save the image to the specified path with the name corresponding to the frame number
        image_name_to_be_write = path_to_write_image + '/image'
        cv2.imwrite(image_name_to_be_write + str(i).zfill(3) + '.png', image)