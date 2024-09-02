import csv
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# Custom dialog to increase the size of input boxes
class CustomDialog(simpledialog._QueryString):
    def __init__(self, master, title, prompt):
        self.entry_width = 40  # Set the desired width of the entry box here
        super().__init__(master, title, prompt)

    def body(self, master):
        tk.Label(master, text=self.prompt, justify=tk.LEFT, wraplength=400).grid(row=0, padx=5, pady=5)
        self.entry = tk.Entry(master, name="entry", width=self.entry_width)
        self.entry.grid(row=1, padx=5, pady=5)
        return self.entry

# All U.S. states with their respective electoral votes
states = {
    "Alabama": 9,
    "Alaska": 3,
    "Arizona": 11,
    "Arkansas": 6,
    "California": 55,
    "Colorado": 9,
    "Connecticut": 7,
    "Delaware": 3,
    "District of Columbia": 3,
    "Florida": 29,
    "Georgia": 16,
    "Hawaii": 4,
    "Idaho": 4,
    "Illinois": 20,
    "Indiana": 11,
    "Iowa": 6,
    "Kansas": 6,
    "Kentucky": 8,
    "Louisiana": 8,
    "Maine": 4,
    "Maryland": 10,
    "Massachusetts": 11,
    "Michigan": 16,
    "Minnesota": 10,
    "Mississippi": 6,
    "Missouri": 10,
    "Montana": 3,
    "Nebraska": 5,
    "Nevada": 6,
    "New Hampshire": 4,
    "New Jersey": 14,
    "New Mexico": 5,
    "New York": 29,
    "North Carolina": 15,
    "North Dakota": 3,
    "Ohio": 18,
    "Oklahoma": 7,
    "Oregon": 7,
    "Pennsylvania": 20,
    "Rhode Island": 4,
    "South Carolina": 9,
    "South Dakota": 3,
    "Tennessee": 11,
    "Texas": 38,
    "Utah": 6,
    "Vermont": 3,
    "Virginia": 13,
    "Washington": 12,
    "West Virginia": 5,
    "Wisconsin": 10,
    "Wyoming": 3,
}

def cast_vote(vote, candidate_1_votes, candidate_2_votes, total_votes, candidate_1_name, candidate_2_name):
    if vote == 1:
        candidate_1_votes += 1
        total_votes += 1
        messagebox.showinfo("Vote Recorded", f"🗳️ Vote recorded for {candidate_1_name}! 🥳")
    elif vote == 2:
        candidate_2_votes += 1
        total_votes += 1
        messagebox.showinfo("Vote Recorded", f"🗳️ Vote recorded for {candidate_2_name}! 🥳")
    else:
        messagebox.showerror("Invalid Vote", "Please enter a valid vote (1 or 2).")
    return candidate_1_votes, candidate_2_votes, total_votes

def export_results_to_csv(candidate_1_votes, candidate_2_votes, total_votes, candidate_1_name, candidate_2_name, candidate_1_electoral_votes, candidate_2_electoral_votes, filename):
    candidate_1_percentage = (candidate_1_votes / total_votes) * 100 if total_votes > 0 else 0
    candidate_2_percentage = (candidate_2_votes / total_votes) * 100 if total_votes > 0 else 0
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Candidate", "Votes", "Percentage", "Electoral Votes"])
        writer.writerow([candidate_1_name, candidate_1_votes, f"{candidate_1_percentage:.2f}%", candidate_1_electoral_votes])
        writer.writerow([candidate_2_name, candidate_2_votes, f"{candidate_2_percentage:.2f}%", candidate_2_electoral_votes])
        writer.writerow(["Total Votes", total_votes])
    messagebox.showinfo("Export Successful", f"📁 Results exported to {filename}")

def simulate_electoral_college(candidate_1_name, candidate_2_name):
    candidate_1_electoral_votes = 0
    candidate_2_electoral_votes = 0

    result_text = "\nElectoral College Results:\n"
    for state, electoral_votes in states.items():
        candidate_1_state_votes = random.randint(0, 100)
        candidate_2_state_votes = 100 - candidate_1_state_votes

        if candidate_1_state_votes > candidate_2_state_votes:
            candidate_1_electoral_votes += electoral_votes
            result_text += f"{candidate_1_name} wins {state} with {candidate_1_state_votes}% of the vote. 🎉\n"
        else:
            candidate_2_electoral_votes += electoral_votes
            result_text += f"{candidate_2_name} wins {state} with {candidate_2_state_votes}% of the vote. 🎉\n"

    result_text += f"\n{candidate_1_name}: {candidate_1_electoral_votes} electoral votes 🗳️\n"
    result_text += f"{candidate_2_name}: {candidate_2_electoral_votes} electoral votes 🗳️\n"

    # Determine the winner based on electoral votes
    if candidate_1_electoral_votes > candidate_2_electoral_votes:
        result_text += f"\n{candidate_1_name} wins the Electoral College with {candidate_1_electoral_votes} votes! 🎉"
    else:
        result_text += f"\n{candidate_2_name} wins the Electoral College with {candidate_2_electoral_votes} votes! 🎉"

    return candidate_1_electoral_votes, candidate_2_electoral_votes, result_text

def run_simulator():
    global root  # Ensure root is declared globally
    while True:
        candidate_1_name = CustomDialog(root, "Candidate 1", "Enter the name of Candidate 1:").result
        if candidate_1_name is None:
            return  # User cancelled

        candidate_2_name = CustomDialog(root, "Candidate 2", "Enter the name of Candidate 2:").result
        if candidate_2_name is None:
            return  # User cancelled

        output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save results as")
        if not output_file:
            return  # User cancelled

        candidate_1_votes = 0
        candidate_2_votes = 0
        total_votes = 0

        while True:
            vote = simpledialog.askinteger("Vote", f"🗳️ Cast your vote:\n1️⃣ for {candidate_1_name}\n2️⃣ for {candidate_2_name}\n0️⃣ to end voting", minvalue=0, maxvalue=2)
            if vote is None:
                return  # User cancelled
            if vote == 0:
                break
            candidate_1_votes, candidate_2_votes, total_votes = cast_vote(vote, candidate_1_votes, candidate_2_votes, total_votes, candidate_1_name, candidate_2_name)

        # Determine winner based on total votes
        if candidate_1_votes == candidate_2_votes:
            messagebox.showwarning("Tie!", f"The votes are tied at {candidate_1_votes} to {candidate_2_votes}. The voting process will be restarted.")
            continue  # Restart the voting process
        elif candidate_1_votes > candidate_2_votes:
            messagebox.showinfo("Winner", f"{candidate_1_name} wins with {candidate_1_votes} votes!")
        else:
            messagebox.showinfo("Winner", f"{candidate_2_name} wins with {candidate_2_votes} votes!")

        candidate_1_electoral_votes, candidate_2_electoral_votes, result_text = simulate_electoral_college(candidate_1_name, candidate_2_name)

        # Check for a tie in the electoral votes
        if candidate_1_electoral_votes == candidate_2_electoral_votes:
            messagebox.showwarning("Tie!", f"There is a tie in electoral votes: {candidate_1_electoral_votes} to {candidate_2_electoral_votes}. The voting process will be restarted.")
            continue  # Restart the voting process
        else:
            display_results(candidate_1_votes, candidate_2_votes, total_votes, candidate_1_name, candidate_2_name)
            messagebox.showinfo("Electoral College Results", result_text)
            export_results_to_csv(candidate_1_votes, candidate_2_votes, total_votes, candidate_1_name, candidate_2_name, candidate_1_electoral_votes, candidate_2_electoral_votes, output_file)
            break

def display_results(candidate_1_votes, candidate_2_votes, total_votes, candidate_1_name, candidate_2_name):
    result_text = f"\nVoting has ended. Here are the results:\n\n"
    result_text += f"{candidate_1_name}: {candidate_1_votes} votes 🗳️\n"
    result_text += f"{candidate_2_name}: {candidate_2_votes} votes 🗳️\n"
    result_text += f"Total Votes Cast: {total_votes}\n"
    messagebox.showinfo("Results", result_text)

def main():
    global root
    root = tk.Tk()
    root.title("🗳️ Electoral Votes Simulator")

    # Set the size of the main window (larger size) and center it on the screen
    window_width = 600
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height/2 - window_height/2)
    position_right = int(screen_width/2 - window_width/2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    tk.Label(root, text="🗳️ Electoral Votes Simulator", font=("Arial", 20)).pack(pady=30)
    tk.Button(root, text="🏁 Start Simulation", command=run_simulator, font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="❌ Exit", command=root.quit, font=("Arial", 14)).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
