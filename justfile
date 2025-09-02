install: 
    uv venv --allow-existing
    source .venv/bin/activate
    uv pip install -e . pytest marimo mobuild

test: 
    uvx mobuild export nbs src
    uv run pytest

publish: test
    uv build
    uv publish
