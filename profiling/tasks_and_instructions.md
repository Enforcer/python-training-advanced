# Tasks

Take a look at comments at the top of `slow_code.py` and `example_snippet.py`, start from `slow_code.py`.

Using profilers, find where's the bottleneck and *fix it.

# Prerequisites

Make sure you're in the profiling directory.

```bash
cd profiling
```

# Profiling with cProfile + visualizing using snakeviz

## Run script, profile it and save results to out.prof file

```bash
uv run python -m cProfile -o out.prof <script.py>
```

## Visualize it in a browser using snakeviz

```bash
uv run snakeviz out.prof
```

# Profiling and visualizing with pyinstrument

```bash
uv run pyinstrument -r html <script.py>
```

e.g. `uv run pyinstrument -r html slow_code.py`
