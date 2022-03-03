import pandas as pd
import env
import os
import acquire

# Prepared Iris Data
def prep_iris(df):
        ''' 
        This function cleans the iris_db by dropping unneeded
        columns and renaming columns to be more helpful. Also, 
        made dummy variables in order to better define findings.
        '''       
        # Drop species_id and measurement_id   
        df = df.drop(columns=['species_id', 'measurement_id'])       
        # Rename species_name to species              
        df = df.rename(columns={'species_name': 'species'})                   
        # Create dummies
        dummy_df = pd.get_dummies(df[['species']],
                                dummy_na = False,
                                drop_first = [True])                  
        # Concat with dummies
        df = pd.concat([df, dummy_df], axis = 1)       
        return df

# Prepares Titanic Data
def prep_titanic(df_titanic):
        '''Cleans up unnecessary columns and uses straight-forward
        column names.
        '''
        # Drop dups
        df.drop_duplicates(inplace=True)    
        # Remove unneeded columns
        df = df.drop(columns= ['deck', 'age', 'embarked', 'class', 'passenger_id'])    
        #Fill in missing values where needed
        df['embark_town'] = df.embark_town.fillna(value='Southampton')   
        # Encode categorical variables
        dummy_df = pd.get_dummies(df[['sex', 'embark_town']],
                            dummy_na = False,
                            drop_first = [True, True])
        df = pd.concat([df_titanic, dummy_df], axis = 1)    
        # Drop unneeded columns without numeric data
        return df.drop(columns =['sex', 'embark_town'])

# Prepared Telco Data
def prep_telco(df):
        '''Cleans up unnecessary columns and uses straight-forward
        column names.
        '''           
        # Drop dups
        df.drop_duplicates(inplace=True)           
        # Remove unneeded columns
        columns_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
        df = df.drop(columns = columns_to_drop)           
        # Encode categorical variables
        dummy_df = pd.get_dummies(df[['payment_type', 
                                        'internet_service_type', 
                                        'contract_type']],
                                            dummy_na = False,
                                            drop_first = [True, True, True, True])          
        # Drop unneeded columns without numeric data
        return df    


