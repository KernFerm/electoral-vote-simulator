# Electoral Votes Simulator

Welcome to the Electoral Votes Simulator! This Python program simulates a voting process between two candidates. Users can cast their votes for either Candidate 1 or Candidate 2, and the program will keep track of the votes. When the voting ends, the program displays the final results and exports them to a CSV file.

## How to Use

1. Clone the repository or download the script.
2. Ensure you have Python installed on your system.
3. Run the script using the following command:

    ```
    python main.py
    ```

4. Follow the on-screen prompts to cast your vote.

    - Type `vote 1` or `1` to vote for Candidate 1.
    - Type `vote 2` or `2` to vote for Candidate 2.
    - Type `end` to finish voting and see the results.

5. After voting ends, the results will be displayed on the screen and saved to a CSV file named `vote_results.csv` in the same directory.

## Example Usage

```
Welcome to the Electoral Votes Simulator! Type 'vote 1' to vote for Candidate 1, 'vote 2' to vote for Candidate 2, or 'end' to finish voting.

Cast your vote (vote 1/vote 2) or type 'end' to finish: 1 Vote recorded for Candidate 1!

Cast your vote (vote 1/vote 2) or type 'end' to finish: 2 Vote recorded for Candidate 2!

Cast your vote (vote 1/vote 2) or type 'end' to finish: 1 Vote recorded for Candidate 1!

Cast your vote (vote 1/vote 2) or type 'end' to finish: end

Voting has ended. Here are the results: Candidate 1: 2 votes Candidate 2: 1 vote Total Votes Cast: 3

Results exported to vote_results.csv
```


## Features

- **Simple Voting Simulation:** Users can cast votes for two candidates.
- **Real-time Feedback:** The program confirms each vote and notifies users of invalid commands.
- **Final Vote Count:** Displays the total votes for each candidate and the overall number of votes.
- **CSV Export:** The final results are saved to a CSV file for easy record-keeping and analysis.

## Future Improvements

- Add more candidates to the simulation.
- Implement advanced voting systems, such as electoral college simulations.
- Simulate randomized vote distributions to create more complex scenarios.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request with your improvements, bug fixes, or new features.
