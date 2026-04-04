class PenguEats:
    def __init__(self):
        # Manage inventory (types of fish, quantity, freshness) [cite: 23]
        self.inventory = {
            "Salmon": {"quantity": 20, "freshness": "High"},
            "Tuna": {"quantity": 10, "freshness": "Medium"},
            "Cod": {"quantity": 15, "freshness": "High"}
        }

        # Track profits and expenses (ice block rent, fish supplier costs)
        self.finances = {
            "revenue": 0.0,
            "expenses": {"ice_block_rent": 200.0, "fish_supplier_costs": 150.0}
        }

        # Learn customer preferences [cite: 27]
        self.customer_history = {}

        self.menu_prices = {"Salmon": 15.0, "Tuna": 18.0, "Cod": 12.0}

    def handle_order(self, customer_name, animal_type, fish_order):
        """Handle customer orders (other animals visiting the restaurant)[cite: 24]."""
        if fish_order in self.inventory and self.inventory[fish_order]["quantity"] > 0:
            # Deduct from inventory
            self.inventory[fish_order]["quantity"] -= 1
            # Add to revenue
            self.finances["revenue"] += self.menu_prices[fish_order]

            # Record history for predictions
            if customer_name not in self.customer_history:
                self.customer_history[customer_name] = {"animal": animal_type, "orders": {}}

            if fish_order not in self.customer_history[customer_name]["orders"]:
                self.customer_history[customer_name]["orders"][fish_order] = 1
            else:
                self.customer_history[customer_name]["orders"][fish_order] += 1

            print(f"Order up! Served {fish_order} to {customer_name} the {animal_type}.")
        else:
            print(f"Sorry {customer_name}, we are out of {fish_order}!")

    def suggest_recipes(self):
        """Suggest recipes (based on fish in stock)."""
        print("\n--- Chef Pingu's Recipe Suggestions ---")
        has_stock = False
        for fish, details in self.inventory.items():
            if details["quantity"] > 0:
                has_stock = True
                if details["freshness"] == "High":
                    print(f"- Premium Ice-Glazed {fish} Sashimi (Requires High Freshness)")
                print(f"- Classic Baked {fish} with Kelp Salad")

        if not has_stock:
            print("No fish in stock! Time to call the supplier.")

    def generate_financial_report(self):
        """Track profits and expenses (ice block rent, fish supplier costs)."""
        total_expenses = sum(self.finances["expenses"].values())
        profit = self.finances["revenue"] - total_expenses

        print("\n--- Financial Report ---")
        print(f"Total Revenue: ${self.finances['revenue']:.2f}")
        print(f"Expenses (Ice Block Rent & Supplier Costs): ${total_expenses:.2f}")
        print(f"Net Profit: ${profit:.2f}")

    def predict_order(self, customer_name):
        """Learn customer preferences[cite: 27]."""
        if customer_name in self.customer_history:
            past_orders = self.customer_history[customer_name]["orders"]
            favorite_fish = max(past_orders, key=past_orders.get)
            print(f"\nWelcome back, {customer_name}! The usual {favorite_fish} today?")
            return favorite_fish
        return None

    def display_sales_chart(self):
        """Generates a text-based bar chart of fish sold."""
        print("\n--- Sales Visualization ---")
        if not self.customer_history:
            print("No sales data available yet.")
            return

        # Aggregate total sales per fish type
        total_sold = {"Salmon": 0, "Tuna": 0, "Cod": 0}
        for customer, data in self.customer_history.items():
            for fish, count in data["orders"].items():
                if fish in total_sold:
                    total_sold[fish] += count
                else:
                    total_sold[fish] = count

        # Print the bar chart
        print("Units Sold per Fish Type:")
        for fish, count in total_sold.items():
            bar = "█" * count  # Creates a bar based on the number sold
            print(f"{fish.ljust(8)} | {bar} ({count})")


# --- Execution Example ---
if __name__ == "__main__":
    restaurant = PenguEats()

    print("--- Welcome to PenguEats! ---")

    #  Suggesting recipes based on current stock
    restaurant.suggest_recipes()

    print("\n--- Lunch Rush ---")
    # Simulating orders
    restaurant.handle_order("Wally", "Walrus", "Salmon")
    restaurant.handle_order("Wally", "Walrus", "Salmon")
    restaurant.handle_order("Sammy", "Seal", "Tuna")
    restaurant.handle_order("Wally", "Walrus", "Salmon")



    # Predicting Wally's next order
    restaurant.predict_order("Wally")

    # Tracking and printing the financial report
    restaurant.generate_financial_report()

    # Display Sales
    restaurant.display_sales_chart()