import tkinter as tk

class Employee:
    def __init__(self, name):
        self.name = name

class TimeLog:
    def __init__(self, employee, hours):
        self.employee = employee
        self.hours = hours

class TimeTrackingSystem:
    def __init__(self):
        self.logs = []

    def add_log(self, employee_name, hours):
        employee = Employee(employee_name)
        log = TimeLog(employee, hours)
        self.logs.append(log)

    def get_logs(self):
        return self.logs


# GUI
system = TimeTrackingSystem()

def add_entry():
    name = name_entry.get()
    hours = hours_entry.get()
    
    if name and hours:
        system.add_log(name, hours)
        output.insert(tk.END, f"{name} worked {hours} hours\n")
        name_entry.delete(0, tk.END)
        hours_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Time Tracking System")

tk.Label(root, text="Employee Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Hours Worked").pack()
hours_entry = tk.Entry(root)
hours_entry.pack()

tk.Button(root, text="Add Entry", command=add_entry).pack()

output = tk.Text(root, height=10, width=30)
output.pack()

root.mainloop()