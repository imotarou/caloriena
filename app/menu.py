import tkinter as tk


class MenuPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.label = tk.Label(self, text="")
        self.label.pack(pady=10)

        self.label_q = tk.Label(self, text="どの食事を入力しますか？")
        self.label_q.pack(pady=10)

        # 各ボタンを作成
        self.button_values = ["朝食", "昼食", "夕食"]
        for value in self.button_values:
            self.button = tk.Button(self, text=value, command=lambda v=value: self.submit(v))
            self.button.pack(side=tk.LEFT, padx=10, pady=5)

    def set_data(self, data):
        # 受け取ったデータを表示
        self.label.config(text=f"ユーザー名: {data}")

    def submit(self,value):
        self.parent.show_frame("InputMealPage",value)