import Tkinter as tk

class App:

    def __init__(self, parent):
        frame = tk.Frame(parent)
        frame.pack()
        
        print_btn = tk.Button(frame, text='Print',
                            command=lambda: self.on_print('Print'))
        print_btn.pack(side = tk.LEFT)

        close_btn = tk.Button(frame, text='close', command=frame.quit)
        close_btn.pack(side = tk.LEFT)

    def on_print(self, num):
        print("You just printed something")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
