""""Write a function that takes a list of tuples, where each tuple contains the name and age of a person, 
and returns a list of the names of all 
the people who are over 18 years old. 
Use pattern matching and unpacking to extract the names and ages from the tuples."""

def fun(arr):
    sol = []
    for record in arr:
        match record:
            case(name, age) if age > 18:
                sol.append(record)
            case _:
                pass
    return sol

"""Write a function that takes a list of tuples, where each tuple contains a person's name and a list of their favorite colors. 
The function should return a dictionary where the keys are the colors and the values are lists of the names of people who like that color. 
Use pattern matching and unpacking to extract the names and favorite colors from the tuples."""
def fun2(arr):
    color_dict = {}
    for person, colors in arr:
        for color in colors:
            match color_dict.get(color):
                case None:
                    color_dict[color] = [person]
                case color_list:
                    color_list.append(person)
    return color_dict
