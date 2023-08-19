"""
Simple: write a function that capitalizes the first and fourth letters of a string
"""


def macdonald(string):
    if len(string) >= 4:
        return string[:3].capitalize()+string[3:].capitalize()
    return "Name is too short."
