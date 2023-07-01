# Build your own workshop

```{note}
This section is about building your own workshop - it should probably be removed
from your workshop material once you have adapted it to your needs.
```

## Build locally

To build this workshop locally and preview the generated materials in html format (as a webpage), follow the steps below.

### 1. Install all required packages

First, [fork this repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo) and clone it to your local system by

```
git clone git@github.com:<your-username>/napari-workshop-template.git
```

In a console/terminal, after installing python on your system using the
distribution of your choice, and ideally
[using a virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/), navigate to the napari-workshop-template folder,
run

```
python -m pip install -r requirements.txt
```

### 2. Build your book

To render the html version of your book, including autogenerating figures or
running Jupyter notebooks, run

```
jupyter book build napari-workshops
```

where `napari-workshops` is the name of the folder where your book is stored.
The rendered version of the workshop materials will be under
`napari-workshops/_build/html`. For more information, see the
[JupyterBook documentation](https://jupyterbook.org/).

**Note:** The html files built by the `jupyter book` commands do not need to be
stored on GitHub, so we added the following path to our `.gitignore` file:

```
napari-workshops/_build/
```

## Publish and share your workshop
### Publish your workshop materials as a static web page

If you want to set up this material to be published as a website from your fork, using [GitHub pages](https://pages.github.com/), follow the steps below.

1. Edit the `.github/workflows/pages.yml` file in your workshop folder to
   include any installation or setup requirements. By default, the following
   commands are run as a setup and build step:

    ```
    - name: Build workshop
      run: |
        python -m pip install -r requirements.txt
        jupyter book build napari-workshops
    ```

2. Edit the `.github/workflows/pages.yml` file in your workshop folder to
   set up the desired folder there the (html) built artifacts are stored. By
   default, the artifacts are in the following path:

    ```
    - name: Upload artifact
      uses: actions/upload-pages-artifact@v1
      with:
        path: 'napari-workshops/_build/html'
    ```

As currently configured, whenever a new commit is added to the `main` branch of the repository, a new deployment is made (the Jupyter book is built, and the
generated pages are uploaded to [GitHub pages](https://docs.github.com/en/pages/quickstart). For this to work, you need to have GitHub pages enabled on your GitHub account. To do this, follow the [deployment guide](deployment_guide).

After GitHub pages is set up for your repository, you will find the workshop materials at

```
https://<your-username>.github.io/<workshop-name>
```

For this template, the built site is at

https://napari.github.io/napari-workshop-template

## Index your workshop using Zenodo (for citation purposes)

If you want people to be able to cite your workshop materials, you can create
a DOI for it using [Zenodo](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).

Select Creative Commons Attribution 4.0 International (CC-BY 4.0) license if you want attribution.

## Enable a citation file for your repository

Check [the GitHub documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) for more details on how to use the `citation.cff` file to enable others to cite your repository.
