def change_text_color(color):
    if color == "green":
        print("\033[1;32;40m\n")
    
    if color == "default":
        print("\033[1;37;40m\n")
    
    if color == "blue":
        print("\033[1;34;40m\n")



def change_text_color_to_green() -> None:
    """
    Changes print color to green
    """
    print("\033[1;32;40m\n")

def change_text_color_to_blue() -> None:
    """
    Changes print color to blue
    """
    print("\033[1;34;40m\n")


def change_text_color_to_default() -> None:
    """
    Changes print color to default
    """
    print("\033[1;37;40m\n")