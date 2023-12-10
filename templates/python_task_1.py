import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # df=pd.read_csv(r'C:\Users\prate\OneDrive\Desktop\dataset-1.csv')

def generate_car_matrix(t):
    x=pd.pivot(data=t,index='id_1',columns='id_2',values='car')
    y=x.to_numpy()
    np.fill_diagonal(y,0)
    df=pd.DataFrame(y,columns=x.columns,index=x.index)
    df=df.iloc[0:6,0:6]
    return(df)

generate_car_matrix(df)


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # function to convert data-
    def pratik(x):
    if x<=15:
        return 'low'
    elif x>15 and x<=25:
        return 'medium'
    else:
        return 'high'
        df['car_type']=df['car'].apply(pratik)
        
# function for returning the count of occurrences for each car_type category-
    
    def get_type_count(df):
    x=df['car_type'].value_counts().reset_index()
    x=x.set_index('index')
    dict=x.to_dict()
    r=dict['car_type']
    key=r.keys()
    key=sorted(key)
    dict={i:r[i] for i in key}
    return dict

get_type_count(df)

def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # def get_bus_indexes(df):
    mean=df['bus'].mean()
    cal_mean=mean*2
    index=df[df['bus']>cal_mean].index
    return list(index)

get_bus_indexes(df)  

def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # def filter_routes(df):
        df=df.groupby('route')['truck'].mean().reset_index()
        df=df[df['truck']>7]
        return list(df.route)

    filter_routes(df)


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # function to convert/multiply the values of data frame-
def multiply_matrix(x):
    if x>20:
        return round(x*0.75,1)
    elif x<=20:
        return round(x*1.25,1)
        
    for i in df.columns:
        df[i]=df[i].apply(multiply_matrix)
here df is the output question 1
multiply_matrix(df)




def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
