import tkinter as tk

# Импортируем компоненты
class UIComponent:
    def __init__(self, master):
        self.master = master
        self.widget = None

    def render(self):
        raise NotImplementedError

    def update_style(self, **kwargs):
        if self.widget:
            for key, value in kwargs.items():
                self.widget[key] = value


class Button(UIComponent):
    def __init__(self, master, text="Button", command=None):
        super().__init__(master)
        self.text = text
        self.command = command

    def render(self):
        self.widget = tk.Button(self.master, text=self.text, command=self.command)
        self.widget.pack(pady=5)


class TextField(UIComponent):
    def __init__(self, master, placeholder=""):
        super().__init__(master)
        self.placeholder = placeholder

    def render(self):
        self.widget = tk.Entry(self.master)
        self.widget.insert(0, self.placeholder)
        self.widget.pack(pady=5)

    def get_text(self):
        return self.widget.get()


class Dropdown(UIComponent):
    def __init__(self, master, options=None):
        super().__init__(master)
        self.options = options or []
        self.selected = tk.StringVar(value=self.options[0] if self.options else "")

    def render(self):
        self.widget = tk.OptionMenu(self.master, self.selected, *self.options)
        self.widget.pack(pady=5)

    def get_selected(self):
        return self.selected.get()


# Основная логика приложения
def main():
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Пример приложения")

    # Функция обработки событий
    def on_button_click():
        text = text_field.get_text()
        selected_option = dropdown.get_selected()
        print(f"Текст: {text}, Выбранный элемент: {selected_option}")
        label.widget.config(text=f"Вы ввели: {text}, выбрали: {selected_option}")

    # Создаем компоненты
    text_field = TextField(root, placeholder="Введите текст...")
    text_field.render()

    dropdown = Dropdown(root, options=["Опция 1", "Опция 2", "Опция 3"])
    dropdown.render()

    button = Button(root, text="Отправить", command=on_button_click)
    button.render()

    label = UIComponent(root)
    label.widget = tk.Label(root, text="Результаты будут здесь")
    label.widget.pack(pady=5)

    # Запускаем главный цикл
    root.mainloop()


if __name__ == "__main__":
    main()