"""
Function to extract the original video as an image one frame at a time.
The first argument is the path to the original video.
The second argument is the path to save the extracted images.
"""
def video_split(video_path, path_to_save_image):
    import cv2
    import sys

    #load a video file
    capture = cv2.VideoCapture(video_path)

    #get the fps of the loaded video file
    global fps
    fps = capture.get(cv2.CAP_PROP_FPS)

    #terminate the system if the video cannot be loaded properly
    if not capture.isOpened():
        print('Failure to load video')
        sys.exit()

    digit = len(str(int(capture.get(cv2.CAP_PROP_FRAME_COUNT))))

    #save the image to the specified path with the name corresponding to the frame number
    n = 0
    while True:
        is_image, frame_img = capture.read()
        if is_image:
            cv2.imwrite(path_to_save_image + '/image' + str(n).zfill(digit) + '.png', frame_img)
        else:
            break
        n += 1
        
    #when everything done, release the capture
    capture.release()