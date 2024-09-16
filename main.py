import csv
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of voting locations
voting_locations = ["School", "Recreation Center", "Office", "Fire Station", "City Hall"]

# Custom dialog to increase the size of input boxes
class CustomDialog(simpledialog._QueryString):
    def __init__(self, master, title, prompt):
        self.entry_width = 50  # Set the desired width of the entry box here
        super().__init__(master, title, prompt)

    def body(self, master):
        tk.Label(master, text=self.prompt, justify=tk.LEFT, wraplength=400).grid(row=0, padx=5, pady=5)
        self.entry = tk.Entry(master, name="entry", width=self.entry_width)
        self.entry.grid(row=1, padx=5, pady=5)
        return self.entry

# Custom dialog for casting votes with a larger window
class VoteDialog(simpledialog.Dialog):
    def __init__(self, master, title, candidate_1_name, candidate_2_name):
        self.candidate_1_name = candidate_1_name
        self.candidate_2_name = candidate_2_name
        super().__init__(master, title)

    def body(self, master):
        self.geometry("400x350")  # Set the desired size of the vote window here
        tk.Label(master, text=f"🗳️ Cast your vote:\nType 'votea' for {self.candidate_1_name}\nType 'voteb' for {self.candidate_2_name}\nType 'end' to end voting", justify=tk.LEFT, wraplength=400).pack(padx=5, pady=5)
        self.entry = tk.Entry(master, name="entry")
        self.entry.pack(padx=5, pady=5)
        return self.entry

    def apply(self):
        self.result = self.entry.get()

# All U.S. states with their respective electoral votes
states = {
    "Alabama": 9,
    "Alaska": 3,
    "Arizona": 11,
    "Arkansas": 6,
    "California": 54, # Adjusted for 2020 Census
    "Colorado": 10,
    "Connecticut": 7,
    "Delaware": 3,
    "District of Columbia": 3, # Washington, D.C.
    "Florida": 30,
    "Georgia": 16,
    "Hawaii": 4,
    "Idaho": 4,
    "Illinois": 19,
    "Indiana": 11,
    "Iowa": 6,
    "Kansas": 6,
    "Kentucky": 8,
    "Louisiana": 8,
    "Maine": 4,
    "Maryland": 10,
    "Massachusetts": 11,
    "Michigan": 15,
    "Minnesota": 10,
    "Mississippi": 6,
    "Missouri": 10,
    "Montana": 3,
    "Nebraska": 5,
    "Nevada": 6,
    "New Hampshire": 4,
    "New Jersey": 14,
    "New Mexico": 5,
    "New York": 28,
    "North Carolina": 16,
    "North Dakota": 3,
    "Ohio": 17,
    "Oklahoma": 7,
    "Oregon": 7,
    "Pennsylvania": 19,
    "Rhode Island": 4,
    "South Carolina": 9,
    "South Dakota": 3,
    "Tennessee": 11,
    "Texas": 40,
    "Utah": 6,
    "Vermont": 3,
    "Virginia": 13,
    "Washington": 12,
    "West Virginia": 4,
    "Wisconsin": 10,
    "Wyoming": 3
}

def cast_vote(vote, candidate_1_votes, candidate_2_votes, total_votes, candidate_1_name, candidate_2_name):
    location = random.choice(voting_locations)  # Randomly select a voting location
    logging.info(f"Vote cast at {location}: {vote}")
    
    if vote.lower() == 'votea':
        candidate_1_votes += 1
        total_votes += 1
        messagebox.showinfo("Vote Recorded", f"🗳️ Vote recorded for {candidate_1_name} at {location}! 🥳")
    elif vote.lower() == 'voteb':
        candidate_2_votes += 1
        total_votes += 1
        messagebox.showinfo("Vote Recorded", f"🗳️ Vote recorded for {candidate_2_name} at {location}! 🥳")
    else:
        messagebox.showerror("Invalid Vote", "Please enter a valid vote ('votea' or 'voteb').")
    
    logging.info(f"Current votes - {candidate_1_name}: {candidate_1_votes}, {candidate_2_name}: {candidate_2_votes}, Total: {total_votes}")
    return candidate_1_votes, candidate_2_votes, total_votes

# (Other functions remain the same)

def run_simulator():
    global root  # Ensure root is declared globally
    while True:
        # Validation loop for Candidate 1 name
        while True:
            candidate_1_name = CustomDialog(root, "Candidate 1", "Enter the name of Candidate 1:").result
            if candidate_1_name is None:
                logging.info("Simulation cancelled by user.")
                return  # User cancelled

            if len(candidate_1_name.strip()) < 2:
                messagebox.showerror("Invalid Name", "Candidate name must be more than one letter. Please enter a valid name.")
                continue
            break

        # Validation loop for Candidate 2 name
        while True:
            candidate_2_name = CustomDialog(root, "Candidate 2", "Enter the name of Candidate 2:").result
            if candidate_2_name is None:
                logging.info("Simulation cancelled by user.")
                return  # User cancelled

            if len(candidate_2_name.strip()) < 2:
                messagebox.showerror("Invalid Name", "Candidate name must be more than one letter. Please enter a valid name.")
                continue
            break

        output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save results as")
        if not output_file:
            logging.info("Simulation cancelled by user.")
            return  # User cancelled

        candidate_1_votes = 0
        candidate_2_votes = 0
        total_votes = 0

        while True:
            vote_dialog = VoteDialog(root, "Vote", candidate_1_name, candidate_2_name)
            vote = vote_dialog.result
            if vote is None:
                logging.info("Voting cancelled by user.")
                return  # User cancelled
            if vote.lower() == 'end':
                break
            candidate_1_votes, candidate_2_votes, total_votes = cast_vote(vote, candidate_1_votes, candidate_2_votes, total_votes, candidate_1_name, candidate_2_name)

        # (Other parts of run_simulator remain the same)

if __name__ == "__main__":
    main()
