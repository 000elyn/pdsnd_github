import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city(chicago, new york city or washington):')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('please choose between chicago, new york city or washington')
    # get user input for month (all, january, february, ... , june)
    month = input('Enter month(January-June or all): ').lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input('ENTER MONTH january, february, ... , june : ').lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter day(Monday-Sunday or all): ').lower()
    while day not in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('ENTER DAY monday, tuesday, ... , sunday : ').lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv('{}.csv'.format(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    df['day'] = df['Start Time'].dt.weekday_name
    if day != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: {}.".format(df['month'].value_counts().idxmax()))

    # display the most common day of week
    print("The most common day is: {}.".format(df['day'].value_counts().idxmax()))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour is: {}.".format(df['hour'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station is: {}".format(df['Start Station'].value_counts().idxmax()))

    # display most commonly used end station
    print("The most common end station is: {}".format(df['End Station'].value_counts().idxmax()))

    # display most frequent combination of start station and end station trip
    print("The most common combination of start station and end station trip")
    combination = df.groupby(['Start Station', 'End Station']).max()
    print(combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):


    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is {} seconds or {} hours.".format(total_travel_time, total_travel_time/3600))


    # display mean travel time
    avg = df['Trip Duration'].mean()
    print("Average travel time is {} seconds or {} hours.".format(avg, avg/3600))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):


    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if CITY_DATA != washington:
    # Display counts of gender
        user_gender = df['Gender'].value_counts()
        print(user_gender)

    # Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].value_counts().idxmax())
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].value_counts().idxmax())
        print("The earliest year of birth is:",earliest_year_of_birth,
            ", most recent one is:",most_recent_year_of_birth,
            "and the most common one is: ",most_common_year_of_birth)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
    while True:
        view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            break
        display_raw_data(df)
        break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
