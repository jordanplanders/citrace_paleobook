# C-iTrace (and friends) Paleobook

This PaleoBook looks at how to slice, dice, navigate, visualize and perhaps consider multi-proxy, spatially resolved model output by exploring output from coarse iTRACE model runs. 

## Motivation

Paleo-model output offers a spatially resolved look at how proxy distributions may have evolved over time--a welcome gift in a field perpetually saddled with navigating sparse data problems. Working with model output comes with a few unique challenges, in addition to some intriguing opportunities. 

## Authors

[Jordan Landers](@jordanplanders)

### Contributors

<a href="https://github.com/jordanplanders/citrace_paleobook/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jordanplanders/citrace_paleobook" />
</a>

## Structure

This Paleobook is made up of two sections: Lifehacks, and Science Bits

### Lifehacks

This section covers nuts and bolts about how to access cloud available data, process it, and make some stock visualizations

### Science Bits

This section applies the technical skills from the Lifehacks section to do standard analysis.

## Running the Notebooks

You can either run the notebook using [Binder](https://mybinder.org/), or on your local machine.

### Running on Binder

The simplest way to interact with a Jupyter Notebook is through
[Binder](https://mybinder.org/), which enables the execution of a
[Jupyter Book](https://jupyterbook.org) in the cloud. The details of how this works are not
important for now. All you need to know is how to launch a PaleoBooks chapter via Binder. Simply navigate your mouse to
the top right corner of the book chapter you are viewing and click
on the rocket ship icon, (see figure below), and be sure to select
“launch Binder”. After a moment you should be presented with a
notebook that you can interact with. I.e. you’ll be able to execute
and even change the example programs. You’ll see that the code cells
have no output at first, until you execute them by pressing
{kbd}`Shift`\+{kbd}`Enter`. Complete details on how to interact with
a live Jupyter notebook are described in [Getting Started with
Jupyter](https://foundations.projectpythia.org/foundations/getting-started-jupyter.html).

### Running on Your Own Machine

If you are interested in running this material locally on your computer, you will need to follow this workflow:

1. Clone the `https://github.com/jordanplanders/LMR_CMIP_paleobook` repository:

   ```bash
    git clone https://github.com/jordanplanders/LMR_CMIP_paleobook.git
   ```

1. Create and activate your conda environment from the `environment.yml` file
   ```bash
   conda env create -f environment.yml
   conda activate conda-env-paleobook-dev-py
   ```
1. Move into the `notebooks` directory and start up Jupyterlab
   ```bash
   cd notebooks/
   jupyter lab
   ```
