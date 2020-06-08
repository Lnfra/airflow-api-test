## Install pyenv to manage python versions
```
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install 3.7.7
pyenv local 3.7.7
```

## Install pipenv to create virtual envionment per project
```
brew install pipenv
echo 'eval "$(pipenv --completion)"' >> ~/.bash_profile
source ~/.bash_profile
```

## Create virtual env
```
cd airflow-api-test
pipenv install
pipenv shell
```

## To run the test
```
python -m unittest discover -s tests
```