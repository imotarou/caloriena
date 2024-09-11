import tkinter as tk
from login import LoginPage
from register import RegisterPage,RegisterSuccessPage
from menu import MenuPage
from input import InputMealPage,SelectMealPage


class Application(tk.Tk):
    user = ''
    id = ''
    input_meal = ''

    def __init__(self):
        super().__init__()
        self.title("Screen Transition with User Input")
        self.geometry("600x500")
        self.frames = {}
        self.create_frames()
        self.show_frame("LoginPage")

    def set_user(self,user_name):
        Application.user = user_name
    
    def set_id(self,user_id):
        Application.id = user_id

    def set_input_meal(self,input_meal):
        Application.input_meal = input_meal

    def create_frames(self):
        # 入力画面 (LoginPage)
        login_page = LoginPage(self)
        self.frames["LoginPage"] = login_page
        login_page.grid(row=0, column=0, sticky="nsew")

        # 登録画面 (RegisterPage)
        register_page = RegisterPage(self)
        self.frames["RegisterPage"] = register_page
        register_page.grid(row=0, column=0, sticky="nsew")

        # 登録完了画面 (RegisterSuccessPage)
        register_success_page = RegisterSuccessPage(self)
        self.frames["RegisterSuccessPage"] = register_success_page
        register_success_page.grid(row=0, column=0, sticky="nsew")

        # メニュー画面 (MenuPage)
        menu_page = MenuPage(self)
        self.frames["MenuPage"] = menu_page
        menu_page.grid(row=0, column=0, sticky="nsew")

        # 食事入力画面 (InputMealPage)
        input_meal_page = InputMealPage(self)
        self.frames["InputMealPage"] = input_meal_page
        input_meal_page.grid(row=0, column=0, sticky="nsew")

        # 食事選択画面 (SelectMealPage)
        select_meal_page = SelectMealPage(self)
        self.frames["SelectMealPage"] = select_meal_page
        select_meal_page.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name, *args):
        frame = self.frames[page_name]
        if args:
            frame.set_data(*args)
        frame.tkraise()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
