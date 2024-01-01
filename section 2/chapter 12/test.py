import tkinter as tk
from datetime import timedelta

class TimeManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Time management app')
        self.master.minsize(width=700, height=500)

        # Creating UI elements
        self.timer_label = tk.Label(self.master, text='', font=('Helvetica', 48))
        self.timer_label.pack(pady=10)

        self.start_button = tk.Button(self.master, text='Start', command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.master, text='Stop', command=self.stop_timer)
        self.stop_button.pack(pady=5)

        # Initial durations for work and break intervals
        self.work_duration = timedelta(minutes=25)
        self.break_duration = timedelta(minutes=5)
        self.is_working = 'Default'

        # Initialize the display
        self.update_display()

    def update_display(self):
        # Update the timer label text and color based on the current interval
        if self.is_working == 'Default':
            self.timer_label.config(text='00:00')
            self.timer_label.config(fg='white')  # Set text color to white for initial state
        elif self.is_working == 'Working':
            self.timer_label.config(text=str(self.work_duration))
            self.timer_label.config(fg='green')  # Set text color to green during work
        else:
            self.timer_label.config(text=str(self.break_duration))
            self.timer_label.config(fg='red')  # Set text color to red during break

    def update_timer(self):
        if self.is_working == 'Working':
            # Decrease work duration by 1 second
            self.work_duration -= timedelta(seconds=1)
        elif self.is_working == 'Break':
            # Decrease break duration by 1 second
            self.break_duration -= timedelta(seconds=1)

        # Update the display
        self.update_display()

        # If there is time remaining, schedule the update_timer function to be called after 1000 milliseconds
        if self.work_duration.total_seconds() > 0 or self.break_duration.total_seconds() > 0:
            self.master.after(1000, self.update_timer)
        else:
            # If the interval is completed, toggle to the next interval
            if self.is_working == 'Working':
                self.is_working = 'Break'
            elif self.is_working == 'Break':
                self.is_working = 'Working'

            # Reset durations based on the next interval
            if self.is_working == 'Working':
                self.work_duration = timedelta(minutes=25)
            elif self.is_working == 'Break':
                self.break_duration = timedelta(minutes=5)

            # Update the display and schedule the next update_timer call
            self.update_display()
            self.master.after(1000, self.update_timer)

    def start_timer(self):
        # Toggle between work and break intervals
        if self.is_working == 'Default':
            self.is_working = 'Working'
        elif self.is_working == 'Working':
            self.is_working = 'Break'
        elif self.is_working == 'Break':
            self.is_working = 'Working'

        self.update_display()
        # Schedule the update_timer function to be called after 1000 milliseconds (1 second)
        self.master.after(1000, self.update_timer)

    def stop_timer(self):
        # Stop the timer
        self.is_working = 'Default'
        self.work_duration = timedelta(minutes=25)
        self.break_duration = timedelta(minutes=5)
        self.update_display()

# Create a Tkinter root window
if __name__ == '__main__':
    root = tk.Tk()
    # Create an instance of the Time management app class
    app = TimeManagementApp(root)
    # Start the Tkinter event loop
    root.mainloop()
