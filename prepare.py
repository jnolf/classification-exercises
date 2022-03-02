



def prep_iris(df_iris):
        ''' 
        This function cleans the iris_db by dropping unneeded
        columns and renaming columns to be more helpful. Also, 
        made dummy variables in order to better define findings.
        '''
        # Acquire
        df_iris = acquire.get_iris_data()
        
        # Drop species_id and measurement_id   
        df_iris = df_iris.drop(['species_id', 'measurement_id'],inplace=True)
        
        # Rename species_name to species              
        df_iris = df_iris.rename(columns={'species_name': 'species'})
                    
        # Create dummies
        dummy_df = pd.get_dummies(df_iris[['species']],
                                dummy_na = False,
                                drop_first = [True])
                    
        # Concat with dummies
        df_iris = pd.concat([df_iris, dummy_df], axis = 1)
        
        return df_iris 



def prep_telco(df_telco):
            '''Cleans up unnecessary columns and uses straight-forward
            column names.
            '''
            # Acquire data
            df_telco = acquire.get_telco_data()
            
            # Drop dups
            df_telco.drop_duplicates(inplace=True)
            
            # Remove unneeded columns
            columns_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
            df_telco = df_telco.drop(columns = columns_to_drop)
            
            # Encode categorical variables
            dummy_df = pd.get_dummies(df_telco[['payment_type', 
                                            'internet_service_type', 
                                            'contract_type']],
                                             dummy_na = False,
                                             drop_first = [True, True, True, True])
            
            # Drop unneeded columns without numeric data
            return df_telco    



 def prep_telco(df_telco):
                '''Cleans up unnecessary columns and uses straight-forward
                column names.
                '''
                # Acquire data
                df_telco = acquire.get_telco_data()
                
                # Drop dups
                df_telco.drop_duplicates(inplace=True)
                
                # Remove unneeded columns
                columns_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
                df_telco = df_telco.drop(columns = columns_to_drop)
                
                # Encode categorical variables
                dummy_df = pd.get_dummies(df_telco[['payment_type', 
                                                'internet_service_type', 
                                                'contract_type']],
                                                 dummy_na = False,
                                                 drop_first = [True, True, True, True])
                
                # Drop unneeded columns without numeric data
                return df_telco