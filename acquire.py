# %%
import pandas as pd
import os
import env 

# %%
titanic_url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/titanic_db'
iris_url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/iris_db'
telco_url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/telco_churn'

# %%
# Get titanic data

def get_titanic_data(use_cache = True):
    filename = 'titanic.csv'
    
    if os.path.exists(filename):
        print('Using cached csv file...')
        return pd.read_csv(filename)

    print('Acquiring data from SQL Database')
    titanic_url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/titanic_db'
    query = '''
    SELECT * 
    FROM passengers

    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, titanic_url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df

get_titanic_data()


# %%

#Get Iris data
def get_iris_data(use_cache = True):
    filename = 'iris_db.csv'
    
    if os.path.exists(filename):
        print('Using cached csv file...')
        return pd.read_csv(filename)

    print('Acquiring data from SQL Database')
    titanic_url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/iris_db'
    query = '''
    SELECT * 
    FROM species

    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, iris_url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df

get_iris_data()

# %%

#Get Telco data
def get_telco_data(use_cache = True):
    filename = 'telco_churn.csv'
    
    if os.path.exists(filename):
        print('Using cached csv file...')
        return pd.read_csv(filename)

    print('Acquiring data from SQL Database')
    titanic_url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/telco_churn'
    query = '''
    SELECT * 
    FROM customers
    JOIN contract_types USING(contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id)

    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, telco_url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df

get_telco_data()
# %%


