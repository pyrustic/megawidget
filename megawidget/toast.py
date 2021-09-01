import tkinter as tk
from viewable import Viewable, CustomView
from tkutil import merge_megaconfig
import tkutil


# parts
BODY = "body"
LABEL_HEADER = "label_header"
LABEL_MESSAGE = "label_message"


class Toast(tk.Toplevel):
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

    def __init__(self,
                 master=None,
                 title=None,
                 header=None,
                 message=None,
                 duration=1234,
                 decoration=False,
                 geometry=None,
                 megaconfig=None):
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
        self.__megaconfig = merge_megaconfig(secondary=megaconfig)
        super().__init__(master=master,
                         class_="Toast",
                         cnf=self.__megaconfig.get(BODY))
        self.__title = title
        self.__header = header
        self.__message = message
        self.__duration = duration
        self.__decoration = decoration
        self.__geometry = geometry
        self.__cancel_id = None
        self.__parts = {}
        self.__setup()

    # ======================================
    #            PROPERTIES
    # ======================================

    @property
    def header(self):
        return self.__header

    @property
    def message(self):
        return self.__message

    @property
    def duration(self):
        return self.__duration

    @property
    def decoration(self):
        return self.__decoration

    @property
    def parts(self):
        """
        Get the parts (widgets instances) used to build this Toast.

        This property returns a dict. The keys are:
            BODY, LABEL_HEADER, LABEL_MESSAGE,
        """
        return self.__parts

    # ======================================
    #            LIFECYCLE
    # ======================================
    def __setup(self):
        custom_view = CustomView(body=self,
                                 builder=self.__build,
                                 on_map=self.__on_map,
                                 on_destroy=self.__on_destroy)
        return custom_view.build()

    def __build(self):
        if not self.__decoration:
            self.overrideredirect(1)
        if self.__geometry:
            self.geometry(self.__geometry)
        if self.__title:
            self.title(self.__title)
        self.bind("<Button-1>", self.__on_click, "+")
        if self.__header:
            label_header = tk.Label(self,
                                    name=LABEL_HEADER,
                                    text=self.__header,
                                    anchor="w",
                                    justify=tk.LEFT,
                                    cnf=self.__megaconfig.get(LABEL_HEADER))
            self.__parts[LABEL_HEADER] = label_header
            label_header.pack(fill=tk.X, padx=10, pady=10)
        if self.__message:
            label_message = tk.Label(self,
                                     name=LABEL_MESSAGE,
                                     text=self.__message,
                                     anchor="w",
                                     justify=tk.LEFT,
                                     cnf=self.__megaconfig.get(LABEL_MESSAGE))
            self.__parts[LABEL_MESSAGE] = label_message
            label_message.pack(fill=tk.X, padx=10, pady=10)

    def __on_map(self):
        tkutil.center_dialog_effect(self,
                                    within=self.master.winfo_toplevel())
        if self.__duration is not None:
            self.__cancel_id = self.after(self.__duration, self.destroy)

    def __on_destroy(self):
        pass

    def __on_click(self, event):
        self.destroy()


class Error(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ""
        super().__init__(self.message)

    def __str__(self):
        return self.message


class _ToastTest(Viewable):

    def __init__(self, root):
        super().__init__()
        self._root = root
        self._body = None

    def _build(self):
        self._body = tk.Frame(self._root)
        btn_launch = tk.Button(self._body, text="launch",
                               command=self._on_click_launch)
        btn_launch.pack()

    def _on_click_launch(self):
        Toast(self._body, title="Toast Title",
              header="Header", message="This is the message",
              duration=3000)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300+0+0")
    toast_test = _ToastTest(root)
    toast_test.body.pack()
    root.mainloop()
