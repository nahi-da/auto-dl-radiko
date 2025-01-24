import tkinter as tk
from tkinter.messagebox import (
    askokcancel,
    askquestion,
    askretrycancel,
    askyesno,
    askyesnocancel,
    showerror,
    showinfo,
    showwarning
)

from tkinter.filedialog import (
    askopenfile,
    askopenfiles,
    askopenfilename,
    askopenfilenames,
    asksaveasfile,
    asksaveasfilename,
    askdirectory,
)


class CustomFileDialog():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1x1")
        self.root.attributes('-alpha', 0.0)  # ウィンドウを透明に設定
        self.root.withdraw()  # メインウィンドウを非表示にする
        self.root.iconify()

    def askopenfile(self, mode='r', **options):
        ans = askopenfile(mode=mode, **options)
        self.root.destroy()
        return ans

    def askopenfiles(self, mode='r', **options):
        ans = askopenfiles(mode=mode, **options)
        self.root.destroy()
        return ans

    def askopenfilename(self, **options):
        ans = askopenfilename(**options)
        self.root.destroy()
        return ans

    def askopenfilenames(self, **options):
        ans = askopenfilenames(**options)
        self.root.destroy()
        return ans

    def asksaveasfile(self, mode='w', **options):
        ans = asksaveasfile(mode=mode, **options)
        self.root.destroy()
        return ans

    def asksaveasfilename(self, **options):
        ans = asksaveasfilename(**options)
        self.root.destroy()
        return ans

    def askdirectory(self, **options):
        ans = askopenfile(**options)
        self.root.destroy()
        return ans


class CustomMsgBox():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1x1")
        self.root.attributes('-alpha', 0.0)  # ウィンドウを透明に設定
        self.root.withdraw()  # メインウィンドウを非表示にする
        self.root.iconify()

    def askyesno(self, title: str | None = None, message: str | None = None, **options):
        ans = askyesno(title, message, **options)
        self.root.destroy()
        return ans
    
    def askyesnocancel(self, title: str | None = None, message: str | None = None, **options):
        ans = askyesnocancel(title, message, **options)
        self.root.destroy()
        return ans
    
    def askokcancel(self, title: str | None = None, message: str | None = None, **options):
        ans = askokcancel(title, message, **options)
        self.root.destroy()
        return ans
    
    def askretrycancel(self, title: str | None = None, message: str | None = None, **options):
        ans = askretrycancel(title, message, **options)
        self.root.destroy()
        return ans
    
    def askquestion(self, title: str | None = None, message: str | None = None, **options):
        ans = askquestion(title, message, **options)
        self.root.destroy()
        return ans
    
    def showerror(self, title: str | None = None, message: str | None = None, **options):
        ans = showerror(title, message, **options)
        self.root.destroy()
        return ans
    
    def showinfo(self, title: str | None = None, message: str | None = None, **options):
        ans = showinfo(title, message, **options)
        self.root.destroy()
        return ans

    def showwarning(self, title: str | None = None, message: str | None = None, **options):
        ans = showwarning(title, message, **options)
        self.root.destroy()
        return ans

