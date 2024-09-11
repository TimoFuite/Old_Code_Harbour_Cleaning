import pandas as pd

def clean_df(df):
    columns_to_encode = ['REMOVED', 'REMOVED', 'REMOVED', 'REMOVED']
    df = pd.get_dummies(df, columns=columns_to_encode, dtype=int)
    
    df['zwaaien'] = df['REMOVED'].map({'REMOVED': 0, 'REMOVED': 1}).astype(int)
    df.drop(columns=['REMOVED'], inplace=True, errors='ignore')
    
    df['loodsen'] = df['REMOVED'].astype(int)
    df.drop(columns=['REMOVED'], inplace=True, errors='ignore')
    
    df = df[df['REMOVED'] != '#']
    
    df = df.dropna().copy()
    
    df['REMOVED'] = (df['REMOVED'] == 'REMOVED').astype(int)
    df.drop(columns=['REMOVED'], inplace=True)
    
    df['REMOVED'] = (df['REMOVED'] <= 20).astype(int)
    df['REMOVED'] = ((df['REMOVED'] > 20) & (df['REMOVED'] <= 30)).astype(int)
    df['REMOVED'] = ((df['REMOVED'] > 30) & (df['REMOVED'] <= 40)).astype(int)
    df['REMOVED'] = df['REMOVED'].astype(int)

    df.drop(columns=["REMOVED", "REMOVED", "REMOVED", "REMOVED",
                     'REMOVED', "REMOVED"], inplace=True, errors='ignore')
    df.drop(columns=['REMOVED', 'REMOVED', 'REMOVED', 'REMOVED', 'REMOVED', 'REMOVED', 'REMOVED'], inplace=True, errors='ignore')

    df.drop(columns=['REMOVED', 'REMOVED', 'REMOVED'], inplace=True, errors='ignore')
    
    df.drop(columns=['REMOVED', 'REMOVED', 'REMOVED'], inplace=True, errors='ignore')
    return df

def tijd(df):
    def bepaal_seizoen(datum):
        maand = datum.month

        if maand % 12 in [0, 1, 2]:
            return 'Winter'
        elif maand % 12 in [3, 4, 5]:
            return 'Lente'
        elif maand % 12 in [6, 7, 8]:
            return 'Zomer'
        elif maand % 12 in [9, 10, 11]:
            return 'Herfst'
        else:
            return '#'

    def time_period(tijd):
        uur = tijd.hour
        
        if 6 <= uur < 12:
            return 'Ochtend'
        elif 12 <= uur < 18:
            return 'Middag'
        elif 18 <= uur < 24:
            return 'Avond'
        elif 0 <= uur < 6:
            return 'Nacht'
        else:
            return '#'

    df['REMOVED'] = pd.to_datetime(df['REMOVED'])
    
    df['seizoen'] = df['REMOVED'].apply(bepaal_seizoen)
    
    df = pd.get_dummies(df, columns=['seizoen'], prefix='seizoen', dtype=int)
    
    df['tijdvak'] = df['REMOVED'].apply(time_period)
    
    df = pd.get_dummies(df, columns=['tijdvak'], prefix='tijdvak', dtype=int)
    
    return df

def wind_direction(df):
    def degrees_to_wind_direction(degrees):
        if 22.5 <= degrees < 67.5:
            return 'NE'
        elif 67.5 <= degrees < 112.5:
            return 'E'
        elif 112.5 <= degrees < 157.5:
            return 'SE'
        elif 157.5 <= degrees < 202.5:
            return 'S'
        elif 202.5 <= degrees < 247.5:
            return 'SW'
        elif 247.5 <= degrees < 292.5:
            return 'W'
        elif 292.5 <= degrees < 337.5:
            return 'NW'
        else:
            return 'N'
    
    df_encoded = pd.get_dummies(df['REMOVED'].apply(degrees_to_wind_direction))
    df_encoded = df_encoded.astype(int)
    df = pd.concat([df, df_encoded], axis=1)
    
    return df
