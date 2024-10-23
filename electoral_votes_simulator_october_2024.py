# Initialize vote counts and electoral votes
total_votes = 0
candidate_1_electoral_votes = 0
candidate_2_electoral_votes = 0


# Electoral Locations and their Electoral Votes

electoral_votes_locations = {
    "Alabama": 9,
    "Alaska": 3,
    "Arizona": 11,
    "Arkansas": 6,
    "California": 54,  # Adjusted for 2020 Census
    "Colorado": 10,
    "Connecticut": 7,
    "Delaware": 3,
    "District of Columbia": 3,  # Washington, D.C.
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
    "Wyoming": 3,
}

counted_locations = {}


def choose_vote_location(candidate_1_electoral_votes, candidate_2_electoral_votes):

    location = input("\nSelect your location (or type 'end' to end election): ").strip()

    if location in electoral_votes_locations:
        print(location)

        state_voting(location, candidate_1_electoral_votes, candidate_2_electoral_votes)

    elif location != "end" and location not in electoral_votes_locations:
        print("Invalid State Chosen")

    elif location == "end":
        end_election()

    return location


def state_voting(location, candidate_1_electoral_votes, candidate_2_electoral_votes):

    if location in counted_locations:

        print(f"{location} has already voted and the polls are closed.")

    else:

        candidate_1_state_votes = 0
        candidate_2_state_votes = 0
        total_state_votes = 0
        winner = ""

        while True:

            vote = input(
                f"Vote for Candidate 1 ('1') or Candidate 2 ('2') or CLOSE the polls. "
            )

            if vote not in ["1", "2", "CLOSE", "close"]:
                print("Invalid selection")

            else:
                if vote == "1":
                    candidate_1_state_votes += 1
                    total_state_votes += 1
                    continue

                elif vote == "2":
                    candidate_2_state_votes += 1
                    total_state_votes += 1
                    continue

                elif vote in ["CLOSE", "close"]:

                    print(f"-" * 60)
                    print(f"The total votes cast in {location} is {total_state_votes}")
                    print(f"-" * 60)
                    print(f"Candidate 1 had a total of {candidate_1_state_votes} votes")
                    print(f"Candidate 2 had a total of {candidate_2_state_votes} votes")
                    print(f"-" * 60)

                    if candidate_1_state_votes > candidate_2_state_votes:
                        winner = "Candidate 1"
                        candidate_1_electoral_votes += electoral_votes_locations[
                            location
                        ]
                    if candidate_2_state_votes > candidate_1_state_votes:
                        winner = "Candidate 2"
                        candidate_2_electoral_votes += electoral_votes_locations[
                            location
                        ]

                    # if candidate_1_votes == candidate_2_votes:
                    # code for handling a tie breaker

                    print(
                        f"The winner of {location} is {winner} gaining {electoral_votes_locations[location]} electoral votes"
                    )

                    counted_locations[location] = [
                        total_state_votes,
                        candidate_1_electoral_votes,
                        candidate_2_electoral_votes,
                    ]

                    break


def end_election():

    sum_votes = 0
    candidate_1_sum = 0
    candidate_2_sum = 0

    # total up all votes cast for entire country
    for k in counted_locations.keys():
        sum_votes += counted_locations[k][0]

    # total up ALL candidate 1 electoral votes from counted dictionary
    for k in counted_locations.keys():
        candidate_1_sum += counted_locations[k][1]

    # total up ALL candidate 2 electoral votes from counted dictionary
    for k in counted_locations.keys():
        candidate_2_sum += counted_locations[k][2]

    print(f"-" * 60)
    print(f"All of the polls in the United States are closed!")
    print(f"-" * 60)
    print(f"Total votes cast across the country : {sum_votes}")

    print(f"-" * 60)

    print(f"Candidate 1 - Total Electoral Votes : {candidate_1_sum}")
    print(f"-" * 60)
    print(f"Candidate 2 - Total Electoral Votes : {candidate_2_sum}")
    print(f"-" * 60)

    if candidate_1_sum > candidate_2_sum:
        print(f"Candidate 1 becomes the new President of the United States!")
    if candidate_2_sum > candidate_1_sum:
        print(f"Candidate 1 becomes the new President of the United States!")
    print(f"-" * 60)

    raise SystemExit


while True:
    choose_vote_location(candidate_1_electoral_votes, candidate_2_electoral_votes)
