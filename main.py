import matplotlib.pyplot as plt  # Import the matplotlib library for data visualization

def get_user_input():
    """
    Function to get user input for income, expenses, and savings goal.
    Returns a tuple containing income, expenses, and savings goal.
    """
    income = float(input("Enter your total income: "))  # Prompt user to enter total income
    expenses = float(input("Enter your total expenses: "))  # Prompt user to enter total expenses
    savings_goal = float(input("Enter your savings goal: "))
    return income, expenses, savings_goal  # Return the input values as a tuple

def calculate_finances(income, expenses):
    """
    Function to calculate total income, total expenses, and savings progress.
    Returns a tuple containing total income, total expenses, and savings progress.
    """
    total_income = income  # Assign the input income as total income
    total_expenses = expenses  # Assign the input expenses as total expenses
    savings_progress = total_income - total_expenses  # Calculate savings progress
    return total_income, total_expenses, savings_progress  # Return the calculated values as a tuple

def display_results(total_income, total_expenses, savings_progress):
    """
    Function to display the total income, total expenses, and savings progress.
    """
    print("\n--- Financial Summary ---")
    print(f"Total Income: ${total_income}")  # Display total income
    print(f"Total Expenses: ${total_expenses}")  # Display total expenses
    print(f"Savings Progress: ${savings_progress}")  # Display savings progress

def visualize_data(expenses):
    """
    Function to create a pie chart showing the breakdown of expenses.
    """
    labels = ['Rent', 'Groceries', 'Transportation', 'Others']  # Define expense categories
    plt.figure(figsize=(6, 6))  # Set the size of the pie chart
    plt.pie(expenses, labels=labels, autopct='%1.1f%%')  # Create the pie chart with expense breakdown
    plt.title('Expense Breakdown')  # Set the title of the pie chart
    plt.show()  # Display the pie chart

def main():
    print("Welcome to the Personal Finance Management System!\n")  # Display welcome message

    # Get user input for income, expenses, and savings goal
    income, expenses, savings_goal = get_user_input()

    # Calculate total income, total expenses, and savings progress
    total_income, total_expenses, savings_progress = calculate_finances(income, expenses)

    # Display the financial summary
    display_results(total_income, total_expenses, savings_progress)

    # Visualize the expense breakdown
    expenses_breakdown = [1000, 1500, 800, 700]  # Example expenses breakdown
    visualize_data(expenses_breakdown)

if __name__ == "__main__":
    main()  # Call the main function to start the program