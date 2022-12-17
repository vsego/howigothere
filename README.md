# HowIGotHere

A package containing a single function `howigothere` that returns a condensed
stack preview. Useful for debugging to easily trace how some call was made,
even through a jungle of calls made by frameworks and other packages.

To see it in action, you can run
[`example.py`](https://github.com/vsego/howigothere/blob/master/example.py) or, if
you didn't install the package but you only downloaded this repository,
[`example.sh`](https://github.com/vsego/howigothere/blob/master/example.sh). Both
approaches require that
[`settings-collector`](https://pypi.org/project/settings-collector/) is
installed. The result should look like this:

![Screenshot](https://raw.githubusercontent.com/vsego/howigothere/master/images/example.png)

**Note:** It's "How I Got Here", not "How I go There".

**Fun fact:** The tests here contain some of the most beautifully ugly stuff
that I've ever wrote, with inspecting tests code, reloading modules, and
mocking one of their imports.
