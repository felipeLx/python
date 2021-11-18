usr/local/bin/python -> ../Cellar/python/2.7.13/bin/python
And the python3 executable is:

/usr/local/bin/python3 -> ../Cellar/python3/3.6.1/bin/python3
What you can do is make the /usr/local/bin/python a new link to the python version you want to use using the command ln.

sudo rm /usr/local/bin/python
sudo ln -s /usr/local/Cellar/python3/3.6.1/bin/python3 /usr/local/bin/python
Now the executable is correct:

/usr/local/bin/python -> /usr/local/Cellar/python3/3.6.1/bin/python3
If I execute the version:

$ python --version
Python 3.6.1