# 
#  .npz to .mat file converter
#
#  Levi Heath
#  Dept. of Math. 
#  UNL, Lincoln, NE 68605
#  
#  For education only. All rights reserved.
#

import os
import numpy as np
import pylab, scipy.io

# path of folder containing files
path_origin = input('Enter path for folder containing .npz data: ')

# ensures path has a backslash at the end
l=len(path_origin)-1
if path_origin[l] != '/':
    path_origin = path_origin + '/'

# converts files from .npz to .mat
npz_files = os.listdir(path_origin)
for file in npz_files:
    data = np.load(path_origin + file)
    base, ext = os.path.splitext(file)
    scipy.io.savemat(base + '.mat', data)