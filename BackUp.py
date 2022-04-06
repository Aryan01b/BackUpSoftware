from functools import singledispatch
import tkinter
from tkinter import filedialog
import os

root = tkinter.Tk()


def init():
    root.resizable(0, 0)
    root.iconbitmap("images/backup.ico")
    root.configure(borderwidth=0, bg="#11404f", padx=100, pady=100)
    root.title("BackUp Files")
    root.attributes('-alpha', 0.95)
    interface()
    root.mainloop()


def open_file():
    filetypes = (
        ('Python Files', '*.py'),
        ('All Files', '*.*')
    )
    filename = filedialog.askopenfilename(
        title="Select a File", filetypes=filetypes)

    file_label = tkinter.Label(
        root, text=filename, bg="#11404f", foreground="white", borderwidth=0, font="monospace")
    file_label.pack(padx=10, pady=10)

    def do_work():
        back_index = str(filename)[::-1].index("/")
        try:
            os.mkdir(filename[0:len(filename)-back_index]+"BackUp/")
        except(FileExistsError):
            print("File Already Exixts!")

        out_filename = filename[0:len(filename)-back_index]+"BackUp/" + \
            filename[len(filename)-back_index:len(filename)-3]+"(BackUp).py"
        backup(filename, out_filename)
        
    run_button = tkinter.Button(root, text="Next", bg="#325f66",activebackground="#11404f", font="monospace", borderwidth=0, command=do_work)
    run_button.pack(side='bottom')


def interface():

    open_button = tkinter.Button(root, bg="#325f66", borderwidth=0, font="monospace", activebackground="#11404f",
                                 text="Select a File", command=open_file, padx=10, pady=10)
    open_button.pack(ipadx=10, ipady=10, padx=10, pady=10)


def backup(filename, output_filename):
    with open(filename, 'r') as exportfile:
        data = exportfile.read()
        with open(output_filename, 'w') as importfile:
            importfile.write(data)
    completel = tkinter.Label(root, text="Backup Successful!!!",
                              bg="#11404f", borderwidth=0, font="monospace", foreground="white")
    completel.pack(side='bottom', padx=10, pady=10)


if __name__ == "__main__":
    init()
