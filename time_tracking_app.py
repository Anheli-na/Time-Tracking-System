import tkinter as tk
from tkinter import messagebox


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

    def get_total_hours(self):
        total = 0
        for log in self.logs:
            total += log.hours
        return total

    def generate_report(self):
        report = "Employee Time Report\n"
        report += "----------------------\n"

        if not self.logs:
            report += "No time entries yet.\n"
        else:
            for log in self.logs:
                report += f"{log.employee.name}: {log.hours} hours\n"

            report += "----------------------\n"
            report += f"Total Hours: {self.get_total_hours()}"

        return report


system = TimeTrackingSystem()


def add_entry():
    name = name_entry.get().strip()
    hours_text = hours_entry.get().strip()

    if name == "" or hours_text == "":
        messagebox.showerror("Input Error", "Please enter both employee name and hours.")
        return

    try:
        hours = float(hours_text)
        if hours <= 0:
            messagebox.showerror("Input Error", "Hours must be greater than 0.")
            return
    except ValueError:
        messagebox.showerror("Input Error", "Hours must be a number.")
        return

    system.add_log(name, hours)
    output.insert(tk.END, f"{name} worked {hours} hours\n")

    name_entry.delete(0, tk.END)
    hours_entry.delete(0, tk.END)


def show_total_hours():
    total = system.get_total_hours()
    output.insert(tk.END, f"\nTotal Hours Worked: {total}\n")


def show_report():
    report = system.generate_report()
    output.delete("1.0", tk.END)
    output.insert(tk.END, report)


root = tk.Tk()
root.title("Time Tracking System")
root.geometry("450x450")

title_label = tk.Label(root, text="Time Tracking System", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

tk.Label(root, text="Employee Name").pack()
name_entry = tk.Entry(root, width=35)
name_entry.pack(pady=5)

tk.Label(root, text="Hours Worked").pack()
hours_entry = tk.Entry(root, width=35)
hours_entry.pack(pady=5)

tk.Button(root, text="Add Entry", width=20, command=add_entry).pack(pady=5)
tk.Button(root, text="Show Total Hours", width=20, command=show_total_hours).pack(pady=5)
tk.Button(root, text="Generate Report", width=20, command=show_report).pack(pady=5)

output = tk.Text(root, height=12, width=50)
output.pack(pady=10)

root.mainloop()