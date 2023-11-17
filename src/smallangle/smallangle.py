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
    "-v",
    "--value",
    default=1,
    help="Argument for chosen function.",
    show_default=True,  # show default in help
)
def sin(value):
    """Function to give a sine of the x value

    Args:
        number (int): value to give the end of the 

    Returns:
        list: containing the integers
    """
    x = np.linspace(0, 2 * pi, value)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@cmd_group.command()
@click.option(
    "-v",
    "--value",
    default=1,
    help="Argument for chosen function.",
    show_default=True,  # show default in help
)
def tan(value):
    """List integers up to a given number.

    Args:
        number (int): list integers up to this number

    Returns:
        list: containing the integers
    """
    x = np.linspace(0, 2 * pi, value)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()