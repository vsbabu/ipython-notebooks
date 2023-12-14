# Sample IPython Notebooks

Just started on data analysis using ipython. Preserving this for learning. Especially, when I need to set it up in another machine. Some of the tools setup in this include the following.

* [ipython](http://ipython.org/), [jupyter](https://jupyter.org/)
* [pandas](http://pandas.pydata.org/)
* [scipy](https://www.scipy.org/), [numpy](http://www.numpy.org/), [matplotlib](http://matplotlib.org/)

## Samples

Currently, only one is available.

* [Funnel Analysis](https://github.com/vsbabu/ipython-notebooks/tree/master/funnel)

## Setup Instructions 

*Edit* - 2023.12.14 - updated for Python 3 and latest version of Pandas, Prophet etc. Tested on Win11 with Anaconda 23.11, Python 3.10.11, Jupyter lab 4.0.8. 


### Setup environment

*Edit* - 2023.12.14 - I just used Anaconda as mentioned above with a conda env. Leaving previous instructions for Py2+Ubuntu 16.04 below for reference.

We will use `virtualenv` to keep things clean.

```sh
# first, navigate to the directory where this repository is cloned

# install python virualenv
#  system-site-packages, while purists can argue is against the spirit of virtualenv,
#  gets tkinter added to deps faster :) that is needed for matplotlib
virtualenv venv --system-site-packages

# use the virtualenv
#  the step below is needed whenever you run ipython for these samples
source venv/bin/activate

# now install dependencies. This will take a while during first time
# this will install latest versions (if you don't have any of these installed)
pip install -r requirements.txt

# run this below once to see you got matplotlib installed properly. You shouldn't see
# any exceptions.
python -c "import matplotlib; import matplotlib.pyplot as plt;"
# if the one above didn't work, please do installation with my requirements_frozen.txt

# start ipython notebook
ipython notebook

```
You should see http://localhost:8888/ opened up. Navigate to that and play around with _*.ipynb_ files. These are the notebooks. Inside the notebooks, you can see information about those.


#### Freezing environment

If things are working, you might want to freeze the dependency versions for future.

```sh
pip freeze --local > requirements_frozen.txt
# Next time onwards, you can use this to install same versions that worked for you. Especially
# when you are setting this up in another machine.

# if you want to upgrade (seriously, you should get a frozen list first so that you can revert
# if something breaks!
# this will give you list of outdated packages
pip list --outdated

# now, if you want to upgrade a specific package-name, run
pip install --upgrade package-name

```



