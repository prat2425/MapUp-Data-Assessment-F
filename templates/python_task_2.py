import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    #df=pd.read_csv(r'C:\Users\prate\OneDrive\Desktop\dataset-3.csv')
df 

import pandas as pd
from scipy.spatial import distance_matrix

def calculate_distance_matrix(df):
    df=pd.DataFrame(distance_matrix(df.values, df.values), index=df.id_start, columns=df.id_start)
    return df



def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # df=pd.read_csv(r'C:\Users\prate\OneDrive\Desktop\dataset-3.csv')

    def unroll_distance_matrix(df):
    df['distance']=df['distance'].cumsum()
    df['id_start']=1001400
    return df
    
    unroll_distance_matrix(df)


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here

    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # def calculate_toll_rate(df):
    df['moto']=df['distance']*0.8

    df['car']=df['distance']*1.2

    df['rv']=df['distance']*1.5

    df['bus']=df['distance']*2.2
    
    df['truck']=df['distance']*3.6
    
    return(df)
   calculate_toll_rate(df)
here df is the output of question-2

def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # def calculate_time_based_toll_rates(df):
    df['start_day']=pd.date_range(start='20-1-2023',end='1-3-2023',periods=44)
    df['Start_Time']=df['start_day'].dt.hour
    df['Start-dayy']=df['start_day'].dt.weekday.replace({0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thrusday',4:'Friday',5:'Saturday',6:'Sunday'})
    df.drop(columns=['start_day','time'],axis=1,inplace=True)
    return df


def calculate_time_based_toll_rates(df)
