"""
WhereAmI example.
"""

import sys

from settings_collector import sc_settings
from whereami import whereami


namespace_x_colors: dict[str, str]
try:
    from colorama import Fore
except ImportError:
    sys.stderr.write(
        "This example would be more colourful if you ran it in an environment"
        " that has colorama installed. :-)\n",
    )
    namespace_x_colors = dict()
else:
    namespace_x_colors = {
        "whereami__x__color_reset": Fore.RESET,
        "whereami__x__color_sep": Fore.BLUE,
        "whereami__x__color_func": Fore.RED,
        "whereami__x__color_path": Fore.GREEN,
        "whereami__x__color_lineno": Fore.YELLOW,
    }


def f():
    """
    Call inner function to print various `whereami()` outputs.
    """
    def g():
        """
        Print various `whereami()` outputs.
        """
        print("Default:            ", whereami())
        print("Namespace 'x':      ", whereami(namespace="x"))
        print("Local arguments:    ", whereami(sep=" ==> ", keep_dirs=None))
        print("Namespace 'mono':   ", whereami(namespace="mono"))
        print("Local monochrome:   ", whereami(no_color=True))
        print("Namespace 'mono__y':", whereami(namespace="mono__y"))
    g()


if __name__ == "__main__":
    sc_settings.update({
        "whereami__x__trim_paths": 2,
        "whereami__x__sep": "~~>",
        "whereami__x__call_format": "{function} [{lineno}: {path}]",
        **namespace_x_colors,
        "whereami__mono__no_color": True,
        "whereami__mono__y__call_format": "{function}",
    })
    f()
