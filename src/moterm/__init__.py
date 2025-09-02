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
        self.stdout = None
        self.stderr = None

    def _display_(self):
        result = subprocess.run(
            self.command,
            shell=True,
            capture_output=True,
            text=True
        )

        console = Console(file=StringIO(), record=True, width=self.width)

        # Log the command and output
        console.print(f"\n[bold blue]> [/bold blue] {self.command}")
        console.print(f"\n{result.stdout}")

        if result.stderr:
            console.print(f"\n{result.stderr}")

        self.stdout = result.stdout
        self.stderr = result.stderr

        return div(console.export_svg(title=""))

    def attempt_dataframe(self):
        """Attempt to convert the stdout to a polars dataframe. It might fail depending on the output."""
        import polars as pl
        return pl.DataFrame([line.split() for line in self.stdout.split("\n") if len(line)])
