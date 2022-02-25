import video_split
#the path to the original video
video_path = 'work_space/OIST/demo_data/Original_mov1.mp4'
#the path to save the extracted images
path_to_save_image = 'work_space/OIST/original_images'
video_split.video_split(video_path, path_to_save_image)

import frame_count
#the path to the images extracted one frame at a time from the original video
original_images_path = 'work_space/OIST/original_images'
#the number of images extracted from the original video one frame at a time
number_of_frame = frame_count.frame_count(original_images_path)

import get_xyposition
#the path to read the Dat file
path_to_read_dat_1 = 'work_space/OIST/demo_data/Tracks1_Original/workstate_0001.dat'
#get the extracted coordinate data
xy_position_1 = get_xyposition.get_xyposition(path_to_read_dat_1)

#the path to read the Dat file
path_to_read_dat_2 = 'work_space/OIST/demo_data/Tracks1_Original/workstate_0014.dat'
#get the extracted coordinate data
xy_position_2 = get_xyposition.get_xyposition(path_to_read_dat_2)

color = {'white':[255, 255, 255], 'light_blue':[255, 255, 0], 'pink':[255, 0, 255], 'purple':[128, 0, 128], 'blue':[255, 0, 0], 'yellow':[0, 255, 255], 'yellow_green':[0, 255, 0], 'red':[0, 0, 255], 'orange':[36, 74, 247]}

#specify the color of the shape to be plotted
figure_color_1 = 'yellow'

#specify the shape to be plotted
figure_type_1 = 'circle'

#specify the color of the trajectory to be plotted
trajectory_color_1 = 'yellow'

#specify the type of trajectory to be plotted
trajectory_type_1 = 'disappear'

#specify the color of the shape to be plotted
figure_color_2 = 'pink'

#specify the shape to be plotted
figure_type_2 = 'square'

#specify the color of the trajectory to be plotted
trajectory_color_2 = 'pink'

#specify the type of trajectory to be plotted
trajectory_type_2 = 'keep'

figure_R_1, figure_G_1, figure_B_1 = color[figure_color_1][0], color[figure_color_1][1], color[figure_color_1][2]

figure_R_2, figure_G_2, figure_B_2 = color[figure_color_2][0], color[figure_color_2][1], color[figure_color_2][2]

trajectory_R_1, trajectory_G_1, trajectory_B_1 = color[trajectory_color_1][0], color[trajectory_color_1][1], color[trajectory_color_1][2]

trajectory_R_2, trajectory_G_2, trajectory_B_2 = color[trajectory_color_2][0], color[trajectory_color_2][1], color[trajectory_color_2][2]

import figure_draw
if figure_type_1 == 'circle':
    #the path to the images extracted from the original video
    path_to_read_image_1 = 'work_space/OIST/original_images'
    #the path to save the plotted images
    path_to_write_image_1 = 'work_space/OIST/figure_images'
    figure_draw.circle_draw(xy_position_1, path_to_read_image_1, path_to_write_image_1, figure_R_1, figure_G_1, figure_B_1)

elif figure_type_1 == 'square':
    #the path to the images extracted from the original video
    path_to_read_image_1 = 'work_space/OIST/original_images'
    #the path to save the plotted images
    path_to_write_image_1 = 'work_space/OIST/figure_images'
    figure_draw.square_draw(xy_position_1, path_to_read_image_1, path_to_write_image_1, figure_R_1, figure_G_1, figure_B_1)

if figure_type_2 == 'circle':
    #the path to the images extracted from the original video
    path_to_read_image_2 = 'work_space/OIST/figure_images'
    #the path to save the plotted images
    path_to_write_image_2 = 'work_space/OIST/figure_images'
    figure_draw.circle_draw(xy_position_2, path_to_read_image_2, path_to_write_image_2, figure_R_2, figure_G_2, figure_B_2)

elif figure_type_2 == 'square':
    #the path to the images extracted from the original video
    path_to_read_image_2 = 'work_space/OIST/figure_images'
    #the path to save the plotted images
    path_to_write_image_2 = 'work_space/OIST/figure_images'
    figure_draw.square_draw(xy_position_2, path_to_read_image_2, path_to_write_image_2, figure_R_2, figure_G_2, figure_B_2)

import trajectory_draw
if trajectory_type_1 == 'disappear':
    #the path to the image where the shape is plotted.
    path_to_read_image_3 = 'work_space/OIST/figure_images'
    #the path to save the plotted images
    path_to_write_image_3 = 'work_space/OIST/trajectory_images'
    trajectory_draw.trajectory_draw_disappear_1(original_images_path, number_of_frame, xy_position_1, path_to_read_image_3, path_to_write_image_3, trajectory_R_1, trajectory_G_1, trajectory_B_1)

elif trajectory_type_1 == 'keep':
    #the path to the image where the shape is plotted.
    path_to_read_image_3 = 'work_space/OIST/figure_images'
    #the path to save the plotted images
    path_to_write_image_3 = 'work_space/OIST/trajectory_images'
    trajectory_draw.trajectory_draw_keep_1(original_images_path, number_of_frame, xy_position_1, path_to_read_image_3, path_to_write_image_3, trajectory_R_1, trajectory_G_1, trajectory_B_1)

if trajectory_type_2 == 'disappear':
    #the path to the image where the shape is plotted.
    path_to_read_image_4 = 'work_space/OIST/trajectory_images'
    #the path to save the plotted images
    path_to_write_image_4 = 'work_space/OIST/trajectory_images'
    trajectory_draw.trajectory_draw_disappear_2(xy_position_2, path_to_read_image_4, path_to_write_image_4, trajectory_R_2, trajectory_G_2, trajectory_B_2)

elif trajectory_type_2 == 'keep':
    #the path to the image where the shape is plotted.
    path_to_read_image_4 = 'work_space/OIST/trajectory_images'
    #the path to save the plotted images
    path_to_write_image_4 = 'work_space/OIST/trajectory_images'
    trajectory_draw.trajectory_draw_keep_2(number_of_frame, xy_position_2, path_to_read_image_4, path_to_write_image_4, trajectory_R_2, trajectory_G_2, trajectory_B_2)

import video_write
#the path to save the created video
written_video_path = 'work_space/OIST/edited_video.mp4'
#the path to the plotted images
path_to_write_video = 'work_space/OIST/trajectory_images'
#the fps of the video to create
fps = video_split.fps

#the width of the video to create
width = figure_draw.width
#the height of the video to create
height = figure_draw.height
video_write.video_write(number_of_frame, written_video_path, path_to_write_video, fps, width, height)