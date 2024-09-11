import tkinter as tk


class LoginPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # 名前の入力欄を作成
        self.label = tk.Label(self, text="名前を入力してください:")
        self.label.pack(pady=10)

        self.user_name = tk.Entry(self)
        self.user_name.pack(pady=10)

        # ボタンを作成し、クリック時にデータを渡して次の画面に遷移
        self.button = tk.Button(self, text="ログイン/登録", command=self.submit)
        self.button.pack(pady=10)

    def submit(self):
        # データを取得して遷移
        user_name = self.user_name.get()
        self.parent.set_user(user_name)
        user_data = ['田中', '佐藤', '鈴木']
        if user_name in user_data:
            print('登録されています')
            self.parent.show_frame("MenuPage", user_name)
        else:
            self.parent.show_frame("RegisterPage", user_name)
