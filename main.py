import tkinter as tk
from tkinter import ttk, messagebox
import password_generator as pg

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("400x400")

        # Длина пароля
        self.length_label = tk.Label(root, text="Длина пароля (8-20):")
        self.length_label.pack(pady=5)
        self.length_slider = tk.Scale(root, from_=8, to=20, orient=tk.HORIZONTAL)
        self.length_slider.set(12)
        self.length_slider.pack(pady=5)

        # Чекбоксы
        self.use_digits = tk.BooleanVar(value=True)
        self.use_letters = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Цифры", variable=self.use_digits).pack(anchor='w')
        tk.Checkbutton(root, text="Буквы", variable=self.use_letters).pack(anchor='w')
        tk.Checkbutton(root, text="Спецсимволы", variable=self.use_special).pack(anchor='w')

        # Кнопка генерации
        self.generate_btn = tk.Button(root, text="Сгенерировать пароль", command=self.generate_password)
        self.generate_btn.pack(pady=10)

        # Поле вывода пароля
        self.password_entry = tk.Entry(root, width=30)
        self.password_entry.pack(pady=5)

        # Кнопка добавления в историю
        self.add_history_btn = tk.Button(root, text="Добавить в историю", command=self.add_to_history)
        self.add_history_btn.pack(pady=5)

        # Таблица истории
        self.tree = ttk.Treeview(root, columns=("password",), show="headings")
        self.tree.heading("password", text="Пароль")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.load_history()

    def generate_password(self):
        length = self.length_slider.get()
        chars = {
            'digits': self.use_digits.get(),
            'letters': self.use_letters.get(),
            'special': self.use_special.get()
        }
        
        if not any(chars.values()):
            messagebox.showerror("Ошибка", "Выберите хотя бы один тип символов!")
            return

        password = pg.generate_password(length, **chars)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def add_to_history(self):
        password = self.password_entry.get()
        if password:
            pg.add_to_history(password)
            self.load_history()
            messagebox.showinfo("Успех", "Пароль добавлен в историю!")

    def load_history(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        history = pg.load_history()
        for pwd in history:
            self.tree.insert("", tk.END, values=(pwd,))
