Back to [Modules overview](https://github.com/pyrustic/megawidget/blob/master/docs/modules/README.md)
  
# Module documentation
>## megawidget.toast.\_\_init\_\_
No description
<br>
[constants (3)](https://github.com/pyrustic/megawidget/blob/master/docs/modules/content/megawidget.toast.__init__/constants.md) &nbsp;.&nbsp; [classes (3)](https://github.com/pyrustic/megawidget/blob/master/docs/modules/content/megawidget.toast.__init__/classes.md)


## Classes
```python
class Error(Exception):
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """


    args = <attribute 'args' of 'BaseException' objects>
    
```

```python
class Toast(tkinter.Toplevel):
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

    # inherited from tkinter.Wm
    def aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None):
        """
        Instruct the window manager to set the aspect ratio (width/height)
        of this widget to be between MINNUMER/MINDENOM and MAXNUMER/MAXDENOM. Return a tuple
        of the actual values if no argument is given.
        """

    # inherited from tkinter.Wm
    def attributes(self, *args):
        """
        This subcommand returns or sets platform specific attributes
        
        The first form returns a list of the platform specific flags and
        their values. The second form returns the value for the specific
        option. The third form sets one or more of the values. The values
        are as follows:
        
        On Windows, -disabled gets or sets whether the window is in a
        disabled state. -toolwindow gets or sets the style of the window
        to toolwindow (as defined in the MSDN). -topmost gets or sets
        whether this is a topmost window (displays above all other
        windows).
        
        On Macintosh, XXXXX
        
        On Unix, there are currently no special attribute values.
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

    # inherited from tkinter.Misc
    def cget(self, key):
        """
        Return the resource value for a KEY given as string.
        """

    # inherited from tkinter.Wm
    def client(self, name=None):
        """
        Store NAME in WM_CLIENT_MACHINE property of this widget. Return
        current value.
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

    # inherited from tkinter.Wm
    def colormapwindows(self, *wlist):
        """
        Store list of window names (WLIST) into WM_COLORMAPWINDOWS property
        of this widget. This list contains windows whose colormaps differ from their
        parents. Return current list of widgets if WLIST is empty.
        """

    # inherited from tkinter.Misc
    def columnconfigure(self, index, cnf={}, **kw):
        """
        Configure column INDEX of a grid.
        
        Valid resources are minsize (minimum size of the column),
        weight (how much does additional space propagate to this column)
        and pad (how much space to let additionally).
        """

    # inherited from tkinter.Wm
    def command(self, value=None):
        """
        Store VALUE in WM_COMMAND property. It is the command
        which shall be used to invoke the application. Return current
        command if VALUE is None.
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

    # inherited from tkinter.Wm
    def deiconify(self):
        """
        Deiconify this widget. If it was never mapped it will not be mapped.
        On Windows it will raise this widget and give it the focus.
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

    # inherited from tkinter.Wm
    def focusmodel(self, model=None):
        """
        Set focus model to MODEL. "active" means that this widget will claim
        the focus itself, "passive" means that the window manager shall give
        the focus. Return current focus model if MODEL is None.
        """

    # inherited from tkinter.Wm
    def forget(self, window):
        """
        The window will be unmapped from the screen and will no longer
        be managed by wm. toplevel windows will be treated like frame
        windows once they are no longer managed by wm, however, the menu
        option configuration will be remembered and the menus will return
        once the widget is managed again.
        """

    # inherited from tkinter.Wm
    def frame(self):
        """
        Return identifier for decorative frame of this widget if present.
        """

    # inherited from tkinter.Wm
    def geometry(self, newGeometry=None):
        """
        Set geometry to NEWGEOMETRY of the form =widthxheight+x+y. Return
        current value if None is given.
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

    # inherited from tkinter.Wm
    def grid(self, baseWidth=None, baseHeight=None, widthInc=None, heightInc=None):
        """
        Instruct the window manager that this widget shall only be
        resized on grid boundaries. WIDTHINC and HEIGHTINC are the width and
        height of a grid unit in pixels. BASEWIDTH and BASEHEIGHT are the
        number of grid units requested in Tk_GeometryRequest.
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

    # inherited from tkinter.Wm
    def group(self, pathName=None):
        """
        Set the group leader widgets for related widgets to PATHNAME. Return
        the group leader of this widget if None is given.
        """

    # inherited from tkinter.Wm
    def iconbitmap(self, bitmap=None, default=None):
        """
        Set bitmap for the iconified widget to BITMAP. Return
        the bitmap if None is given.
        
        Under Windows, the DEFAULT parameter can be used to set the icon
        for the widget and any descendents that don't have an icon set
        explicitly.  DEFAULT can be the relative path to a .ico file
        (example: root.iconbitmap(default='myicon.ico') ).  See Tk
        documentation for more information.
        """

    # inherited from tkinter.Wm
    def iconify(self):
        """
        Display widget as icon.
        """

    # inherited from tkinter.Wm
    def iconmask(self, bitmap=None):
        """
        Set mask for the icon bitmap of this widget. Return the
        mask if None is given.
        """

    # inherited from tkinter.Wm
    def iconname(self, newName=None):
        """
        Set the name of the icon for this widget. Return the name if
        None is given.
        """

    # inherited from tkinter.Wm
    def iconphoto(self, default=False, *args):
        """
        Sets the titlebar icon for this window based on the named photo
        images passed through args. If default is True, this is applied to
        all future created toplevels as well.
        
        The data in the images is taken as a snapshot at the time of
        invocation. If the images are later changed, this is not reflected
        to the titlebar icons. Multiple images are accepted to allow
        different images sizes to be provided. The window manager may scale
        provided icons to an appropriate size.
        
        On Windows, the images are packed into a Windows icon structure.
        This will override an icon specified to wm_iconbitmap, and vice
        versa.
        
        On X, the images are arranged into the _NET_WM_ICON X property,
        which most modern window managers support. An icon specified by
        wm_iconbitmap may exist simultaneously.
        
        On Macintosh, this currently does nothing.
        """

    # inherited from tkinter.Wm
    def iconposition(self, x=None, y=None):
        """
        Set the position of the icon of this widget to X and Y. Return
        a tuple of the current values of X and X if None is given.
        """

    # inherited from tkinter.Wm
    def iconwindow(self, pathName=None):
        """
        Set widget PATHNAME to be displayed instead of icon. Return the current
        value if None is given.
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

    # inherited from tkinter.Wm
    def manage(self, widget):
        """
        The widget specified will become a stand alone top-level window.
        The window will be decorated with the window managers title bar,
        etc.
        """

    # inherited from tkinter.Wm
    def maxsize(self, width=None, height=None):
        """
        Set max WIDTH and HEIGHT for this widget. If the window is gridded
        the values are given in grid units. Return the current values if None
        is given.
        """

    # inherited from tkinter.Wm
    def minsize(self, width=None, height=None):
        """
        Set min WIDTH and HEIGHT for this widget. If the window is gridded
        the values are given in grid units. Return the current values if None
        is given.
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

    # inherited from tkinter.Wm
    def overrideredirect(self, boolean=None):
        """
        Instruct the window manager to ignore this widget
        if BOOLEAN is given with 1. Return the current value if None
        is given.
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

    # inherited from tkinter.Misc
    def place_slaves(self):
        """
        Return a list of all slaves of this widget
        in its packing order.
        """

    # inherited from tkinter.Wm
    def positionfrom(self, who=None):
        """
        Instruct the window manager that the position of this widget shall
        be defined by the user if WHO is "user", and by its own policy if WHO is
        "program".
        """

    # inherited from tkinter.Misc
    def propagate(self, flag=['_noarg_']):
        """
        Set or get the status for propagation of geometry information.
        
        A boolean argument specifies whether the geometry information
        of the slaves will determine the size of this widget. If no argument
        is given the current setting will be returned.
        """

    # inherited from tkinter.Wm
    def protocol(self, name=None, func=None):
        """
        Bind function FUNC to command NAME for this widget.
        Return the function bound to NAME if None is given. NAME could be
        e.g. "WM_SAVE_YOURSELF" or "WM_DELETE_WINDOW".
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

    # inherited from tkinter.Wm
    def resizable(self, width=None, height=None):
        """
        Instruct the window manager whether this width can be resized
        in WIDTH or HEIGHT. Both values are boolean values.
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

    # inherited from tkinter.Wm
    def sizefrom(self, who=None):
        """
        Instruct the window manager that the size of this widget shall
        be defined by the user if WHO is "user", and by its own policy if WHO is
        "program".
        """

    # inherited from tkinter.Misc
    def slaves(self):
        """
        Return a list of all slaves of this widget
        in its packing order.
        """

    # inherited from tkinter.Wm
    def state(self, newstate=None):
        """
        Query or set the state of this widget as one of normal, icon,
        iconic (see wm_iconwindow), withdrawn, or zoomed (Windows only).
        """

    # inherited from tkinter.Wm
    def title(self, string=None):
        """
        Set the title of this widget.
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

    # inherited from tkinter.Wm
    def transient(self, master=None):
        """
        Instruct the window manager that this widget is transient
        with regard to widget MASTER.
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

    # inherited from tkinter.Wm
    def withdraw(self):
        """
        Withdraw this widget from the screen such that it is unmapped
        and forgotten by the window manager. Re-draw it with wm_deiconify.
        """

    # inherited from tkinter.Wm
    def wm_aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None):
        """
        Instruct the window manager to set the aspect ratio (width/height)
        of this widget to be between MINNUMER/MINDENOM and MAXNUMER/MAXDENOM. Return a tuple
        of the actual values if no argument is given.
        """

    # inherited from tkinter.Wm
    def wm_attributes(self, *args):
        """
        This subcommand returns or sets platform specific attributes
        
        The first form returns a list of the platform specific flags and
        their values. The second form returns the value for the specific
        option. The third form sets one or more of the values. The values
        are as follows:
        
        On Windows, -disabled gets or sets whether the window is in a
        disabled state. -toolwindow gets or sets the style of the window
        to toolwindow (as defined in the MSDN). -topmost gets or sets
        whether this is a topmost window (displays above all other
        windows).
        
        On Macintosh, XXXXX
        
        On Unix, there are currently no special attribute values.
        """

    # inherited from tkinter.Wm
    def wm_client(self, name=None):
        """
        Store NAME in WM_CLIENT_MACHINE property of this widget. Return
        current value.
        """

    # inherited from tkinter.Wm
    def wm_colormapwindows(self, *wlist):
        """
        Store list of window names (WLIST) into WM_COLORMAPWINDOWS property
        of this widget. This list contains windows whose colormaps differ from their
        parents. Return current list of widgets if WLIST is empty.
        """

    # inherited from tkinter.Wm
    def wm_command(self, value=None):
        """
        Store VALUE in WM_COMMAND property. It is the command
        which shall be used to invoke the application. Return current
        command if VALUE is None.
        """

    # inherited from tkinter.Wm
    def wm_deiconify(self):
        """
        Deiconify this widget. If it was never mapped it will not be mapped.
        On Windows it will raise this widget and give it the focus.
        """

    # inherited from tkinter.Wm
    def wm_focusmodel(self, model=None):
        """
        Set focus model to MODEL. "active" means that this widget will claim
        the focus itself, "passive" means that the window manager shall give
        the focus. Return current focus model if MODEL is None.
        """

    # inherited from tkinter.Wm
    def wm_forget(self, window):
        """
        The window will be unmapped from the screen and will no longer
        be managed by wm. toplevel windows will be treated like frame
        windows once they are no longer managed by wm, however, the menu
        option configuration will be remembered and the menus will return
        once the widget is managed again.
        """

    # inherited from tkinter.Wm
    def wm_frame(self):
        """
        Return identifier for decorative frame of this widget if present.
        """

    # inherited from tkinter.Wm
    def wm_geometry(self, newGeometry=None):
        """
        Set geometry to NEWGEOMETRY of the form =widthxheight+x+y. Return
        current value if None is given.
        """

    # inherited from tkinter.Wm
    def wm_grid(self, baseWidth=None, baseHeight=None, widthInc=None, heightInc=None):
        """
        Instruct the window manager that this widget shall only be
        resized on grid boundaries. WIDTHINC and HEIGHTINC are the width and
        height of a grid unit in pixels. BASEWIDTH and BASEHEIGHT are the
        number of grid units requested in Tk_GeometryRequest.
        """

    # inherited from tkinter.Wm
    def wm_group(self, pathName=None):
        """
        Set the group leader widgets for related widgets to PATHNAME. Return
        the group leader of this widget if None is given.
        """

    # inherited from tkinter.Wm
    def wm_iconbitmap(self, bitmap=None, default=None):
        """
        Set bitmap for the iconified widget to BITMAP. Return
        the bitmap if None is given.
        
        Under Windows, the DEFAULT parameter can be used to set the icon
        for the widget and any descendents that don't have an icon set
        explicitly.  DEFAULT can be the relative path to a .ico file
        (example: root.iconbitmap(default='myicon.ico') ).  See Tk
        documentation for more information.
        """

    # inherited from tkinter.Wm
    def wm_iconify(self):
        """
        Display widget as icon.
        """

    # inherited from tkinter.Wm
    def wm_iconmask(self, bitmap=None):
        """
        Set mask for the icon bitmap of this widget. Return the
        mask if None is given.
        """

    # inherited from tkinter.Wm
    def wm_iconname(self, newName=None):
        """
        Set the name of the icon for this widget. Return the name if
        None is given.
        """

    # inherited from tkinter.Wm
    def wm_iconphoto(self, default=False, *args):
        """
        Sets the titlebar icon for this window based on the named photo
        images passed through args. If default is True, this is applied to
        all future created toplevels as well.
        
        The data in the images is taken as a snapshot at the time of
        invocation. If the images are later changed, this is not reflected
        to the titlebar icons. Multiple images are accepted to allow
        different images sizes to be provided. The window manager may scale
        provided icons to an appropriate size.
        
        On Windows, the images are packed into a Windows icon structure.
        This will override an icon specified to wm_iconbitmap, and vice
        versa.
        
        On X, the images are arranged into the _NET_WM_ICON X property,
        which most modern window managers support. An icon specified by
        wm_iconbitmap may exist simultaneously.
        
        On Macintosh, this currently does nothing.
        """

    # inherited from tkinter.Wm
    def wm_iconposition(self, x=None, y=None):
        """
        Set the position of the icon of this widget to X and Y. Return
        a tuple of the current values of X and X if None is given.
        """

    # inherited from tkinter.Wm
    def wm_iconwindow(self, pathName=None):
        """
        Set widget PATHNAME to be displayed instead of icon. Return the current
        value if None is given.
        """

    # inherited from tkinter.Wm
    def wm_manage(self, widget):
        """
        The widget specified will become a stand alone top-level window.
        The window will be decorated with the window managers title bar,
        etc.
        """

    # inherited from tkinter.Wm
    def wm_maxsize(self, width=None, height=None):
        """
        Set max WIDTH and HEIGHT for this widget. If the window is gridded
        the values are given in grid units. Return the current values if None
        is given.
        """

    # inherited from tkinter.Wm
    def wm_minsize(self, width=None, height=None):
        """
        Set min WIDTH and HEIGHT for this widget. If the window is gridded
        the values are given in grid units. Return the current values if None
        is given.
        """

    # inherited from tkinter.Wm
    def wm_overrideredirect(self, boolean=None):
        """
        Instruct the window manager to ignore this widget
        if BOOLEAN is given with 1. Return the current value if None
        is given.
        """

    # inherited from tkinter.Wm
    def wm_positionfrom(self, who=None):
        """
        Instruct the window manager that the position of this widget shall
        be defined by the user if WHO is "user", and by its own policy if WHO is
        "program".
        """

    # inherited from tkinter.Wm
    def wm_protocol(self, name=None, func=None):
        """
        Bind function FUNC to command NAME for this widget.
        Return the function bound to NAME if None is given. NAME could be
        e.g. "WM_SAVE_YOURSELF" or "WM_DELETE_WINDOW".
        """

    # inherited from tkinter.Wm
    def wm_resizable(self, width=None, height=None):
        """
        Instruct the window manager whether this width can be resized
        in WIDTH or HEIGHT. Both values are boolean values.
        """

    # inherited from tkinter.Wm
    def wm_sizefrom(self, who=None):
        """
        Instruct the window manager that the size of this widget shall
        be defined by the user if WHO is "user", and by its own policy if WHO is
        "program".
        """

    # inherited from tkinter.Wm
    def wm_state(self, newstate=None):
        """
        Query or set the state of this widget as one of normal, icon,
        iconic (see wm_iconwindow), withdrawn, or zoomed (Windows only).
        """

    # inherited from tkinter.Wm
    def wm_title(self, string=None):
        """
        Set the title of this widget.
        """

    # inherited from tkinter.Wm
    def wm_transient(self, master=None):
        """
        Instruct the window manager that this widget is transient
        with regard to widget MASTER.
        """

    # inherited from tkinter.Wm
    def wm_withdraw(self):
        """
        Withdraw this widget from the screen such that it is unmapped
        and forgotten by the window manager. Re-draw it with wm_deiconify.
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

