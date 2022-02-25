"""
Function to create a video from the plotted images.
The first argument is the number of images extracted from the original video one frame at a time.
The second argument is the path to save the created video.
The third argument is the path to the plotted images.
The fourth argument is the fps of the video to create.
The fifth argument is the width of the video to create.
The sixth argument is the height of the video to create.
"""
def video_write(number_of_frame, written_video_path, path_to_write_video, fps, width, height):
    import sys
    import cv2

    #define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(written_video_path, fourcc, fps, (width, height))

    #terminate the system if the video cannot be loaded properly
    if not video.isOpened():
        print("can't be opened")
        sys.exit()

    for i in range(number_of_frame):
        path_to_read_image = path_to_write_video + '/image%03d.png' % i
        image = cv2.imread(path_to_read_image)

        if image is None:
            print("can't read")
            break

        #create a video from the plotted images
        video.write(image)

    #when everything done, release the video
    video.release()