
Back to [Reference Overview](https://github.com/pyrustic/megawidget/blob/master/docs/reference/README.md)

# megawidget.pathentry



<br>


```python
BODY = "body"

BUTTON = "button"

DIALOG = "dialog"

ENTRY = "entry"

```

<br>

```python

class Error:
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

```

<br>

```python

class Pathentry:
    """
        
    """

    def __init__(self, master=None, browse='file', textvariable=None, width=17, title=None, initialdir=None, megaconfig=None):
        """
        - master: widget parent. Example: an instance of tk.Frame
        """

    @property
    def parts(self):
        """
                
        """

    @property
    def path(self):
        """
        
        """

    @path.setter
    def path(self, val):
        """
        
        """

    @property
    def string_var(self):
        """
        
        """

```

