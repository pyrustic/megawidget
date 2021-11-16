Back to [Modules overview](https://github.com/pyrustic/megawidget/blob/master/docs/modules/README.md)
  
# Module documentation
>## megawidget.scrollbox.\_\_init\_\_
No description
<br>
[constants (8)](https://github.com/pyrustic/megawidget/blob/master/docs/modules/content/megawidget.scrollbox.__init__/constants.md) &nbsp;.&nbsp; [classes (3)](https://github.com/pyrustic/megawidget/blob/master/docs/modules/content/megawidget.scrollbox.__init__/classes.md)


## Classes
```python
class Error(Exception):
    """
    Common base class for all non-exit exceptions.
    """

    # inherited from Exception
    def __init__(self, /, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """


    args = <attribute 'args' of 'BaseException' objects>
    
```

```python
class ScrollBox(tkinter.Frame):
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

    def __init__(self, master=None, orient='vertical', megaconfig=None):
        """
        - master: widget parent. Example: an instance of tk.Frame
        
        - orient: could be one of: VERTICAL, HORIZONTAL, BOTH
        
        - options: dictionary of widgets options
            The widgets keys are: BODY, CANVAS, BOX, HSB, VSB
            Example: Assume that you want to set the CANVAS background to red
                options = {CANVAS: {"background": "red"}}
        """


    _last_child_ids = None
    
    _noarg_ = ['_noarg_']
    
    _subst_format = ('%#', '%b', '%f', '%h', '%k', '%s', '%t', '%w', '%x', '%y', '%A', '%E', '%K', '%N', '%W', '%T', '%X', '%Y', '%D')
    
    _subst_format_str = "%# %b %f %h %k %s %t %w %x %y %A %E %K %N %W %T %X %Y %D"
    
    _tclCommands = None
    
    # inherited from tkinter.Misc
    @property
    def _windowingsystem(self):
        """
        Internal function.
        """

    @property
    def box(self):
        """
        
        """

    @property
    def orient(self):
        """
        
        """

    @property
    def parts(self):
        """
        Get the parts (widgets instances) used to build this scrollbox.
        
        This property returns a dict. The keys are:
            BODY, CANVAS, BOX, HSB, VSB
        
        Warning: check the presence of key before usage. Example,
        the widget linked to the HSB key may be missing because
        only VSB is used
        """

    # inherited from tkinter.Misc
    def after(self, ms, func=None, *args):
        """
        Call function once after given time.
        
        MS specifies the time in milliseconds. FUNC gives the
        function which shall be called. Additional parameters
        are given as parameters to the function call.  Return
        identifier to cancel scheduling with after_cancel.
        """

    # inherited from tkinter.Misc
    def after_cancel(self, id):
        """
        Cancel scheduling of function identified with ID.
        
        Identifier returned by after or after_idle must be
        given as first parameter.
        """

    # inherited from tkinter.Misc
    def after_idle(self, func, *args):
        """
        Call FUNC once if the Tcl main loop has no event to
        process.
        
        Return an identifier to cancel the scheduling with
        after_cancel.
        """

    # inherited from tkinter.Misc
    def anchor(self, anchor=None):
        """
        The anchor value controls how to place the grid within the
        master when no row/column has any weight.
        
        The default anchor is nw.
        """

    # inherited from tkinter.Misc
    def bbox(self, column=None, row=None, col2=None, row2=None):
        """
        Return a tuple of integer coordinates for the bounding
        box of this widget controlled by the geometry manager grid.
        
        If COLUMN, ROW is given the bounding box applies from
        the cell with row and column 0 to the specified
        cell. If COL2 and ROW2 are given the bounding box
        starts at that cell.
        
        The returned integers specify the offset of the upper left
        corner in the master widget and the width and height.
        """

    # inherited from tkinter.Misc
    def bell(self, displayof=0):
        """
        Ring a display's bell.
        """

    # inherited from tkinter.Misc
    def bind(self, sequence=None, func=None, add=None):
        """
        Bind to this widget at event SEQUENCE a call to function FUNC.
        
        SEQUENCE is a string of concatenated event
        patterns. An event pattern is of the form
        <MODIFIER-MODIFIER-TYPE-DETAIL> where MODIFIER is one
        of Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4,
        Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,
        B3, Alt, Button4, B4, Double, Button5, B5 Triple,
        Mod1, M1. TYPE is one of Activate, Enter, Map,
        ButtonPress, Button, Expose, Motion, ButtonRelease
        FocusIn, MouseWheel, Circulate, FocusOut, Property,
        Colormap, Gravity Reparent, Configure, KeyPress, Key,
        Unmap, Deactivate, KeyRelease Visibility, Destroy,
        Leave and DETAIL is the button number for ButtonPress,
        ButtonRelease and DETAIL is the Keysym for KeyPress and
        KeyRelease. Examples are
        <Control-Button-1> for pressing Control and mouse button 1 or
        <Alt-A> for pressing A and the Alt key (KeyPress can be omitted).
        An event pattern can also be a virtual event of the form
        <<AString>> where AString can be arbitrary. This
        event can be generated by event_generate.
        If events are concatenated they must appear shortly
        after each other.
        
        FUNC will be called if the event sequence occurs with an
        instance of Event as argument. If the return value of FUNC is
        "break" no further bound function is invoked.
        
        An additional boolean parameter ADD specifies whether FUNC will
        be called additionally to the other bound function or whether
        it will replace the previous function.
        
        Bind will return an identifier to allow deletion of the bound function with
        unbind without memory leak.
        
        If FUNC or SEQUENCE is omitted the bound function or list
        of bound events are returned.
        """

    # inherited from tkinter.Misc
    def bind_all(self, sequence=None, func=None, add=None):
        """
        Bind to all widgets at an event SEQUENCE a call to function FUNC.
        An additional boolean parameter ADD specifies whether FUNC will
        be called additionally to the other bound function or whether
        it will replace the previous function. See bind for the return value.
        """

    # inherited from tkinter.Misc
    def bind_class(self, className, sequence=None, func=None, add=None):
        """
        Bind to widgets with bindtag CLASSNAME at event
        SEQUENCE a call of function FUNC. An additional
        boolean parameter ADD specifies whether FUNC will be
        called additionally to the other bound function or
        whether it will replace the previous function. See bind for
        the return value.
        """

    # inherited from tkinter.Misc
    def bindtags(self, tagList=None):
        """
        Set or get the list of bindtags for this widget.
        
        With no argument return the list of all bindtags associated with
        this widget. With a list of strings as argument the bindtags are
        set to this list. The bindtags determine in which order events are
        processed (see bind).
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

    # inherited from tkinter.Misc
    def cget(self, key):
        """
        Return the resource value for a KEY given as string.
        """

    def clear(self):
        """
        Clears the Scrollbox.
        This method doesn't destruct this object but BOX's children
        """

    # inherited from tkinter.Misc
    def clipboard_append(self, string, **kw):
        """
        Append STRING to the Tk clipboard.
        
        A widget specified at the optional displayof keyword
        argument specifies the target display. The clipboard
        can be retrieved with selection_get.
        """

    # inherited from tkinter.Misc
    def clipboard_clear(self, **kw):
        """
        Clear the data in the Tk clipboard.
        
        A widget specified for the optional displayof keyword
        argument specifies the target display.
        """

    # inherited from tkinter.Misc
    def clipboard_get(self, **kw):
        """
        Retrieve data from the clipboard on window's display.
        
        The window keyword defaults to the root window of the Tkinter
        application.
        
        The type keyword specifies the form in which the data is
        to be returned and should be an atom name such as STRING
        or FILE_NAME.  Type defaults to STRING, except on X11, where the default
        is to try UTF8_STRING and fall back to STRING.
        
        This command is equivalent to:
        
        selection_get(CLIPBOARD)
        """

    # inherited from tkinter.Misc
    def columnconfigure(self, index, cnf={}, **kw):
        """
        Configure column INDEX of a grid.
        
        Valid resources are minsize (minimum size of the column),
        weight (how much does additional space propagate to this column)
        and pad (how much space to let additionally).
        """

    # inherited from tkinter.Misc
    def config(self, cnf=None, **kw):
        """
        Configure resources of a widget.
        
        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.
        """

    # inherited from tkinter.Misc
    def configure(self, cnf=None, **kw):
        """
        Configure resources of a widget.
        
        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.
        """

    # inherited from tkinter.Misc
    def deletecommand(self, name):
        """
        Internal function.
        
        Delete the Tcl command provided in NAME.
        """

    # inherited from tkinter.BaseWidget
    def destroy(self):
        """
        Destroy this and all descendants widgets.
        """

    # inherited from tkinter.Misc
    def event_add(self, virtual, *sequences):
        """
        Bind a virtual event VIRTUAL (of the form <<Name>>)
        to an event SEQUENCE such that the virtual event is triggered
        whenever SEQUENCE occurs.
        """

    # inherited from tkinter.Misc
    def event_delete(self, virtual, *sequences):
        """
        Unbind a virtual event VIRTUAL from SEQUENCE.
        """

    # inherited from tkinter.Misc
    def event_generate(self, sequence, **kw):
        """
        Generate an event SEQUENCE. Additional
        keyword arguments specify parameter of the event
        (e.g. x, y, rootx, rooty).
        """

    # inherited from tkinter.Misc
    def event_info(self, virtual=None):
        """
        Return a list of all virtual events or the information
        about the SEQUENCE bound to the virtual event VIRTUAL.
        """

    # inherited from tkinter.Misc
    def focus(self):
        """
        Direct input focus to this widget.
        
        If the application currently does not have the focus
        this widget will get the focus if the application gets
        the focus through the window manager.
        """

    # inherited from tkinter.Misc
    def focus_displayof(self):
        """
        Return the widget which has currently the focus on the
        display where this widget is located.
        
        Return None if the application does not have the focus.
        """

    # inherited from tkinter.Misc
    def focus_force(self):
        """
        Direct input focus to this widget even if the
        application does not have the focus. Use with
        caution!
        """

    # inherited from tkinter.Misc
    def focus_get(self):
        """
        Return the widget which has currently the focus in the
        application.
        
        Use focus_displayof to allow working with several
        displays. Return None if application does not have
        the focus.
        """

    # inherited from tkinter.Misc
    def focus_lastfor(self):
        """
        Return the widget which would have the focus if top level
        for this widget gets the focus from the window manager.
        """

    # inherited from tkinter.Misc
    def focus_set(self):
        """
        Direct input focus to this widget.
        
        If the application currently does not have the focus
        this widget will get the focus if the application gets
        the focus through the window manager.
        """

    # inherited from tkinter.Pack
    def forget(self):
        """
        Unmap this widget and do not use it for the packing order.
        """

    # inherited from tkinter.Misc
    def getboolean(self, s):
        """
        Return a boolean value for Tcl boolean values true and false given as parameter.
        """

    # inherited from tkinter.Misc
    def getdouble(self, s):
        """
        
        """

    # inherited from tkinter.Misc
    def getint(self, s):
        """
        
        """

    # inherited from tkinter.Misc
    def getvar(self, name='PY_VAR'):
        """
        Return value of Tcl variable NAME.
        """

    # inherited from tkinter.Misc
    def grab_current(self):
        """
        Return widget which has currently the grab in this application
        or None.
        """

    # inherited from tkinter.Misc
    def grab_release(self):
        """
        Release grab for this widget if currently set.
        """

    # inherited from tkinter.Misc
    def grab_set(self):
        """
        Set grab for this widget.
        
        A grab directs all events to this and descendant
        widgets in the application.
        """

    # inherited from tkinter.Misc
    def grab_set_global(self):
        """
        Set global grab for this widget.
        
        A global grab directs all events to this and
        descendant widgets on the display. Use with caution -
        other applications do not get events anymore.
        """

    # inherited from tkinter.Misc
    def grab_status(self):
        """
        Return None, "local" or "global" if this widget has
        no, a local or a global grab.
        """

    # inherited from tkinter.Grid
    def grid(self, cnf={}, **kw):
        """
        Position a widget in the parent widget in a grid. Use as options:
        column=number - use cell identified with given column (starting with 0)
        columnspan=number - this widget will span several columns
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        row=number - use cell identified with given row (starting with 0)
        rowspan=number - this widget will span several rows
        sticky=NSEW - if cell is larger on which sides will this
                      widget stick to the cell boundary
        """

    # inherited from tkinter.Misc
    def grid_anchor(self, anchor=None):
        """
        The anchor value controls how to place the grid within the
        master when no row/column has any weight.
        
        The default anchor is nw.
        """

    # inherited from tkinter.Misc
    def grid_bbox(self, column=None, row=None, col2=None, row2=None):
        """
        Return a tuple of integer coordinates for the bounding
        box of this widget controlled by the geometry manager grid.
        
        If COLUMN, ROW is given the bounding box applies from
        the cell with row and column 0 to the specified
        cell. If COL2 and ROW2 are given the bounding box
        starts at that cell.
        
        The returned integers specify the offset of the upper left
        corner in the master widget and the width and height.
        """

    # inherited from tkinter.Misc
    def grid_columnconfigure(self, index, cnf={}, **kw):
        """
        Configure column INDEX of a grid.
        
        Valid resources are minsize (minimum size of the column),
        weight (how much does additional space propagate to this column)
        and pad (how much space to let additionally).
        """

    # inherited from tkinter.Grid
    def grid_configure(self, cnf={}, **kw):
        """
        Position a widget in the parent widget in a grid. Use as options:
        column=number - use cell identified with given column (starting with 0)
        columnspan=number - this widget will span several columns
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        row=number - use cell identified with given row (starting with 0)
        rowspan=number - this widget will span several rows
        sticky=NSEW - if cell is larger on which sides will this
                      widget stick to the cell boundary
        """

    # inherited from tkinter.Grid
    def grid_forget(self):
        """
        Unmap this widget.
        """

    # inherited from tkinter.Grid
    def grid_info(self):
        """
        Return information about the options
        for positioning this widget in a grid.
        """

    # inherited from tkinter.Misc
    def grid_location(self, x, y):
        """
        Return a tuple of column and row which identify the cell
        at which the pixel at position X and Y inside the master
        widget is located.
        """

    # inherited from tkinter.Misc
    def grid_propagate(self, flag=['_noarg_']):
        """
        Set or get the status for propagation of geometry information.
        
        A boolean argument specifies whether the geometry information
        of the slaves will determine the size of this widget. If no argument
        is given, the current setting will be returned.
        """

    # inherited from tkinter.Grid
    def grid_remove(self):
        """
        Unmap this widget but remember the grid options.
        """

    # inherited from tkinter.Misc
    def grid_rowconfigure(self, index, cnf={}, **kw):
        """
        Configure row INDEX of a grid.
        
        Valid resources are minsize (minimum size of the row),
        weight (how much does additional space propagate to this row)
        and pad (how much space to let additionally).
        """

    # inherited from tkinter.Misc
    def grid_size(self):
        """
        Return a tuple of the number of column and rows in the grid.
        """

    # inherited from tkinter.Misc
    def grid_slaves(self, row=None, column=None):
        """
        Return a list of all slaves of this widget
        in its packing order.
        """

    # inherited from tkinter.Misc
    def image_names(self):
        """
        Return a list of all existing image names.
        """

    # inherited from tkinter.Misc
    def image_types(self):
        """
        Return a list of all available image types (e.g. photo bitmap).
        """

    # inherited from tkinter.Pack
    def info(self):
        """
        Return information about the packing options
        for this widget.
        """

    # inherited from tkinter.Misc
    def keys(self):
        """
        Return a list of all resource names of this widget.
        """

    # inherited from tkinter.Misc
    def lift(self, aboveThis=None):
        """
        Raise this widget in the stacking order.
        """

    # inherited from tkinter.Grid
    def location(self, x, y):
        """
        Return a tuple of column and row which identify the cell
        at which the pixel at position X and Y inside the master
        widget is located.
        """

    # inherited from tkinter.Misc
    def lower(self, belowThis=None):
        """
        Lower this widget in the stacking order.
        """

    # inherited from tkinter.Misc
    def mainloop(self, n=0):
        """
        Call the mainloop of Tk.
        """

    # inherited from tkinter.Misc
    def nametowidget(self, name):
        """
        Return the Tkinter instance of a widget identified by
        its Tcl name NAME.
        """

    # inherited from tkinter.Misc
    def option_add(self, pattern, value, priority=None):
        """
        Set a VALUE (second parameter) for an option
        PATTERN (first parameter).
        
        An optional third parameter gives the numeric priority
        (defaults to 80).
        """

    # inherited from tkinter.Misc
    def option_clear(self):
        """
        Clear the option database.
        
        It will be reloaded if option_add is called.
        """

    # inherited from tkinter.Misc
    def option_get(self, name, className):
        """
        Return the value for an option NAME for this widget
        with CLASSNAME.
        
        Values with higher priority override lower values.
        """

    # inherited from tkinter.Misc
    def option_readfile(self, fileName, priority=None):
        """
        Read file FILENAME into the option database.
        
        An optional second parameter gives the numeric
        priority.
        """

    # inherited from tkinter.Pack
    def pack(self, cnf={}, **kw):
        """
        Pack a widget in the parent widget. Use as options:
        after=widget - pack it after you have packed widget
        anchor=NSEW (or subset) - position widget according to
                                  given direction
        before=widget - pack it before you will pack widget
        expand=bool - expand widget if parent size grows
        fill=NONE or X or Y or BOTH - fill widget if widget grows
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
        """

    # inherited from tkinter.Pack
    def pack_configure(self, cnf={}, **kw):
        """
        Pack a widget in the parent widget. Use as options:
        after=widget - pack it after you have packed widget
        anchor=NSEW (or subset) - position widget according to
                                  given direction
        before=widget - pack it before you will pack widget
        expand=bool - expand widget if parent size grows
        fill=NONE or X or Y or BOTH - fill widget if widget grows
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
        """

    # inherited from tkinter.Pack
    def pack_forget(self):
        """
        Unmap this widget and do not use it for the packing order.
        """

    # inherited from tkinter.Pack
    def pack_info(self):
        """
        Return information about the packing options
        for this widget.
        """

    # inherited from tkinter.Misc
    def pack_propagate(self, flag=['_noarg_']):
        """
        Set or get the status for propagation of geometry information.
        
        A boolean argument specifies whether the geometry information
        of the slaves will determine the size of this widget. If no argument
        is given the current setting will be returned.
        """

    # inherited from tkinter.Misc
    def pack_slaves(self):
        """
        Return a list of all slaves of this widget
        in its packing order.
        """

    # inherited from tkinter.Place
    def place(self, cnf={}, **kw):
        """
        Place a widget in the parent widget. Use as options:
        in=master - master relative to which the widget is placed
        in_=master - see 'in' option description
        x=amount - locate anchor of this widget at position x of master
        y=amount - locate anchor of this widget at position y of master
        relx=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to width of master (1.0 is right edge)
        rely=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to height of master (1.0 is bottom edge)
        anchor=NSEW (or subset) - position anchor according to given direction
        width=amount - width of this widget in pixel
        height=amount - height of this widget in pixel
        relwidth=amount - width of this widget between 0.0 and 1.0
                          relative to width of master (1.0 is the same width
                          as the master)
        relheight=amount - height of this widget between 0.0 and 1.0
                           relative to height of master (1.0 is the same
                           height as the master)
        bordermode="inside" or "outside" - whether to take border width of
                                           master widget into account
        """

    # inherited from tkinter.Place
    def place_configure(self, cnf={}, **kw):
        """
        Place a widget in the parent widget. Use as options:
        in=master - master relative to which the widget is placed
        in_=master - see 'in' option description
        x=amount - locate anchor of this widget at position x of master
        y=amount - locate anchor of this widget at position y of master
        relx=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to width of master (1.0 is right edge)
        rely=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to height of master (1.0 is bottom edge)
        anchor=NSEW (or subset) - position anchor according to given direction
        width=amount - width of this widget in pixel
        height=amount - height of this widget in pixel
        relwidth=amount - width of this widget between 0.0 and 1.0
                          relative to width of master (1.0 is the same width
                          as the master)
        relheight=amount - height of this widget between 0.0 and 1.0
                           relative to height of master (1.0 is the same
                           height as the master)
        bordermode="inside" or "outside" - whether to take border width of
                                           master widget into account
        """

    # inherited from tkinter.Place
    def place_forget(self):
        """
        Unmap this widget.
        """

    # inherited from tkinter.Place
    def place_info(self):
        """
        Return information about the placing options
        for this widget.
        """

    # inherited from tkinter.Misc
    def place_slaves(self):
        """
        Return a list of all slaves of this widget
        in its packing order.
        """

    # inherited from tkinter.Misc
    def propagate(self, flag=['_noarg_']):
        """
        Set or get the status for propagation of geometry information.
        
        A boolean argument specifies whether the geometry information
        of the slaves will determine the size of this widget. If no argument
        is given the current setting will be returned.
        """

    # inherited from tkinter.Misc
    def quit(self):
        """
        Quit the Tcl interpreter. All widgets will be destroyed.
        """

    # inherited from tkinter.Misc
    def register(self, func, subst=None, needcleanup=1):
        """
        Return a newly created Tcl function. If this
        function is called, the Python function FUNC will
        be executed. An optional function SUBST can
        be given which will be executed before FUNC.
        """

    # inherited from tkinter.Misc
    def rowconfigure(self, index, cnf={}, **kw):
        """
        Configure row INDEX of a grid.
        
        Valid resources are minsize (minimum size of the row),
        weight (how much does additional space propagate to this row)
        and pad (how much space to let additionally).
        """

    # inherited from tkinter.Misc
    def selection_clear(self, **kw):
        """
        Clear the current X selection.
        """

    # inherited from tkinter.Misc
    def selection_get(self, **kw):
        """
        Return the contents of the current X selection.
        
        A keyword parameter selection specifies the name of
        the selection and defaults to PRIMARY.  A keyword
        parameter displayof specifies a widget on the display
        to use. A keyword parameter type specifies the form of data to be
        fetched, defaulting to STRING except on X11, where UTF8_STRING is tried
        before STRING.
        """

    # inherited from tkinter.Misc
    def selection_handle(self, command, **kw):
        """
        Specify a function COMMAND to call if the X
        selection owned by this widget is queried by another
        application.
        
        This function must return the contents of the
        selection. The function will be called with the
        arguments OFFSET and LENGTH which allows the chunking
        of very long selections. The following keyword
        parameters can be provided:
        selection - name of the selection (default PRIMARY),
        type - type of the selection (e.g. STRING, FILE_NAME).
        """

    # inherited from tkinter.Misc
    def selection_own(self, **kw):
        """
        Become owner of X selection.
        
        A keyword parameter selection specifies the name of
        the selection (default PRIMARY).
        """

    # inherited from tkinter.Misc
    def selection_own_get(self, **kw):
        """
        Return owner of X selection.
        
        The following keyword parameter can
        be provided:
        selection - name of the selection (default PRIMARY),
        type - type of the selection (e.g. STRING, FILE_NAME).
        """

    # inherited from tkinter.Misc
    def send(self, interp, cmd, *args):
        """
        Send Tcl command CMD to different interpreter INTERP to be executed.
        """

    # inherited from tkinter.Misc
    def setvar(self, name='PY_VAR', value='1'):
        """
        Set Tcl variable NAME to VALUE.
        """

    # inherited from tkinter.Misc
    def size(self):
        """
        Return a tuple of the number of column and rows in the grid.
        """

    # inherited from tkinter.Misc
    def slaves(self):
        """
        Return a list of all slaves of this widget
        in its packing order.
        """

    # inherited from tkinter.Misc
    def tk_bisque(self):
        """
        Change the color scheme to light brown as used in Tk 3.6 and before.
        """

    # inherited from tkinter.Misc
    def tk_focusFollowsMouse(self):
        """
        The widget under mouse will get automatically focus. Can not
        be disabled easily.
        """

    # inherited from tkinter.Misc
    def tk_focusNext(self):
        """
        Return the next widget in the focus order which follows
        widget which has currently the focus.
        
        The focus order first goes to the next child, then to
        the children of the child recursively and then to the
        next sibling which is higher in the stacking order.  A
        widget is omitted if it has the takefocus resource set
        to 0.
        """

    # inherited from tkinter.Misc
    def tk_focusPrev(self):
        """
        Return previous widget in the focus order. See tk_focusNext for details.
        """

    # inherited from tkinter.Misc
    def tk_setPalette(self, *args, **kw):
        """
        Set a new color scheme for all widget elements.
        
        A single color as argument will cause that all colors of Tk
        widget elements are derived from this.
        Alternatively several keyword parameters and its associated
        colors can be given. The following keywords are valid:
        activeBackground, foreground, selectColor,
        activeForeground, highlightBackground, selectBackground,
        background, highlightColor, selectForeground,
        disabledForeground, insertBackground, troughColor.
        """

    # inherited from tkinter.Misc
    def tk_strictMotif(self, boolean=None):
        """
        Set Tcl internal variable, whether the look and feel
        should adhere to Motif.
        
        A parameter of 1 means adhere to Motif (e.g. no color
        change if mouse passes over slider).
        Returns the set value.
        """

    # inherited from tkinter.Misc
    def tkraise(self, aboveThis=None):
        """
        Raise this widget in the stacking order.
        """

    # inherited from tkinter.Misc
    def unbind(self, sequence, funcid=None):
        """
        Unbind for this widget for event SEQUENCE  the
        function identified with FUNCID.
        """

    # inherited from tkinter.Misc
    def unbind_all(self, sequence):
        """
        Unbind for all widgets for event SEQUENCE all functions.
        """

    # inherited from tkinter.Misc
    def unbind_class(self, className, sequence):
        """
        Unbind for all widgets with bindtag CLASSNAME for event SEQUENCE
        all functions.
        """

    # inherited from tkinter.Misc
    def update(self):
        """
        Enter event loop until all pending events have been processed by Tcl.
        """

    # inherited from tkinter.Misc
    def update_idletasks(self):
        """
        Enter event loop until all idle callbacks have been called. This
        will update the display of windows but not process events caused by
        the user.
        """

    # inherited from tkinter.Misc
    def wait_variable(self, name='PY_VAR'):
        """
        Wait until the variable is modified.
        
        A parameter of type IntVar, StringVar, DoubleVar or
        BooleanVar must be given.
        """

    # inherited from tkinter.Misc
    def wait_visibility(self, window=None):
        """
        Wait until the visibility of a WIDGET changes
        (e.g. it appears).
        
        If no parameter is given self is used.
        """

    # inherited from tkinter.Misc
    def wait_window(self, window=None):
        """
        Wait until a WIDGET is destroyed.
        
        If no parameter is given self is used.
        """

    # inherited from tkinter.Misc
    def waitvar(self, name='PY_VAR'):
        """
        Wait until the variable is modified.
        
        A parameter of type IntVar, StringVar, DoubleVar or
        BooleanVar must be given.
        """

    # inherited from tkinter.Misc
    def winfo_atom(self, name, displayof=0):
        """
        Return integer which represents atom NAME.
        """

    # inherited from tkinter.Misc
    def winfo_atomname(self, id, displayof=0):
        """
        Return name of atom with identifier ID.
        """

    # inherited from tkinter.Misc
    def winfo_cells(self):
        """
        Return number of cells in the colormap for this widget.
        """

    # inherited from tkinter.Misc
    def winfo_children(self):
        """
        Return a list of all widgets which are children of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_class(self):
        """
        Return window class name of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_colormapfull(self):
        """
        Return true if at the last color request the colormap was full.
        """

    # inherited from tkinter.Misc
    def winfo_containing(self, rootX, rootY, displayof=0):
        """
        Return the widget which is at the root coordinates ROOTX, ROOTY.
        """

    # inherited from tkinter.Misc
    def winfo_depth(self):
        """
        Return the number of bits per pixel.
        """

    # inherited from tkinter.Misc
    def winfo_exists(self):
        """
        Return true if this widget exists.
        """

    # inherited from tkinter.Misc
    def winfo_fpixels(self, number):
        """
        Return the number of pixels for the given distance NUMBER
        (e.g. "3c") as float.
        """

    # inherited from tkinter.Misc
    def winfo_geometry(self):
        """
        Return geometry string for this widget in the form "widthxheight+X+Y".
        """

    # inherited from tkinter.Misc
    def winfo_height(self):
        """
        Return height of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_id(self):
        """
        Return identifier ID for this widget.
        """

    # inherited from tkinter.Misc
    def winfo_interps(self, displayof=0):
        """
        Return the name of all Tcl interpreters for this display.
        """

    # inherited from tkinter.Misc
    def winfo_ismapped(self):
        """
        Return true if this widget is mapped.
        """

    # inherited from tkinter.Misc
    def winfo_manager(self):
        """
        Return the window manager name for this widget.
        """

    # inherited from tkinter.Misc
    def winfo_name(self):
        """
        Return the name of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_parent(self):
        """
        Return the name of the parent of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_pathname(self, id, displayof=0):
        """
        Return the pathname of the widget given by ID.
        """

    # inherited from tkinter.Misc
    def winfo_pixels(self, number):
        """
        Rounded integer value of winfo_fpixels.
        """

    # inherited from tkinter.Misc
    def winfo_pointerx(self):
        """
        Return the x coordinate of the pointer on the root window.
        """

    # inherited from tkinter.Misc
    def winfo_pointerxy(self):
        """
        Return a tuple of x and y coordinates of the pointer on the root window.
        """

    # inherited from tkinter.Misc
    def winfo_pointery(self):
        """
        Return the y coordinate of the pointer on the root window.
        """

    # inherited from tkinter.Misc
    def winfo_reqheight(self):
        """
        Return requested height of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_reqwidth(self):
        """
        Return requested width of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_rgb(self, color):
        """
        Return tuple of decimal values for red, green, blue for
        COLOR in this widget.
        """

    # inherited from tkinter.Misc
    def winfo_rootx(self):
        """
        Return x coordinate of upper left corner of this widget on the
        root window.
        """

    # inherited from tkinter.Misc
    def winfo_rooty(self):
        """
        Return y coordinate of upper left corner of this widget on the
        root window.
        """

    # inherited from tkinter.Misc
    def winfo_screen(self):
        """
        Return the screen name of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_screencells(self):
        """
        Return the number of the cells in the colormap of the screen
        of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_screendepth(self):
        """
        Return the number of bits per pixel of the root window of the
        screen of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_screenheight(self):
        """
        Return the number of pixels of the height of the screen of this widget
        in pixel.
        """

    # inherited from tkinter.Misc
    def winfo_screenmmheight(self):
        """
        Return the number of pixels of the height of the screen of
        this widget in mm.
        """

    # inherited from tkinter.Misc
    def winfo_screenmmwidth(self):
        """
        Return the number of pixels of the width of the screen of
        this widget in mm.
        """

    # inherited from tkinter.Misc
    def winfo_screenvisual(self):
        """
        Return one of the strings directcolor, grayscale, pseudocolor,
        staticcolor, staticgray, or truecolor for the default
        colormodel of this screen.
        """

    # inherited from tkinter.Misc
    def winfo_screenwidth(self):
        """
        Return the number of pixels of the width of the screen of
        this widget in pixel.
        """

    # inherited from tkinter.Misc
    def winfo_server(self):
        """
        Return information of the X-Server of the screen of this widget in
        the form "XmajorRminor vendor vendorVersion".
        """

    # inherited from tkinter.Misc
    def winfo_toplevel(self):
        """
        Return the toplevel widget of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_viewable(self):
        """
        Return true if the widget and all its higher ancestors are mapped.
        """

    # inherited from tkinter.Misc
    def winfo_visual(self):
        """
        Return one of the strings directcolor, grayscale, pseudocolor,
        staticcolor, staticgray, or truecolor for the
        colormodel of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_visualid(self):
        """
        Return the X identifier for the visual for this widget.
        """

    # inherited from tkinter.Misc
    def winfo_visualsavailable(self, includeids=False):
        """
        Return a list of all visuals available for the screen
        of this widget.
        
        Each item in the list consists of a visual name (see winfo_visual), a
        depth and if includeids is true is given also the X identifier.
        """

    # inherited from tkinter.Misc
    def winfo_vrootheight(self):
        """
        Return the height of the virtual root window associated with this
        widget in pixels. If there is no virtual root window return the
        height of the screen.
        """

    # inherited from tkinter.Misc
    def winfo_vrootwidth(self):
        """
        Return the width of the virtual root window associated with this
        widget in pixel. If there is no virtual root window return the
        width of the screen.
        """

    # inherited from tkinter.Misc
    def winfo_vrootx(self):
        """
        Return the x offset of the virtual root relative to the root
        window of the screen of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_vrooty(self):
        """
        Return the y offset of the virtual root relative to the root
        window of the screen of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_width(self):
        """
        Return the width of this widget.
        """

    # inherited from tkinter.Misc
    def winfo_x(self):
        """
        Return the x coordinate of the upper left corner of this widget
        in the parent.
        """

    # inherited from tkinter.Misc
    def winfo_y(self):
        """
        Return the y coordinate of the upper left corner of this widget
        in the parent.
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

    # inherited from tkinter.Misc
    def _bind(self, what, sequence, func, add, needcleanup=1):
        """
        Internal function.
        """

    # inherited from tkinter.Misc
    def _configure(self, cmd, cnf, kw):
        """
        Internal function.
        """

    # inherited from tkinter.Misc
    def _displayof(self, displayof):
        """
        Internal function.
        """

    # inherited from tkinter.BaseWidget
    def _do(self, name, args=()):
        """
        
        """

    # inherited from tkinter.Misc
    def _getboolean(self, string):
        """
        Internal function.
        """

    # inherited from tkinter.Misc
    def _getconfigure(self, *args):
        """
        Call Tcl configure command and return the result as a dict.
        """

    # inherited from tkinter.Misc
    def _getconfigure1(self, *args):
        """
        
        """

    # inherited from tkinter.Misc
    def _getdoubles(self, string):
        """
        Internal function.
        """

    # inherited from tkinter.Misc
    def _getints(self, string):
        """
        Internal function.
        """

    # inherited from tkinter.Misc
    def _grid_configure(self, command, index, cnf, kw):
        """
        Internal function.
        """

    # inherited from tkinter.Misc
    def _gridconvvalue(self, value):
        """
        
        """

    # inherited from tkinter.Misc
    def _nametowidget(self, name):
        """
        Return the Tkinter instance of a widget identified by
        its Tcl name NAME.
        """

    # inherited from tkinter.Misc
    def _options(self, cnf, kw=None):
        """
        Internal function.
        """

    # inherited from tkinter.Misc
    def _register(self, func, subst=None, needcleanup=1):
        """
        Return a newly created Tcl function. If this
        function is called, the Python function FUNC will
        be executed. An optional function SUBST can
        be given which will be executed before FUNC.
        """

    # inherited from tkinter.Misc
    def _report_exception(self):
        """
        Internal function.
        """

    # inherited from tkinter.Misc
    def _root(self):
        """
        Internal function.
        """

    # inherited from tkinter.BaseWidget
    def _setup(self, master, cnf):
        """
        Internal function. Sets up information about children.
        """

    # inherited from tkinter.Misc
    def _substitute(self, *args):
        """
        Internal function.
        """

```

