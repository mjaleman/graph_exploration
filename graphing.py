"Explore graphs with matplotlib"

import csv

import matplotlib.pyplot as plt
import numpy as np


def delay_bar_graph():
    """Create bar graph of first ten flight results.

    This function was made to explore how to make a bar graph with python
    and a set of data. The data is on ariplane delays across the US
    provided by The Collection of Really Great,Interesting, Situated
    Datasets.
    """

    num_delays = []
    term_codes = []

    with open("./airlines.csv", 'r') as csv_file:
        airline_reader = csv.DictReader(csv_file)
        for row in airline_reader:
            # Creates a list from the values under 'Delayed'
            num_delays.append(row['Delayed'])
            # Creates a list from the values under 'Code'
            term_codes.append(row['Code'])
    # Creates new list containing just the first 10
    # y values (number of Delays).
    first_ten = num_delays[0:10]
    # Creates new list containing the X values to be used as labels for the bar
    # graph (Terminal codes).
    first_terms = term_codes[0:10]
    # Converts values in first_ten to integer values through list coprehension.
    new_ones = [int(x) for x in first_ten]
    y_pos = np.arange(len(first_terms))
    plt.bar(y_pos, new_ones)
    plt.xticks(y_pos, first_terms)
    plt.title("Delays per Terminal")
    plt.xlabel("Terminal Codes")
    plt.ylabel("Amount of Flights Delayed")
    plt.show()


def delay_scatter_plot():
    """Create a scatter plot from all flight results.

    This function was made to explore how to make a scatter plot with python
    and a set of data. The data is on ariplane delays across the US provided
    by The Collection of Really Great,Interesting, Situated Datasets.

    """

    num_delays = []
    term_codes = []
    airline_dict = {}
    fig, ax = plt.subplots()
    N = 50
    # saves the file as a reference in 'csv_file'. Keeps file open only while
    # it's used within the statement.
    with open('./airlines.csv', 'r') as csv_file:
        airline_reader = csv.DictReader(csv_file)
        # Creates a list from 'Code' and 'Delayed'
        for row in airline_reader:
            key = row['Code']
            value = row['Delayed']
            # Adds keys and values to their designated lists as well as the
            # dictionary.
            if key not in term_codes:
                term_codes.append(key)
                num_delays.append(value)
                airline_dict[key] = value
            # If the Terminal code is already in the list it adds the value
            # of delays.
            if key in term_codes:
                delay_amount = int(airline_dict[key])
                airline_dict[key] = value
                for key in airline_dict:
                    value = int(value) + delay_amount
                    num_delays.append(airline_dict[key])
        # Plots X and Y values per terminal. The index of a terminal
        # represents its x axis.
        for i in range((len(term_codes) - 1)):
            x = i
            y = int(num_delays[i])
            plt.scatter(x, y)
        plt.show()


def line_plot_minute_delays():
    """Create a line graph from the amount of minutes delayed.

    This function was made to explore line plots with python and a set of data.
    The data is on ariplane delays across the US provided by The Collection of
    Really Great, Interesting, Situated Datasets.

    """
    airline_dict = {}
    term_codes = []
    values = []
    with open('./airlines.csv', 'r') as csv_file:
        airline_reader = csv.DictReader(csv_file)
        # Grabs data from addresed columns.
        for row in airline_reader:
            key = row['Code']
            value = row['Minutes Delayed.Total']
        # Places data in dictionary and in term_codes list.
            if key not in airline_dict:
                airline_dict[key] = value
                term_codes.append(key)
        # Adds up new and old amounts of minutes delayed.
            if key in airline_dict:
                new_val = airline_dict[key]
                value = int(value) + int(new_val)
                airline_dict[key] = value
        # Adds the amount if minutes delayed to the 'values' list.
        for key in airline_dict:
            values.append(airline_dict[key])
        # Plots data.
        fig, ax = plt.subplots()
        y = values
        y_pos = np.arange(len(term_codes))
        plt.xticks(y_pos, term_codes)
        line1, = ax.plot(y)
        plt.xlabel('Terminals')
        plt.ylabel('Average minutes delayed (Thousands)')
        plt.title('Average Delays Per Terminal')
        plt.show()


def percentage_delayed_linegraph():
    """Create a line graph from the percentage of delays.

    This function was made to explore line plots with python and a set of data.
    It adds and dives the data to get the percentage of delays per terminal and
    the plots the points in the designated area. The data is on ariplane delays
    across the US provided by The Collection of Really Great, Interesting,
    Situated Datasets.

    """

    airline_dict = {}
    delayed_dict = {}
    term_codes = []
    delay_average = []
    with open('./airlines.csv', 'r') as csv_file:
        airline_reader = csv.DictReader(csv_file)
        # Grabs data from each of the columns.
        for row in airline_reader:
            key = row['Code']
            flights = row['Flights.Total']
            delayed_amt = row['Delayed']
            # Adds data to dictionaries and to term_codes list.
            if key not in airline_dict:
                airline_dict[key] = flights
                delayed_dict[key] = delayed_amt
                term_codes.append(key)
            # Adds up the total number of flights abd total amount of delays.
            if key in airline_dict:
                flight_old_val = int(airline_dict[key])
                flight_val = flight_old_val + int(flights)
                airline_dict[key] = flight_val
                delayed_old_val = int(delayed_dict[key])
                delayed_val = delayed_old_val + int(delayed_amt)
                delayed_dict[key] = delayed_val
        # Calculates the average amount of delays.
        for key in airline_dict:
            average_of_flights = int(airline_dict[key]) // 152
            average_of_delays = int(delayed_dict[key]) // 152
            percent_delay = round((average_of_delays / average_of_flights)
                * 100)
            delay_average.append(percent_delay)
        # Plots the values generated.
        fig, ax = plt.subplots()
        y = delay_average
        y_pos = np.arange(len(term_codes))
        plt.xticks(y_pos, term_codes)
        line1, = ax.plot(y)
        plt.title("Average Percentage of Delays")
        plt.xlabel('Terminals')
        plt.ylabel('Percentage of Delays to the Amount of Flights')
        plt.show()


def percentage_weather_delay_bar():
    """Create a bar graph from the percentage of weather delays.

    This function was made to explore how to make a bar graph with python and
    a set of data. It calculates the average percantage of delays and rounds
    the data, then plots it in the form of a bar graph. The data is on
    ariplane delays across the US provided by The Collection of Really Great,
    Interesting, Situated Datasets.

    """

    weather_dict = {}
    airline_dict = {}
    term_codes = []
    delay_average = []
    with open('./airlines.csv', 'r') as csv_file:
        airline_reader = csv.DictReader(csv_file)
        for row in airline_reader:
            key = row['Code']
            delayed = row['Delayed']
            weather_delayed = row['# of Delays.Weather']
            if key not in weather_dict:
                weather_dict[key] = weather_delayed
                airline_dict[key] = delayed
                term_codes.append(key)
            if key in weather_dict:
                weather_old_delay = int(weather_dict[key])
                weather_new_delay = weather_old_delay + int(weather_delayed)
                weather_dict[key] = weather_new_delay
                old_delay = airline_dict[key]
                new_delay = int(old_delay) + int(delayed)
                airline_dict[key] = new_delay
        for key in weather_dict:
            average_weather_delays = round((int(weather_dict[key]) /
                int(airline_dict[key])) * 100)
            delay_average.append(average_weather_delays)

        y_pos = np.arange(len(term_codes))
        plt.bar(y_pos, delay_average)
        plt.xticks(y_pos, term_codes)
        plt.title("Percentage of Weather Delays")
        plt.xlabel('Terminal Codes')
        plt.ylabel('Percentage of Total Dleays(%)')
        plt.show()

# Selection of type of graph
selection = int(input("Make a selection (1-5) : "))
if selection == 1:
    delay_bar_graph()
if selection == 2:
    delay_scatter_plot()
if selection == 3:
    line_plot_minute_delays()
if selection == 4:
    percentage_delayed_linegraph()
if selection == 5:
    percentage_weather_delay_bar()

if __name__ == "__main__":
    delay_bar_graph()
    delay_scatter_plot()
    line_plot_minute_delays()
    percentage_delayed_linegraph()
    percentage_weather_delay_bar()
