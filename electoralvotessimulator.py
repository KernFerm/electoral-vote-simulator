import random

def cast_vote(vote, candidate_1_votes, candidate_2_votes, total_votes):
    if vote == "vote 1":
        candidate_1_votes += 1
        total_votes += 1
        print("Vote recorded for Candidate 1!")
    elif vote == "vote 2":
        candidate_2_votes += 1
        total_votes += 1
        print("Vote recorded for Candidate 2!")
    else:
        print("Invalid command. Please try again.")
    return candidate_1_votes, candidate_2_votes, total_votes

def display_results(candidate_1_votes, candidate_2_votes, total_votes):
    print("\nVoting has ended. Here are the results:")
    print(f"Candidate 1: {candidate_1_votes} votes")
    print(f"Candidate 2: {candidate_2_votes} votes")
    print(f"Total Votes Cast: {total_votes}")

def main():
    # Initialize vote counts
    candidate_1_votes = 0
    candidate_2_votes = 0
    total_votes = 0

    print("Welcome to the Electoral Votes Simulator!")
    print("Type 'vote 1' to vote for Candidate 1, 'vote 2' for Candidate 2, or 'end' to finish voting.\n")

    while True:
        vote = input("Cast your vote (vote 1/vote 2) or type 'end' to finish: ").strip().lower()

        if vote == "end":
            break
        else:
            candidate_1_votes, candidate_2_votes, total_votes = cast_vote(vote, candidate_1_votes, candidate_2_votes, total_votes)

    display_results(candidate_1_votes, candidate_2_votes, total_votes)

if __name__ == "__main__":
    main()
