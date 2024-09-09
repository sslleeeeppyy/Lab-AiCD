'''
Требуется написать объектно-ориентированную программу с графическим интерфейсом в соответствии со своим вариантом.
В программе должны быть реализованы минимум один класс, три атрибута, четыре метода (функции).
Ввод данных из файла с контролем правильности ввода.
Базы данных использовать нельзя. При необходимости сохранять информацию в виде файлов, разделяя значения запятыми или пробелами.
Для GUI использовать библиотеку tkinter.

Вариант 8
Объекты – круги
Функции:	проверка пересечения
визуализация
раскраска
перемещение на плоскости
'''
import tkinter as tk
from tkinter import messagebox
import random
import math


class Circle:
    def __init__(self, x, y, radius, number, color="black"):
        self.x = x
        self.y = y
        self.radius = radius
        self.number = number
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius,
                           outline=self.color, fill=self.color)
        canvas.create_text(self.x, self.y, text=str(self.number), fill="white")

    def intersects(self, other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distance < (self.radius + other.radius)


class CircleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle App")
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        self.circles = []
        self.circle_counter = 1
        self.setup_ui()

    def setup_ui(self):
        self.add_circle_frame = tk.Frame(self.root)
        self.add_circle_frame.pack()

        tk.Label(self.add_circle_frame, text="Координата X:").grid(row=0, column=0)
        self.x_entry = tk.Entry(self.add_circle_frame)
        self.x_entry.grid(row=0, column=1)

        tk.Label(self.add_circle_frame, text="Координата Y:").grid(row=1, column=0)
        self.y_entry = tk.Entry(self.add_circle_frame)
        self.y_entry.grid(row=1, column=1)

        tk.Label(self.add_circle_frame, text="Радиус:").grid(row=2, column=0)
        self.radius_entry = tk.Entry(self.add_circle_frame)
        self.radius_entry.grid(row=2, column=1)

        self.add_button = tk.Button(self.add_circle_frame, text="Добавить круг", command=self.add_circle)
        self.add_button.grid(row=3, columnspan=2)

        self.move_button = tk.Button(self.root, text="Передвинуть фигуры", command=self.move_circles)
        self.move_button.pack()

        self.color_button = tk.Button(self.root, text="Поменять цвет фигур", command=self.color_circles)
        self.color_button.pack()

        self.check_button = tk.Button(self.root, text="Проверить пересечение фигур", command=self.check_intersections)
        self.check_button.pack()

    def add_circle(self):
        try:
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
            radius = int(self.radius_entry.get())
            if radius <= 0:
                raise ValueError("Radius must be positive")
            circle = Circle(x, y, radius, self.circle_counter)
            self.circles.append(circle)
            self.circle_counter += 1
            self.draw_circles()
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def draw_circles(self):
        self.canvas.delete("all")
        for circle in self.circles:
            circle.draw(self.canvas)

    def move_circles(self):
        for circle in self.circles:
            circle.move(10, 10)  # Move each circle by 10 pixels
        self.draw_circles()

    def color_circles(self):
        for circle in self.circles:
            circle.color = random.choice(["red", "green", "blue", "yellow", "purple"])
        self.draw_circles()

    def check_intersections(self):
        intersections = []
        for i, circle1 in enumerate(self.circles):
            for j, circle2 in enumerate(self.circles):
                if i != j and circle1.intersects(circle2):
                    intersections.append((circle1.number, circle2.number))

        if intersections:
            messagebox.showinfo("Intersections", f"Пересекающиеся круги: {intersections}")
        else:
            messagebox.showinfo("Intersections", "No intersections found")

if __name__ == "__main__":
    root = tk.Tk()
    app = CircleApp(root)
    root.mainloop()
