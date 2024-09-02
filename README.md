# Electoral Votes Simulator 🗳️

Welcome to the Electoral Votes Simulator! This Python program simulates a voting process between two candidates through an engaging graphical user interface (GUI). Users can cast their votes for either Candidate 1 or Candidate 2, and the program will keep track of the votes. When the voting ends, the program displays the final results and exports them to a CSV file.

## How to Use

1. Clone the repository or download the script.
2. Ensure you have Python installed on your system.
3. Run the script using the following command:

    ```bash
    python main.py
    ```

4. Follow the on-screen prompts to cast your vote.

    - Click the `Start Simulation` button to begin.
    - Enter the names of the two candidates.
    - Cast your vote by selecting the appropriate option (1️⃣ for Candidate 1, 2️⃣ for Candidate 2).
    - Click `0️⃣` to finish voting and see the results.

5. After voting ends, the results will be displayed on the screen and saved to a CSV file in the location you choose.

## Screenshots

![1ST](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/1ST.png)
![2ND](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/2ND.png)
![3RD](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/3RD.png)
![4TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/4TH.png)
![5TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/5TH.png)
![6TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/6TH.png)
![7TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/7TH.png)
![8TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/8TH.png)
![9TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/9TH.png)
![10TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/10TH.png)
## after the tie you have to re input the candidates name and re do the voting
![11TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/11TH.png)
![12TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/12TH.png)
![13TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/13TH.png)
![14TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/14TH.png)

## Example CSV Output

```csv
Candidate,Votes,Percentage,Electoral Votes
JOHN ,1,33.33%,151
STEVE,2,66.67%,387
Total Votes,3
```

## Example Usage

```
🗳️ Electoral Votes Simulator
🏁 Start Simulation ❌ Exit
[User clicks 'Start Simulation']
```

```
Enter the name of Candidate 1: Alice
Enter the name of Candidate 2: Bob
```

```
🗳️ Cast your vote:
1️⃣ for Alice
2️⃣ for Bob
0️⃣ to end voting
[User casts votes and ends voting]
```

- Voting has ended. Here are the results:
    - Alice: 2 votes 🗳️
    - Bob: 1 vote 🗳️
    - Total Votes Cast: 3
    - Results exported to vote_results.csv

## Features

- **Interactive GUI:** A user-friendly graphical interface that guides users through the voting process.
- **Real-Time Feedback:** Users receive instant feedback as votes are cast, with dynamic updates to the vote counts.
- **Electoral College Simulation:** The program simulates an electoral college system based on state votes, providing a realistic representation of the voting process.
- **Tie Handling:** The program detects ties in both popular and electoral votes and automatically restarts the voting process to ensure a clear winner.
- **CSV Export:** The final results, including both popular and electoral votes, are saved to a CSV file for easy record-keeping and analysis.
- **Error Handling:** Robust error handling ensures the program runs smoothly even if unexpected inputs are encountered.

## Contributing
- Contributions are welcome! Please feel free to submit a Pull Request with your improvements, bug fixes, or new features.

---

Happy Voting! 🎉

## Acknowledgements 

- **Contributed by:** [Bubbles The Dev](https://github.com/kernferm)
- **Forked from:** [jpb1991](https://github.com/jpb1991)









