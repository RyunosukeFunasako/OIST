"""
Function to count the number of images extracted from the original video one frame at a time.
The argument is the path to the images extracted one frame at a time from the original video.
"""
def frame_count(original_images_path):
    import os
    frame_list = os.listdir(original_images_path)
    number_of_frame = 0
    for frame_index in frame_list:
        item = frame_index.split('.')
        if item[1] == 'png':
            number_of_frame += 1
    return number_of_frame