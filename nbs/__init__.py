# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "mohtml==0.1.11",
#     "pandas==2.3.2",
#     "polars==1.33.0",
#     "rich==14.1.0",
# ]
# ///

import marimo

__generated_with = "0.15.2"
app = marimo.App(width="columns")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    ## EXPORT

    import subprocess
    from io import StringIO
    from rich.console import Console
    from mohtml import div


    class Kmd:
        """
        Kmd is a class that allows you to run commands in the terminal and display the output in a rich console.

        The resulting object will contain the stdout and stderr of the command and will be rendered as a html object.
        """

        def __init__(self, command, width=80):
            self.command = command
            self.width = width
            result = subprocess.run(self.command, shell=True, capture_output=True, text=True)
            self.stdout = result.stdout
            self.stderr = result.stderr
        
        def _display_(self):
            """Show a pretty display for marimo notebooks."""
            console = Console(file=StringIO(), record=True, width=self.width)

            # Log the command and output
            console.print(f"\n[bold blue]>[/bold blue] {self.command}")
            console.print(f"\n{self.stdout}")

            if self.stderr:
                console.print(f"\n{self.stderr}")

            return div(console.export_svg(title=""))

        def show(self): 
            """Explicitly generate the rendered terminal"""
            return self._display_()

        def __iter__(self):
            """Iterate through all the lines."""
            out = self.stdout.split("\n")
            if self.stderr:
                out + self.stderr.split("\n")
            return out.__iter__()
        
        def attempt_dataframe(self):
            """Attempt to convert the stdout to a polars dataframe. It might fail depending on the output."""
            import polars as pl

            return pl.DataFrame([line.split() for line in self.stdout.split("\n") if len(line)])
    return (Kmd,)


@app.cell
def _(Kmd):
    Kmd("ls")
    return


@app.cell
def _(Kmd):
    Kmd("cat justfile")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Usecase

    Besides looking very cool, this project also carries a real use-case. The reactive nature of marimo allows you to take the output variables of these terminal commands which also lets you determine when they should run.
    """
    )
    return


@app.cell
def _(Kmd):
    create = Kmd("echo 'a,b\n1,2\n3,4' > demo.csv")
    Kmd("cat demo.csv")
    return (create,)


@app.cell
def _(create):
    import pandas as pd 

    # Including this variable here means that we guarantee that the dataset exists. 
    create

    pd.read_csv("demo.csv")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
