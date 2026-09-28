import tkinter as tk
from tkinter import simpledialog, messagebox
import importlib

# 03_ATM.py safely load karna
atm_file = importlib.import_module("03_ATM")
ATM = atm_file.ATM

class ATM_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")

        # Window size & Resizable configuration
        self.root.geometry("450x550")
        self.root.minsize(360, 480)
        self.root.resizable(True, True)

        # Backend logic connect
        self.atm_logic = ATM()

        # Center alignment container frame
        self.main_container = tk.Frame(self.root)
        self.main_container.pack(expand=True)

        # Title Label
        tk.Label(
            self.main_container, 
            text="🏧 ATM INTERFACE", 
            font=("Arial", 18, "bold"), 
            fg="#1e272e"
        ).pack(pady=20)

        # Button Styling
        btn_style = {"width": 24, "height": 2, "font": ("Arial", 10, "bold")}

        # Action Buttons
        tk.Button(self.main_container, text="1. Create PIN", command=self.handle_create_pin, **btn_style).pack(pady=6)
        tk.Button(self.main_container, text="2. Change PIN", command=self.handle_change_pin, **btn_style).pack(pady=6)
        tk.Button(self.main_container, text="3. Check Balance", command=self.handle_check_balance, **btn_style).pack(pady=6)
        tk.Button(self.main_container, text="4. Withdraw Cash", command=self.handle_withdraw, **btn_style).pack(pady=6)
        tk.Button(self.main_container, text="5. Exit", fg="red", command=self.root.destroy, **btn_style).pack(pady=10)

    # 1. Create PIN: Pehle PIN database mein save hoga, phir Balance
    def handle_create_pin(self):
        # Step A: Pehle PIN maangna
        pin = simpledialog.askstring("Input", "Enter your PIN: ")
        if pin:
            success, msg = self.atm_logic.register_pin(pin)
            if not success:
                messagebox.showerror("Error", msg)
                return

            # Step B: PIN insert hone ke baad Balance maangna aur update karna
            balance = simpledialog.askinteger("Input", "Enter your balance = ")
            if balance is not None:
                final_msg = self.atm_logic.update_initial_balance(pin, balance)
                messagebox.showinfo("Result", final_msg)

    # 2. Change PIN
    def handle_change_pin(self):
        old_pin = simpledialog.askstring("Input", "enter old pin: ")
        if old_pin:
            new_pin = simpledialog.askstring("Input", "Enter the new pin = ")
            if new_pin:
                success, msg = self.atm_logic.change_pin(old_pin, new_pin)
                if success:
                    messagebox.showinfo("Success", msg)
                else:
                    messagebox.showerror("Error", msg)

    # 3. Check Balance
    def handle_check_balance(self):
        user_pin = simpledialog.askstring("Input", "Enter the pin: ")
        if user_pin:
            success, msg = self.atm_logic.check_balance(user_pin)
            if success:
                messagebox.showinfo("Balance", msg)
            else:
                messagebox.showerror("Error", msg)

    # 4. Withdraw Cash
    def handle_withdraw(self):
        user_pin = simpledialog.askstring("Input", "Enter your pin = ")
        if user_pin:
            amount = simpledialog.askinteger("Input", "Enter the amount = ")
            if amount is not None:
                success, msg = self.atm_logic.Withdraw(user_pin, amount)
                if success:
                    messagebox.showinfo("Success", msg)
                else:
                    messagebox.showerror("Failed", msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = ATM_GUI(root)
    root.mainloop()