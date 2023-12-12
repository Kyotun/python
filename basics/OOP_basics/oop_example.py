from prettytable import  PrettyTable

# Create a PrettyTable object.
table = PrettyTable()

# Add column name and column variables.
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Tychoon"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Align the table to the left.
table.align = "l"

# Print the table.
print(table)