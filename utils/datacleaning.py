def data_cleaning(dataframe):
    """
    Function to clean the data.
    """
    # Replace missing values with column mean
    dataframe.fillna(dataframe.mean(), inplace=True)
    
    # remove duplicate rows
    dataframe.drop_duplicates(inplace=True)
    
    # Remove unnecessary columns
    # dataframe.drop(['columna1', 'columna2'], axis=1, inplace=True)
    
    # Replace incorrect values with correct values
    # dataframe.replace({'columna': {'valor_incorrecto': 'valor_correcto'}}, inplace=True)
    
    # convert data types
    # dataframe['columna'] = dataframe['columna'].astype('tipo_dato')

    # replace column names in lowercase and remove whitespace by _
    dataframe = dataframe.rename(columns=lambda x: x.replace(' ', '_').lower())

    # print('execution ends.')

    return dataframe