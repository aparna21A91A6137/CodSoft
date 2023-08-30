import tkinter as tk
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.username_label = tk.Label(root, text="Enter Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)

        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.length_label = tk.Label(root, text="Enter Password Length:")
        self.length_label.grid(row=1, column=0, padx=10, pady=10)

        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=1, column=1, padx=10, pady=10)

        self.generated_password_label = tk.Label(root, text="Generated Password:")
        self.generated_password_label.grid(row=2, column=0, padx=10, pady=10)

        self.generated_password_var = tk.StringVar()
        self.generated_password_entry = tk.Entry(root, textvariable=self.generated_password_var, state="readonly")
        self.generated_password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.reset_button = tk.Button(root, text="Accept", command=self.reset)
        self.reset_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError

            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choice(characters) for _ in range(length))

            self.generated_password_var.set(generated_password)
        except ValueError:
            self.generated_password_var.set("Invalid length")

    def reset(self):
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.generated_password_var.set("")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    app.run()
