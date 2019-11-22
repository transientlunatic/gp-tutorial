"""
This file contains some code which is useful for plotting,
but if you're following the tutorials you shouldn't need to worry about it.
"""

from cycler import cycler

blueprint = {
    "xtick.labelsize":10,
    "xtick.major.size": 5,
    "xtick.minor.visible": True,
    "xtick.color": "k",
    "ytick.labelsize":10,
    "ytick.major.size": 5,
    "ytick.minor.visible": True,
    # Lines
    "lines.linewidth": 2,
    "axes.prop_cycle": cycler("color", ['#FFFFFF', '#CCCCCC', '#AAAAAA']),
    # Fonts
    "font.monospace": ["Source code pro"],
    "font.sans-serif": ["Source sans pro"],
    "font.family": "monospace",
    # Grid
    "axes.grid": True,
    "axes.grid.which": "both",
    "grid.color": "#CED8F7",
    "grid.alpha": 0.3,
    "grid.linestyle": "-",
    "grid.linewidth": 0.25,
    # Plot display
    "figure.dpi": 300,
    # Plot facecolors
    "axes.facecolor": "#11496f",
    "figure.facecolor": "#FFFFFFFF"
}

pastle = {
    "xtick.labelsize":10,
    "xtick.major.size": 5,
    "xtick.minor.visible": True,
    "xtick.color": "k",
    "ytick.labelsize":10,
    "ytick.major.size": 5,
    "ytick.minor.visible": True,
    # Lines
    "lines.linewidth": 2,
    "axes.prop_cycle": cycler("color", ['#8dd3c7', '#ffffb3', '#bebada',
                                        '#fb8072', '#80b1d3', '#fdb462',
                                        '#b3de69', '#fccde5', '#d9d9d9',
                                        '#bc80bd', '#ccebc5', '#ffed6f']),
    # Fonts
    "font.monospace": ["Source code pro"],
    "font.sans-serif": ["Source sans pro"],
    "font.family": "monospace",
    # Grid
    "grid.color": "#4298bd",
    "grid.alpha": 0.5,
    # Display
    "figure.dpi": 300,
    # Face colors
    "axes.facecolor": "#ecf5f8",
    "figure.facecolor": "#FFFFFFFF"
}
