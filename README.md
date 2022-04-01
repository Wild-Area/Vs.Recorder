# Vs. Recorder

**Important note: We restarted this project in another repo and another programming language.**
**Please see [`VsRecorder.jl`](https://github.com/Wild-Area/VsRecorder.jl).**

The Vs. Recorder missing in Pokemon Sword & Shield.

## Installation & Usage

## Development

### Install pipenv

```
pip3 install pipenv --user
```

### Install dependencies

```
pipenv install --dev
```

### Enter pipenv shell

```
pipenv shell
```

### Setup VS Code

Frist, get the python path from pipenv:

```
pipenv --py
```

Then, set the path to `.vscode/settings.json`:
```
{
    "python.pythonPath": "/home/myuser/.local/share/virtualenvs/projectname/bin/python"
}
```

### Run tests

```
pytest
```

## License

-----
WIP. See the [issue list](https://github.com/sunoru/Vs.Recorder/issues) for TODOs and milestones.
