# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 07:47:09 2018

@author: Xia Chen
"""


import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities=['chicago','new york city', 'washington']
months=[ 'all','january', 'february', 'march','april','may','june']
days=['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # 1: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Which city would you like to explore, Chicago, New York City, or Washington?\n')
        city=city.lower()
        if city not in cities:
            print('\nInvalid iput, please choose one of the three cities:\n')
        else:
            break
         
    # 2: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Which month do you want to see?\n')
        month=month.lower()
        if month not in months:
            print('\nInvalid iput, Please type \'all\' or a month between January and June to explore:\n')
        else:
            break
        
     # 3: get user input for day of week (all, monday, tuesday, ... sunday)   
    while True:
        day=input('Which day of week do you want to see:\n')
        day=day.lower()
        if day not in days:
            print('\nInvalid input, please type \'all\' or a week day between Monday and Friday:\n')
        else:
            break
    print('-'*40)
    return city, month, day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour_of_day']=df['Start Time'].dt.hour
    if month != 'all':
        month = months.index(month)              
        df = df[df['month']==month]
           
    if day != 'all' :
        df =df[df['day_of_week']==day.title()] 
    print('-'*40)  
    
    return df
    




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time=time.time()
    # 4: display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)
    
    # 5: display the most common day of week
    popular_day_of_week =df['day_of_week'].mode()[0]
    print('Most Popular day of week:',  popular_day_of_week) 
    
    # 5: display the most common start hour
    popular_hour_of_day= df['hour_of_day'].mode()[0]
    print('Most Popular hour of day',  popular_hour_of_day)
    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)
        


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time=time.time()

    # 6: display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)
    
    # 7: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)
    

    # 8: display most frequent combination of start station and end station trip
    
    popular_trip= df['Start Station']+'to'+df['End Station']
    popular_trip=popular_trip.mode()[0]
    print('Most popular trip:', popular_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
   
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # 9: display total travel time
    
    total_travel_time=df['Trip Duration'].sum()
    hours,rest=divmod(total_travel_time,3600)
    minutes, seconds=divmod(rest,60)
    print('The total trip takes:{} hours,{} minutes and {} seconds.'.format(int(hours),int(minutes),int(seconds)))

    # 10: display mean travel time
    average_travel_time=df['Trip Duration'].mean()
    hours,rest=divmod(average_travel_time,3600)
    minutes, seconds=divmod(rest,60)
    print('The average trip duration takes:{} hours, {} minutes and {} seconds.'.format(int(hours),int(minutes),int(seconds)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    # 11: Display counts of user types
    print('\nCalculating user stats...\n')
    start_time = time.time()
    user_type = df['User Type'].value_counts()
    print('The number of users by type:\n', user_type.to_string())
    
    print('-'*40)
    
    # 12: Display counts of gender
    print('\nCalculating gender of users...\n')
    if city.lower()=='washington':
        print('Sorry, the gender information for Washington is missing!')
    else:
        gender=df['Gender'].value_counts()
        print('The number of users by gender:\n', gender.to_string())
      
    print('-'*40)
    
    # 13: Display earliest, most recent, and most common year of birth
    print('\nCalculating birth year of users...\n')
    if city.lower()=='washington':
        print('Sorry, the birth year information for Washington is missing!')
    else:
        earlist_birth_year=df['Birth Year'].min()
        latest_birth_year=df['Birth Year'].max()
        popular_birth_year=df['Birth Year'].mode()[0]
        print('The oldest users are born in {}.' '\nThe youngest users are born in {}.'
          '\nThe most popular year of birth {}' .format(earlist_birth_year, latest_birth_year, popular_birth_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df,city):
    count=10
    raw=input('Would you like to see some raw data?' )
    if raw.lower()=='yes':
        df=pd.read_csv(CITY_DATA[city]).head()
        print(df)
    while True:
        more_raw=input('Would you like to see 5 more raw data?' )
        if more_raw.lower()=='yes':
            df=pd.read_csv(CITY_DATA[city]).head(count)
            count+=5
            print(df)
        else:
            break
            
        
def main():
    
    while True:
           
        city,month,day=get_filters()
        
        df = load_data(city, month, day)
        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df,city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
    main()


            
         