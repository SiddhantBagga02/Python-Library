def calculate_total_salary(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Check if the file is empty
        if not lines:
            print(f"Error: File '{file_name}' is empty.")
            return None

        # Calculate the sum of all valid salaries
        total_salary = 0
        for salary in lines:
            salary = salary.strip()
            try:
                total_salary += int(salary)
            except ValueError:
                print(f"Warning: Invalid data found in '{file_name}': '{salary}' is not a valid integer.")

        # Display the sum
        print(f"Sum of all valid salaries in '{file_name}':", total_salary)
        return total_salary

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example Usage:
total_salary = calculate_total_salary('Eula.txt')
if total_salary is not None:
    # Now you can use 'total_salary' in further operations if needed
    pass
