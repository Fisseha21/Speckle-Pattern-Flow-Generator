# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:30:13 2024

@author: Fisseha
"""

import numpy as np
import cv2
import random
import argparse
import os.path as osp
from glob import glob
import os
import matplotlib.pyplot as plt


def speckle_pattern_generator(dimensions):

    # Image dimensions
    width, height = dimensions
    width = 2*width
    height = 2*height
    
    # Create a black background
    image = np.zeros((height, width), dtype=np.uint8)
    
    # Number of ellipses
    num_ellipses = random.randint(4000, 5000)
    
    for _ in range(num_ellipses):
        # Random center location
        center_x = random.randint(0, width - 1)
        center_y = random.randint(0, height - 1)
    
        # Random axis lengths (major and minor)
        axis_length = (random.randint(5, 25), random.randint(5, 25))
    
        # Random angle of rotation
        angle = random.randint(0, 180)
    
        # Random grayscale intensity
        intensity = random.randint(0, 255)
    
        # Fully filled ellipse by setting thickness to -1
        thickness = -1
    
        # Draw the filled ellipse on the image
        cv2.ellipse(image, (center_x, center_y), axis_length, angle, 0, 360, intensity, thickness)
    
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    #cv2.imwrite('speckle_pattern.png', image)
    
    return blurred_image


def write_flo(filename, u, v):
    """
    Write optical flow to a .flo file.
    
    Parameters:
    filename (str): Name of the .flo file to save.
    u (np.ndarray): Horizontal displacement (u) field.
    v (np.ndarray): Vertical displacement (v) field.
    """
    # Verify that u and v have the same shape
    assert u.shape == v.shape, "The shape of u and v must be the same."

    # Get the height and width of the displacement fields
    height, width = u.shape

    # Create the .flo file and write the magic number, width, and height
    with open(filename, 'wb') as f:
        # Write the magic number (float32)
        f.write(np.array([202021.25], dtype=np.float32).tobytes())
        
        # Write width and height (int32)
        f.write(np.array([width, height], dtype=np.int32).tobytes())
        
        # Interleave u and v and write the displacement field (float32)
        uv = np.stack((u, v), axis=2)  # Combine u and v into a 3D array
        uv = uv.astype(np.float32)
        f.write(uv.tobytes())
        
def warp_image_with_flow(image, u, v):
    """
    Warp an image using an optical flow field (u, v).
    
    Parameters:
    image (np.ndarray): The input image to warp.
    u (np.ndarray): Horizontal displacement field (flow in x-direction).
    v (np.ndarray): Vertical displacement field (flow in y-direction).
    
    Returns:
    np.ndarray: Warped image.
    """
    # Verify that the displacement field matches the image dimensions
    assert u.shape == v.shape == image.shape[:2], "Flow field dimensions must match image dimensions."

    # Get image dimensions
    height, width = u.shape

    # Create a grid of coordinates corresponding to the image's pixels
    x, y = np.meshgrid(np.arange(width), np.arange(height))

    # Add the flow field to the pixel coordinates
    map_x = (x - u).astype(np.float32)
    map_y = (y - v).astype(np.float32)

    # Warp the image using remap with bilinear interpolation
    warped_image = cv2.remap(image, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)

    return warped_image

def random_deformation_pattern(dimensions):
    # Image size
    height, width = dimensions
    width = 2*width
    height = 2*height
    
    # Generate a grid of coordinates
    x, y = np.meshgrid(np.arange(width), np.arange(height))

    # Random parameters for Gaussian functions
    dx = 0
    dy = 0
    
    for i in range(2):
        Ax = np.random.uniform(0.003, 0.60)    # Amplitude for x deformation
        Ay = np.random.uniform(0.003, 0.60)    # Amplitude for y deformation
        sigmax0 = np.random.uniform(0.06, 0.5)  # Standard deviation for x deformation (center x0)
        sigmax1 = np.random.uniform(0.06, 0.5)  # Standard deviation for x deformation (center x1)
        sigmay0 = np.random.uniform(0.06, 0.5)  # Standard deviation for y deformation (center y0)
        sigmay1 = np.random.uniform(0.06, 0.5)  # Standard deviation for y deformation (center y1)
        x0 = np.random.uniform(0, width-1)    # Center for x deformation
        x1 = np.random.uniform(0, width-1)    # Center for x deformation
        y0 = np.random.uniform(0, height-1)   # Center for y deformation
        y1 = np.random.uniform(0, height-1)   # Center for y deformation
        
        
        dx += Ax * np.exp(-0.5*((x-x0)/sigmax0)**2 - 0.5*((y-y0)/sigmay0)**2)
        dy += Ay * np.exp(-0.5*((y-y1)/sigmay1)**2 - 0.5*((x-x1)/sigmax1)**2)
    
    # Random scale factors
    stx = np.random.uniform(0.96, 1.04)
    sty = np.random.uniform(0.96, 1.04)
    
    # Random shear factors
    shx = np.random.uniform(-0.03, 0.03)
    shy = np.random.uniform(-0.03, 0.03)
    
    # Random rotation angle (in radians)
    theta = np.random.uniform(-0.01*np.pi, 0.01* np.pi)
    
    #Shear plus scale
    x_shear_scale = x*(stx-1) + y*shx 
    y_shear_scale = x*shy + y*(sty-1)
    
    #Gaussian function deformation
    x_deformed = x_shear_scale + dx
    y_deformed = y_shear_scale + dy
    
    # Apply rotation
    x_rotated = np.cos(theta) * x_deformed + np.sin(theta) * y_deformed
    y_rotated = -np.sin(theta) * x_deformed + np.cos(theta) * y_deformed
    
    #Apply translation
    tx = np.random.uniform(-4, 4)
    ty = np.random.uniform(-4, 4)
    
    u = x_rotated + tx
    v = y_rotated + ty
    
    return u, v

def vizualize_flow(path, u, v):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.title('Displacement Field u (x-direction)')
    plt.imshow(u, cmap='jet')
    plt.colorbar()
    
    plt.subplot(1, 3, 2)
    plt.title('Displacement Field v (y-direction)')
    plt.imshow(v, cmap='jet')
    plt.colorbar()
    
    plt.subplot(1, 3, 3)
    plt.title('Displacement Field magnitude ')
    
    uu = (v**2 + u**2)
    
    plt.imshow(uu, cmap='jet')
    plt.colorbar()
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def data_generator(output_path, number_of_sequences, seq_length, output_dimension):
    
    h, w = output_dimension
        
    h1 = h - h // 2 #work on twice the image size and crop h,w around the center
    h2 = h + h // 2
    
    w1 = w - w // 2
    w2 = w + w // 2
    
    for i in range(number_of_sequences):
          
        
        image1 = speckle_pattern_generator(output_dimension) #generate speckle pattern
        u1, v1 = random_deformation_pattern(output_dimension) #generate random deformation field
        image2 = warp_image_with_flow(image1, u1, v1)
        
        
        image_output_dir = os.path.join(output_path, 'Sequences', 'Seq_%03d' % i)
        if not os.path.exists(image_output_dir):
            os.makedirs(image_output_dir)
        
        flow_output_dir = os.path.join(output_path, 'Flow', 'Seq_%03d' % i)
        if not os.path.exists(flow_output_dir):
            os.makedirs(flow_output_dir)
            
        flow_vis_output_dir = os.path.join(output_path, 'Flow_vis', 'Seq_%03d' % i)
        if not os.path.exists(flow_vis_output_dir):
            os.makedirs(flow_vis_output_dir)
        
        print(image_output_dir)
        
        
        cv2.imwrite(os.path.join(image_output_dir, 'frame%03d.png' % 1), image1[h1:h2, w1:w2]) #save image1 (speckle pattern)
        cv2.imwrite(os.path.join(image_output_dir, 'frame%03d.png' % 2), image2[h1:h2, w1:w2])
        
        write_flo(os.path.join(flow_output_dir, 'flow%03d.flo' % 1), u1[h1:h2, w1:w2], v1[h1:h2, w1:w2]) #flow 1
        vizualize_flow(os.path.join(flow_vis_output_dir, 'flow%03d.png' % 1), u1[h1:h2, w1:w2], v1[h1:h2, w1:w2])
        
        
        u, v = u1, v1
        image = image2
        #for more than two frame cases add some random incremental flows
        for j in range (2, seq_length, 1):
            u1, v1 = random_deformation_pattern(output_dimension)
            u = u + 0.2*u1
            v = v + 0.2*v1
            
            image = warp_image_with_flow(image, u, v)
            
            cv2.imwrite(os.path.join(image_output_dir, 'frame%03d.png' % (j+1) ), image[h1:h2, w1:w2])
            write_flo(os.path.join(flow_output_dir, 'flow%03d.flo' % j), u[h1:h2, w1:w2], v[h1:h2, w1:w2])
            vizualize_flow(os.path.join(flow_vis_output_dir, 'flow%03d.png' % j), u[h1:h2, w1:w2], v[h1:h2, w1:w2])
    


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="A script that generates random multiple frame speckle pattern sequences, grount truth flow")
    
    # Add arguments
    parser.add_argument('--output_path', type=str, help="Path to save sequences and gt flow", required=True)
    parser.add_argument('--seq_number', type=int, help="Number of sequences to generate", required=True)
    parser.add_argument('--seq_length', type=int, help="Number of frames per sequence", required=True)
    parser.add_argument('--dimensions', type=int, nargs=2, help="Output image dimensions as height and width", required=True)
    
    # Parse the arguments
    args = parser.parse_args()
        
    data_generator(args.output_path, args.seq_number, args.seq_length, args.dimensions)
    

if __name__ == "__main__":
    main()
