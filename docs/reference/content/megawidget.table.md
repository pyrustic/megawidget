
Back to [Reference Overview](https://github.com/pyrustic/megawidget/blob/master/docs/reference/README.md)

# megawidget.table



<br>


```python
ASC = "[+]"

BODY = "body"

BOTH = "both"

BROWSE = "browse"

CANVAS = "canvas"

COLUMN_OPTIONS = ['background', 'borderwidth', 'cursor', 'disabledforeground', 'exportselection', 'font', 'foreground', 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'justify', 'relief', 'selectbackground', 'selectborderwidth', 'selectforeground', 'setgrid', 'state', 'takefocus', 'width']

DESC = "[-]"

EQUALLY = "equally"

EXTENDED = "extended"

FRAMES_HEADERS = "frames_headers"

FRAME_BACKGROUND = "frame_background"

HORIZONTAL = "horizontal"

HSB = "hsb"

LABELS_SORTING = "labels_sorting"

LABELS_TITLES = "labels_titles"

LISTBOXES_COLUMNS = "listboxes_columns"

MULTIPLE = "multiple"

PROPORTIONALLY = "proportionally"

SINGLE = "single"

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

class Table:
    """
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
    """

    def __init__(self, master=None, titles=None, data=None, hidden_columns=None, sorting=True, mask=None, select_mode='browse', layout='equally', orient='both', megaconfig=None):
        """
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
        """

    @property
    def data(self):
        """
        
        """

    @data.setter
    def data(self, val):
        """
        Data is a sequence of sequences of strings.
        This property overwrite the existing data.
        Example:
            Assume that the titles are: ("Name", "Age")
            Data: ( ("Jack", 56), ("Jane", 47) )
        """

    @property
    def hidden_columns(self):
        """
        
        """

    @hidden_columns.setter
    def hidden_columns(self, val):
        """
        val: sequence of indexes to hide.
        Warning, even if you want to hide just one index,
        you should put this index into a tuple or list.
        Example: hide the column of index 1: (1, ) or [1]
        """

    @property
    def layout(self):
        """
        
        """

    @property
    def mask(self):
        """
        
        """

    @mask.setter
    def mask(self, val):
        """
        val: a callable that will be called at each insertion of line of data
        in the table.
            The mask must accept 2 arguments:
                - index: int, index of the row (line)
                - data: the sequence of strings to insert at this given row
            The mask must returns a new data with same length or the same old data
        """

    @property
    def orient(self):
        """
        
        """

    @property
    def parts(self):
        """
        Get the parts (widgets instances) used to build this dialog.
        
        This property returns a dict. The keys are:
            BODY, VSB, HSB, CANVAS, FRAME_BACKGROUND,
            FRAMES_HEADERS, LISTBOXES_COLUMNS, LABELS_SORTING and LABELS_TITLES
        Warning: FRAMES_HEADERS, LABELS_TITLES, LABELS_SORTING
         and LISTBOXES_COLUMNS are sequences of widgets by index
        """

    @property
    def select_mode(self):
        """
        
        """

    @property
    def selection(self):
        """
        Return a sequence of the current selection.
        selection = ( item_1, item_2, ...)
        item_i = {"index": int, "data": data}
        data = a sequence of string representing the row at the index.
        """

    @property
    def table_size(self):
        """
        returns the length of columns and rows: (rows, cols)
        Example:
            Assume that the table has 3 columns and 10 rows,
            this property will return (10, 3)
        """

    @property
    def titles(self):
        """
        
        """

    @titles.setter
    def titles(self, val):
        """
        Titles are a sequence of strings. This property overwrite the existing titles.
        """

    def cget_column(self, index=None, option='background'):
        """
        If index is None, returns a sequence of options of listboxes (columns).
        Else returns the options of the column at the given index
        """

    def clear(self):
        """
        Clear the table
        """

    def config_column(self, index=None, **options):
        """
        Configure column. If index is None, all columns will be configured
        """

    def delete(self, index_start, index_end=None):
        """
        Deletes lines (rows) from the table
        """

    def fill(self, titles=None, data=None):
        """
        This will overwrite the titles and/or data with the new given titles or data
        """

    def get(self, index_start, index_end=None):
        """
        Returns a line if you don't give a 'index_end'.
        Returns a sequence of lines if you give a 'index_end'.
        """

    def handle_row_event(self, sequence, handler):
        """
        This callback will be called at a specific row event (sequence = string):
            handler(table, row_data, row_index, column_index)
        """

    def handle_row_selected(self, handler):
        """
        This callback will be called at the event 'row selection':
            handler(table, row_data, row_index, column_index)
        """

    def insert(self, index, data):
        """
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
        """

    def see(self, index='end'):
        """
        The table will scroll to the given index
        """

```

