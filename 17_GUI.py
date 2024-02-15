# GUI with Database Connectivity:
# Develop a database-driven GUI program to manage student information. 
# Set up database connection and Implement features for adding, updating, and deleting student records.

import sqlite3
import tkinter as tk
from tkinter import messagebox
def create_table():
 conn = sqlite3.connect('student_info.db')
 cursor = conn.cursor()
 cursor.execute('''CREATE TABLE IF NOT EXISTS students (
 id INTEGER PRIMARY KEY,
 name TEXT,
 age INTEGER,
 course TEXT
 )''')
 conn.commit()
 conn.close()
# insert data
def insert_record(name, age, course):
 conn = sqlite3.connect('student_info.db')
 cursor = conn.cursor()
 cursor.execute('''INSERT INTO students (name, age, course) VALUES (?, ?, ?)''', (name, age, course))
 conn.commit()
 conn.close()
# update data
def update_record(id, name, age, course):
 conn = sqlite3.connect('student_info.db')
 cursor = conn.cursor()
 cursor.execute('''UPDATE students SET name=?, age=?, course=? WHERE id=?''', (name, age, course, id))
 conn.commit()
 conn.close()
# delete data
def delete_record(id):
 conn = sqlite3.connect('student_info.db')
 cursor = conn.cursor()
 cursor.execute('''
 DELETE FROM students WHERE id=?''', (id,))
 conn.commit()
 conn.close()
# display all records
def show_all_records():
 conn = sqlite3.connect('student_info.db')
 cursor = conn.cursor()
 cursor.execute('''SELECT * FROM students''')
 records = cursor.fetchall()
 conn.close()
 return records
def insert():
 name = name_entry.get()
 age = age_entry.get()
 course = course_entry.get()
 if name and age and course:
  insert_record(name, age, course)
  messagebox.showinfo("Success", "Record inserted successfully.")
 else:
  messagebox.showerror("Error", "Please fill in all fields.")
def update():
 id = id_entry.get()
 name = name_entry.get()
 age = age_entry.get()
 course = course_entry.get()
 if id and name and age and course:
  update_record(id, name, age, course)
  messagebox.showinfo("Success", "Record updated successfully.")
 else:
  messagebox.showerror("Error", "Please fill in all fields.")
def delete():
 id = id_entry.get()
 if id:
  delete_record(id)
  messagebox.showinfo("Success", "Record deleted successfully.")
 else:
  messagebox.showerror("Error", "Please enter ID.")
def display_records():
 records = show_all_records()
 if records:
  for record in records:
   print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Course: {record[3]}")
 else:
   messagebox.showinfo("Empty", "No records found.")
leo = tk.Tk()
leo.title("Student Information")
leo.geometry("400x300")
leo.configure(bg='#e6e6e6')
create_table()
id_label = tk.Label(leo, text="ID:", bg='#e6e6e6')
id_label.grid(row=0, column=0, padx=5, pady=5)
id_entry = tk.Entry(leo)
id_entry.grid(row=0, column=1, padx=5, pady=5)
name_label = tk.Label(leo, text="Name:", bg='#e6e6e6')
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(leo)
name_entry.grid(row=1, column=1, padx=5, pady=5)
age_label = tk.Label(leo, text="Age:", bg='#e6e6e6')
age_label.grid(row=2, column=0, padx=5, pady=5)
age_entry = tk.Entry(leo)
age_entry.grid(row=2, column=1, padx=5, pady=5)
course_label = tk.Label(leo, text="Course:", bg='#e6e6e6')
course_label.grid(row=3, column=0, padx=5, pady=5)
course_entry = tk.Entry(leo)
course_entry.grid(row=3, column=1, padx=5, pady=5)
insert_button = tk.Button(leo, text="Insert Record", command=insert,
bg='#4CAF50', fg='white') # Set background color
insert_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
update_button = tk.Button(leo, text="Update Record",
command=update, bg='#008CBA', fg='white') # Set background color
update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
delete_button = tk.Button(leo, text="Delete Record", command=delete,
bg='#FF0000', fg='white') # Set background color
delete_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
show_all_button = tk.Button(leo, text="Show All Records",
command=display_records, bg='#808080', fg='white') # Set background color
show_all_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
leo.mainloop()


#Assignment(Explore & Try this yourself)
# Imagine you are tasked with developing a registration form for an upcoming event.
# Create a Python script using Tkinter to design a GUI registration form. The form should include the following fields: A text entry for
# the participant to enter their full name. An entry for the participant's age. An entry for the participant's email address. Include a
# dropdown menu or radio buttons for the participant to select their event category (e.g., Workshop, Seminar, Networking). 
# Submit button to print filled form details.
