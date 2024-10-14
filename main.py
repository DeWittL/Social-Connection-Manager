import networkx as nx
import matplotlib.pyplot as plt


class ConnectionsManager:
    def __init__(self):
        # Dictionary to store users and their connections
        self.network = {}

    def add_user(self, user):
        if user in self.network:
            print(f"User '{user}' already exists.")
        else:
            self.network[user] = []
            print(f"User '{user}' added successfully.")

    def add_connection(self, user1, user2):
        if user1 not in self.network:
            print(f"User '{user1}' does not exist. Please add them first.")
        elif user2 not in self.network:
            print(f"User '{user2}' does not exist. Please add them first.")
        else:
            # Add connection from user1 to user2 and vice versa
            if user2 not in self.network[user1]:
                self.network[user1].append(user2)
            if user1 not in self.network[user2]:
                self.network[user2].append(user1)
            print(f"Connection added between '{user1}' and '{user2}'.")

    def view_all_users(self):
        if not self.network:
            print("No users in the network.")
        else:
            print("Users in the network:")
            for user in self.network:
                print(user)

    def view_all_connections(self):
        if not self.network:
            print("No connections in the network.")
        else:
            print("Connections in the network:")
            for user, connections in self.network.items():
                if connections:
                    for connection in connections:
                        print(f"{user} is connected to {connection}")
                else:
                    print(f"{user} has no connections.")

    def display_graph(self):
        if not self.network:
            print("No users or connections to display.")
            return

        # Create a graph object using networkx
        G = nx.Graph()

        # Add edges (connections) to the graph
        for user, connections in self.network.items():
            for connection in connections:
                G.add_edge(user, connection)

        # Draw the graph
        plt.figure(figsize=(8, 6))
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold')
        plt.title("Social Network Connections")
        plt.show()


def main_menu():
    manager = ConnectionsManager()

    while True:
        print("\n=== Social Media Connections Manager ===")
        print("1. Add User")
        print("2. Add Connection")
        print("3. View All Users")
        print("4. View All Connections")
        print("5. Display Graph")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            user = input("Enter the username to add: ")
            manager.add_user(user)
        elif choice == '2':
            user1 = input("Enter the first username: ")
            user2 = input("Enter the second username: ")
            manager.add_connection(user1, user2)
        elif choice == '3':
            manager.view_all_users()
        elif choice == '4':
            manager.view_all_connections()
        elif choice == '5':
            manager.display_graph()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()
