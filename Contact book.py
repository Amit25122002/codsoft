import tkinter as tk
from tkinter import ttk, messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    update_contact_list()

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search_term = search_entry.get().lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    contact_list.delete(0, tk.END)
    for contact in results:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        contacts.pop(selected_index[0])
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "No contact selected.")

root = tk.Tk()
root.title("Contact Management System")
root.geometry("800x600")

style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 12))
style.configure("TLabel", font=('Helvetica', 12))
style.configure("TEntry", font=('Helvetica', 12))

name_label = ttk.Label(root, text="Name:")
name_label.pack()

name_entry = ttk.Entry(root, width=50)
name_entry.pack()

phone_label = ttk.Label(root, text="Phone:")
phone_label.pack()

phone_entry = ttk.Entry(root, width=50)
phone_entry.pack()

email_label = ttk.Label(root, text="Email:")
email_label.pack()

email_entry = ttk.Entry(root, width=50)
email_entry.pack()

address_label = ttk.Label(root, text="Address:")
address_label.pack()

address_entry = ttk.Entry(root, width=50)
address_entry.pack()

add_button = ttk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

search_label = ttk.Label(root, text="Search:")
search_label.pack()

search_entry = ttk.Entry(root, width=50)
search_entry.pack()

search_button = ttk.Button(root, text="Search", command=search_contact)
search_button.pack()

delete_button = ttk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

contact_list = tk.Listbox(root, width=80, height=10)
contact_list.pack()

update_contact_list()

root.mainloop()
