<div align="center">

# 🏧 OOP & Database-Driven ATM System

**Object-Oriented Programming in Python × Oracle Database × Tkinter GUI**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Oracle](https://img.shields.io/badge/Oracle-FREEPDB1-F80000?logo=oracle&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-2C7BB6)
![Status](https://img.shields.io/badge/Status-Learning%20Project-orange)

</div>

---

## 📖 Overview

This project demonstrates how real-world business logic maps to **classes, objects, encapsulated state, and persistent relational storage**. An ATM terminal is modelled as a Python class, connected to an **Oracle Database** backend, and exposed through a resizable **Tkinter** interface.

## 📑 Table of Contents

- [🧠 Core OOP Concepts](#-core-oop-concepts)
- [🛠️ Tech Stack](#️-tech-stack)
- [✨ Features](#-features)
- [🗄️ Database Schema](#️-database-schema)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [🔐 Security Notes](#-security-notes)
- [🗺️ Future Improvements](#️-future-improvements)
- [👤 Author](#-author)

---

## 🧠 Core OOP Concepts

| Concept | How it is applied |
|---|---|
| 🧱 **Classes & Objects** | The `ATM` class encapsulates instance data, connection state, and operational logic. The GUI creates an instance (`self.atm_logic = ATM()`) with its own database cursor and lifetime. |
| 🔒 **Encapsulation** | `03_ATM.py` owns business rules, validation, and SQL. `04_ATM_GUI.py` only calls backend methods and never touches the SQL layer. |
| 🧩 **Separation of Concerns** | Backend (logic + data) and frontend (presentation + events) are fully decoupled. |
| 💾 **State & Persistence** | Runtime object state is combined with persistent relational data using `INSERT`, `SELECT`, and `UPDATE`. |

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| 🐍 Language | Python 3.x |
| 🖥️ GUI | `tkinter` |
| 🗃️ Database | Oracle Database (PDB: `FREEPDB1`) |
| 🔌 Driver | `oracledb` |
| 🧰 Tools | VS Code, Oracle SQL Developer |

## ✨ Features

- 📝 **Two-step registration**: register a unique PIN first, then bind the starting balance.
- 💰 **Transactions**: deposit on registration, balance check, withdrawals, and PIN change.
- 🪟 **Responsive window**: resizable and maximizable, with dynamic centering (`pack(expand=True)`).
- 🛡️ **Robust error handling**: non-existent accounts, duplicate registrations, invalid credentials, and overdraft attempts.

## 🗄️ Database Schema

Run this once before starting the app:

```sql
CREATE TABLE accounts (
    id      NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pin     VARCHAR2(10) NOT NULL UNIQUE,
    balance NUMBER(12, 2) NOT NULL
);
```

## 📁 Project Structure

```
OOP_Class_Object_Python/
├── 01_OOP.py            # Core syntax and foundational class structures
├── 02_OOP.concept.py    # Advanced OOP behavior and attribute scoping
├── 03_ATM.py            # Business logic and Oracle Database operations
├── 04_ATM_GUI.py        # Tkinter frontend (resizable / maximizable)
├── 05_Own_Datatype.py   # Custom data representations and structures
└── README.md
```

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x installed
- A running Oracle Database instance reachable at `localhost:1521/FREEPDB1`

### 📥 Installation

```bash
git clone https://github.com/rajukumardeewan313-eng/OOP_Class_Object_Python.git
cd OOP_Class_Object_Python
pip install oracledb
```

### ⚙️ Configuration

1. Create the `accounts` table using the schema above.
2. Set your credentials as environment variables instead of hardcoding them:

```bash
# Linux / macOS
export ORACLE_USER="your_user"
export ORACLE_PASSWORD="your_password"
export ORACLE_DSN="localhost:1521/FREEPDB1"

# Windows (PowerShell)
$env:ORACLE_USER="your_user"
$env:ORACLE_PASSWORD="your_password"
$env:ORACLE_DSN="localhost:1521/FREEPDB1"
```

3. Update the connection in `03_ATM.py`:

```python
import os
import oracledb

self.conn = oracledb.connect(
    user=os.getenv("ORACLE_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN"),
)
```

### ▶️ Run

```bash
python 04_ATM_GUI.py   # 🖥️ GUI mode
python 03_ATM.py       # ⌨️ Terminal mode
```

## 🔐 Security Notes

> ⚠️ This is a **learning project** and is not production-ready.

- 🔑 Never commit real database credentials. Use environment variables and a dedicated DB user instead of `SYSTEM`.
- 🧂 PINs are currently stored as plain text. Hash them (for example with `bcrypt`) before any real-world use.

## 🗺️ Future Improvements

- [ ] 🔐 Hash PINs before storing them
- [ ] 📜 Add a transaction history table
- [ ] 🧪 Add unit tests for the `ATM` class
- [ ] 📸 Add GUI screenshots to this README

## 👤 Author

**Raju Kumar**

- 🐙 GitHub: [rajukumardeewan313-eng](https://github.com/rajukumardeewan313-eng)
- 💼 LinkedIn: [raju-kumar-ai](https://www.linkedin.com/in/raju-kumar-ai)
- 📧 Email: rajukumardeewan313@gmail.com

---

<div align="center">

⭐ If you found this project helpful, consider giving it a star!

</div>
