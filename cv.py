import imageio
import numpy as np
from skimage.transform import resize

# Create reader objects
gif1 = imageio.get_reader(r'D:\NCKH2023\demo\assets\h2s\gt_1.gif')
gif2 = imageio.get_reader(r'D:\NCKH2023\demo\assets\h2s\out_1.gif')

# Take minimum number of frames
number_of_frames = min(gif1.get_length(), gif2.get_length())

# Get the shape of a frame from gif1
sample_shape_1 = gif1.get_data(0).shape  # (height, width, channels)
sample_shape_2 = gif2.get_data(0).shape  # (height, width, channels)
target_shape = (sample_shape_1[0], 
                sample_shape_1[0] * 2)  # Double height and width

# Create writer object
new_gif = imageio.get_writer('output.gif', mode='I')

for frame_number in range(number_of_frames):
    img1 = gif1.get_data(frame_number)
    img2 = gif2.get_data(frame_number)

    # Resize img2 to match img1 if necessary
    # if img1.shape != img2.shape:
    #     img2 = resize(img2, img1.shape, preserve_range=True).astype(np.uint8)

    # Concatenate side by side
    combined = np.hstack((img1, img2))

    # Resize the combined image to 2× gif1 frame size
    resized = resize(combined, target_shape, preserve_range=True).astype(np.uint8)

    # Write to new gif
    new_gif.append_data(resized)

# Close readers and writer
gif1.close()
gif2.close()
new_gif.close()
