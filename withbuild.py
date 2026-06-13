def get_employee_names(names_str):
    return names_str.split(",")


def get_ratings(ratings_str):
    return [int(rating) for rating in ratings_str.split(",")]


def highest_rating_employee(names, ratings):
    highest = max(ratings)
    index = ratings.index(highest)
    return names[index], highest


def lowest_rating_employee(names, ratings):
    lowest = min(ratings)
    index = ratings.index(lowest)
    return names[index], lowest


def average_rating(ratings):
    return sum(ratings) / len(ratings)


def employees_above_average(names, ratings, avg):
    return [names[i] for i in range(len(ratings)) if ratings[i] > avg]


# Input
names_input = input("Employee Names: ")
ratings_input = input("Ratings: ")

names = get_employee_names(names_input)
ratings = get_ratings(ratings_input)

highest_emp, highest_rating = highest_rating_employee(names, ratings)
lowest_emp, lowest_rating = lowest_rating_employee(names, ratings)
avg = average_rating(ratings)

print(f"\nEmployee with Highest Rating : {highest_emp} ({highest_rating})")
print(f"Employee with Lowest Rating : {lowest_emp} ({lowest_rating})")
print(f"Average Rating : {avg}")

print("\nEmployees Above Average:")
for employee in employees_above_average(names, ratings, avg):
    print(employee)