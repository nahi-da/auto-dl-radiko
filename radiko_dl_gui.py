import tkinter as tk
from tkinter import ttk

class CustomEntry(ttk.Entry):
    def __init__(self, parent, *args,**kwargs):
        ttk.Entry.__init__(self, parent, *args, **kwargs)
        self.popup_menu=tk.Menu(self, tearoff=0, activeborderwidth=5)
        self.popup_menu.add_command(label="Cut                     ",command=self.Cut,
                                    accelerator='Ctrl+V')
        self.popup_menu.add_command(label="Copy                    ",command=self.Copy,compound=tk.LEFT,
                                    accelerator='Ctrl+C')
    
        self.popup_menu.add_command(label="Paste                   ",command=self.Paste,accelerator='Ctrl+V')
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Select all",command=self.select_all,accelerator="Ctrl+A")
        self.popup_menu.add_command(label="Delete",command=self.delete_only,accelerator="Delete")
        self.popup_menu.add_command(label="Delete all",command=self.delete_selected,accelerator="Ctrl+D")
        self.bind('<Button-3>',self.popup)
        self.bind("<Control-d>",self.delete_selected_with_e1)
        self.bind('<App>',self.popup)
        
    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root + 10, event.y_root + 10, 0)
        finally:
            self.popup_menu.grab_release()

    def Copy(self):
        self.event_generate('<<Copy>>')

    def Paste(self):
        self.event_generate('<<Paste>>')

    def Cut(self):
        self.event_generate('<<Cut>>')

    def delete_selected_with_e1(self, event):
        self.select_range(0, tk.END)
        self.focus()
        self.event_generate("<Delete>")

    def delete_selected(self):
        self.select_range(0, tk.END)
        self.focus()
        self.event_generate("<Delete>")

    def delete_only(self):
        self.event_generate("<BackSpace>")

    def select_all(self):
        self.select_range(0, tk.END)
        self.focus()

def select_input_method():
    # OKまたはキャンセルが押されたかどうかを追跡
    result = {"selection": None, "manual_input": None}

    def update_input_state():
        if selection.get() == "browser":
            manual_entry.configure(state="disabled")  # 手動入力欄を無効化
        elif selection.get() == "manual":
            manual_entry.configure(state="normal")  # 手動入力欄を有効化

    def on_ok(e=None):
        result["selection"] = selection.get()
        result["manual_input"] = manual_entry.get()
        root.destroy()  # ウィンドウを閉じる

    def on_cancel(e=None):
        global result
        result = None
        root.destroy()  # ウィンドウを閉じる

    # メインウィンドウ
    root = tk.Tk()
    root.title("")

    # ウィンドウの閉じるイベントに on_close をバインド
    root.protocol("WM_DELETE_WINDOW", on_cancel)

    # ラジオボタンの選択肢
    selection = tk.StringVar(value="browser")  # デフォルトはブラウザー選択

    # スペーサー
    tk.Label(root, text=" ").pack()

    # ブラウザーで選択のラジオボタン
    browser_radio = ttk.Radiobutton(root, text="ブラウザーで選択", variable=selection, value="browser", command=update_input_state)
    browser_radio.pack(anchor="w", padx=10)

    # 手動入力のラジオボタン
    manual_radio = ttk.Radiobutton(root, text="URL手動入力", variable=selection, value="manual", command=update_input_state)
    manual_radio.pack(anchor="w", padx=10)

    # 手動入力欄（デフォルトは無効化）
    manual_entry = CustomEntry(root, state="disabled", width=60, validate="key", validatecommand=(root.register(lambda x: len(x) < 50), "%P"))
    manual_entry.pack(padx=10, pady=10)
    manual_entry.bind("<Return>", on_ok)

    # OKとキャンセルボタン
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)

    ok_button = ttk.Button(button_frame, text="OK", command=on_ok)
    ok_button.pack(side="left", padx=5)

    cancel_button = ttk.Button(button_frame, text="キャンセル", command=on_cancel)
    cancel_button.pack(side="left", padx=5)

    # メインループ開始
    root.mainloop()

    # 結果を返す
    return result

# この関数を呼び出して、選択結果を取得
# result = select_input_method()

# 結果を表示
# print(f"選択: {result['selection']}, 手動入力: {result['manual_input']}")
