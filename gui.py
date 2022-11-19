import sql
import tkinter as tk

root = tk.Tk()
root.title("Database")
root.geometry("400x550")

def create_db():

    def button(dbname):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.create_db(dbname)
        tk.Label(root, text="Database created successfully").grid(row=0, column=0)
    
        menu()

    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Button(root, text="Create Database", command=lambda: button(dbname.get())).grid(row=1, column=1)
    
    menu()

def create_table():
    
    def button(dbname, table_name, structure):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.create_table(dbname, table_name, structure)
        tk.Label(root, text="Table created successfully").grid(row=0, column=0)
    
        menu()

    for child in root.winfo_children():
        child.destroy()

    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the structure: ").grid(row=2, column=0)
    structure = tk.Entry(root)
    structure.grid(row=2, column=1)
    tk.Button(root, text="Create Table", command=lambda: button(dbname.get(), table_name.get(), structure.get())).grid(row=4, column=1)
    
    menu()

def drop_column():
    
    def button(dbname, table_name, column_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.drop_column(dbname, table_name, column_name)
        tk.Label(root, text="Column dropped successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
     
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.Button(root, text="Drop Column", command=lambda: button(dbname.get(), table_name.get(), column_name.get())).grid(row=4, column=1)
    
    menu()

def create_column():
    
    def button(dbname, table_name, column_name, column_type):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.create_column(dbname, table_name, column_name, column_type)
        tk.Label(root, text="Column created successfully").grid(row=0, column=0)
    
        menu()

    for child in root.winfo_children():
        child.destroy()

    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.Label(root, text="Enter the column type: ").grid(row=3, column=0)
    column_type = tk.Entry(root)
    column_type.grid(row=3, column=1)
    tk.Button(root, text="Create Column", command=lambda: button(dbname.get(), table_name.get(), column_name.get(), column_type.get())).grid(row=4, column=1)
    
    menu()

def insert_data():
    
    def button(dbname , table_name, values):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.insert_data(dbname, table_name, values)
        tk.Label(root, text="Data inserted successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
     
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the values: ").grid(row=2, column=0)
    values = tk.Entry(root)
    values.grid(row=2, column=1)
    tk.Button(root, text="Insert Data", command=lambda: button(dbname.get(), table_name.get(), values.get())).grid(row=4, column=1)
    
    menu()

def update_data():
    
    def button(dbname, table_name, column_names, column_values, condition):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.update_data(dbname , table_name, column_names, column_values, condition)
        tk.Label(root, text="Data updated successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the values: ").grid(row=2, column=0)
    values = tk.Entry(root)
    values.grid(row=2, column=1)
    tk.Label(root, text="Enter the where clause: ").grid(row=3, column=0)
    where_clause = tk.Entry(root)
    where_clause.grid(row=3, column=1)
    tk.Label(root, text="Enter the column names: ").grid(row=4, column=0)
    column_names = tk.Entry(root)
    column_names.grid(row=4, column=1)
    tk.Label(root, text="Enter the column values: ").grid(row=5, column=0)
    column_values = tk.Entry(root)
    column_values.grid(row=5, column=1)
    tk.Button(root, text="Update Data", command=lambda: button(dbname.get(), table_name.get(), column_names.get(), column_values.get(), where_clause.get())).grid(row=4, column=1)
    
    menu()

def delete_data():
    
    def button(dbname, table_name, condition):
    
        for child in root.winfo_children():
            child.destroy()
        sql.delete_data(dbname, table_name, condition)
        tk.Label(root, text="Data deleted successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the where clause: ").grid(row=2, column=0)
    where_clause = tk.Entry(root)
    where_clause.grid(row=2, column=1)
    tk.Button(root, text="Delete Data", command=lambda: button(dbname.get(), table_name.get(), where_clause.get())).grid(row=4, column=1)
    
    menu()

def show_table():

    def button(dbname):
    
        for child in root.winfo_children():
            child.destroy()
    
        result = sql.show_table(dbname)

        tk.Label(root, text="Table: ").grid(row=0, column=0)

        for i in range(len(result)):
            tk.Label(root, text=result[i]).grid(row=i+1, column=0)        
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Button(root, text="Show Table", command=lambda: button(dbname.get())).grid(row=4, column=1)

    menu()

def describe():
    
    def button(dbname, table_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        result = sql.describe(dbname, table_name)

        tk.Label(root, text="Result: ").grid(row=0, column=0)
        result_box = tk.Text(root, height=10, width=30)
        result_box.grid(row=1, column=0)
        result_box.config(state="normal")
        result_box.config(height=len(result))
        result_box.config(width= 50)

        for i in range(len(result)):

            result_box.insert(tk.END, result[i])
            result_box.insert(tk.END, "\n")

        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Button(root, text="Describe Table", command=lambda: button(dbname.get(), table_name.get())).grid(row=4, column=1)
    
    menu()

def add_primary_key():
    
    def button(dbname, table_name, column_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.add_primary_key(dbname, table_name, column_name)
        tk.Label(root, text="Primary key added successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
     
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.Button(root, text="Add Primary Key", command=lambda: button(dbname.get(), table_name.get(), column_name.get())).grid(row=4, column=1)
    
    menu()

def delete_primary_key():
    
    def button(dbname, table_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.delete_primary_key(dbname, table_name)
        tk.Label(root, text="Primary key deleted successfully").grid(row=0, column=0)
    
        menu()

    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Button(root, text="Delete Primary Key", command=lambda: button(dbname.get(), table_name.get())).grid(row=4, column=1)
    
    menu()

def aggregate():
    
    def button(dbname, table_name, column_name, aggregate_function):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.aggregate(dbname, table_name, column_name, aggregate_function)
        tk.Label(root, text="Aggregate performed successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
     
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.Label(root, text="Enter the aggregate function: ").grid(row=3, column=0)
    function = tk.Entry(root)
    function.grid(row=3, column=1)
    tk.Button(root, text="Aggregate", command=lambda: button(dbname.get(), table_name.get(), column_name.get(), function.get())).grid(row=4, column=1)
    
    menu()

def drop_db():
    
    def button(dbname):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.drop_db(dbname)
        tk.Label(root, text="Database dropped successfully").grid(row=0, column=0)
    
        menu()

    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Button(root, text="Drop Database", command=lambda: button(dbname.get())).grid(row=4, column=1)
    
    menu()

def drop_table():
    
    def button(dbname, table_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.drop_table(dbname, table_name)
        tk.Label(root, text="Table dropped successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Button(root, text="Drop Table", command=lambda: button(dbname.get(), table_name.get())).grid(row=4, column=1)
    
    menu()

def drop_column():
    
    def button(dbname, table_name, column_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.drop_column(dbname, table_name, column_name)
        tk.Label(root, text="Column dropped successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.Button(root, text="Drop Column", command=lambda: button(dbname.get(), table_name.get(), column_name.get())).grid(row=4, column=1)
    
    menu()

def select():
    
    def button(dbname, table_name, column_names, value):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.select(dbname, table_name, column_names, value)
        
        tk.Label(root, text="Select performed successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.Label(root, text="Enter the where clause of the column: ").grid(row=3, column=0)
    value = tk.Entry(root)
    value.grid(row=3, column=1)
    tk.Button(root, text="Select", command=lambda: button(dbname.get(), table_name.get(), column_name.get(), value.get())).grid(row=4, column=1)
    
    menu()

def show_databases():
    
    for child in root.winfo_children():
        child.destroy()
    
    result = sql.show_databases()
    tk.Label(root, text="Databases displayed successfully").grid(row=0, column=0)
    
    for i in range(len(result)):
        tk.Label(root, text=result[i]).grid(row=i+1, column=0, sticky=tk.W)
    tk.Label(root, text="").grid(row=2, column=0)

    menu()

def truncate_table():
    
    def button(dbname, table_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.truncate_table(dbname, table_name)
        tk.Label(root, text="Table truncated successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Button(root, text="Truncate Table", command=lambda: button(dbname.get(), table_name.get())).grid(row=4, column=1)
    
    menu()

def backup_db():

    def button(dbname, path, differential):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.backup_db(dbname, path, differential)
        tk.Label(root, text="Database backed up successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()

    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the path of the backup: ").grid(row=1, column=0)
    path = tk.Entry(root)
    path.grid(row=1, column=1)
    tk.Label(root, text="Is this a differential backup? (y-1/n-0): ").grid(row=2, column=0)
    differential = tk.Entry(root)
    differential.grid(row=2, column=1)
    tk.Button(root, text="Backup Database", command=lambda: button(dbname.get(), path.get(), differential.get())).grid(row=4, column=1)

    menu()

def restore_db():

    def button(dbname, path):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.restore_db(dbname, path)
        tk.Label(root, text="Database restored successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()

    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the path of the backup: ").grid(row=1, column=0)
    path = tk.Entry(root)
    path.grid(row=1, column=1)
    tk.Button(root, text="Restore Database", command=lambda: button(dbname.get(), path.get())).grid(row=4, column=1)

    menu()


def menu():

    menu = tk.Menu(root)
    
    root.config(menu=menu)
    
    subMenu = tk.Menu(menu)
    menu.add_cascade(label=" Create", menu=subMenu)
    subMenu.add_command(label="Database", command=create_db)
    subMenu.add_command(label="Table", command=create_table)
    subMenu.add_command(label="Column", command=create_column)
    
    subMenu = tk.Menu(menu)
    menu.add_cascade(label="Drop", menu=subMenu)
    subMenu.add_command(label="Database", command=drop_db)
    subMenu.add_command(label="Table", command=drop_table)
    subMenu.add_command(label="Column", command=drop_column)
    subMenu.add_command(label="Truncate", command=truncate_table)
    
    subMenu = tk.Menu(menu)
    menu.add_cascade(label="Query", menu=subMenu)
    subMenu.add_command(label="Aggregate", command= aggregate)
    subMenu.add_command(label="Select", command= select)
    
    subMenu = tk.Menu(menu)
    menu.add_cascade(label="Schema", menu=subMenu)
    subMenu.add_command(label="Show Tables", command= show_table)
    subMenu.add_command(label="Show Databases", command= show_databases)
    subMenu.add_command(label="Describe", command= describe)

    subMenu = tk.Menu(menu)
    menu.add_cascade(label="DML", menu=subMenu)
    subMenu.add_command(label="Add Primary Key", command= add_primary_key)
    subMenu.add_command(label="Delete Primary Key", command= delete_primary_key)
    subMenu.add_command(label="Insert", command= insert_data)
    subMenu.add_command(label="Update", command= update_data)
    subMenu.add_command(label="Delete", command= delete_data)

    subMenu = tk.Menu(menu)
    menu.add_cascade(label="Backup", menu=subMenu)
    subMenu.add_command(label="Backup Database", command= backup_db)
    subMenu.add_command(label="Restore Database", command= restore_db)

    subMenu = tk.Menu(menu)
    menu.add_cascade(label="Exit", menu=subMenu)
    subMenu.add_command(label="Exit", command=root.quit)
    
    return menu

menu()
root.mainloop()