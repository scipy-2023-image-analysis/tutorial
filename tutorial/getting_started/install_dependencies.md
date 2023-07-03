(install-dependencies)=
# Install Python and dependencies

```{tip}
If you have any issues with installation, head over to our Zulip servers where we can help you get
unstuck!
- https://skimage.zulipchat.com
- https://napari.zulipchat.com/
```

## Installing Python using conda

In this tutorial, we will install Python via miniforge, a distribution of
Python based in the [conda package manager](https://docs.conda.io/en/latest/).
If you already have anaconda, miniconda, or miniforge installed, those will work
as well and you can skip to the next section.

1. In your web browser, navigate to the
   [miniforge page](https://github.com/conda-forge/miniforge). 
2. Scroll down to the "Miniforge3" header of the "Downloads" section. Click the
   link to download the appropriate version for your operating system. *Note
   that even if you have a new Apple computer with an M1 processor, you should
   download the OS X x86_64 version.*
    - Windows: `Miniforge3-Windows-x86_64`
    - Mac with Intel processor: `Miniforge3-MacOSX-x86_64`
    - Mac with M1 ("Apple silicon"): `Miniforge3-MacOSX-x86_64`
    - Linux with an Intel processor: `Miniforge3-Linux-x86_64`
3. Once you have downloaded miniforge installer, run it to install Python.
    - **Windows**
        1. Find the file you downloaded (`Miniforge3-Windows-x86_64.exe`) and
           double click to execute it. Follow the instructions to complete the
           installation.
        2. Once the installation has completed, you can verify it was correctly
           installed by searching for the "miniforge prompt" in your Start menu.
    - **Mac OS**
        1. Open your Terminal (you can search for it in spotlight - `cmd` +
           `space`)
        2. Navigate to the folder you downloaded the installer to. For example,
           if the file was downloaded to your Downloads folder, you would enter:

            ```bash
            cd ~/Downloads
            ```

        3. Execute the installer with the command below. You can use your arrow
           keys to scroll up and down to read it/agree to it.

            ```bash
            bash Miniforge3-MacOSX-x86_64.sh -b
            ```

        4. To verify that your installation worked, close your Terminal window
           and open a new one. You should see `(base)` to the left of your
           prompt.
        5. Finally, initialize miniforge with the command below. This makes sure
           that your terminal is set up correctly for your python installation.

            ```bash
            conda init
            ```

    - **Linux**
        1. Open your terminal application
        2. Navigate to the folder you downloaded the installer to. For example,
           if the file was downloaded to your Downloads folder, you would enter:

            ```bash
            cd ~/Downloads
            ```

        3. Execute the installer with the command below. You can use your arrow
           keys to scroll up and down to read it/agree to it.

            ```bash
             bash Miniforge3-Linux-x86_64.sh -b
            ```

        4. To verify that your installation worked, close your Terminal window
           and open a new one. You should see `(base)` to the left of your
           prompt.
        5. Finally, initialize miniforge with the command below. This makes sure
           that your terminal is set up correctly for your python installation.

            ```bash
            conda init
            ```

## Setting up your environment
1. Open your terminal.
   - **Windows**: Open the "miniforge prompt" from your start menu
   - **Mac OS**: Open Terminal (you can search for it in spotlight - `cmd` +
     `space`)
   - **Linux**: Open your terminal application
2. We use an environment to encapsulate the Python tools used for this workshop.
   This ensures that the requirements for this workshop do not interfere with
   your other Python projects. To create the environment (named
   `image-analysis-23`) and install Python 3.10 in it, enter the following command:

    ```bash
    conda env create -f environment.yml
    ```

3. Once the environment setup has finished, activate the environment:

    ```bash
    conda activate image-analysis-23
    ```

    If you successfully activated the environment, you should now see
   `(image-analysis-23)` to the left of your command prompt.

4. Test that your notebook installation is working. We will be using notebooks
   for interactive analysis. Enter the command below and it should launch the
   `jupyter notebook` application in a web browser. Once you've confirmed it
   launches, close the web browser and press `ctrl+c` in the terminal window to
   stop the notebook server.

    ```bash
    jupyter notebook
    ```

````{admonition} Errors launching?
Sometimes, `napari` installation can fail on an M1 Mac due to mismatching
dependencies on `pip`.

If you get an error above, or can't launch `napari` after
installation, you should try to delete your `image-analysis-23` environment, and
follow the installation instructions below.

1. Delete your `image-analysis-23` environment

   ```bash
   conda activate base
   conda env remove -n image-analysis-23
   ```

2. Create your environment and install `napari` from `conda-forge`

   ```bash
   conda create -y -n image-analysis-23 python=3.10 napari
   ```

3. Then, after creation:

   ```bash
   conda activate image-analysis-23
   conda install -f environment.yml
   ```
````

## Checking that your installation works

If you have installed everything correctly, you should be able to run:

```
python test-env.py
```

Some of the libraries take a while to run the first time, so be patient. You
should see (1) a matplotlib window with three image panels pop up; when you
close this, (2) a napari window showing the same coins image should show up.
When you close this, the script should finish without errors.
