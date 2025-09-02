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
