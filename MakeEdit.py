import matplotlib.pyplot as plt
import numpy as np

# Load the original image
img = plt.imread("asjopdjopasdjopaspojdsdf.png")
orig_height, orig_width = img.shape[:2]

# Add exactly 10 pixels of white padding at the bottom
# (1.0 assumes float image data; use 255 if uint8)
pad_val = 1.0 if img.dtype != np.uint8 else 255
padded_img = np.pad(
    img, ((0, 10), (0, 0), (0, 0)), mode="constant", constant_values=pad_val
)

# Setup figure matching the new dimensions
fig_dpi = 300
fig, ax = plt.subplots(
    figsize=(padded_img.shape[1] / 100, padded_img.shape[0] / 100),
    dpi=fig_dpi,
)
ax.imshow(padded_img)
ax.axis("off")

# Add the smaller, gray serif text inside the 10px bottom padding area
ax.text(
    x=orig_width / 2,
    y=orig_height + 5,  # Centered right in the 10px bottom padding
    s="R1 pre-registered, R2-R4 specified after seeing data",
    fontsize=8,  # Smaller font size
    fontfamily="serif",  # Matches the plot's serif font
    color="gray",  # Gray text color matching axis labels
    ha="center",
    va="center",
)

# Save the final image
plt.savefig("image_4401bd_fixed.png", bbox_inches="tight", pad_inches=0)
plt.close()