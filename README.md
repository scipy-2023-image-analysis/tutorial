# image analysis and visualization in Python with scikit-image, napari, and
# friends

## A SciPy 2023 tutorial

See the [tutorial page on the SciPy 2023
site](https://cfp.scipy.org/2023/talk/NEUUKG/) for details.

## installation

⚠️ WARNING: You should reinstall this just before the conference as we might
have made some changes by then. ⚠️

You can install the requirements for this workshop in two ways:

### using conda/mamba

To use [conda](https://docs.conda.io/en/latest/) or
[mamba](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html), use the
provided `environment.yml` file. For example:

```
conda env create -f environment.yml
```

then:

```
conda activate image-analysis-23
```

### using your own environment manager

If you want to install into your own environment (as a reminder, never install
to your operating system's system-wide Python install; if you don't know what
this means, use conda as described above), you can use:

```
python -m pip install -r requirements.txt
```

## Checking that your installation works

If you have installed everything correctly, you should be able to run:

```
python test-env.py
```

Some of the libraries take a while to run the first time, so be patient. You
should see (1) a matplotlib window with three image panels pop up; when you
close this, (2) a napari window showing the same coins image should show up.
When you close this, the script should finish without errors.

## Running this workshop

This workshop uses .md files to represent jupyter notebooks managed by
[jupytext](https://jupytext.readthedocs.io/en/latest/). Once you have installed
jupytext (as per the instructions above), the experience should be the same as
using a regular Jupyter notebook: launch jupyter notebook or jupyter lab, go to
the "notebooks" folder, and click on each notebook as instructed by the tutors.

