import pandas as pd

def get_data(file_path='data/city_pollution.csv', sep=','):
    try:
        return pd.read_csv(file_path, sep=sep)
    except FileNotFoundError as e:
        print('Unable to locate the file at the provided path')
    except Exception as e:
        print(e)

def display_data(data, col_num = 5):
    print(data.head(col_num))

def filter_data_row(data, col_name, row_filter):
    assert col_name in data.columns, "The column name {} does not exist".format(col_name)
    assert row_filter in data[col_name].unique(), "The city name {} does not exist".format(row_filter)
    return data[data[col_name] == row_filter]

def filter_data_col(data, col_name=[]):
    for items in col_name:
        assert items in data.columns, "The column name {} does not exist".format(items)
    return data[col_name]

def export_data(data, file_name=''):
    data.to_csv('data/{}.csv'.format(file_name),index=False)
    

if __name__ == '__main__':
    
    data = get_data()

    data_processing = filter_data_row(data, 'city', 'Delhi')
    processed_data = filter_data_col(data_processing, ['date', 'pm2.5'])

    export_data(processed_data, 'pm2.5')
