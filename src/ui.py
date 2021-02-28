class debug:
    def __init__(self, e):
        import tkinter as tk
        root = tk.Tk()
        root.title("ERROR!")

        text_e = tk.Text(root, padx=5, pady=5)
        text_e.insert(tk.END, e)
        text_e["state"] = tk.DISABLED
        text_e.pack()

        root.geometry()
        root.mainloop()
