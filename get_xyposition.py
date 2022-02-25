"""
Function to extract only coordinate data from Dat file.
The argument is the path to read the Dat file.
"""
def get_xyposition(path_to_read_dat):
    import pandas as pd
    import numpy as np

    #load a datfile as DataFrame
    loaded_dat = pd.read_csv(path_to_read_dat, sep=',', header=None)

    #transform a DataFrame into a list
    list_of_traj_draw = loaded_dat.values.tolist()

    nparray_of_traj_draw = [None for _ in range(len(list_of_traj_draw))]
    index = 0

    for row in list_of_traj_draw:
        normalized_row = row[0]
        #normalize multiple spaces into a single space
        while '  ' in normalized_row:
            normalized_row = normalized_row.replace('  ', ' ')
        #extract values except for spaces from normalized_row
        nparray_of_traj_draw[index] = np.array(normalized_row.split(' ')[1:7])
        index += 1

    #transform a list into a numpy array to get columns
    nparray_of_traj_draw = np.array(nparray_of_traj_draw)

    np_float = np.vectorize(float)

    #apply each element in a numpy array to the float function
    return np_float(nparray_of_traj_draw[:, 1:3])