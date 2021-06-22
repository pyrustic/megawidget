
Back to [Reference Overview](https://github.com/pyrustic/megawidget/blob/master/docs/reference/README.md)

# megawidget.choice



<br>


```python
BODY = "body"

BUTTON_CANCEL = "button_cancel"

BUTTON_CONTINUE = "button_continue"

CHECK = "check"

CHECKBUTTONS = "checkbuttons"

FRAME_FOOTER = "frame_footer"

FRAME_PANE = "frame_pane"

LABEL_HEADER = "label_header"

LABEL_MESSAGE = "label_message"

RADIO = "radio"

RADIOBUTTONS = "radiobuttons"

SCROLLBOX = "scrollbox"

```

<br>

```python

class Choice:
    """
    Choice is a dialog box to make the user select some items among others.
    The Choice could be implemented with either radiobuttons or checkbuttons.
    
    Example:
    
        import tkinter as tk
        from pyrustic.widget.choice import Choice
    
        def my_handler(result):
            print(result)
    
        root = tk.Tk()
        my_items = ("first", "second", "third")
        choice = Choice(root, title="Choice", header="Make a choice",
                        items=my_items, handler=my_handler)
        choice.build()
        root.mainloop()
    """

    def __init__(self, master=None, title=None, header=None, message=None, items=None, selected=None, flavor='radio', handler=None, geometry=None, cnfs=None):
        """
        PARAMETERS:
        
        - master: widget parent. Example: an instance of tk.Frame
        
        - title: title of dialog box
        
        - header: the text to show as header
        
        - message: the text to show as message
        
        - use_scrollbox: bool, set it to True to make the Dialog scrollable
        
        - items: a sequence of strings. Example: ("banana", "apple").
        
        - selected: a sequence of indexes to indicate default selection.
        Set it to None if u don't need it.
        
        - flavor: it could be either RADIO or CHECK
        for respectively radiobutton and checkbutton
        
        - handler: a callback to be executed immediately
        after closing the dialog box.
        The callback should allow one parameter, the result:
        
            - If the flavor is RADIO,
             then, result is a tuple like: (the selected index, item string).
        
            - If the flavor is CHECK,
             then, result is a sequence of tuples.
             Each tuple is like: (integer, item string),
             with integer being 1 if the button has been clicked, else 0.
        
        - geometry: str, as the dialog box is a toplevel (BODY),
         you can edit its geometry. Example: "500x300"
        
        - options: dictionary of widgets options
            The widgets keys are: BODY, LABEL_HEADER, SCROLLBOX, LABEL_MESSAGE,
            FRAME_PANE, FRAME_FOOTER, BUTTON_CONTINUE, BUTTON_CANCEL,
            RADIOBUTTONS, CHECKBUTTONS.
        
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
            BODY, LABEL_HEADER, SCROLLBOX, LABEL_MESSAGE,
            FRAME_PANE, FRAME_FOOTER, BUTTON_CONTINUE, BUTTON_CANCEL,
            RADIOBUTTONS, CHECKBUTTONS.
        
        Warning: radiobuttons and checkbuttons are sequences of widgets positioned
        in the sequence according to the index.
        
        Another Warning: check the presence of key before usage.
        """

    @property
    def flavor(self):
        """
        
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
    def items(self):
        """
        
        """

    @property
    def message(self):
        """
        
        """

    @property
    def selected(self):
        """
        - If the flavor is RADIO,
             then, result is a tuple like: (the selected index, item string).
             Example: 3 items, the second has been selected:
                result = (1, "Item at index 1")
        
        - If the flavor is CHECK,
         then, result is a sequence of tuples, each positioned in
         the sequence according to its index number.
         Each tuple is like: (integer, item string),
         with integer being 1 if the button has been clicked, else 0.
         Example: 3 items, only the last 2 are checked:
            result = ( (0, "item 1"), (1, "item 2"), (1, "item 3") )
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

