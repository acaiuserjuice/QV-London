
# 5 hypothetical programs for participant to use voting credits on, ideas based around knife crime in London.
def quadratic_voting_interface():
    projects = [
        'Youth Empowerment and Mentorship Program',
        'Community Safety and Policing Reform Initiative',
        'Mental Health Support and Counseling Services Expansion',
        'Education and Outreach Campaign on Conflict Resolution',
        'Rehabilitation and Reintegration Program for Former Offenders'
    ]

    print('Thank you for participating in the test run for Quadratic Voting. \nFor more information on this project please check the README.')
    print('You have 100 voice credits to distribute among the following projects:')

# iterate through the index of our 5 projects (1-5)
    for idx, project in enumerate(projects):
        print(f'{idx + 1}. {project}')

    print('\nThe cost of allocating n votes to a project is n^2 voice credits. \ni.e passing 2 votes will take 4 voice credits, 5 votes will take 25 voice credits.')

# here our initial state is a list, votes = [0,0,0,0,0] which will populate as participant votes
# the list will populate. e.g votes = [5,2,3,5,1], remaining credits factoring n^2 = 36 remaining credits

    votes = [0] * len(projects)
    remaining_credits = 100

# the 'master' while loop. A lot of back and forth for user interaction.
# 1. user choses project, project must be counted and assigned
# 2. establish credits remaining then allow distribution of credits
# 3. ensure number of votes do not exceed remaining credits.
# 4. enable user to continue voting until insufficient credits
# 5. last 'if' statement that factors the quadrtic increase in votes populating the idx
    while remaining_credits > 0:
        try:
            voter_choice = int(input('\nEnter the project number you want to vote for (1-5): ')) - 1   # - 1 will confirm to our project based on its true zero index.
            if voter_choice < 0 or voter_choice >= len(projects):
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue

            max_votes = int(remaining_credits**0.5) # indication of votes left by square root  of remaining credits: max_votes = int(36**0.5) = int(6) = 6
            print(f"You can allocate up to {max_votes} votes to this project.")
            num_votes = int(input(f"Enter the number of votes you want to allocate (0 to {max_votes}): "))

            if num_votes < 0 or num_votes > max_votes:
                print(f"Invalid number of votes. Please enter a number between 0 and {max_votes}.") # ensure user does not exceed if so loop back.
                continue

# crux of loop, updating quadratically with count memory.
            current_votes = votes[voter_choice]   # refer us back to our list of 5 idx, retreive.
            new_total_votes = current_votes + num_votes  # should user wish to update vote of existing idx
            additional_cost = new_total_votes ** 2 - current_votes ** 2 # inform user how many votes left, remaining redits have to be updated quadratically.
#
            if additional_cost > remaining_credits:
                print(f"Not enough credits. The cost of these votes would be {additional_cost} credits, but you only have {remaining_credits} credits remaining.")
                continue

            votes[voter_choice] = new_total_votes

