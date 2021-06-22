import tkinter as tk
from tkinter import filedialog
from viewable import CustomView
from tkutil import merge_cnfs


BODY = "body"
ENTRY = "entry"
BUTTON = "button"
DIALOG = "dialog"


class Pathentry(tk.Frame):
    """
    """
    def __init__(self,
                 master=None,
                 browse="file",
                 width=17,
                 title=None,
                 initialdir=None,
                 cnfs=None):
        """
        - master: widget parent. Example: an instance of tk.Frame

        """
        cache = {ENTRY: {"width": width},
                 DIALOG: {"initialdir": initialdir, "title": title}}
        self.__cnfs = merge_cnfs(cache, cnfs,
                                 components=(BODY, ENTRY, BUTTON, DIALOG))
        super().__init__(master=master,
                         class_="Pathentry",
                         cnf=self.__cnfs[BODY])
        self.__browse = browse
        self.__title = title
        self.__initialdir = initialdir
        self.__entry = None
        self.__button = None
        self.__components = {}
        self.__string_var = tk.StringVar(value="")
        # build
        self.__setup()
    # ==============================================
    #                   PROPERTIES
    # ==============================================
    @property
    def components(self):
        """
        """
        return self.__components

    @property
    def string_var(self):
        return self.__string_var

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, val):
        self.__path = val

    def __setup(self):
        custom_view = CustomView(body=self,
                                 builder=self.__build,
                                 on_map=self.__on_map,
                                 on_destroy=self.__on_destroy)
        return custom_view.build()

    def __build(self):
        self.__entry = tk.Entry(self, textvariable=self.__string_var,
                                cnf=self.__cnfs[ENTRY])
        self.__entry.pack(side=tk.LEFT, pady=0, fill=tk.X, expand=1)
        self.__components["entry"] = self.__entry
        self.__button = tk.Button(self, text="...",
                                  command=self.__on_click_button,
                                  cnf=self.__cnfs[BUTTON])
        self.__button.pack(side=tk.LEFT, padx=(2, 0), fill=tk.Y)
        self.__components["button"] = self.__button

    def __on_map(self):
        pass

    def __on_destroy(self):
        pass

    def __on_click_button(self):
        if self.__browse == "file":
            try:
                filename = filedialog.askopenfilename(**self.__cnfs[DIALOG])
            except Exception as e:
                return
            path = None
            if not filename:
                pass
            elif isinstance(filename, str):
                path = filename
            else:
                path = ";".join(filename)
            if path:
                self.__string_var.set(path)
        else:
            try:
                filename = filedialog.askdirectory(**self.__cnfs[DIALOG])
            except Exception as e:
                return
            path = None
            if not filename:
                pass
            elif isinstance(filename, str):
                path = filename
            else:
                path = ";".join(filename)
            if path:
                self.__string_var.set(path)
        self.__entry.icursor("end")


class Error(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ""
        super().__init__(self.message)

    def __str__(self):
        return self.message


if __name__ == "__main__":
    root = tk.Tk()
    pathentry_test = Pathentry(root, browse="dir",
                               cnfs={"dialog":
                                         {"title": "Hello"}})
    pathentry_test.pack(fill=tk.BOTH, expand=1)
    root.mainloop()
