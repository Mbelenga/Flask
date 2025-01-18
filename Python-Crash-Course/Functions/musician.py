def get_formatted_name(first_name, last_name):
    """  This function returns a full name """
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('Alicia', 'Keys')
print(musician)