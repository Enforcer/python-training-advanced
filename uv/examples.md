# Projects

## Initializing a new project

```bash
uv init [--python <python version>] <nazwa projektu>


uv init hello-world
uv init --python 3.14 hello-world


cd hello-world
uv sync  # finish by creating virtualenv
```

## Structure

```bash
.
├── .venv/
├── .python-version
├── README.md
├── main.py
├── pyproject.toml
└── uv.lock
```

## Managing dependencies

### Installing new package

```
uv add more-itertools
```

### Installing specific versions

### Removing packages

```
uv remove more-itertools
```

### Install packages in the current environment

```
uv sync
```

### Adding packages to the group

```
uv add --group <name of the group> <name of package>

uv add --group dev import-linter
```

### Working with uv

### Running interpreter

```bash
uv run python
```

### Running some command installed with the project or dependencies

```bash
uv run lint-imports
```

## Tools

### Managing installed tools

```
uv tool install <name>
uv tool install Pygments

uv tool uninstall <name>
uv tool uninstall Pygments
```

### Running tools without installing

```
uv tool run <name>
uvx <name>

uv tool run twine
uvx twine
```

# Scripts

## Metadata example

```
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "rich",
# ]
# ///
def main():
    print("Hello from hello-world!")


if __name__ == "__main__":
    main()

```

## Managing script dependencies

### Add depdendencies and initialize metadata if they are not there

```
uv add --script <filename.py> [--python <python version>] <package>

uv add --script hello.py --python 3.13 rich
```

### Create lockfile for the script

```
uv lock --script hello.py
```

### Running script

```
uv run hello.py
```
