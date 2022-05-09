# Introduction to scikit-image for 3D image analysis

* Support material for the tutorial _Introduction to scikit-image for 3D image analysis_ at the Computational Biology Skills Seminar.

This tutorial will introduce how to analyze three dimensional stacked and volumetric images in Python, mainly using scikit-image. Here we will study how to:
  * pre-process data using filtering, binarization and segmentation techniques.
  * inspect, count and measure attributes of objects and regions of interest in the data.
  * visualize large 3D data.

For more info:
  * [[scikit-image]](https://scikit-image.org/)
  * [[Computational Biology Core Skills Seminars]](https://ccb.berkeley.edu/outreach/workshops-bootcamps/#core-skills-seminars)
  * [[CompBio Skills Seminar]](https://ccbskillssem.github.io/): webpage containing previous talks, slides and code

## Preparing your PC

If you are new to Python, please install the [Anaconda distribution](https://www.anaconda.com/downloads) for Python 3 (available on Linux, OSX, and Windows). If you have more experience, feel free to use your favorite distribution.

Please ensure the requirements below are met:
- `numpy` >= 1.22
- `scipy` >= 1.8
- `matplotlib` >= 3.5
- `scikit-image` >= 0.19
- `jupyter-notebook` >= 6.4
- `itk` >= 5.2
- `itkwidgets` >= 0.32

 For more details, see "Test your setup" below.

### If you're using conda

Please create an environment ready for this tutorial using the
YAML file provided. The command is:

```bash
conda env create --file=environment.yml
```

The environment created in the last step is called `ccb_skimage`,
and you can start using it with the command `conda activate`:

`conda activate ccb_skimage`

## Download the material

To download the material for this tutorial, you can clone or download the
repository at [https://github.com/alexdesiqueira/ccb_skimage3d_tutorial](https://github.com/alexdesiqueira/ccb_skimage3d_tutorial).

## Test your setup

You can use the script `check_setup.py` to check if your environment is ready.
```bash
python check_setup.py
```

On my computer, the command results in:
```
[✓] numpy            1.22.3
[✓] scipy            1.8.0
[✓] matplotlib       3.5.2
[✓] scikit-image     0.19.2
[✓] jupyter-notebook 6.4.11
[✓] itk              5.2.0
[✓] itkwidgets       0.32.0
```

Please note that your version numbers may differ.
