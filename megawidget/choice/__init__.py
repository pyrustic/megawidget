import tkinter as tk
import tkutil
from megawidget.scrollbox import ScrollBox
from viewable import Viewable, CustomView
from tkutil import merge_megaconfig


# select button flavor
CHECK = "check"  # for checkbutton
RADIO = "radio"  # for radiobutton


# Parts
BODY = "body"
LABEL_HEADER = "label_header"
SCROLLBOX = "scrollbox"
LABEL_MESSAGE = "label_message"
FRAME_PANE = "frame_pane"
FRAME_FOOTER = "frame_footer"
BUTTON_CONTINUE = "button_continue"
BUTTON_CANCEL = "button_cancel"
RADIOBUTTONS = "radiobuttons"
CHECKBUTTONS = "checkbuttons"


class Choice(tk.Frame):
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

    def __init__(self,
                 master=None,
                 items=None,
                 selection=None,
                 flavor="radio",
                 stacking="vertical",
                 on_change=None,
                 megaconfig=None):
        """
        """
        self.__megaconfig = merge_megaconfig(secondary=megaconfig)
        super().__init__(master=master,
                         class_="Choice",
                         cnf=self.__megaconfig.get("body"))
        self.__items = [] if not items else items
        self.__selection = selection
        self.__flavor = flavor
        self.__stacking = stacking
        self.__on_change = on_change
        #
        self.__result = None
        self.__closing_context = "close"
        self.__parts = dict()
        self.__intvar = tk.IntVar()
        self.__intvars = []
        # parts
        self.__parts = {}
        # setup
        self.__setup()

    # ======================================
    #            PROPERTIES
    # ======================================

    @property
    def items(self):
        return tuple(self.__items)

    @property
    def selection(self):
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
        result = None
        if self.__flavor == "radio":
            index = self.__intvar.get()
            result = (index, self.__items[index])
        elif self.__flavor == "check":
            result = []
            for i, intvar in enumerate(self.__intvars):
                is_selected = bool(intvar.get())
                if not is_selected:
                    continue
                cache = (i, self.__items[i])
                result.append(cache)
        return tuple(result)

    @property
    def flavor(self):
        return self.__flavor

    @property
    def stacking(self):
        return self.__stacking

    @property
    def on_change(self):
        return self.__on_change

    @property
    def overview(self):
        result = []
        if self.__flavor == "radio":
            selected_index = self.__intvar.get()
            for i, item in enumerate(self.__items):
                if i == selected_index:
                    cache = (True, item)
                else:
                    cache = (False, item)
                result.append(cache)
        elif self.__flavor == "check":
            for i, intvar in enumerate(self.__intvars):
                is_selected = bool(intvar.get())
                cache = (is_selected, self.__items[i])
                result.append(cache)
        return tuple(result)

    @property
    def parts(self):
        """
        Get the parts (widgets instances) used to build this dialog.

        This property returns a dict. The keys are:
            BODY, LABEL_HEADER, SCROLLBOX, LABEL_MESSAGE,
            FRAME_PANE, FRAME_FOOTER, BUTTON_CONTINUE, BUTTON_CANCEL,
            RADIOBUTTONS, CHECKBUTTONS.

        Warning: radiobuttons and checkbuttons are sequences of widgets positioned
        in the sequence according to the index.

        Another Warning: check the presence of key before usage.
        """
        return self.__parts.copy()

    # ======================================
    #            INTERNAL
    # ======================================
    def __setup(self):
        custom_view = CustomView(body=self,
                                 builder=self.__build,
                                 on_map=self.__on_map,
                                 on_destroy=self.__on_destroy)
        custom_view.build()
        self.__populate()

    def __build(self):
        # install and populate check/radio buttons
        key = RADIOBUTTONS if self.__flavor == "radio" else CHECKBUTTONS
        self.__parts[key] = []
        cache = None
        command = (lambda self=self:
                   self.__on_change(self)
                   if self.__on_change else None)
        for i, choice in enumerate(self.__items):
            if not self.__flavor or self.__flavor not in ("radio", "check"):
                break
            if self.__flavor == "radio":
                cache = tk.Radiobutton(self,
                                       variable=self.__intvar,
                                       text=choice, value=i,
                                       command=command,
                                       cnf=self.__megaconfig.get(RADIOBUTTONS))
                self.__parts[RADIOBUTTONS].append(cache)
            elif self.__flavor == "check":
                tk_var = tk.IntVar()
                self.__intvars.append(tk_var)
                cache = tk.Checkbutton(self,
                                       variable=tk_var,
                                       onvalue=1, offvalue=0,
                                       text=choice,
                                       command=command,
                                       cnf=self.__megaconfig.get(CHECKBUTTONS))
                self.__parts[CHECKBUTTONS].append(cache)
            if cache:
                if self.__stacking == "horizontal":
                    cache.pack(side=tk.LEFT)
                elif self.__stacking == "vertical":
                    cache.pack(side=tk.TOP, anchor="w")
                else:
                    raise Error("Unknown stacking value")
                #cache.pack(anchor="w", expand=1)

    def __on_map(self):
        pass

    def __on_destroy(self):
        pass

    def __populate(self):
        # fill selected items
        if self.__flavor == RADIO and self.__selection is not None:
            if isinstance(self.__selection, int) and self.__selection >= 0:
                self.__intvar.set(self.__selection)
        elif self.__flavor == CHECK and self.__selection is not None:
            if isinstance(self.__selection, tuple):
                for i in self.__selection:
                    try:
                        self.__intvars[i].set(1)
                    except IndexError:
                        pass
            elif isinstance(self.__selection, int):
                self.__intvars[self.__selection].set(1)


class ChoiceDialog(tk.Toplevel):
    def __init__(self,
                 master=None,
                 title=None,
                 header=None,
                 message=None,
                 items=None,
                 selection=None,
                 flavor="radio",
                 on_close=None,
                 geometry=None,
                 megaconfig=None):
        """
        """
        self.__megaconfig = merge_megaconfig(secondary=megaconfig)
        super().__init__(master=master,
                         class_="ChoiceDialog",
                         cnf=self.__megaconfig.get(BODY))
        self.__title = title
        self.__header = header
        self.__message = message
        self.__on_close = on_close
        self.__geometry = geometry
        self.__items = items
        self.__selection = selection
        self.__flavor = flavor
        self.__choice = None
        self.__parts = {}
        # build
        self.__setup()

    # ====================================
    #           PROPERTIES
    # ====================================

    @property
    def header(self):
        return self.__header

    @property
    def message(self):
        return self.__message

    @property
    def on_close(self):
        return self.__on_close

    @property
    def choice(self):
        """
        """
        return self.__choice

    @property
    def parts(self):
        """
        Get the parts (widgets instances) used to build this dialog.

        This property returns a dict. The keys are:
            BODY, LABEL_HEADER,
            LABEL_MESSAGE, FRAME_FOOTER, BUTTON_CANCEL, BUTTON_CONFIRM

        Warning: check the presence of key before usage
        """
        return self.__parts

    # ====================================
    #               INTERNAL
    # ====================================
    def __setup(self):
        custom_view = CustomView(body=self,
                                 builder=self.__build,
                                 on_map=self.__on_map,
                                 on_destroy=self.__on_destroy)
        return custom_view.build()

    def __build(self):
        self.title(self.__title)
        self.resizable(0, 0)
        #
        #
        if self.__geometry:
            self.geometry(self.__geometry)
        #
        if self.__header:
            label_header = tk.Label(self,
                                    text=self.__header,
                                    anchor="w",
                                    justify=tk.LEFT,
                                    name=LABEL_HEADER,
                                    cnf=self.__megaconfig.get(LABEL_HEADER))
            self.__parts[LABEL_HEADER] = label_header
            label_header.pack(fill=tk.X, expand=1, anchor="w", pady=5, padx=5)
        #
        if self.__message:
            label_message = tk.Label(self,
                                     name=LABEL_MESSAGE,
                                     text=self.__message,
                                     anchor="w",
                                     justify=tk.LEFT,
                                     cnf=self.__megaconfig.get(LABEL_MESSAGE))
            self.__parts[LABEL_MESSAGE] = label_message
            label_message.pack(fill=tk.X, padx=5, pady=5)
        # choice frame
        self.__choice = Choice(self, items=self.__items,
                               selection=self.__selection,
                               flavor=self.__flavor,
                               megaconfig=self.__megaconfig.get("choice"))
        self.__choice.pack(fill=tk.BOTH, expand=1, padx=5, pady=(5, 10))
        #
        frame_footer = tk.Frame(self, cnf=self.__megaconfig.get(FRAME_FOOTER))
        self.__parts[FRAME_FOOTER] = frame_footer
        frame_footer.pack(anchor="e", pady=(0, 2), padx=2)
        #
        button_continue = tk.Button(frame_footer,
                                   text="Confirmation",
                                   name=BUTTON_CONTINUE,
                                   command=self.__on_click_confirm,
                                   cnf=self.__megaconfig.get(BUTTON_CONTINUE))
        self.__parts[BUTTON_CONTINUE] = button_continue
        button_continue.pack(side=tk.RIGHT)
        #
        button_cancel = tk.Button(frame_footer,
                                  text="Cancel",
                                  name=BUTTON_CANCEL,
                                  command=self.__on_click_cancel,
                                  cnf=self.__megaconfig.get(BUTTON_CANCEL))
        self.__parts[BUTTON_CANCEL] = button_cancel
        button_cancel.pack(side=tk.RIGHT, padx=(0, 2))

    def __on_map(self):
        tkutil.center_dialog_effect(self,
                                    within=self.master.winfo_toplevel())

    def __on_destroy(self):
        if self.__on_close:
            self.__on_close(self.__choice)

    def __on_click_cancel(self):
        self.__ok = False
        self.destroy()

    def __on_click_confirm(self):
        self.__ok = True
        self.destroy()


class Error(Exception):
    pass


class _ChoiceTest(Viewable):
    def __init__(self, root):
        super().__init__()
        self._root = root
        self._body = None

    def _build(self):
        self._body = tk.Frame(self._root)
        btn_launch_check_choice = tk.Button(self._body,
                                            text="Launch checkbutton choice",
                                            command=self._on_click_btn_check)
        btn_launch_check_choice.pack(side=tk.LEFT, anchor="nw")
        btn_launch_radio_choice = tk.Button(self._body,
                                            text="Launch radiobutton choice",
                                            command=self._on_click_btn_radio)
        btn_launch_radio_choice.pack(side=tk.LEFT, anchor="nw")

    def _on_click_btn_check(self):
        ChoiceDialog(self._body, title="Title", header="header", flavor="check",
                        message="message",
                        items=["first", "second", "third"],
                        selection=1, on_close=self._on_close)

    def _on_click_btn_radio(self):
        ChoiceDialog(self._root,
               title="Title", header="header", flavor="radio",
               message="message",
               items=["first", "second", "third"],
               selection=1, on_close=self._on_close)

    def _on_close(self, choice):
        print("Choice: {}".format(choice.selection))


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300+0+0")
    choice_test = _ChoiceTest(root)
    choice_test.build_pack()
    root.mainloop()
