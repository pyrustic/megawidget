
Back to [Reference Overview](https://github.com/pyrustic/megawidget/blob/master/docs/reference/README.md)

# megawidget.confirm



<br>


```python
BODY = "body"

BUTTON_CANCEL = "button_cancel"

BUTTON_CONFIRM = "button_confirm"

FRAME_FOOTER = "frame_footer"

LABEL_HEADER = "label_header"

LABEL_MESSAGE = "label_message"

```

<br>

```python

class Confirm:
    """
    Confirm is a dialog box to ask the user to confirm an action.
    
    Example:
    
        import tkinter as tk
        from pyrustic.widget.confirm import Confirm
    
        def my_handler(result):
            print(result)
    
        root = tk.Tk()
        confirm = Confirm(root, title="Confirm", header="Confirmation",
                        message="Do you really want to continue ?",
                        handler=my_handler)
        confirm.build()
        root.mainloop()
    """

    def __init__(self, master=None, title=None, header=None, message=None, handler=None, geometry=None, cnfs=None):
        """
        PARAMETERS:
        
        - master: widget parent. Example: an instance of tk.Frame
        
        - title: title of dialog box
        
        - header: the text to show as header
        
        - message: the text to show as message
        
        - handler: a callback to be executed immediately after closing the dialog box.
            This callback should accept a boolean positional argument.
            True means Ok, confirmed.
        
        - geometry: str, as the dialog box is a toplevel (BODY),
         you can edit its geometry. Example: "500x300"
        
        - options: dictionary of widgets options
            The widgets keys are: BODY, LABEL_HEADER,
             LABEL_MESSAGE, FRAME_FOOTER, BUTTON_CANCEL, BUTTON_CONFIRM.
        
            Example: Assume that you want to set the LABEL_MESSAGE's background to black
            and the BODY's background to red:
                options = { BODY: {"background": "red"},
                            LABEL_MESSAGE: {"background": "black"} }
        """

    @property
    def components(self):
        """
        Get the components (widgets instances) used to build this dialog.
        
        This property returns a dict. The keys are:
            BODY, LABEL_HEADER,
            LABEL_MESSAGE, FRAME_FOOTER, BUTTON_CANCEL, BUTTON_CONFIRM
        
        Warning: check the presence of key before usage
        """

    @property
    def handler(self):
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
    def ok(self):
        """
        Returns True if user confirmed, else get False
        """

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

