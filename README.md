# Electoral Votes Simulator 🗳️

Welcome to the Electoral Votes Simulator! This Python application simulates a voting process between two candidates using a user-friendly graphical interface. It allows users to cast votes, see the results, and export the data to a CSV file.

## Features

- **Intuitive GUI**: Simple and interactive interface for an engaging user experience.
- **Customizable Dialogs**: Input dialogs with adjustable sizes for easier data entry.
- **Real-Time Voting**: Cast votes for two candidates and view results instantly.
- **CSV Export**: Save voting results to a CSV file for record-keeping and analysis.
- **Detailed Logging**: Monitor and track user interactions and system activities.

## Prerequisites

Ensure Python is installed on your system. The script uses standard Python libraries, so no additional packages are required:

- `tkinter` (usually included with Python)
- `logging` (standard library)
- `csv` (standard library)
- `random` (standard library)

## Installation

1. **Download the Script**: Obtain the `main.py` script from the repository or another source.
2. **Install Python**: Make sure Python is installed on your computer. If not, download and install it from [python.org](https://www.python.org/).

## Usage

1. **Run the Script**: Open a terminal or command prompt and navigate to the directory containing `main.py`. Execute the script with:

    ```bash
    python main.py
    ```

2. **Start the Simulation**:
    - Click the `Start Simulation` button to begin.
    - Enter the names of the two candidates when prompted.
    - Cast your vote by entering `1️⃣` for Candidate 1 or `2️⃣` for Candidate 2.
    - Enter `0️⃣` to end voting and display the results.

3. **View Results**:
    - After voting concludes, the results will be shown on-screen.
    - Choose a location to save the results in a CSV file for future reference.

4. **Handling Ties**:
    - In case of a tie, you will be prompted to re-enter the candidates' names and restart the voting process.


## Screenshots

Here are some screenshots of the application:

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
![11TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/11TH.png)
![12TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/12TH.png)
![13TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/13TH.png)
![14TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/14TH.png)
![15TH](https://github.com/KernFerm/electoral-vote-simulator/blob/main/screenshots/15TH.png)

## Logging

The Electoral Votes Simulator includes detailed logging functionality to help monitor user interactions and system activities. The logging feature is configured at the start of the script and records significant events during the application's runtime. 

### How Logging is Used

1. **Initialization**:
   - When the application starts, a log entry is created to indicate the launch of the simulator.

2. **User Actions**:
   - Every time a vote is cast, the system logs the vote details, including which candidate received the vote and the current vote count.
   - If the user cancels the simulation or voting process, this action is also logged for future reference.

3. **Simulation Results**:
   - The results of the voting process, including the final vote tally for each candidate and the overall winner, are logged.
   - Electoral College simulation results are logged, detailing how many electoral votes each candidate received.

4. **Data Export**:
   - When the voting results are exported to a CSV file, the system logs the file path and confirms the successful export.

### Log Format

The logs are written in the following format:

**Example:**
```
2024-09-03 12:34:56,789 - INFO - Electoral Votes Simulator started.
2024-09-03 12:35:01,234 - INFO - Vote cast: votea
2024-09-03 12:35:05,678 - INFO - Current votes - Candidate 1: 5, Candidate 2: 3, Total: 8
2024-09-03 12:35:10,456 - INFO - Results exported to /path/to/results.csv
```
- Note: The application uses the `os` module to ensure that file paths are accurate and absolute, especially when exporting results to a CSV file. This helps avoid issues related to relative paths and ensures that the log accurately reflects the correct file location.

## Contribution

If you encounter issues or have suggestions for improvements, feel free to modify the script or contact the repository maintainer.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/KernFerm/electoral-vote-simulator/blob/main/LICENSE) file for details.

## Acknowledgements

- **`tkinter`**: For providing a powerful and flexible GUI toolkit.
- **Python Community**: For continuous support and development of Python libraries.

Enjoy using the Electoral Votes Simulator! If you have any questions or feedback, don't hesitate to reach out.
