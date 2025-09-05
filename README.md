# moterm

Makes it more fun to add terminal commands to marimo notebooks

<img width="990" height="527" alt="localhost_2722_" src="https://github.com/user-attachments/assets/6e614dde-6bfe-4f83-852a-75d0560a2d21" />

## Install 

```
uv pip install moterm
```

## Usage

The moterm library offers a `Kmd` class that lets you run a terminal command as you would normally. The output is stored and can be displayed as a nice view (thanks to rich) but the real benefit is that this allows marimo users to reactively add terminal commands to their notebook. 

Suppose that you have a specific CLI that can download the right data for you. Maybe something like this: 

```python
from moterm import Kmd

download = Kmd("wget https://some.url/download/demo.csv")
```

Then you can use the variable `download` in another cell to ensure that this dataset is downloaded beforehand. 

```
import polars as pl

download
pl.read_csv("demo.csv")
```

By adding the `download` variable here, you guarantee that the `Kmd` ran before the cell with the polars code runs. 

> [!IMPORTANT]  
> In this particular case it'd be better to use `pl.read_csv("https://some.url/download/demo.csv")` directly, but the power here is that `Kmd` could work with general CLI tools. That would include those outside of the Python ecosystem. 
> 
> Another fair warning is that using `Kmd` might make the notebook less reproducible because you might assume tools that don't exist on the machine. 


## Demo 

For a full demo, check out this YouTube video. 

<a href="https://www.youtube.com/watch?v=2LAX-u5WYpU"><img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/913e9949-9d37-4c57-a902-f09e37347971" /></a>
