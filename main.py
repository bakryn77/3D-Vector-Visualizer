import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from vector_math import (
    add_vectors,
    subtract_vectors,
    dot_product,
    magnitude,
    normalize
)

class VectorVisualizerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Vector Visualizer V1")

        # Input fields
        ttk.Label(root, text="Vector 1 (x,y,z):").grid(row=0, column=0)
        self.v1_entry = ttk.Entry(root)
        self.v1_entry.grid(row=0, column=1)

        ttk.Label(root, text="Vector 2 (x,y,z):").grid(row=1, column=0)
        self.v2_entry = ttk.Entry(root)
        self.v2_entry.grid(row=1, column=1)

        # Buttons
        ttk.Button(root, text="Add", command=self.add).grid(row=2, column=0)
        ttk.Button(root, text="Subtract", command=self.subtract).grid(row=2, column=1)
        ttk.Button(root, text="Dot Product", command=self.dot).grid(row=3, column=0)
        ttk.Button(root, text="Normalize", command=self.normalize_vectors).grid(row=3, column=1)

        # Output label
        self.output_label = ttk.Label(root, text="", foreground="blue")
        self.output_label.grid(row=4, column=0, columnspan=2)

        # Matplotlib figure for vector plot
        self.fig = Figure(figsize=(5, 4))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=2)

    def parse_vectors(self):
        v1 = list(map(float, self.v1_entry.get().split(",")))
        v2 = list(map(float, self.v2_entry.get().split(",")))
        return np.array(v1), np.array(v2)

    def update_plot(self, v1, v2):
        self.ax.clear()

        origin = np.array([0, 0, 0])

        # Draw vector 1
        self.ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color="red", label="Vector 1")

        # Draw vector 2
        self.ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color="blue", label="Vector 2")

        self.ax.set_xlim([-10, 10])
        self.ax.set_ylim([-10, 10])
        self.ax.set_zlim([-10, 10])
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        self.ax.legend()

        self.canvas.draw()

    def add(self):
        v1, v2 = self.parse_vectors()
        result = add_vectors(v1, v2)
        self.output_label.config(text=f"Addition: {result}")
        self.update_plot(v1, v2)

    def subtract(self):
        v1, v2 = self.parse_vectors()
        result = subtract_vectors(v1, v2)
        self.output_label.config(text=f"Subtraction: {result}")
        self.update_plot(v1, v2)

    def dot(self):
        v1, v2 = self.parse_vectors()
        result = dot_product(v1, v2)
        self.output_label.config(text=f"Dot Product: {result}")
        self.update_plot(v1, v2)

    def normalize_vectors(self):
        v1, v2 = self.parse_vectors()
        n1 = normalize(v1)
        n2 = normalize(v2)
        self.output_label.config(text=f"Normalized V1: {n1}, Normalized V2: {n2}")
        self.update_plot(v1, v2)

def main():
    root = tk.Tk()
    app = VectorVisualizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()



