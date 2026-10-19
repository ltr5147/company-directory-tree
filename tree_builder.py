
class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        side = side.strip().lower()

        if self.root is None:
            print("Add a team lead before adding employees.")
            return False

        if side not in ("left", "right"):
            print("Invalid side. Please enter left or right.")
            return False

        if current_node is None:
            current_node = self.root

        # Check if we found the manager
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is not None:
                    print(f"The left side of {manager_name} is already taken.")
                    return False
                current_node.left = EmployeeNode(employee_name)

            else:
                if current_node.right is not None:
                    print(f"The right side of {manager_name} is already taken.")
                    return False
                current_node.right = EmployeeNode(employee_name)

            return True

        # Search the left side recursively
        if current_node.left is not None:
            result = self.insert(
                manager_name, employee_name, side, current_node.left
            )
            if result is not None:
                return result

        # Search the right side recursively
        if current_node.right is not None:
            result = self.insert(
                manager_name, employee_name, side, current_node.right
            )
            if result is not None:
                return result

        # If we searched everything, the manager does not exist
        if current_node is self.root:
            print(f"Manager '{manager_name}' was not found.")
            return False

        return None

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root

            if node is None:
                if level == 0:
                    print("The team directory is empty.")
                return

        print("  " * level + "- " + node.name)

        # Print both sides of the tree
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


def company_directory():
    team = TeamTree()

    while True:
        print("\nTeam Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if team.root is not None:
                print("A team lead already exists.")
                continue

            name = input("Enter team lead's name: ").strip()

            if not name:
                print("Name cannot be empty.")
            else:
                team.root = EmployeeNode(name)
                print(f"{name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ").strip()
            employee = input("Enter the new employee's name: ").strip()
            side = input(
                "Should the employee be on the LEFT or RIGHT? "
            ).strip().lower()

            if not manager or not employee:
                print("Names cannot be empty.")

            elif team.insert(manager, employee, side):
                print(
                    f"{employee} added to the {side.upper()} of {manager}."
                )

        elif choice == "3":
            print("\nCurrent Team Structure:")
            team.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("Please choose a number from 1 to 4.")


if __name__ == "__main__":
    company_directory()
