# SEATWORK 1 - CANDIDATE VERIFICATION

from pyscript import document


# List of MONARCH Dance Club members
club_members = [
    'Apple White',
    'Raven Queen',
    'Ashlynn Ella',
    'Hello Kitty',
    'Isabelle Cabatu',
    'Sonny Angel',
    'Nathan Bautista',
    'Josua Ortiz'
]


# Function to check if a candidate is a club member
def member_checker(e):

    # Get and format the first name
    first_name = document.getElementById(
        'firstname'
    ).value.strip().title()

    # Get and format the last name
    last_name = document.getElementById(
        'lastname'
    ).value.strip().title()

    # Combine first and last name
    full_name = first_name + ' ' + last_name

    # Check if the candidate is in the club members list
    member_found = full_name in club_members

    # Store the possible messages in a tuple
    messages = (
        f'Sorry {full_name}, your name is not on the list.',
        f'Congratulations {full_name}! You are now part of MONARCH Dance Club!'
    )

    # Display the appropriate message
    document.getElementById(
        'result'
    ).innerHTML = messages[member_found]
