import tkinter as tk
from tkinter import filedialog
from viewable import CustomView
from tkutil import merge_megaconfig


BODY = "body"
ENTRY = "entry"
BUTTON = "button"
DIALOG = "dialog"


class PathField(tk.Frame):
    """
    """
    def __init__(self,
                 master=None,
                 browse="file",
                 textvariable=None,
                 width=17,
                 title=None,
                 initialdir=None,
                 initialfile=None,
                 mustexist=None,
                 defaultextension=None,
                 filetypes=None,
                 megaconfig=None):
        """
        - master: widget parent. Example: an instance of tk.Frame

        """
        filetypes = filetypes if filetypes else []
        cache = {ENTRY: {"width": width}}
        if browse == "dir":
            cache[DIALOG] = {"initialdir": initialdir, "title": title,
                          "parent": master.winfo_toplevel(),
                          "initialdir": initialdir,
                          "mustexist": mustexist}
        elif browse == "file":
            cache[DIALOG] = {"initialdir": initialdir, "title": title,
                          "parent": master.winfo_toplevel(), "filetypes": filetypes,
                          "initialfile": initialfile,
                          "defaultextension": defaultextension}
        self.__megaconfig = merge_megaconfig(primary=cache, secondary=megaconfig)
        super().__init__(master=master,
                         class_="PathField",
                         cnf=self.__megaconfig.get(BODY))
        self.__browse = browse
        self.__title = title
        self.__initialdir = initialdir
        self.__initialfile = initialfile
        self.__filetypes = filetypes
        self.__defaultextension = defaultextension
        self.__entry = None
        self.__button = None
        self.__parts = {}
        self.__string_var = textvariable if textvariable else tk.StringVar(value="")
        # build
        self.__setup()
    # ==============================================
    #                   PROPERTIES
    # ==============================================
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, val):
        self.__title = val

    @property
    def initialdir(self):
        return self.__initialdir

    @initialdir.setter
    def initialdir(self, val):
        self.__initialdir = val

    @property
    def initialfile(self):
        return self.__initialfile

    @initialfile.setter
    def initialfile(self, val):
        self.__initialfile = val

    @property
    def defaultextension(self):
        return self.__defaultextension

    @defaultextension.setter
    def defaultextension(self, val):
        self.__defaultextension = val

    @property
    def filetypes(self):
        return self.__filetypes

    @filetypes.setter
    def filetypes(self, val):
        self.__filetypes = val

    @property
    def parts(self):
        """
        """
        return self.__parts

    @property
    def path(self):
        return self.__string_var.get()

    @path.setter
    def path(self, val):
        self.__string_var.set(val)

    def __setup(self):
        custom_view = CustomView(body=self,
                                 builder=self.__build,
                                 on_map=self.__on_map,
                                 on_destroy=self.__on_destroy)
        return custom_view.build()

    def __build(self):
        self.__entry = tk.Entry(self, textvariable=self.__string_var,
                                cnf=self.__megaconfig.get(ENTRY))
        self.__entry.pack(side=tk.LEFT, pady=0, fill=tk.X, expand=1)
        self.__parts["entry"] = self.__entry
        self.__button = tk.Button(self, text="...",
                                  command=self.__on_click_button,
                                  pady=0,
                                  cnf=self.__megaconfig.get(BUTTON))
        self.__button.pack(side=tk.LEFT, padx=(1, 0))
        self.__parts["button"] = self.__button

    def __on_map(self):
        pass

    def __on_destroy(self):
        pass

    def __on_click_button(self):
        if self.__browse == "file":
            try:
                filename = filedialog.askopenfilename(**self.__megaconfig.get(DIALOG, dict()))
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
        elif self.__browse == "dir":
            try:
                filename = filedialog.askdirectory(**self.__megaconfig.get(DIALOG, {}))
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
            raise Error("Unknown browse option.")
        self.__entry.icursor("end")


class Error(Exception):
    pass


if __name__ == "__main__":
    root = tk.Tk()
    dialog_config = {"title": "Hello"}
    pathfield_test = PathField(root, browse="file",
                               megaconfig={"dialog": dialog_config})
    pathfield_test.pack(side=tk.RIGHT)
    root.mainloop()
