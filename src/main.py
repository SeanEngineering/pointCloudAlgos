import numpy as np
import matplotlib.pyplot as plt
import copy
import os
import sys
import open3d as o3d

# Reading the polygon and turning it into a point cloud
pcd = o3d.io.read_point_cloud('./models/poly.ply')

# Downsampling the point cloud for testing purposes
downpcd = pcd.voxel_down_sample(voxel_size=0.05)

# Changing to uniform color
downpcd.paint_uniform_color([0.1, 0.1, 0.7])

# change the color of the first and last point
downpcd.colors[1] = [1, 0, 0]
downpcd.colors[-1] = [1, 0, 1]

# Displaying the first 30 points
print(np.asarray(downpcd.points)[:30][:])

# Rendering the point cloud out the display
o3d.visualization.draw_geometries([downpcd])
