import tkinter as tk
import tkutil
from viewable import Viewable, CustomView
from tkutil import merge_cnfs


# Components
BODY = "body"
LABEL_HEADER = "label_header"
LABEL_MESSAGE = "label_message"
FRAME_FOOTER = "frame_footer"
BUTTON_CANCEL = "button_cancel"
BUTTON_CONFIRM = "button_confirm"


class Confirm(tk.Toplevel):
    """
    Confirm is a dialog box to ask the user to confirm an action.

    Example:

        import tkinter as tk
        from pyrustic.widget.confirm import Confirm

        def my_handler(result):
            print(result)

        root = tk.Tk()
        confirm = Confirm(root, title="Confirm", header="Confirmation",
                        message="Do you really want to continue ?",
                        handler=my_handler)
        confirm.build()
        root.mainloop()

    """
    def __init__(self,
                 master=None,
                 title=None,
                 header=None,
                 message=None,
                 handler=None,
                 geometry=None,
                 cnfs=None):
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
        self.__cnfs = merge_cnfs(None, cnfs, components=(BODY,
                        LABEL_HEADER, LABEL_MESSAGE, FRAME_FOOTER,
                        BUTTON_CANCEL, BUTTON_CONFIRM))
        super().__init__(master=master,
                         class_="Confirm",
                         cnf=self.__cnfs[BODY])
        self.__title = title
        self.__header = header
        self.__message = message
        self.__handler = handler
        self.__geometry = geometry
        self.__components = {}
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
    def handler(self):
        return self.__handler

    @property
    def ok(self):
        """
        Returns True if user confirmed, else get False
        """
        return self.__ok

    @property
    def components(self):
        """
        Get the components (widgets instances) used to build this dialog.

        This property returns a dict. The keys are:
            BODY, LABEL_HEADER,
            LABEL_MESSAGE, FRAME_FOOTER, BUTTON_CANCEL, BUTTON_CONFIRM

        Warning: check the presence of key before usage
        """
        return self.__components

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
                                    cnf=self.__cnfs[LABEL_HEADER])
            self.__components[LABEL_HEADER] = label_header
            label_header.pack(fill=tk.X, expand=1, anchor="w", pady=5, padx=5)
        #
        if self.__message:
            label_message = tk.Label(self,
                                     name=LABEL_MESSAGE,
                                     text=self.__message,
                                     anchor="w",
                                     justify=tk.LEFT,
                                     cnf=self.__cnfs[LABEL_MESSAGE])
            self.__components[LABEL_MESSAGE] = label_message
            label_message.pack(fill=tk.BOTH,
                               expand=1, padx=5, pady=(5, 10))

        #
        frame_footer = tk.Frame(self, cnf=self.__cnfs[FRAME_FOOTER])
        self.__components[FRAME_FOOTER] = frame_footer
        frame_footer.pack(anchor="e", pady=(0, 2), padx=2)
        #
        button_confirm = tk.Button(frame_footer,
                                   text="Confirm",
                                   name=BUTTON_CONFIRM,
                                   command=self.__on_click_confirm,
                                   cnf=self.__cnfs[BUTTON_CONFIRM])
        self.__components[BUTTON_CONFIRM] = button_confirm
        button_confirm.pack(side=tk.RIGHT)
        #
        button_cancel = tk.Button(frame_footer,
                                  text="Cancel",
                                  name=BUTTON_CANCEL,
                                  command=self.__on_click_cancel,
                                  cnf=self.__cnfs[BUTTON_CANCEL])
        self.__components[BUTTON_CANCEL] = button_cancel
        button_cancel.pack(side=tk.RIGHT, padx=(0, 2))

    def __on_map(self):
        tkutil.center_dialog_effect(self,
                                    within=self.master.winfo_toplevel())

    def __on_destroy(self):
        if self.__handler:
            self.__handler(self.__ok)

    def __on_click_cancel(self):
        self.__ok = False
        self.destroy()

    def __on_click_confirm(self):
        self.__ok = True
        self.destroy()


class Error(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ""
        super().__init__(self.message)

    def __str__(self):
        return self.message


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
        confirm = Confirm(root, title="Confirm",
                          header="Confirmation",
                          message="Do you really want to continue ?\nPress ok to continue\nOr die !")
        confirm.wait_window()
        print("Confirm:", confirm.ok)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300+0+0")
    confirm_test = _ConfirmTest(root)
    confirm_test.body.pack()
    root.mainloop()
