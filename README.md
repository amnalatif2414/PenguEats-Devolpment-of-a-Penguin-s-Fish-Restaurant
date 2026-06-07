# PenguEats 🐧

A Python restaurant management system built as a university project.A Python-based restaurant management system where Pingu the penguin runs 
a fish restaurant using code instead of pen and paper.

## Description
PenguEats is a command-line application built using object-oriented Python. It demonstrates how 
programming can model and automate real-world business operations. The entire system is contained 
inside a single class with no external dependencies, making it 
lightweight, readable, and easy to run on any machine with Python installed.

The system handles everything from taking customer orders and tracking stock 
to generating financial reports and learning what returning customers like to 
order. It reflects a realistic restaurant workflow — starting from stock 
readiness, moving through customer service, and ending with business analysis.

## Features

- **Inventory Management** — tracks fish types, quantities, and freshness 
  levels. Freshness determines which recipes are available to suggest.

- **Order Handling** — checks stock before serving, deducts inventory, 
  records revenue, and logs the order to the customer history automatically.

- **Financial Tracking** — calculates total revenue, fixed expenses 
  (ice block rent and supplier costs), and net profit or loss after every 
  session.

- **Recipe Suggestions** — recommends dishes based on what is currently 
  in stock. High-freshness fish unlock premium menu options.

- **Customer Preference Learning** — remembers each customer's order 
  history within a session and predicts their favourite fish on return visits.

- **Sales Visualisation** — generates a text-based bar chart in the terminal 
  showing units sold per fish type, built without any external libraries.

## Dependencies

None. PenguEats uses only Python's built-in features.

- No pip installs required
- No external libraries
- No frameworks

Only requirement is **Python 3.x**

## Usage

Run the program directly:
```bash
python pengu_eats.py
```

## Known Limitations

- Data does not persist between sessions — everything resets on restart
- Command-line only, no graphical interface
- Menu is limited to three fish types
- Expenses are fixed and do not update dynamically

## Future Improvements

- SQLite database for permanent data storage
- Graphical user interface
- Automatic restocking alerts when stock runs low
- Online ordering simulation
- Advanced sales analytics with charts
