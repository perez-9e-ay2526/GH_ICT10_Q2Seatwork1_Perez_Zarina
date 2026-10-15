# Confirm Cadet Officer

from pyscript import display, document

def confirm_officer(e):
    document.getElementById('output').innerHTML = ''
    input_first = str(document.getElementById('firstname').value) # gets the user input
    input_last = str(document.getElementById('lastname').value)

    input_full = str(input_first) + " " + str(input_last)

    input_final = input_full.title() # changes the case of the name

    officer_names = ['Zarina Perez', 'Maryam Ledesma', 'Nathan Bautista', 'Hans Baquiran', 'Aiva Suson', 'Zoey Reyes'] 

    officer_checker = input_final in officer_names # checks if user input is valid

    display_message = (f'You are not a part of the Cadet Corps.', f'Welcome 1CL 2LT Cadet {input_final}!')
    
    display(display_message[officer_checker], target="output")