import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage.color import label2rgb
from skimage.filters import sobel
from skimage.measure import label
from skimage.segmentation import expand_labels, watershed

# Check that skimage works
coins = data.coins()

## Make segmentation using edge-detection and watershed.
edges = sobel(coins)

## Identify some background and foreground pixels from the intensity values.
## These pixels are used as seeds for watershed.
markers = np.zeros_like(coins)
foreground, background = 1, 2
markers[coins < 30.0] = background
markers[coins > 150.0] = foreground

ws = watershed(edges, markers)
seg1 = label(ws == foreground)

expanded = expand_labels(seg1, distance=10)

# Check that mpl works

## Show the segmentations.
fig, axes = plt.subplots(
    nrows=1,
    ncols=3,
    figsize=(9, 5),
    sharex=True,
    sharey=True,
)

axes[0].imshow(coins, cmap="Greys_r")
axes[0].set_title("Original")

color1 = label2rgb(seg1, image=coins, bg_label=0)
axes[1].imshow(color1)
axes[1].set_title("Sobel+Watershed")

color2 = label2rgb(expanded, image=coins, bg_label=0)
axes[2].imshow(color2)
axes[2].set_title("Expanded labels")

for a in axes:
    a.axis("off")
fig.tight_layout()
plt.show()

# Check that napari works

import napari

viewer = napari.Viewer()
image_layer = viewer.add_image(coins)
labels_layer = viewer.add_labels(seg1)

napari.run()

# Check that sklearn runs

from sklearn.linear_model import LogisticRegression

lg = LogisticRegression(solver='liblinear')

# Check that remote datasets can be loaded

cells = data.cells3d()
