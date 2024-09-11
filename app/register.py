import tkinter as tk


class RegisterPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.label = tk.Label(self, text="")
        self.label.pack(pady=10)

        # ラベルと入力項目を作成
        # 身長・体重・性別・年齢を入力
        self.label_h = tk.Label(self, text="身長を入力してください。")
        self.label_h.pack(pady=10)

        self.user_h = tk.Entry(self)
        self.user_h.pack(pady=10)

        self.label_w = tk.Label(self, text="体重を入力してください。")
        self.label_w.pack(pady=10)

        self.user_w = tk.Entry(self)
        self.user_w.pack(pady=10)

        self.label_a = tk.Label(self, text="年齢を入力してください。")
        self.label_a.pack(pady=10)

        self.user_a = tk.Entry(self)
        self.user_a.pack(pady=10)

        self.label_g = tk.Label(self, text="性別を選択してください。")
        self.label_g.pack(pady=10)
        self.user_g = tk.StringVar()
        self.user_g.set('男')

        gender = [("男", "男"), ("女", "女")]

        for text, value in gender:
            radio = tk.Radiobutton(
                self, text=text, value=value, variable=self.user_g)
            radio.pack(anchor=tk.W)

        # ボタンを作成し、クリック時にデータを渡して次の画面に遷移
        self.button = tk.Button(self, text="登録", command=self.submit)
        self.button.pack(pady=10)

    def set_data(self, user_name):
        # 受け取ったデータを表示
        self.user_name = user_name
        self.label.config(text=f"ユーザー名: {user_name}")

    def submit(self):
        # エントリからデータを取得し、RegisterSuccessPageに渡して遷移
        user_data = {'身長': self.user_h.get(), '体重': self.user_w.get(
        ), '年齢': self.user_a.get(), '性別': self.user_g.get()}
        self.parent.show_frame("RegisterSuccessPage", user_data)


class RegisterSuccessPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.label = tk.Label(self, text="")
        self.label.pack(pady=10)

        self.button = tk.Button(
            self, text="メニューへ進む", command=lambda: parent.show_frame("MenuPage"))
        self.button.pack(pady=10)

    def set_data(self, data):
        # 受け取ったデータを表示
        user_data = "\n".join(f"{key}: {value}" for key, value in data.items())
        self.label.config(text=(f'以下の内容で登録しました。\n{user_data}'))
