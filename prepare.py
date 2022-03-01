#Prep Iris
def prep_iris(iris):
    iris = get_iris_data()
    new_iris = iris.drop(columns=['species_id', 'measurement_id'])
    new_iris.rename(columns={'species_name':'species'}, inplace=True)
    dummy_df = pd.get_dummies(new_iris[['species']], dummy_na=False, drop_first=True)
    df = pd.concat([dummy_df, new_iris], axis =1)
    return df

#Prep Titanic
def prep_titanic(df):
    df.drop_duplicates(inplace=True)
    df = df.drop(columns=['age', 'deck', 'embarked', 'class','passenger_id'])
    df['embark_town'] = df.embark_town.fillna(value='Southampton')
    cat_col = [col for col in df.columns if df[col].dtypes == 'object']
    dummy_df = pd.get_dummies(df[cat_col], dummy_na=False, drop_first = [True,True])
    df = pd.concat([dummy_df, df], axis =1)
    return df

#Prep Telco
def prep_telco(telco):
    telco.drop(columns =['customer_id', 'contract_type_id', 'internet_service_type_id', 'payment_type_id', 'Unnamed: 0'], inplace =True)

    telco['total_charges'] = telco['total_charges'].str.strip()
    telco = telco[telco.total_charges != '']
    telco['total_charges'] = telco.total_charges.astype(float)

    dummy_df = pd.get_dummies(telco[['multiple_lines',
                              'online_security',
                              'online_backup',
                              'device_protection',
                              'tech_support',
                              'streaming_tv',
                              'streaming_movies',
                              'contract_type',
                              'internet_service_type',
                              'payment_type',
                              'gender',
                              'partner',
                              'dependents',
                              'phone_service',
                              'paperless_billing',
                              'churn']], dummy_na=False, drop_first=True)
    telco = pd.concat([telco, dummy_df], axis=1)
    return telco
