'''This module contains all the functions necessary to display a main menu containing
submenus for entering a valid phone number, zip code, and doing matrix operations on
two 3x3 matrices.
'''
import colorama
import pandas as pd
import matplotlib.pyplot as plt
from astropy.visualization import hist
HOUSING_FILE = "resources/housing.csv"
POPULATION_FILE = "resources/PopChange.csv"
def clear():
    '''Allows the menu to be persistent in one location. Clears the terminal window by
    printing \x1B[2J character, which colorama can handle on windows.
    '''
    colorama.init()
    print(chr(27) + "[2J")
def column_data(frame, key):
    '''Takes a single column of data and turns it into the required output
    to show count, mean, standard deviation, min, and max in a new frame for
    display.
    '''
    output_frame = pd.DataFrame({'' : [round(len(frame), 0), #number of rows
                            round(frame[key].mean(0), 3), #mean of the column
                            round(frame[key].std(0), 3), #standard deviation of the column
                            round(frame[key].min(0), 3), #minimum of the column
                            round(frame[key].max(0), 3) #maximum of the column
                            ]},
                            index = ['Count',
                                    'Mean',
                                    'Standard Deviation',
                                    'Min',
                                    'Max'])
    output_frame.index.name = "Statistics for " + key + ":"
    return output_frame
def plot_histogram(display_frame, key, minimum = 0, maximum = 10000, step = 10):
    '''Takes a DisplayFrame, column key, and optionally a min, max and step.
    Creates a histogram from the provided parameters and shows the plot with
    plt.
    '''
    hist(display_frame[key],
                    bins = 'blocks')
    plt.show()
def pop_menu():
    '''Population data submenu for the program.
    '''
    user_input = "" #stores user input temporarily
    status_msg = "" #displays status information to the user
    #Menu items for the population data menu
    menu_msg = "\n1.    Pop Apr 1" +\
            "\n2.    Pop Jul 1" +\
            "\n3.    Change Pop" +\
            "\nq.    Exit Column"
    try:
        #reads data from the appropriate csv
        population_frame = pd.read_csv(POPULATION_FILE)
        stats_frame = pd.DataFrame() #empty DataFrame to store and display statistics
        display_msg = "" #used to display stats back to the user
        output_msg = "\nPlease select the column you want to analyze or press 'q' to go back:"
        running = True
        while running:
            clear()
            user_input = input(status_msg + menu_msg + display_msg + output_msg)
            match user_input:
                case '1':
                    #Selects the appropriate column from the primary frame and
                    #creates the stats frame from the data, then displays it.
                    status_msg = ""
                    stats_frame = column_data(population_frame, "Pop Apr 1")
                    display_msg = "\n\n" + str(stats_frame) + "\n"
                    clear()
                    print(status_msg + menu_msg + display_msg + output_msg)
                    #Creates a histogram from the column with the appropriate key
                    plot_histogram(population_frame,
                                'Pop Apr 1',
                                int(population_frame['Pop Apr 1'].min()),
                                225000,
                                11250)
                case '2':
                    #Selects the appropriate column from the primary frame and
                    #creates the stats frame from the data, then displays it.
                    status_msg = ""
                    stats_frame = column_data(population_frame, "Pop Jul 1")
                    display_msg = "\n\n" + str(stats_frame) + "\n"
                    clear()
                    print(status_msg + menu_msg + display_msg + output_msg)
                    plot_histogram(population_frame,
                                'Pop Jul 1',
                                int(population_frame['Pop Jul 1'].min()),
                                225000,
                                11250)
                case '3':
                    #Selects the appropriate column from the primary frame and
                    #creates the stats frame from the data, then displays it.
                    status_msg = ""
                    stats_frame = column_data(population_frame, "Change Pop")
                    display_msg = "\n\n" + str(stats_frame) + "\n"
                    clear()
                    print(status_msg + menu_msg + display_msg + output_msg)
                    plot_histogram(population_frame,
                                'Change Pop',
                                -15000,
                                15000,
                                750)
                case 'q':
                    #Stops the loop for the menu and returns to the previous menu
                    status_msg = ""
                    running = False
                case _:
                    status_msg = "Error: Invalid menu selection."
    except FileNotFoundError:
        input(f"Cannot find the file: {POPULATION_FILE}.\n" +\
            "Press any key to continue to the main menu:")
def housing_menu():
    '''Housing data submenu for the program.
    '''
    user_input = ""
    status_msg = ""
    menu_msg = "\n1.    Age" +\
            "\n2.    Bedrooms" +\
            "\n3.    Built" +\
            "\n4.    Rooms" +\
            "\n5.    Utility" +\
            "\nq.    Exit Column"
    #reads data from the appropriate csv
    try:
        housing_frame = pd.read_csv(HOUSING_FILE)
        stats_frame = pd.DataFrame() #empty DataFrame to store and display statistics
        display_msg = ""
        output_msg = "\nPlease select the column you want to analyze or press 'q' to go back:"
        running = True
        while running:
            clear()
            user_input = input(status_msg + menu_msg + display_msg + output_msg)
            match user_input:
                case '1':
                    #Selects the appropriate column from the primary frame and
                    #creates the stats frame from the data, then displays it.
                    status_msg = ""
                    stats_frame = column_data(housing_frame, "AGE")
                    display_msg = "\n\n" + str(stats_frame) + "\n"
                    clear()
                    print(status_msg + menu_msg + display_msg + output_msg)
                    #Creates a histogram from the column with the appropriate key
                    plot_histogram(housing_frame, 'AGE', int(housing_frame["AGE"].min()),
                                                int(housing_frame["AGE"].max()),
                                                10)
                case '2':
                    #Selects the appropriate column from the primary frame and
                    #creates the stats frame from the data, then displays it.
                    status_msg = ""
                    stats_frame = column_data(housing_frame, "BEDRMS")
                    display_msg = "\n\n" + str(stats_frame) + "\n"
                    clear()
                    print(status_msg + menu_msg + display_msg + output_msg)
                    #Creates a histogram from the column with the appropriate key
                    plot_histogram(housing_frame, 'BEDRMS', int(housing_frame["BEDRMS"].min()),
                                                int(housing_frame["BEDRMS"].max()),
                                                1)
                case '3':
                    #Selects the appropriate column from the primary frame and
                    #creates the stats frame from the data, then displays it.
                    status_msg = ""
                    stats_frame = column_data(housing_frame, "BUILT")
                    display_msg = "\n\n" + str(stats_frame) + "\n"
                    clear()
                    print(status_msg + menu_msg + display_msg + output_msg)
                    #Creates a histogram from the column with the appropriate key
                    plot_histogram(housing_frame, 'BUILT', int(housing_frame["BUILT"].min()),
                                                int(housing_frame["BUILT"].max()),
                                                10)
                case '4':
                    status_msg = ""
                    stats_frame = column_data(housing_frame, "ROOMS")
                    display_msg = "\n\n" + str(stats_frame) + "\n"
                    clear()
                    print(status_msg + menu_msg + display_msg + output_msg)
                    #Creates a histogram from the column with the appropriate key
                    plot_histogram(housing_frame, 'ROOMS', int(housing_frame["ROOMS"].min()), \
                                                int(housing_frame["ROOMS"].max()),
                                                1)
                case '5':
                    #Selects the appropriate column from the primary frame and
                    #creates the stats frame from the data, then displays it.
                    status_msg = ""
                    stats_frame = column_data(housing_frame, "UTILITY")
                    display_msg = "\n\n" + str(stats_frame) + "\n"
                    clear()
                    print(status_msg + menu_msg + display_msg + output_msg)
                    #Creates a histogram from the column with the appropriate key
                    plot_histogram(housing_frame, 'UTILITY', int(housing_frame["UTILITY"].min()),
                                                int(housing_frame["UTILITY"].max()),
                                                30)
                case 'q':
                    #Stops the running loop and backs out of the menu
                    status_msg = ""
                    running = False
                case _:
                    status_msg = "Error: Invalid menu selection."
    except FileNotFoundError:
        input(f"Cannot find the file: {HOUSING_FILE}.\n" +\
            "Press any key to continue to the main menu:")
def main():
    '''Main menu for the program.
    '''
    user_input = ""
    status_msg = "~~~~Welcome to the Python Data Analysis App~~~~"
    menu_msg = "\n1.    Population Data" +\
            "\n2.    Housing Data" +\
            "\nq.    Exit the program"
    display_msg = ""
    output_msg = "\nPlease make a selection from the menu:"
    running = True
    while running:
        clear()
        #Update the display_msg
        display_msg = ""
        user_input = input(status_msg + menu_msg + display_msg + output_msg)
        match user_input:
            case '1':
                status_msg = ""
                pop_menu()
            case '2':
                status_msg = ""
                housing_menu()
            case 'q':
                status_msg = ""
                print("Thank you for using the Python Data Analysis App!")
                running = False
            case _:
                status_msg = "Error: Invalid menu selection."
main()
