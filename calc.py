import torch
import tkinter as tk
from PIL import Image, ImageTk

torch.manual_seed(42)

img = Image.open("/home/wizard/python/Pytorch/Calc/213337872.png")
width, height = img.size

root = tk.Tk()
root.title("Calc PyTorch")
root.geometry(f"{width}x{height}")

bg_img = ImageTk.PhotoImage(img)
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

text_input = tk.Text(root, font=("Arial", 70), height=2, width=25)
text_input.place(x=20, y=20)

def calculate():
    try:
        expr = text_input.get("1.0", tk.END).strip()
        if '+' in expr:
            numbers = expr.split('+')
            nums = torch.tensor([float(n) for n in numbers])
            result = torch.sum(nums)
        elif '-' in expr:
            numbers = expr.split('-')
            nums = torch.tensor([float(n) for n in numbers])
            result = nums[0] - nums[1]
        elif '*' in expr:
            numbers = expr.split('*')
            nums = torch.tensor([float(n) for n in numbers])
            result = nums[0] * nums[1]
        elif '/' in expr:
            numbers = expr.split('/')
            nums = torch.tensor([float(n) for n in numbers])
            if nums[1] == 0:
                raise ZeroDivisionError
            result = nums[0] / nums[1]
        else:
            raise ValueError("Invalid expression")

        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, f"result: {result.item()}")

    except:
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, "error!")

btn = tk.Button(root, text="calc", font=("Arial", 16), command=calculate)
btn.place(x=20, y=90)

root.mainloop()
