def get_employee_names(names_str):
    return names_str.split(",")


def get_ratings(ratings_str):
    ratings = []
    for rating in ratings_str.split(","):
        ratings.append(int(rating))
    return ratings


def highest_rating_employee(names, ratings):
    highest = ratings[0]
    employee = names[0]

    for i in range(len(ratings)):
        if ratings[i] > highest:
            highest = ratings[i]
            employee = names[i]

    return employee, highest


def lowest_rating_employee(names, ratings):
    lowest = ratings[0]
    employee = names[0]

    for i in range(len(ratings)):
        if ratings[i] < lowest:
            lowest = ratings[i]
            employee = names[i]

    return employee, lowest


def average_rating(ratings):
    total = 0

    for rating in ratings:
        total += rating

    return total / len(ratings)


def employees_above_average(names, ratings, avg):
    print("\nEmployees Above Average:")

    for i in range(len(ratings)):
        if ratings[i] > avg:
            print(names[i])


# Input
names_input = input("Employee Names: ")
ratings_input = input("Ratings: ")

# Processing
names = get_employee_names(names_input)
ratings = get_ratings(ratings_input)

highest_emp, highest_rating = highest_rating_employee(names, ratings)
lowest_emp, lowest_rating = lowest_rating_employee(names, ratings)
avg = average_rating(ratings)

# Output
print(f"\nEmployee with Highest Rating : {highest_emp} ({highest_rating})")
print(f"Employee with Lowest Rating : {lowest_emp} ({lowest_rating})")
print(f"Average Rating : {avg}")

employees_above_average(names, ratings, avg)