
Back to [Reference Overview](https://github.com/pyrustic/megawidget/blob/master/docs/reference/README.md)

# megawidget.toast



<br>


```python
BODY = "body"

LABEL_HEADER = "label_header"

LABEL_MESSAGE = "label_message"

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

class Toast:
    """
    A toast is a dialog box with or without decoration
    that is displayed for a given duration.
    
    Any "click" action on the Toast's body will close it.
    
    Example:
        import tkinter as tk
        from pyrustic.widget.toast import Toast
    
        root = tk.Tk()
        toast = Toast(root, header="My Header", message="My Message")
        toast.build()
        root.mainloop()
    """

    def __init__(self, master=None, title=None, header=None, message=None, duration=1234, decoration=False, geometry=None, megaconfig=None):
        """
        PARAMETERS:
        
        - master: widget parent. Example: an instance of tk.Frame
        
        - title: title of dialog box
        
        - header: the text to show as header
        
        - message: the text to show as message
        
        - duration: int, in milliseconds.
            You can set None to duration to cancel the self-destroying timer
        
        - decoration: True or False to allow Window decoration
        
        - geometry: str, as the dialog box is a toplevel (BODY),
         you can edit its geometry. Example: "500x300"
        
        - options: dictionary of widgets options
            The widgets keys are: BODY, LABEL_HEADER, LABEL_MESSAGE.
        
            Example: Assume that you want to set the LABEL_MESSAGE's background to black
            and the BODY's background to red:
                options = { BODY: {"background": "red"},
                            LABEL_MESSAGE: {"background": "black"} }
        """

    @property
    def decoration(self):
        """
        
        """

    @property
    def duration(self):
        """
        
        """

    @property
    def header(self):
        """
        
        """

    @property
    def message(self):
        """
        
        """

    @property
    def parts(self):
        """
        Get the parts (widgets instances) used to build this Toast.
        
        This property returns a dict. The keys are:
            BODY, LABEL_HEADER, LABEL_MESSAGE,
        """

```

