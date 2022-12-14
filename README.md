# WhereAmI

A package containing a single function `whereami` that returns a condensed
stack preview. Useful for debugging to easily trace how some call was made,
even through a jungle of calls made by frameworks and other packages.

To see it in action, you can run
[`example.py`](https://github.com/vsego/whereami/blob/master/example.py) or, if
you didn't install the package but you only downloaded this repository,
[`example.sh`](https://github.com/vsego/whereami/blob/master/example.sh). Both
approaches require that
[`settings-collector`](https://pypi.org/project/settings-collector/) is
installed. The result should look like this:

![Screenshot](https://raw.githubusercontent.com/vsego/whereami/master/images/example.png)

**Fun fact:** The tests here contain some of the most beautifully ugly stuff
that I've ever wrote, with inspecting tests code, reloading modules, and
mocking one of their imports.
