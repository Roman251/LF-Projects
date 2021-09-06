import data_process
import pandas as pd


def data_frame():
    return pd.DataFrame({
        'col_a' : ['a', 'a', 'b'],
        'col_b' : ['b', 'b', 'c'],
        'col_c' : ['c', 'c', 'd'],
        'col_d' : ['d', 'd', 'e'],
        'col_e' : ['e', 'e', 'f'],
    })

data = data_frame()

def test_filter_row():
    actual = data_process.filter_data_row(data, 'col_c', 'd')
    expected = pd.DataFrame({'col_a' : ['b'],
        'col_b' : ['c'],
        'col_c' : ['d'],
        'col_d' : ['e'],
        'col_e' : ['f'],})

    assert all(actual.reset_index(drop=True) == expected.reset_index(drop=True))

def test_filter_col():
    actual = data_process.filter_data_col(data, ['col_a', 'col_d', 'col_e'])
    expected = pd.DataFrame({
        'col_a' : ['a', 'a', 'b'],
        'col_d' : ['d', 'd', 'e'],
        'col_e' : ['e', 'e', 'f'],
    })
    
    assert all(actual.reset_index(drop=True) == expected.reset_index(drop=True))


