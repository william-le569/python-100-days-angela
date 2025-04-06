def format_name(f_name, l_name):
    """ Take first and last name & format it 
    to return the title case version of the name
    """
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name + " " + l_name


f_name = "BILL"
l_name = "LE"

name = format_name(f_name, l_name)

print(name)