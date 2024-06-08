
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

    while remaining_credits > 0:
        try:
            voter_choice = int(input('\nEnter the project number you want to vote for (1-5): ')) - 1