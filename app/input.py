import tkinter as tk
from selenium_app import GetCalorie


class InputMealPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.label = tk.Label(self, text="")
        self.label.pack(pady=10)

        self.input_m = tk.Entry(self)
        self.input_m.pack(pady=10)

        # ボタンを作成し、クリック時にデータを渡して次の画面に遷移
        self.button = tk.Button(self, text="登録", command=self.submit)
        self.button.pack(pady=10)

    def set_data(self, meal):
        # 受け取ったデータを表示
        self.meal = meal
        self.label.config(text=f"{self.meal}の内容を(ひらがなで)入力してください。")

    def submit(self):
        self.parent.set_input_meal(self.input_m.get())
        get_calorie = GetCalorie()
        self.meal_list = get_calorie.meal_serach(self.parent.input_meal)
        self.parent.show_frame("SelectMealPage", self.meal_list)


class SelectMealPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.label = tk.Label(self, text="")
        self.label.pack(pady=10)

    def set_data(self, meal_list):
        # 受け取ったデータを表示
        self.meal_list = meal_list
        self.label.config(text=f"食事内容を以下のリストから選択してください。")

        # Listboxの作成
        self.listbox = tk.Listbox(self)
        self.listbox.pack(padx=20, pady=20)

        # リストボックスにアイテムを追加
        for item in meal_list:
            self.listbox.insert(tk.END, item)

        self.button = tk.Button(self, text="食事を選択", command=self.submit)
        self.button.pack(pady=10)

    def submit(self):
        self.selected_index = self.listbox.curselection()
        self.select_meal = self.listbox.get(self.selected_index)
        get_calorie = GetCalorie()
        self.meal_list = get_calorie.meal_list(self.parent.input_meal, self.select_meal)
        print(self.meal_list)
        # self.parent.show_frame("ResultPage", self.meal_list)
