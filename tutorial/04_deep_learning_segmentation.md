---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# What about deep learning

Deep learning-based segmentation is getting extremely good, so why learn "the
classics"? A few reasons:

1. It's important to know the basics to be able to troubleshoot when advanced
methods fail.
2. The fundamentals make it easier to understand how these kinds of data are
*represented*. Segmentation approaches all start and end with the same
representation. PyTorch arrays are *basically* like NumPy arrays, with a few
extra bells and whistles.

To see what we mean, let's try out a state of the art tool for segmentation of
cellular images.

### Exercise: cellpose (2D)

Cellpose is a deep-learning based segmentation tool for images of cells. It's
outstanding at segmenting 2D images, so you should try it on 2D datasets from
scikit-image:

https://scikit-image.org/docs/dev/auto_examples/data/plot_scientific.html

You can also grab a slice of the 3D cells (which would also be a nice
refresher for chapter 0!).

As input, cellpose requires a 2D image with channels as the final axis.

- Read the Cellpose documentation example notebook [here](https://cellpose.readthedocs.io/en/latest/notebook.html).
- (Optional) index the middle plane of your image if it's 3D.
- (Optional) Use
  [`np.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)
  to ensure the channel axis to the final position in the array.
- Call cellpose with the appropriate channel settings (carefully read the example in the Cellpose documentation).
- Display the image channels and the segmentation masks overlaid in napari.


```{code-cell} ipython3
# solution ...
```
