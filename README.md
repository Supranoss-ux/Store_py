"# Store Management" 
🛍️ Terminal Shop Management System
A simple command-line based store management system written in Python, designed to manage products, customers, dealers, and purchases. This project was built by me while learning object-oriented programming concepts in Python. It's not meant to be enterprise-level — it's for learning, experimenting, and having fun!

📌 Features
Add/remove products, customers, and dealers

Record purchases and view purchase history

Show customers who bought a specific product

Show products sold by a dealer

Calculate total purchases by a customer

Display number of units sold per product

Summarize total sales for each dealer

Input validation and simple error handling included

Fully object-oriented — each entity is represented with a Python class

📁 Classes Used
Person → Base class for common attributes

Product → Represents a store item

Customer → Inherits from Person and adds location and ID

Dealer → Contains info about the seller

Purchase → Stores purchase transactions with references to other objects

🛠 Technologies
Python 3

No external libraries required

Command-line only

Uses dict and list for storage (no database or file persistence yet)

⚠️ Limitations
Data is stored in memory only — exiting the program deletes all data

Not yet optimized for edge cases or large-scale data

No GUI or web interface (for now!)

Basic error messages, no extensive validation system

💡 Future Improvements (as I learn more)
Add file-based storage (JSON/CSV or SQLite)

Build a simple GUI using Tkinter

Add authentication for dealer/customer roles

Add unit testing for class logic

📸 Sample Use
bash
Copy
Edit
1. Add a Product
2. Remove a Product
3. Add a Customer
4. Remove a Customer
...
14. Exit the Program :
👨‍💻 Author
Made by Younes on the path to becoming a pro Python developer!
