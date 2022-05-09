import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWe have data for Chicago, New York, and Washington. Which city you want to explore more?\n").lower().strip()
        if city.lower() in CITY_DATA:
            print("\n{} is a magnificent city, if this is not your choice please restart the program now!".format(city.title()))
            break
        else:
            print("\nInvalid input!!\nPlease Choose a city from Chicago, New York, and Washington")

    while True:
        x = input("\nWould you like to filter the data by month, day, both, or 'None' for no filter\n").lower().strip()
        if x.lower() == 'month':
            print("\nWe will make sure the data is filtered by Month!\n")
            while True:
                months = ['January', 'February', 'March', 'April', 'May', 'June']
                month = input("\nWhich Month you prefer? You can choose January, February, March, April, May, or June.\n").lower().strip()
                if month.title() in months:
                    month = month.title()
                    day = None
                    break
                else:
                    print("\nInvalid input!!\nPlease Choose a month from January, February, March, April, May, or June.\n")
            break
        elif x.lower() == 'day':
            print("\nWe will make sure the data is filtered by Day!\n")
            while True:
                days = {'Mon' : 'Monday', 'Tue' : 'Tuesday', 'Wed' : 'Wednesday', 'Thu' : 'Thursday', 'Fri' : 'Friday', 'Sat' : 'Saturday', 'Sun' : 'Sunday'}
                day = input("\nWhich day you prefer? You can Type Mon, Tue, Wed, Thu, Fri, Sat, or Sun.\n").lower().strip()
                if day.title() in days:
                    month = None
                    day = days[day.title()]
                    break
                else:
                    print("\nInvalid input!!\nPlease Choose a day from Mon, Tue, Wed, Thu, Fri, Sat, or Sun.\n")
            break
        elif x.lower() == 'both':
            print("\nWe will make sure the data is filtered by Month and Day!\n")
            while True:
                months = ['January', 'February', 'March', 'April', 'May', 'June']
                month = input("\nWhich Month you prefer? You can choose January, February, March, April, May, or June.\n").lower().strip()
                if month.title() in months:
                    month = month.title()
                    break
                else:
                    print("\nInvalid input!!\nPlease Choose a month from January, February, March, April, May, or June.\n")
            while True:
                days = {'Mon' : 'Monday', 'Tue' : 'Tuesday', 'Wed' : 'Wednesday', 'Thu' : 'Thursday', 'Fri' : 'Friday', 'Sat' : 'Saturday', 'Sun' : 'Sunday'}
                day = input("\nWhich day you prefer? You can Type Mon, Tue, Wed, Thu, Fri, Sat, or Sun.\n").lower().strip()
                if day.title() in days:
                    day = days[day.title()]
                    break
                else:
                    print("\nInvalid input!!\nPlease Choose a day from Mon, Tue, Wed, Thu, Fri, Sat, or Sun.\n")
            break
        elif x.lower() == 'none':
            print("\nWe will make sure NO FILTER will be applied to the data!\n")
            month = None
            day = None
            break
        else:
            print("\nInvalid input!!\nPlease Choose if you would like to filter by Month, Day, Both or None\n")

    #display the final choices to start the calculations
    print('\nYou choose to view data of {} City.\nThe data will be filtered by Month of {} and {} Day.'.format(city.title(), month, day))

    print('-'*100)
    print('-'*100)

    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.strftime('%I %p')

    #df['hour'] = df['Start Time'].dt.hour
    if month != None and day != None:
        df = df[df['month'] == month]
        df = df[df['day_of_week'] == day]
    elif month != None:
        df = df[df['month'] == month]
    elif day != None:
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):

    """
    Displays statistics on the most frequent times of travel.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        most common month
        most common day
        most common hour
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('\nThe most common Month is {} with total count of {}.'
    .format(most_common_month, max(df['month'].value_counts())))

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\nThe most common Day of Week is {} with total count of {}.'
    .format(most_common_day, max(df['day_of_week'].value_counts())))

    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('\nThe most common Hour is {} with a total count of {}.'
    .format(most_common_hour, max(df['hour'].value_counts())))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):

    """
    Displays statistics on the most popular stations and trip.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        most common start station
        most common end station
        most frequent combination of start station and end station trip
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('\nThe most common Start Station is {} with total count of {}.'
    .format(most_common_start, max(df['Start Station'].value_counts())))

    # display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('\nThe most common End Station is {} with a total count of {}.'
    .format(most_common_end, max(df['End Station'].value_counts())))

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + '/' + df['End Station']
    trip_dict= {}

    for trip in df['trip'].values:
        trip_dict[trip] = trip_dict.get(trip,0) +1

    trip_start_end = max(trip_dict, key = trip_dict.get)
    trip_count = trip_dict[max(trip_dict, key = trip_dict.get)]

    print("\nWith a total count of {},\nThe most frequent Combination for start and end station trip is\nFrom {} station to {} station."
          .format(trip_count,trip_start_end.split('/')[0],trip_start_end.split('/')[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):

    """
    Displays statistics on the total and average trip duration.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        Total Trip Duration for the filtered data in Seconds, Minutes, Hours, and Days.
        Average Trip Duration for the filtered data in Seconds and Minutes.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The Total Travel Dration is {} Seconds,'.format(round((sum(df['Trip Duration'].values)))))
    print('which is equivalent to {} Minutes,'.format(round((sum(df['Trip Duration'].values)/60))))
    print('which is equivalent to {} Hours,'.format(round((sum(df['Trip Duration'].values)/60/60))))
    print('which is equivalent to {} Days.'.format(round((sum(df['Trip Duration'].values)/60/60/24))))

    # display mean travel time
    print('\nThe Average Travel Dration is {} Seconds,'.format(round(df['Trip Duration'].values.mean())))
    print('which is equivalent to {} Minutes.'.format(round((df['Trip Duration'].values.mean()/60), 1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):

    """
    Displays statistics on bikeshare users.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day if applicable.

    Returns:
        Counts of different membership types.
        Counts of Gender types if applicable.
        Earliest, most recent, and most common year of birth if applicable.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('We have a total of {} users in {} different membership types as follow:\n'
          .format(sum(df['User Type'].value_counts()), len(df['User Type'].value_counts())))
    print(df['User Type'].value_counts())

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\nOut of {} users,\n{} did not Specify their Gender, and {} state their Gender.'
              .format(sum(df['User Type'].value_counts()), df['Gender'].isnull().sum(), sum(df['Gender'].value_counts())))
        print('\nThe {} users who stated their Gender can be differentiated as follow:\n{}'.format(sum(df['Gender'].value_counts()), gender))
    except:
        print('\nNo Gender Data Found!')

    # Display earliest, most recent, and most common year of birth
    try:
        birth_year = df['Birth Year'].value_counts()
        print('\nThe Youngest user was born in {}.'.format(int(max(df['Birth Year']))))
        print('\nThe Oldest user was born in {}.'.format(int(min(df['Birth Year']))))
        print('\nThe most common Year of Birth is {}, for {} users out of total {} users.'
              .format(int(df['Birth Year'].mode()[0]), max(df['Birth Year'].value_counts()), sum(df['User Type'].value_counts())))
    except:
        print('\nNo Birth Year Data Found!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def display_data(df):

    """
    Displays some raw data from the Data Frame.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        The first 5 rows of data if wanted by the user.
        The next 5 rows of data if wanted by the user.
    """

    df.drop(['month', 'day_of_week', 'hour', 'trip'], inplace=True, axis =1)
    df.rename(columns = {'Unnamed: 0':'Trip ID'}, inplace = True)
    start_loc = 0
    end_loc = 0
    while True:
        first_5 = input("\nWould you like to see the first 5 Trips of the selected data? Enter 'yes' or 'no'.\n").lower().strip()
        if first_5 == 'yes':
            df_dict = df.to_dict('records')
            end_loc += 5
            for num in range(start_loc,end_loc):
                print("\nTrip {}".format(num+1))
                for k,v in df_dict[num].items():
                    print(k,':',v)
            start_loc += 5
            while True:
                next_5 = input("\nWould you like to see the next 5 Trips of the selected data? Enter 'yes' or 'no'.\n").lower().strip()
                if next_5 == 'yes':
                    end_loc += 5
                    for num in range(start_loc,end_loc):
                        print("\nTrip {}".format(num+1))
                        for k,v in df_dict[num].items():
                            print(k,':',v)
                    start_loc += 5
                else:
                    break
        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input("\nWould you like to restart? Enter 'yes' or 'no'.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
