
Back to [Reference Overview](https://github.com/pyrustic/megawidget/blob/master/docs/reference/README.md)

# megawidget.scrollbox



<br>


```python
BODY = "body"

BOTH = "both"

BOX = "box"

CANVAS = "canvas"

HORIZONTAL = "horizontal"

HSB = "hsb"

VERTICAL = "vertical"

VSB = "vsb"

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

class Scrollbox:
    """
    Scrollbox is a scrollable surface. You just need to use its property "box" as
    your layout's parent.
    
    Example:
    
        import tkinter as tk
        from pyrustic.widget.scrollbox import Scrollbox
    
        root = tk.Tk()
        scrollbox = Scrollbox(root)
        scrollbox.build_pack()
        # Pack 50 Label on the box
        for i in range(50):
            label = tk.Label(scrollbox.box, text="Label {}".format(i))
            label.pack(anchor=tk.W)
        root.mainloop()
    """

    def __init__(self, master=None, orient='vertical', box_sticky='nswe', resizable_box=True, cnfs=None):
        """
        - master: widget parent. Example: an instance of tk.Frame
        
        - orient: could be one of: VERTICAL, HORIZONTAL, BOTH
        
        - options: dictionary of widgets options
            The widgets keys are: BODY, CANVAS, BOX, HSB, VSB
            Example: Assume that you want to set the CANVAS background to red
                options = {CANVAS: {"background": "red"}}
        """

    @property
    def box(self):
        """
        
        """

    @property
    def components(self):
        """
        Get the components (widgets instances) used to build this scrollbox.
        
        This property returns a dict. The keys are:
            BODY, CANVAS, BOX, HSB, VSB
        
        Warning: check the presence of key before usage. Example,
        the widget linked to the HSB key may be missing because
        only VSB is used
        """

    @property
    def orient(self):
        """
        
        """

    def box_config(self, **options):
        """
        As the BOX is an item compared to CANVAS, some
        the options concerning the BOX can be edited only via
        CANVAS "itemconfig" method.
        Use this method to edit these options.
        itemconfig options are: anchor, state, height, width.
        
        Warning: these options are not the same as the arguments
         of BOX's own constructor !
        """

    def clear(self):
        """
        Clears the Scrollbox.
        This method doesn't destruct this object but BOX's children
        """

    def xview_moveto(self, fraction):
        """
        Calls canvas's method 'xview_moveto'
        Set:
            - 0: to scroll to left
            - 1: to scroll to right
        """

    def yview_moveto(self, fraction):
        """
        Calls canvas's method 'yview_moveto'
        Set:
            - 0: to scroll to top
            - 1: to scroll to bottom
        """

```

