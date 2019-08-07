# pipenv-playground

learn [pipenv](https://github.com/pypa/pipenv)

> Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. Windows is a first-class citizen, in our world.

> It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever-important Pipfile.lock, which is used to produce deterministic builds.

* based on <https://docs.python-guide.org/dev/virtualenvs/>

### Usage

```sh
# install
pip3 install pipenv

# create directory
cd ~/tmp
mkdir pipenv-playground
cd pipenv-playground

# install dependency
pipenv install requests

# write some code that uses the dependency
touch main.py

# run it using the created virtualenv
pipenv run python main.py

# can also specify `python3` explicitly
pipenv run python3 main.py

# try with jupyter notebook
cd ..
mkdir jupyter-notebook-playground
cd jupyter-notebook-playground
pipenv install jupyter
pipenv run jupyter notebook

# try with jupyterlab
pipenv install jupyterlab
pipenv run jupyter lab
touch README.md .gitignore

```