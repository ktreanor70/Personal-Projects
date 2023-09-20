from datetime import date, timedelta
import random

DAYS_IN_YEAR = 365


def random_date() -> date:
    # Create a random number between 0 and 364
    random_days = random.randrange(DAYS_IN_YEAR)
    # Add the random days to Jan 1, 2023 to get a random date in that year
    random_date = date(2023, 1, 1) + timedelta(days=random_days)

    return random_date


def duplicate_count(birthdays: list) -> int:
    # Since sets can't have duplicates, if we cast the list into a set it will remove the duplicates for us
    # Now just subtract the set count from the original count, if it's greater than 0 there were duplicates
    return len(birthdays) - len(set(birthdays))


people = int(input("How many people at the party: "))
simulations = int(input("How many times do you want me to simulate this party: "))

matching_birthdays = 0
# Simulation loop
for i in range(simulations):
    birthdays = []
    # People loop
    for j in range(people):
        birthdays.append(random_date())
    # If there were duplicates increment the counter
    if (duplicate_count(birthdays)) > 0:
        matching_birthdays += 1

print(
    f"Running the simulation {simulations} times, there a matching birthday {matching_birthdays} times"
)
print(f"This is an average of {(matching_birthdays / simulations):.2%}")
