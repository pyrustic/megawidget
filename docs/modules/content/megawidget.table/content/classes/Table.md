Back to [All Modules](https://github.com/pyrustic/megawidget/blob/master/docs/modules/README.md#readme)

# Module Overview

**megawidget.table**
 
No description

> **Classes:** &nbsp; [Table](https://github.com/pyrustic/megawidget/blob/master/docs/modules/content/megawidget.table/content/classes/Table.md#class-table)
>
> **Functions:** &nbsp; [\_check\_option](https://github.com/pyrustic/megawidget/blob/master/docs/modules/content/megawidget.table/content/functions.md#_check_option) &nbsp;&nbsp; [\_verify\_options](https://github.com/pyrustic/megawidget/blob/master/docs/modules/content/megawidget.table/content/functions.md#_verify_options)
>
> **Constants:** &nbsp; ASC &nbsp;&nbsp; BODY &nbsp;&nbsp; BOTH &nbsp;&nbsp; BROWSE &nbsp;&nbsp; CANVAS &nbsp;&nbsp; COLUMN_OPTIONS &nbsp;&nbsp; DESC &nbsp;&nbsp; EQUALLY &nbsp;&nbsp; EXTENDED &nbsp;&nbsp; FRAMES_HEADERS &nbsp;&nbsp; FRAME_BACKGROUND &nbsp;&nbsp; HORIZONTAL &nbsp;&nbsp; HSB &nbsp;&nbsp; LABELS_SORTING &nbsp;&nbsp; LABELS_TITLES &nbsp;&nbsp; LISTBOXES_COLUMNS &nbsp;&nbsp; MULTIPLE &nbsp;&nbsp; PROPORTIONALLY &nbsp;&nbsp; SINGLE &nbsp;&nbsp; VERTICAL &nbsp;&nbsp; VSB

# Class Table
Table supports data sorting, multiple selection modes, and more...

Example:
```python
import tkinter as tk
from pyrustic.widget.table import Table

root = tk.Tk()
my_titles = ("Name", "Job")
my_data = (("Jack", "Architect"), ("Diana", "Physicist"))
table = Table(root, titles=my_titles, data=my_data)
table.build_pack()
root.mainloop()
```

## Base Classes
tkinter.Frame

## Class Attributes
\_last\_child\_ids (inherited from tkinter.Misc) &nbsp;&nbsp; \_noarg\_ (inherited from tkinter.Misc) &nbsp;&nbsp; \_subst\_format (inherited from tkinter.Misc) &nbsp;&nbsp; \_subst\_format\_str (inherited from tkinter.Misc) &nbsp;&nbsp; \_tclCommands (inherited from tkinter.Misc)

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|_windowingsystem|getter|Internal function.|tkinter.Misc|
|data|getter|None||
|data|setter|Data is a sequence of sequences of strings. This property overwrite the existing data. Example:     Assume that the titles are: ("Name", "Age")     Data: ( ("Jack", 56), ("Jane", 47) )||
|hidden_columns|getter|None||
|hidden_columns|setter|val: sequence of indexes to hide. Warning, even if you want to hide just one index, you should put this index into a tuple or list. Example: hide the column of index 1: (1, ) or [1]||
|layout|getter|None||
|mask|getter|None||
|mask|setter|val: a callable that will be called at each insertion of line of data in the table.     The mask must accept 2 arguments:         - index: int, index of the row (line)         - data: the sequence of strings to insert at this given row     The mask must returns a new data with same length or the same old data||
|orient|getter|None||
|parts|getter|Get the parts (widgets instances) used to build this dialog.  This property returns a dict. The keys are:     BODY, VSB, HSB, CANVAS, FRAME_BACKGROUND,     FRAMES_HEADERS, LISTBOXES_COLUMNS, LABELS_SORTING and LABELS_TITLES Warning: FRAMES_HEADERS, LABELS_TITLES, LABELS_SORTING  and LISTBOXES_COLUMNS are sequences of widgets by index||
|select_mode|getter|None||
|selection|getter|Return a sequence of the current selection. selection = ( item_1, item_2, ...) item_i = {"index": int, "data": data} data = a sequence of string representing the row at the index.||
|table_size|getter|returns the length of columns and rows: (rows, cols) Example:     Assume that the table has 3 columns and 10 rows,     this property will return (10, 3)||
|titles|getter|None||
|titles|setter|Titles are a sequence of strings. This property overwrite the existing titles.||



# All Methods
[\_misc\_\_winfo\_getint](#_Misc__winfo_getint) &nbsp;&nbsp; [\_misc\_\_winfo\_parseitem](#_Misc__winfo_parseitem) &nbsp;&nbsp; [\_table\_\_adjust\_selection\_after\_insertion](#_Table__adjust_selection_after_insertion) &nbsp;&nbsp; [\_table\_\_build](#_Table__build) &nbsp;&nbsp; [\_table\_\_build\_handler\_for\_row\_event](#_Table__build_handler_for_row_event) &nbsp;&nbsp; [\_table\_\_build\_header\_and\_columns](#_Table__build_header_and_columns) &nbsp;&nbsp; [\_table\_\_build\_table](#_Table__build_table) &nbsp;&nbsp; [\_table\_\_check\_data\_row\_size](#_Table__check_data_row_size) &nbsp;&nbsp; [\_table\_\_extract\_listboxes\_color](#_Table__extract_listboxes_color) &nbsp;&nbsp; [\_table\_\_fix\_selection\_in\_multiple\_selectmode](#_Table__fix_selection_in_multiple_selectmode) &nbsp;&nbsp; [\_table\_\_insert](#_Table__insert) &nbsp;&nbsp; [\_table\_\_manage\_selection\_garbage](#_Table__manage_selection_garbage) &nbsp;&nbsp; [\_table\_\_on\_configure\_background](#_Table__on_configure_background) &nbsp;&nbsp; [\_table\_\_on\_destroy](#_Table__on_destroy) &nbsp;&nbsp; [\_table\_\_on\_header\_clicked](#_Table__on_header_clicked) &nbsp;&nbsp; [\_table\_\_on\_map](#_Table__on_map) &nbsp;&nbsp; [\_table\_\_on\_mouse\_wheel](#_Table__on_mouse_wheel) &nbsp;&nbsp; [\_table\_\_on\_row\_selected](#_Table__on_row_selected) &nbsp;&nbsp; [\_table\_\_reset\_data](#_Table__reset_data) &nbsp;&nbsp; [\_table\_\_reset\_titles](#_Table__reset_titles) &nbsp;&nbsp; [\_table\_\_scroll\_listboxes\_and\_scrollbar\_sync](#_Table__scroll_listboxes_and_scrollbar_sync) &nbsp;&nbsp; [\_table\_\_scroll\_listboxes\_sync](#_Table__scroll_listboxes_sync) &nbsp;&nbsp; [\_table\_\_set\_scrollbars](#_Table__set_scrollbars) &nbsp;&nbsp; [\_table\_\_setup](#_Table__setup) &nbsp;&nbsp; [\_table\_\_sort\_data](#_Table__sort_data) &nbsp;&nbsp; [\_table\_\_sync\_selection](#_Table__sync_selection) &nbsp;&nbsp; [\_table\_\_sync\_selection\_for\_multiple\_or\_extended\_mode](#_Table__sync_selection_for_multiple_or_extended_mode) &nbsp;&nbsp; [\_table\_\_sync\_selection\_for\_single\_or\_browse\_mode](#_Table__sync_selection_for_single_or_browse_mode) &nbsp;&nbsp; [\_table\_\_table\_sorter](#_Table__table_sorter) &nbsp;&nbsp; [\_table\_\_update\_sorting](#_Table__update_sorting) &nbsp;&nbsp; [\_\_init\_\_](#__init__) &nbsp;&nbsp; [\_bind](#_bind) &nbsp;&nbsp; [\_configure](#_configure) &nbsp;&nbsp; [\_displayof](#_displayof) &nbsp;&nbsp; [\_do](#_do) &nbsp;&nbsp; [\_getboolean](#_getboolean) &nbsp;&nbsp; [\_getconfigure](#_getconfigure) &nbsp;&nbsp; [\_getconfigure1](#_getconfigure1) &nbsp;&nbsp; [\_getdoubles](#_getdoubles) &nbsp;&nbsp; [\_getints](#_getints) &nbsp;&nbsp; [\_grid\_configure](#_grid_configure) &nbsp;&nbsp; [\_gridconvvalue](#_gridconvvalue) &nbsp;&nbsp; [\_nametowidget](#_nametowidget) &nbsp;&nbsp; [\_options](#_options) &nbsp;&nbsp; [\_register](#_register) &nbsp;&nbsp; [\_report\_exception](#_report_exception) &nbsp;&nbsp; [\_root](#_root) &nbsp;&nbsp; [\_setup](#_setup) &nbsp;&nbsp; [\_substitute](#_substitute) &nbsp;&nbsp; [after](#after) &nbsp;&nbsp; [after\_cancel](#after_cancel) &nbsp;&nbsp; [after\_idle](#after_idle) &nbsp;&nbsp; [anchor](#anchor) &nbsp;&nbsp; [bbox](#bbox) &nbsp;&nbsp; [bell](#bell) &nbsp;&nbsp; [bind](#bind) &nbsp;&nbsp; [bind\_all](#bind_all) &nbsp;&nbsp; [bind\_class](#bind_class) &nbsp;&nbsp; [bindtags](#bindtags) &nbsp;&nbsp; [cget](#cget) &nbsp;&nbsp; [cget\_column](#cget_column) &nbsp;&nbsp; [clear](#clear) &nbsp;&nbsp; [clipboard\_append](#clipboard_append) &nbsp;&nbsp; [clipboard\_clear](#clipboard_clear) &nbsp;&nbsp; [clipboard\_get](#clipboard_get) &nbsp;&nbsp; [columnconfigure](#columnconfigure) &nbsp;&nbsp; [config](#config) &nbsp;&nbsp; [config\_column](#config_column) &nbsp;&nbsp; [configure](#configure) &nbsp;&nbsp; [delete](#delete) &nbsp;&nbsp; [deletecommand](#deletecommand) &nbsp;&nbsp; [destroy](#destroy) &nbsp;&nbsp; [event\_add](#event_add) &nbsp;&nbsp; [event\_delete](#event_delete) &nbsp;&nbsp; [event\_generate](#event_generate) &nbsp;&nbsp; [event\_info](#event_info) &nbsp;&nbsp; [fill](#fill) &nbsp;&nbsp; [focus](#focus) &nbsp;&nbsp; [focus\_displayof](#focus_displayof) &nbsp;&nbsp; [focus\_force](#focus_force) &nbsp;&nbsp; [focus\_get](#focus_get) &nbsp;&nbsp; [focus\_lastfor](#focus_lastfor) &nbsp;&nbsp; [focus\_set](#focus_set) &nbsp;&nbsp; [forget](#forget) &nbsp;&nbsp; [get](#get) &nbsp;&nbsp; [getboolean](#getboolean) &nbsp;&nbsp; [getdouble](#getdouble) &nbsp;&nbsp; [getint](#getint) &nbsp;&nbsp; [getvar](#getvar) &nbsp;&nbsp; [grab\_current](#grab_current) &nbsp;&nbsp; [grab\_release](#grab_release) &nbsp;&nbsp; [grab\_set](#grab_set) &nbsp;&nbsp; [grab\_set\_global](#grab_set_global) &nbsp;&nbsp; [grab\_status](#grab_status) &nbsp;&nbsp; [grid](#grid) &nbsp;&nbsp; [grid\_anchor](#grid_anchor) &nbsp;&nbsp; [grid\_bbox](#grid_bbox) &nbsp;&nbsp; [grid\_columnconfigure](#grid_columnconfigure) &nbsp;&nbsp; [grid\_configure](#grid_configure) &nbsp;&nbsp; [grid\_forget](#grid_forget) &nbsp;&nbsp; [grid\_info](#grid_info) &nbsp;&nbsp; [grid\_location](#grid_location) &nbsp;&nbsp; [grid\_propagate](#grid_propagate) &nbsp;&nbsp; [grid\_remove](#grid_remove) &nbsp;&nbsp; [grid\_rowconfigure](#grid_rowconfigure) &nbsp;&nbsp; [grid\_size](#grid_size) &nbsp;&nbsp; [grid\_slaves](#grid_slaves) &nbsp;&nbsp; [handle\_row\_event](#handle_row_event) &nbsp;&nbsp; [handle\_row\_selected](#handle_row_selected) &nbsp;&nbsp; [image\_names](#image_names) &nbsp;&nbsp; [image\_types](#image_types) &nbsp;&nbsp; [info](#info) &nbsp;&nbsp; [insert](#insert) &nbsp;&nbsp; [keys](#keys) &nbsp;&nbsp; [lift](#lift) &nbsp;&nbsp; [location](#location) &nbsp;&nbsp; [lower](#lower) &nbsp;&nbsp; [mainloop](#mainloop) &nbsp;&nbsp; [nametowidget](#nametowidget) &nbsp;&nbsp; [option\_add](#option_add) &nbsp;&nbsp; [option\_clear](#option_clear) &nbsp;&nbsp; [option\_get](#option_get) &nbsp;&nbsp; [option\_readfile](#option_readfile) &nbsp;&nbsp; [pack](#pack) &nbsp;&nbsp; [pack\_configure](#pack_configure) &nbsp;&nbsp; [pack\_forget](#pack_forget) &nbsp;&nbsp; [pack\_info](#pack_info) &nbsp;&nbsp; [pack\_propagate](#pack_propagate) &nbsp;&nbsp; [pack\_slaves](#pack_slaves) &nbsp;&nbsp; [place](#place) &nbsp;&nbsp; [place\_configure](#place_configure) &nbsp;&nbsp; [place\_forget](#place_forget) &nbsp;&nbsp; [place\_info](#place_info) &nbsp;&nbsp; [place\_slaves](#place_slaves) &nbsp;&nbsp; [propagate](#propagate) &nbsp;&nbsp; [quit](#quit) &nbsp;&nbsp; [register](#register) &nbsp;&nbsp; [rowconfigure](#rowconfigure) &nbsp;&nbsp; [see](#see) &nbsp;&nbsp; [selection\_clear](#selection_clear) &nbsp;&nbsp; [selection\_get](#selection_get) &nbsp;&nbsp; [selection\_handle](#selection_handle) &nbsp;&nbsp; [selection\_own](#selection_own) &nbsp;&nbsp; [selection\_own\_get](#selection_own_get) &nbsp;&nbsp; [send](#send) &nbsp;&nbsp; [setvar](#setvar) &nbsp;&nbsp; [size](#size) &nbsp;&nbsp; [slaves](#slaves) &nbsp;&nbsp; [tk\_bisque](#tk_bisque) &nbsp;&nbsp; [tk\_focusfollowsmouse](#tk_focusFollowsMouse) &nbsp;&nbsp; [tk\_focusnext](#tk_focusNext) &nbsp;&nbsp; [tk\_focusprev](#tk_focusPrev) &nbsp;&nbsp; [tk\_setpalette](#tk_setPalette) &nbsp;&nbsp; [tk\_strictmotif](#tk_strictMotif) &nbsp;&nbsp; [tkraise](#tkraise) &nbsp;&nbsp; [unbind](#unbind) &nbsp;&nbsp; [unbind\_all](#unbind_all) &nbsp;&nbsp; [unbind\_class](#unbind_class) &nbsp;&nbsp; [update](#update) &nbsp;&nbsp; [update\_idletasks](#update_idletasks) &nbsp;&nbsp; [wait\_variable](#wait_variable) &nbsp;&nbsp; [wait\_visibility](#wait_visibility) &nbsp;&nbsp; [wait\_window](#wait_window) &nbsp;&nbsp; [waitvar](#waitvar) &nbsp;&nbsp; [winfo\_atom](#winfo_atom) &nbsp;&nbsp; [winfo\_atomname](#winfo_atomname) &nbsp;&nbsp; [winfo\_cells](#winfo_cells) &nbsp;&nbsp; [winfo\_children](#winfo_children) &nbsp;&nbsp; [winfo\_class](#winfo_class) &nbsp;&nbsp; [winfo\_colormapfull](#winfo_colormapfull) &nbsp;&nbsp; [winfo\_containing](#winfo_containing) &nbsp;&nbsp; [winfo\_depth](#winfo_depth) &nbsp;&nbsp; [winfo\_exists](#winfo_exists) &nbsp;&nbsp; [winfo\_fpixels](#winfo_fpixels) &nbsp;&nbsp; [winfo\_geometry](#winfo_geometry) &nbsp;&nbsp; [winfo\_height](#winfo_height) &nbsp;&nbsp; [winfo\_id](#winfo_id) &nbsp;&nbsp; [winfo\_interps](#winfo_interps) &nbsp;&nbsp; [winfo\_ismapped](#winfo_ismapped) &nbsp;&nbsp; [winfo\_manager](#winfo_manager) &nbsp;&nbsp; [winfo\_name](#winfo_name) &nbsp;&nbsp; [winfo\_parent](#winfo_parent) &nbsp;&nbsp; [winfo\_pathname](#winfo_pathname) &nbsp;&nbsp; [winfo\_pixels](#winfo_pixels) &nbsp;&nbsp; [winfo\_pointerx](#winfo_pointerx) &nbsp;&nbsp; [winfo\_pointerxy](#winfo_pointerxy) &nbsp;&nbsp; [winfo\_pointery](#winfo_pointery) &nbsp;&nbsp; [winfo\_reqheight](#winfo_reqheight) &nbsp;&nbsp; [winfo\_reqwidth](#winfo_reqwidth) &nbsp;&nbsp; [winfo\_rgb](#winfo_rgb) &nbsp;&nbsp; [winfo\_rootx](#winfo_rootx) &nbsp;&nbsp; [winfo\_rooty](#winfo_rooty) &nbsp;&nbsp; [winfo\_screen](#winfo_screen) &nbsp;&nbsp; [winfo\_screencells](#winfo_screencells) &nbsp;&nbsp; [winfo\_screendepth](#winfo_screendepth) &nbsp;&nbsp; [winfo\_screenheight](#winfo_screenheight) &nbsp;&nbsp; [winfo\_screenmmheight](#winfo_screenmmheight) &nbsp;&nbsp; [winfo\_screenmmwidth](#winfo_screenmmwidth) &nbsp;&nbsp; [winfo\_screenvisual](#winfo_screenvisual) &nbsp;&nbsp; [winfo\_screenwidth](#winfo_screenwidth) &nbsp;&nbsp; [winfo\_server](#winfo_server) &nbsp;&nbsp; [winfo\_toplevel](#winfo_toplevel) &nbsp;&nbsp; [winfo\_viewable](#winfo_viewable) &nbsp;&nbsp; [winfo\_visual](#winfo_visual) &nbsp;&nbsp; [winfo\_visualid](#winfo_visualid) &nbsp;&nbsp; [winfo\_visualsavailable](#winfo_visualsavailable) &nbsp;&nbsp; [winfo\_vrootheight](#winfo_vrootheight) &nbsp;&nbsp; [winfo\_vrootwidth](#winfo_vrootwidth) &nbsp;&nbsp; [winfo\_vrootx](#winfo_vrootx) &nbsp;&nbsp; [winfo\_vrooty](#winfo_vrooty) &nbsp;&nbsp; [winfo\_width](#winfo_width) &nbsp;&nbsp; [winfo\_x](#winfo_x) &nbsp;&nbsp; [winfo\_y](#winfo_y)

## \_Misc\_\_winfo\_getint
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, x)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Misc\_\_winfo\_parseitem
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, t)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_adjust\_selection\_after\_insertion
None



**Signature:** (self, index, len\_data)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_build
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_build\_handler\_for\_row\_event
None



**Signature:** (self, event, handler, i)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_build\_header\_and\_columns
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_build\_table
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_check\_data\_row\_size
None



**Signature:** (self, data)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_extract\_listboxes\_color
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_fix\_selection\_in\_multiple\_selectmode
None



**Signature:** (self, selection)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_insert
None



**Signature:** (self, index, elements)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_manage\_selection\_garbage
None



**Signature:** (self, selection)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_on\_configure\_background
None



**Signature:** (self, event)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_on\_destroy
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_on\_header\_clicked
None



**Signature:** (self, event, i)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_on\_map
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_on\_mouse\_wheel
None



**Signature:** (self, event)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_on\_row\_selected
None



**Signature:** (self, event, column\_index)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_reset\_data
None



**Signature:** (self, data)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_reset\_titles
None



**Signature:** (self, titles)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_scroll\_listboxes\_and\_scrollbar\_sync
None



**Signature:** (self, \*args)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_scroll\_listboxes\_sync
None



**Signature:** (self, \*args)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_set\_scrollbars
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_setup
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_sort\_data
None



**Signature:** (self, i)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_sync\_selection
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_sync\_selection\_for\_multiple\_or\_extended\_mode
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_sync\_selection\_for\_single\_or\_browse\_mode
None



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_table\_sorter
None



**Signature:** (self, data, index, count\_columns, sorting='[+]')





**Return Value:** None.

[Back to Top](#module-overview)


## \_Table\_\_update\_sorting
None



**Signature:** (self, i)





**Return Value:** None.

[Back to Top](#module-overview)


## \_\_init\_\_
PARAMETERS:

- master: widget parent. Example: an instance of tk.Frame

- titles: sequence of titles. Example: ("Name", "Job")

- data: sequence of sequences. Each sub-sequence must have same size as titles.
    Example: ( ("Jack, "Architect"), ("Diana", "Physicist") )

- hidden_columns: sequence of columns to hide.
    Example: (1, 2) will hide the column at the index 1 and 2.
    Example: (0, ) will hide only the first column

- sorting: boolean, set to True if you want the table to be able to do sorting when user
    clicks on a column title. Default: True

- mask: a callable that will be called at each insertion of line of data
in the table.
    The mask must accept 2 arguments:
        - index: int, index of the row (line)
        - data: the sequence of strings to insert at this given row
    The mask must returns a new data with same length or the same old data

- select_mode: selection modes: SINGLE, BROWSE,
 MULTIPLE and EXTENDED. Default: SINGLE.
 Selection modes are the same as described in the tk.Listbox's documentation.

- layout: EQUALLY or PROPORTIONALLY. Default: EQUALLY

- orient: orientation for scrollbars. BOTH or VERTICAL or HORIZONTAL

- options: dictionary of widgets options
    The widgets keys are: BODY, VSB, HSB, CANVAS, FRAME_BACKGROUND,
    FRAMES_HEADERS, LISTBOXES_COLUMNS, LABELS_SORTING and LABELS_TITLES.
    Example: Assume that you want to set the BODY's background to black
    and the horizontal scrollbar's background to red:
        options = {"BODY": {"background": "red"},
                   "HSB": {"background": "black"}}



**Signature:** (self, master=None, titles=None, data=None, hidden\_columns=None, sorting=True, mask=None, select\_mode='browse', layout='equally', orient='both', megaconfig=None)





**Return Value:** None.

[Back to Top](#module-overview)


## \_bind
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, what, sequence, func, add, needcleanup=1)





**Return Value:** None.

[Back to Top](#module-overview)


## \_configure
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, cmd, cnf, kw)





**Return Value:** None.

[Back to Top](#module-overview)


## \_displayof
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, displayof)





**Return Value:** None.

[Back to Top](#module-overview)


## \_do
None

**Inherited from:** tkinter.BaseWidget

**Signature:** (self, name, args=())





**Return Value:** None.

[Back to Top](#module-overview)


## \_getboolean
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, string)





**Return Value:** None.

[Back to Top](#module-overview)


## \_getconfigure
Call Tcl configure command and return the result as a dict.

**Inherited from:** tkinter.Misc

**Signature:** (self, \*args)





**Return Value:** None.

[Back to Top](#module-overview)


## \_getconfigure1
None

**Inherited from:** tkinter.Misc

**Signature:** (self, \*args)





**Return Value:** None.

[Back to Top](#module-overview)


## \_getdoubles
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, string)





**Return Value:** None.

[Back to Top](#module-overview)


## \_getints
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, string)





**Return Value:** None.

[Back to Top](#module-overview)


## \_grid\_configure
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, command, index, cnf, kw)





**Return Value:** None.

[Back to Top](#module-overview)


## \_gridconvvalue
None

**Inherited from:** tkinter.Misc

**Signature:** (self, value)





**Return Value:** None.

[Back to Top](#module-overview)


## \_nametowidget
Return the Tkinter instance of a widget identified by
its Tcl name NAME.

**Inherited from:** tkinter.Misc

**Signature:** (self, name)





**Return Value:** None.

[Back to Top](#module-overview)


## \_options
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, cnf, kw=None)





**Return Value:** None.

[Back to Top](#module-overview)


## \_register
Return a newly created Tcl function. If this
function is called, the Python function FUNC will
be executed. An optional function SUBST can
be given which will be executed before FUNC.

**Inherited from:** tkinter.Misc

**Signature:** (self, func, subst=None, needcleanup=1)





**Return Value:** None.

[Back to Top](#module-overview)


## \_report\_exception
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_root
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## \_setup
Internal function. Sets up information about children.

**Inherited from:** tkinter.BaseWidget

**Signature:** (self, master, cnf)





**Return Value:** None.

[Back to Top](#module-overview)


## \_substitute
Internal function.

**Inherited from:** tkinter.Misc

**Signature:** (self, \*args)





**Return Value:** None.

[Back to Top](#module-overview)


## after
Call function once after given time.

MS specifies the time in milliseconds. FUNC gives the
function which shall be called. Additional parameters
are given as parameters to the function call.  Return
identifier to cancel scheduling with after_cancel.

**Inherited from:** tkinter.Misc

**Signature:** (self, ms, func=None, \*args)





**Return Value:** None.

[Back to Top](#module-overview)


## after\_cancel
Cancel scheduling of function identified with ID.

Identifier returned by after or after_idle must be
given as first parameter.

**Inherited from:** tkinter.Misc

**Signature:** (self, id)





**Return Value:** None.

[Back to Top](#module-overview)


## after\_idle
Call FUNC once if the Tcl main loop has no event to
process.

Return an identifier to cancel the scheduling with
after_cancel.

**Inherited from:** tkinter.Misc

**Signature:** (self, func, \*args)





**Return Value:** None.

[Back to Top](#module-overview)


## anchor
The anchor value controls how to place the grid within the
master when no row/column has any weight.

The default anchor is nw.

**Inherited from:** tkinter.Misc

**Signature:** (self, anchor=None)





**Return Value:** None.

[Back to Top](#module-overview)


## bbox
Return a tuple of integer coordinates for the bounding
box of this widget controlled by the geometry manager grid.

If COLUMN, ROW is given the bounding box applies from
the cell with row and column 0 to the specified
cell. If COL2 and ROW2 are given the bounding box
starts at that cell.

The returned integers specify the offset of the upper left
corner in the master widget and the width and height.

**Inherited from:** tkinter.Misc

**Signature:** (self, column=None, row=None, col2=None, row2=None)





**Return Value:** None.

[Back to Top](#module-overview)


## bell
Ring a display's bell.

**Inherited from:** tkinter.Misc

**Signature:** (self, displayof=0)





**Return Value:** None.

[Back to Top](#module-overview)


## bind
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

**Inherited from:** tkinter.Misc

**Signature:** (self, sequence=None, func=None, add=None)





**Return Value:** None.

[Back to Top](#module-overview)


## bind\_all
Bind to all widgets at an event SEQUENCE a call to function FUNC.
An additional boolean parameter ADD specifies whether FUNC will
be called additionally to the other bound function or whether
it will replace the previous function. See bind for the return value.

**Inherited from:** tkinter.Misc

**Signature:** (self, sequence=None, func=None, add=None)





**Return Value:** None.

[Back to Top](#module-overview)


## bind\_class
Bind to widgets with bindtag CLASSNAME at event
SEQUENCE a call of function FUNC. An additional
boolean parameter ADD specifies whether FUNC will be
called additionally to the other bound function or
whether it will replace the previous function. See bind for
the return value.

**Inherited from:** tkinter.Misc

**Signature:** (self, className, sequence=None, func=None, add=None)





**Return Value:** None.

[Back to Top](#module-overview)


## bindtags
Set or get the list of bindtags for this widget.

With no argument return the list of all bindtags associated with
this widget. With a list of strings as argument the bindtags are
set to this list. The bindtags determine in which order events are
processed (see bind).

**Inherited from:** tkinter.Misc

**Signature:** (self, tagList=None)





**Return Value:** None.

[Back to Top](#module-overview)


## cget
Return the resource value for a KEY given as string.

**Inherited from:** tkinter.Misc

**Signature:** (self, key)





**Return Value:** None.

[Back to Top](#module-overview)


## cget\_column
If index is None, returns a sequence of options of listboxes (columns).
Else returns the options of the column at the given index



**Signature:** (self, index=None, option='background')





**Return Value:** None.

[Back to Top](#module-overview)


## clear
Clear the table



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## clipboard\_append
Append STRING to the Tk clipboard.

A widget specified at the optional displayof keyword
argument specifies the target display. The clipboard
can be retrieved with selection_get.

**Inherited from:** tkinter.Misc

**Signature:** (self, string, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## clipboard\_clear
Clear the data in the Tk clipboard.

A widget specified for the optional displayof keyword
argument specifies the target display.

**Inherited from:** tkinter.Misc

**Signature:** (self, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## clipboard\_get
Retrieve data from the clipboard on window's display.

The window keyword defaults to the root window of the Tkinter
application.

The type keyword specifies the form in which the data is
to be returned and should be an atom name such as STRING
or FILE_NAME.  Type defaults to STRING, except on X11, where the default
is to try UTF8_STRING and fall back to STRING.

This command is equivalent to:

selection_get(CLIPBOARD)

**Inherited from:** tkinter.Misc

**Signature:** (self, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## columnconfigure
Configure column INDEX of a grid.

Valid resources are minsize (minimum size of the column),
weight (how much does additional space propagate to this column)
and pad (how much space to let additionally).

**Inherited from:** tkinter.Misc

**Signature:** (self, index, cnf={}, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## config
Configure resources of a widget.

The values for resources are specified as keyword
arguments. To get an overview about
the allowed keyword arguments call the method keys.

**Inherited from:** tkinter.Misc

**Signature:** (self, cnf=None, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## config\_column
Configure column. If index is None, all columns will be configured



**Signature:** (self, index=None, \*\*options)





**Return Value:** None.

[Back to Top](#module-overview)


## configure
Configure resources of a widget.

The values for resources are specified as keyword
arguments. To get an overview about
the allowed keyword arguments call the method keys.

**Inherited from:** tkinter.Misc

**Signature:** (self, cnf=None, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## delete
Deletes lines (rows) from the table



**Signature:** (self, index\_start, index\_end=None)





**Return Value:** None.

[Back to Top](#module-overview)


## deletecommand
Internal function.

Delete the Tcl command provided in NAME.

**Inherited from:** tkinter.Misc

**Signature:** (self, name)





**Return Value:** None.

[Back to Top](#module-overview)


## destroy
Destroy this and all descendants widgets.

**Inherited from:** tkinter.BaseWidget

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## event\_add
Bind a virtual event VIRTUAL (of the form <<Name>>)
to an event SEQUENCE such that the virtual event is triggered
whenever SEQUENCE occurs.

**Inherited from:** tkinter.Misc

**Signature:** (self, virtual, \*sequences)





**Return Value:** None.

[Back to Top](#module-overview)


## event\_delete
Unbind a virtual event VIRTUAL from SEQUENCE.

**Inherited from:** tkinter.Misc

**Signature:** (self, virtual, \*sequences)





**Return Value:** None.

[Back to Top](#module-overview)


## event\_generate
Generate an event SEQUENCE. Additional
keyword arguments specify parameter of the event
(e.g. x, y, rootx, rooty).

**Inherited from:** tkinter.Misc

**Signature:** (self, sequence, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## event\_info
Return a list of all virtual events or the information
about the SEQUENCE bound to the virtual event VIRTUAL.

**Inherited from:** tkinter.Misc

**Signature:** (self, virtual=None)





**Return Value:** None.

[Back to Top](#module-overview)


## fill
This will overwrite the titles and/or data with the new given titles or data



**Signature:** (self, titles=None, data=None)





**Return Value:** None.

[Back to Top](#module-overview)


## focus
Direct input focus to this widget.

If the application currently does not have the focus
this widget will get the focus if the application gets
the focus through the window manager.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## focus\_displayof
Return the widget which has currently the focus on the
display where this widget is located.

Return None if the application does not have the focus.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## focus\_force
Direct input focus to this widget even if the
application does not have the focus. Use with
caution!

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## focus\_get
Return the widget which has currently the focus in the
application.

Use focus_displayof to allow working with several
displays. Return None if application does not have
the focus.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## focus\_lastfor
Return the widget which would have the focus if top level
for this widget gets the focus from the window manager.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## focus\_set
Direct input focus to this widget.

If the application currently does not have the focus
this widget will get the focus if the application gets
the focus through the window manager.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## forget
Unmap this widget and do not use it for the packing order.

**Inherited from:** tkinter.Pack

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## get
Returns a line if you don't give a 'index_end'.
Returns a sequence of lines if you give a 'index_end'.



**Signature:** (self, index\_start, index\_end=None)





**Return Value:** None.

[Back to Top](#module-overview)


## getboolean
Return a boolean value for Tcl boolean values true and false given as parameter.

**Inherited from:** tkinter.Misc

**Signature:** (self, s)





**Return Value:** None.

[Back to Top](#module-overview)


## getdouble
None

**Inherited from:** tkinter.Misc

**Signature:** (self, s)





**Return Value:** None.

[Back to Top](#module-overview)


## getint
None

**Inherited from:** tkinter.Misc

**Signature:** (self, s)





**Return Value:** None.

[Back to Top](#module-overview)


## getvar
Return value of Tcl variable NAME.

**Inherited from:** tkinter.Misc

**Signature:** (self, name='PY\_VAR')





**Return Value:** None.

[Back to Top](#module-overview)


## grab\_current
Return widget which has currently the grab in this application
or None.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## grab\_release
Release grab for this widget if currently set.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## grab\_set
Set grab for this widget.

A grab directs all events to this and descendant
widgets in the application.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## grab\_set\_global
Set global grab for this widget.

A global grab directs all events to this and
descendant widgets on the display. Use with caution -
other applications do not get events anymore.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## grab\_status
Return None, "local" or "global" if this widget has
no, a local or a global grab.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## grid
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

**Inherited from:** tkinter.Grid

**Signature:** (self, cnf={}, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_anchor
The anchor value controls how to place the grid within the
master when no row/column has any weight.

The default anchor is nw.

**Inherited from:** tkinter.Misc

**Signature:** (self, anchor=None)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_bbox
Return a tuple of integer coordinates for the bounding
box of this widget controlled by the geometry manager grid.

If COLUMN, ROW is given the bounding box applies from
the cell with row and column 0 to the specified
cell. If COL2 and ROW2 are given the bounding box
starts at that cell.

The returned integers specify the offset of the upper left
corner in the master widget and the width and height.

**Inherited from:** tkinter.Misc

**Signature:** (self, column=None, row=None, col2=None, row2=None)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_columnconfigure
Configure column INDEX of a grid.

Valid resources are minsize (minimum size of the column),
weight (how much does additional space propagate to this column)
and pad (how much space to let additionally).

**Inherited from:** tkinter.Misc

**Signature:** (self, index, cnf={}, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_configure
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

**Inherited from:** tkinter.Grid

**Signature:** (self, cnf={}, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_forget
Unmap this widget.

**Inherited from:** tkinter.Grid

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_info
Return information about the options
for positioning this widget in a grid.

**Inherited from:** tkinter.Grid

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_location
Return a tuple of column and row which identify the cell
at which the pixel at position X and Y inside the master
widget is located.

**Inherited from:** tkinter.Misc

**Signature:** (self, x, y)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_propagate
Set or get the status for propagation of geometry information.

A boolean argument specifies whether the geometry information
of the slaves will determine the size of this widget. If no argument
is given, the current setting will be returned.

**Inherited from:** tkinter.Misc

**Signature:** (self, flag=['\_noarg\_'])





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_remove
Unmap this widget but remember the grid options.

**Inherited from:** tkinter.Grid

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_rowconfigure
Configure row INDEX of a grid.

Valid resources are minsize (minimum size of the row),
weight (how much does additional space propagate to this row)
and pad (how much space to let additionally).

**Inherited from:** tkinter.Misc

**Signature:** (self, index, cnf={}, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_size
Return a tuple of the number of column and rows in the grid.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## grid\_slaves
Return a list of all slaves of this widget
in its packing order.

**Inherited from:** tkinter.Misc

**Signature:** (self, row=None, column=None)





**Return Value:** None.

[Back to Top](#module-overview)


## handle\_row\_event
This callback will be called at a specific row event (sequence = string):
    handler(table, row_data, row_index, column_index)



**Signature:** (self, sequence, handler)





**Return Value:** None.

[Back to Top](#module-overview)


## handle\_row\_selected
This callback will be called at the event 'row selection':
    handler(table, row_data, row_index, column_index)



**Signature:** (self, handler)





**Return Value:** None.

[Back to Top](#module-overview)


## image\_names
Return a list of all existing image names.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## image\_types
Return a list of all available image types (e.g. photo bitmap).

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## info
Return information about the packing options
for this widget.

**Inherited from:** tkinter.Pack

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## insert
Insert into the table this data at this index.
Index is an integer or the string "end" (meaning, put the data at the end of table).
This method doesn't wipe the previous data stored at this index but instead,
pull that data down.

data is a sequence of sequences of strings.

Example:
Assume you want to push the new line ("Matrix", "Cameraman") at index 0.
    insert(0, [("Matrix", "Cameraman")])
Assume you want to push ("Matrix", "Cameraman") and ("Diana", "Seller")
at index "end".
    insert("end", [("Matrix", "Cameraman"), ("Diana", "Seller")])



**Signature:** (self, index, data)





**Return Value:** None.

[Back to Top](#module-overview)


## keys
Return a list of all resource names of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## lift
Raise this widget in the stacking order.

**Inherited from:** tkinter.Misc

**Signature:** (self, aboveThis=None)





**Return Value:** None.

[Back to Top](#module-overview)


## location
Return a tuple of column and row which identify the cell
at which the pixel at position X and Y inside the master
widget is located.

**Inherited from:** tkinter.Grid

**Signature:** (self, x, y)





**Return Value:** None.

[Back to Top](#module-overview)


## lower
Lower this widget in the stacking order.

**Inherited from:** tkinter.Misc

**Signature:** (self, belowThis=None)





**Return Value:** None.

[Back to Top](#module-overview)


## mainloop
Call the mainloop of Tk.

**Inherited from:** tkinter.Misc

**Signature:** (self, n=0)





**Return Value:** None.

[Back to Top](#module-overview)


## nametowidget
Return the Tkinter instance of a widget identified by
its Tcl name NAME.

**Inherited from:** tkinter.Misc

**Signature:** (self, name)





**Return Value:** None.

[Back to Top](#module-overview)


## option\_add
Set a VALUE (second parameter) for an option
PATTERN (first parameter).

An optional third parameter gives the numeric priority
(defaults to 80).

**Inherited from:** tkinter.Misc

**Signature:** (self, pattern, value, priority=None)





**Return Value:** None.

[Back to Top](#module-overview)


## option\_clear
Clear the option database.

It will be reloaded if option_add is called.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## option\_get
Return the value for an option NAME for this widget
with CLASSNAME.

Values with higher priority override lower values.

**Inherited from:** tkinter.Misc

**Signature:** (self, name, className)





**Return Value:** None.

[Back to Top](#module-overview)


## option\_readfile
Read file FILENAME into the option database.

An optional second parameter gives the numeric
priority.

**Inherited from:** tkinter.Misc

**Signature:** (self, fileName, priority=None)





**Return Value:** None.

[Back to Top](#module-overview)


## pack
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

**Inherited from:** tkinter.Pack

**Signature:** (self, cnf={}, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## pack\_configure
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

**Inherited from:** tkinter.Pack

**Signature:** (self, cnf={}, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## pack\_forget
Unmap this widget and do not use it for the packing order.

**Inherited from:** tkinter.Pack

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## pack\_info
Return information about the packing options
for this widget.

**Inherited from:** tkinter.Pack

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## pack\_propagate
Set or get the status for propagation of geometry information.

A boolean argument specifies whether the geometry information
of the slaves will determine the size of this widget. If no argument
is given the current setting will be returned.

**Inherited from:** tkinter.Misc

**Signature:** (self, flag=['\_noarg\_'])





**Return Value:** None.

[Back to Top](#module-overview)


## pack\_slaves
Return a list of all slaves of this widget
in its packing order.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## place
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

**Inherited from:** tkinter.Place

**Signature:** (self, cnf={}, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## place\_configure
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

**Inherited from:** tkinter.Place

**Signature:** (self, cnf={}, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## place\_forget
Unmap this widget.

**Inherited from:** tkinter.Place

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## place\_info
Return information about the placing options
for this widget.

**Inherited from:** tkinter.Place

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## place\_slaves
Return a list of all slaves of this widget
in its packing order.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## propagate
Set or get the status for propagation of geometry information.

A boolean argument specifies whether the geometry information
of the slaves will determine the size of this widget. If no argument
is given the current setting will be returned.

**Inherited from:** tkinter.Misc

**Signature:** (self, flag=['\_noarg\_'])





**Return Value:** None.

[Back to Top](#module-overview)


## quit
Quit the Tcl interpreter. All widgets will be destroyed.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## register
Return a newly created Tcl function. If this
function is called, the Python function FUNC will
be executed. An optional function SUBST can
be given which will be executed before FUNC.

**Inherited from:** tkinter.Misc

**Signature:** (self, func, subst=None, needcleanup=1)





**Return Value:** None.

[Back to Top](#module-overview)


## rowconfigure
Configure row INDEX of a grid.

Valid resources are minsize (minimum size of the row),
weight (how much does additional space propagate to this row)
and pad (how much space to let additionally).

**Inherited from:** tkinter.Misc

**Signature:** (self, index, cnf={}, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## see
The table will scroll to the given index



**Signature:** (self, index='end')





**Return Value:** None.

[Back to Top](#module-overview)


## selection\_clear
Clear the current X selection.

**Inherited from:** tkinter.Misc

**Signature:** (self, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## selection\_get
Return the contents of the current X selection.

A keyword parameter selection specifies the name of
the selection and defaults to PRIMARY.  A keyword
parameter displayof specifies a widget on the display
to use. A keyword parameter type specifies the form of data to be
fetched, defaulting to STRING except on X11, where UTF8_STRING is tried
before STRING.

**Inherited from:** tkinter.Misc

**Signature:** (self, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## selection\_handle
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

**Inherited from:** tkinter.Misc

**Signature:** (self, command, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## selection\_own
Become owner of X selection.

A keyword parameter selection specifies the name of
the selection (default PRIMARY).

**Inherited from:** tkinter.Misc

**Signature:** (self, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## selection\_own\_get
Return owner of X selection.

The following keyword parameter can
be provided:
selection - name of the selection (default PRIMARY),
type - type of the selection (e.g. STRING, FILE_NAME).

**Inherited from:** tkinter.Misc

**Signature:** (self, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## send
Send Tcl command CMD to different interpreter INTERP to be executed.

**Inherited from:** tkinter.Misc

**Signature:** (self, interp, cmd, \*args)





**Return Value:** None.

[Back to Top](#module-overview)


## setvar
Set Tcl variable NAME to VALUE.

**Inherited from:** tkinter.Misc

**Signature:** (self, name='PY\_VAR', value='1')





**Return Value:** None.

[Back to Top](#module-overview)


## size
Return a tuple of the number of column and rows in the grid.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## slaves
Return a list of all slaves of this widget
in its packing order.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## tk\_bisque
Change the color scheme to light brown as used in Tk 3.6 and before.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## tk\_focusFollowsMouse
The widget under mouse will get automatically focus. Can not
be disabled easily.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## tk\_focusNext
Return the next widget in the focus order which follows
widget which has currently the focus.

The focus order first goes to the next child, then to
the children of the child recursively and then to the
next sibling which is higher in the stacking order.  A
widget is omitted if it has the takefocus resource set
to 0.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## tk\_focusPrev
Return previous widget in the focus order. See tk_focusNext for details.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## tk\_setPalette
Set a new color scheme for all widget elements.

A single color as argument will cause that all colors of Tk
widget elements are derived from this.
Alternatively several keyword parameters and its associated
colors can be given. The following keywords are valid:
activeBackground, foreground, selectColor,
activeForeground, highlightBackground, selectBackground,
background, highlightColor, selectForeground,
disabledForeground, insertBackground, troughColor.

**Inherited from:** tkinter.Misc

**Signature:** (self, \*args, \*\*kw)





**Return Value:** None.

[Back to Top](#module-overview)


## tk\_strictMotif
Set Tcl internal variable, whether the look and feel
should adhere to Motif.

A parameter of 1 means adhere to Motif (e.g. no color
change if mouse passes over slider).
Returns the set value.

**Inherited from:** tkinter.Misc

**Signature:** (self, boolean=None)





**Return Value:** None.

[Back to Top](#module-overview)


## tkraise
Raise this widget in the stacking order.

**Inherited from:** tkinter.Misc

**Signature:** (self, aboveThis=None)





**Return Value:** None.

[Back to Top](#module-overview)


## unbind
Unbind for this widget for event SEQUENCE  the
function identified with FUNCID.

**Inherited from:** tkinter.Misc

**Signature:** (self, sequence, funcid=None)





**Return Value:** None.

[Back to Top](#module-overview)


## unbind\_all
Unbind for all widgets for event SEQUENCE all functions.

**Inherited from:** tkinter.Misc

**Signature:** (self, sequence)





**Return Value:** None.

[Back to Top](#module-overview)


## unbind\_class
Unbind for all widgets with bindtag CLASSNAME for event SEQUENCE
all functions.

**Inherited from:** tkinter.Misc

**Signature:** (self, className, sequence)





**Return Value:** None.

[Back to Top](#module-overview)


## update
Enter event loop until all pending events have been processed by Tcl.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## update\_idletasks
Enter event loop until all idle callbacks have been called. This
will update the display of windows but not process events caused by
the user.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## wait\_variable
Wait until the variable is modified.

A parameter of type IntVar, StringVar, DoubleVar or
BooleanVar must be given.

**Inherited from:** tkinter.Misc

**Signature:** (self, name='PY\_VAR')





**Return Value:** None.

[Back to Top](#module-overview)


## wait\_visibility
Wait until the visibility of a WIDGET changes
(e.g. it appears).

If no parameter is given self is used.

**Inherited from:** tkinter.Misc

**Signature:** (self, window=None)





**Return Value:** None.

[Back to Top](#module-overview)


## wait\_window
Wait until a WIDGET is destroyed.

If no parameter is given self is used.

**Inherited from:** tkinter.Misc

**Signature:** (self, window=None)





**Return Value:** None.

[Back to Top](#module-overview)


## waitvar
Wait until the variable is modified.

A parameter of type IntVar, StringVar, DoubleVar or
BooleanVar must be given.

**Inherited from:** tkinter.Misc

**Signature:** (self, name='PY\_VAR')





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_atom
Return integer which represents atom NAME.

**Inherited from:** tkinter.Misc

**Signature:** (self, name, displayof=0)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_atomname
Return name of atom with identifier ID.

**Inherited from:** tkinter.Misc

**Signature:** (self, id, displayof=0)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_cells
Return number of cells in the colormap for this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_children
Return a list of all widgets which are children of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_class
Return window class name of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_colormapfull
Return true if at the last color request the colormap was full.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_containing
Return the widget which is at the root coordinates ROOTX, ROOTY.

**Inherited from:** tkinter.Misc

**Signature:** (self, rootX, rootY, displayof=0)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_depth
Return the number of bits per pixel.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_exists
Return true if this widget exists.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_fpixels
Return the number of pixels for the given distance NUMBER
(e.g. "3c") as float.

**Inherited from:** tkinter.Misc

**Signature:** (self, number)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_geometry
Return geometry string for this widget in the form "widthxheight+X+Y".

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_height
Return height of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_id
Return identifier ID for this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_interps
Return the name of all Tcl interpreters for this display.

**Inherited from:** tkinter.Misc

**Signature:** (self, displayof=0)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_ismapped
Return true if this widget is mapped.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_manager
Return the window manager name for this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_name
Return the name of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_parent
Return the name of the parent of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_pathname
Return the pathname of the widget given by ID.

**Inherited from:** tkinter.Misc

**Signature:** (self, id, displayof=0)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_pixels
Rounded integer value of winfo_fpixels.

**Inherited from:** tkinter.Misc

**Signature:** (self, number)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_pointerx
Return the x coordinate of the pointer on the root window.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_pointerxy
Return a tuple of x and y coordinates of the pointer on the root window.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_pointery
Return the y coordinate of the pointer on the root window.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_reqheight
Return requested height of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_reqwidth
Return requested width of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_rgb
Return tuple of decimal values for red, green, blue for
COLOR in this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self, color)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_rootx
Return x coordinate of upper left corner of this widget on the
root window.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_rooty
Return y coordinate of upper left corner of this widget on the
root window.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_screen
Return the screen name of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_screencells
Return the number of the cells in the colormap of the screen
of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_screendepth
Return the number of bits per pixel of the root window of the
screen of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_screenheight
Return the number of pixels of the height of the screen of this widget
in pixel.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_screenmmheight
Return the number of pixels of the height of the screen of
this widget in mm.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_screenmmwidth
Return the number of pixels of the width of the screen of
this widget in mm.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_screenvisual
Return one of the strings directcolor, grayscale, pseudocolor,
staticcolor, staticgray, or truecolor for the default
colormodel of this screen.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_screenwidth
Return the number of pixels of the width of the screen of
this widget in pixel.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_server
Return information of the X-Server of the screen of this widget in
the form "XmajorRminor vendor vendorVersion".

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_toplevel
Return the toplevel widget of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_viewable
Return true if the widget and all its higher ancestors are mapped.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_visual
Return one of the strings directcolor, grayscale, pseudocolor,
staticcolor, staticgray, or truecolor for the
colormodel of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_visualid
Return the X identifier for the visual for this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_visualsavailable
Return a list of all visuals available for the screen
of this widget.

Each item in the list consists of a visual name (see winfo_visual), a
depth and if includeids is true is given also the X identifier.

**Inherited from:** tkinter.Misc

**Signature:** (self, includeids=False)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_vrootheight
Return the height of the virtual root window associated with this
widget in pixels. If there is no virtual root window return the
height of the screen.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_vrootwidth
Return the width of the virtual root window associated with this
widget in pixel. If there is no virtual root window return the
width of the screen.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_vrootx
Return the x offset of the virtual root relative to the root
window of the screen of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_vrooty
Return the y offset of the virtual root relative to the root
window of the screen of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_width
Return the width of this widget.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_x
Return the x coordinate of the upper left corner of this widget
in the parent.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## winfo\_y
Return the y coordinate of the upper left corner of this widget
in the parent.

**Inherited from:** tkinter.Misc

**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)



