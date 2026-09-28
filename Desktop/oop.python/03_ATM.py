import oracledb

class ATM:
    def __init__(self):
        # Oracle database connection setup
        self.conn = oracledb.connect(
            user="system",
            password="Oracle123",
            dsn="localhost:1521/FREEPDB1"
        )
        self.cursor = self.conn.cursor()

    # Step 1: Pehle sirf PIN database mein jayega (Initial balance 0)
    def register_pin(self, user_pin):
        p = str(user_pin).strip()
        
        # Check if PIN exists
        self.cursor.execute("SELECT pin FROM accounts WHERE pin = :1", [p])
        if self.cursor.fetchone():
            return False, "This PIN already exists! Choose another."
        
        # Insert PIN into accounts table
        self.cursor.execute("INSERT INTO accounts (pin, balance) VALUES (:1, 0)", [p])
        self.conn.commit()
        return True, "PIN registered successfully!"

    # Step 2: Usi PIN ke record mein Balance update hoga
    def update_initial_balance(self, user_pin, user_balance):
        p = str(user_pin).strip()
        bal = float(user_balance)

        self.cursor.execute("UPDATE accounts SET balance = :1 WHERE pin = :2", [bal, p])
        self.conn.commit()
        return f"Account Created!\nPIN: {p}\nBalance Set: Rs. {bal}"

    # Terminal Menu
    def menu(self):
        user_input = input("""
        Hi, How Can I Help You?

        1. Press 1 to create PIN
        2. Press 2 to Change PIN
        3. Press 3 to Check Balance
        4. Press 4 to Withdraw
        5. Exit

        Enter your choice: """)

        if user_input == '1':
            p = input("Enter your PIN: ").strip()
            success, msg = self.register_pin(p)
            print(msg)
            if success:
                bal = float(input("Enter your balance = "))
                result = self.update_initial_balance(p, bal)
                print(result)
            self.menu()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.Withdraw()
        else:
            exit()

    # 2. Change PIN
    def change_pin(self, old_pin=None, new_pin=None):
        if old_pin is None and new_pin is None:
            old_p = str(input('enter old pin: ')).strip()
            new_p = str(input('Enter the new pin = ')).strip()
        else:
            old_p = str(old_pin).strip()
            new_p = str(new_pin).strip()

        self.cursor.execute("SELECT id FROM accounts WHERE pin = :1", [old_p])
        record = self.cursor.fetchone()

        if record:
            self.cursor.execute("UPDATE accounts SET pin = :1 WHERE pin = :2", [new_p, old_p])
            self.conn.commit()
            if old_pin is None:
                print('pin change sucessfully')
                self.menu()
            return True, "pin change sucessfully"
        else:
            if old_pin is None:
                print('Not Possible')
                self.menu()
            return False, "Not Possible"

    # 3. Check Balance
    def check_balance(self, user_pin=None):
        if user_pin is None:
            p = str(input('Enter the pin: ')).strip()
        else:
            p = str(user_pin).strip()

        self.cursor.execute("SELECT balance FROM accounts WHERE pin = :1", [p])
        record = self.cursor.fetchone()

        if record:
            curr_balance = record[0]
            if user_pin is None:
                print('Your balance is =', curr_balance)
                self.menu()
            return True, f"Your balance is = {curr_balance}"
        else:
            if user_pin is None:
                print('invalid pin')
                self.menu()
            return False, "invalid pin"

    # 4. Withdraw Cash
    def Withdraw(self, user_pin=None, amount=None):
        if user_pin is None and amount is None:
            p = str(input('Enter your pin = ')).strip()
            amt = float(input('Enter the amount = '))
        else:
            p = str(user_pin).strip()
            amt = float(amount)

        self.cursor.execute("SELECT balance FROM accounts WHERE pin = :1", [p])
        record = self.cursor.fetchone()

        if not record:
            if user_pin is None:
                print('sale chor')
                self.menu()
            return False, "sale chor"

        curr_balance = record[0]
        if amt <= curr_balance:
            new_bal = curr_balance - amt
            self.cursor.execute("UPDATE accounts SET balance = :1 WHERE pin = :2", [new_bal, p])
            self.conn.commit()
            if user_pin is None:
                print('Withdraw successfully is =', new_bal)
                self.menu()
            return True, f"Withdraw successfully is = {new_bal}"
        else:
            if user_pin is None:
                print('abhe gareeb !')
                self.menu()
            return False, "abhe gareeb !"


if __name__ == "__main__":
    obj = ATM()
    obj.menu()