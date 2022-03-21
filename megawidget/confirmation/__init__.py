import tkinter as tk
import tkutil
from megawidget import error
from viewable import Viewable, implement_lifecycle
from tkutil import merge_megaconfig


# parts
BODY = "body"
LABEL_HEADER = "label_header"
LABEL_MESSAGE = "label_message"
FRAME_FOOTER = "frame_footer"
BUTTON_CANCEL = "button_cancel"
BUTTON_CONFIRM = "button_confirm"


class Confirmation(tk.Toplevel):
    """
    Confirmation is a dialog box to ask the user to confirm an action.

    Example:

        import tkinter as tk
        from megawidget import Confirmation

        def my_handler(result):
            print(result)

        root = tk.Tk()
        confirmation = Confirmation(root, title="Confirmation", header="Confirmation",
                        message="Do you really want to continue ?",
                        handler=my_handler)
        confirmation.build()
        root.mainloop()

    """
    def __init__(self,
                 master=None,
                 title=None,
                 header=None,
                 message=None,
                 on_close=None,
                 geometry=None,
                 megaconfig=None):
        """
        PARAMETERS:

        - master: widget parent. Example: an instance of tk.Frame

        - title: title of dialog box

        - header: the text to show as header

        - message: the text to show as message

        - handler: a callback to be executed immediately after closing the dialog box.
            This callback should accept a boolean positional argument.
            True means Ok, confirmed.

        - geometry: str, as the dialog box is a toplevel (BODY),
         you can edit its geometry. Example: "500x300"

        - options: dictionary of widgets options
            The widgets keys are: BODY, LABEL_HEADER,
             LABEL_MESSAGE, FRAME_FOOTER, BUTTON_CANCEL, BUTTON_CONFIRM.

            Example: Assume that you want to set the LABEL_MESSAGE's background to black
            and the BODY's background to red:
                options = { BODY: {"background": "red"},
                            LABEL_MESSAGE: {"background": "black"} }

        """
        self.__megaconfig = merge_megaconfig(secondary=megaconfig)
        super().__init__(master=master,
                         class_="Confirmation",
                         cnf=self.__megaconfig.get(BODY))
        self.__title = title
        self.__header = header
        self.__message = message
        self.__on_close = on_close
        self.__geometry = geometry
        self.__parts = {}
        self.__ok = False
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
    def ok(self):
        """
        Returns True if user confirmed, else get False
        """
        return self.__ok

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
        self.__build()
        implement_lifecycle(body=self, on_map=self.__on_map,
                            on_destroy=self.__on_destroy)

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
            label_message.pack(fill=tk.BOTH,
                               expand=1, padx=5, pady=(5, 10))

        #
        frame_footer = tk.Frame(self, cnf=self.__megaconfig.get(FRAME_FOOTER))
        self.__parts[FRAME_FOOTER] = frame_footer
        frame_footer.pack(anchor="e", pady=(0, 2), padx=2)
        #
        button_confirm = tk.Button(frame_footer,
                                   text="Confirmation",
                                   name=BUTTON_CONFIRM,
                                   command=self.__on_click_confirm,
                                   cnf=self.__megaconfig.get(BUTTON_CONFIRM))
        self.__parts[BUTTON_CONFIRM] = button_confirm
        button_confirm.pack(side=tk.RIGHT)
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
            self.__on_close(self.__ok)

    def __on_click_cancel(self):
        self.__ok = False
        self.destroy()

    def __on_click_confirm(self):
        self.__ok = True
        self.destroy()


class _ConfirmTest(Viewable):
    def __init__(self, root):
        super().__init__()
        self._root = root
        self._body = None

    def _build(self):
        self._body = tk.Frame(self._root)
        btn_launch = tk.Button(self._body, text="Launch",
                               command=self._on_click_launch)
        btn_launch.pack()

    def _on_click_launch(self):
        confirmation = Confirmation(self._body, title="Confirmation",
                          header="Confirmation",
                          message="Do you really want to continue ?\nPress ok to continue\nOr die !")
        confirmation.wait_window()
        print("Confirmation:", confirmation.ok)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300+0+0")
    confirm_test = _ConfirmTest(root)
    confirm_test.build_pack()
    root.mainloop()
