# Author: Sameh Mikhail
# Student number: 14003597
# Date: 17-11-2023

import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-s",
    "--steps",
    default=1,
    help="steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
def sin(steps):
    """Takes the sine of a list of values

    Args:
        steps (int): amount of steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, steps)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@cmd_group.command()
@click.option(
    "-s",
    "--steps",
    default=1,
    help="steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
def tan(steps):
    """Takes the tangens of a list of values

    Args:
        steps (int): amount of steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, steps)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()