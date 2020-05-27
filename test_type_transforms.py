"""
Purpose: Data types used in DataDisca applications are defined here

Contributors:
<chaitanya anantha>

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""
import pytest
import pandas as pd
from type_transforms import BooleanTransformedData, NumericTransformedData, TypeTransformedData
from type_transforms import CategoryTransformedData, DateTimeTransformedData, StringTransformedData
import pandas as pd
def test__import_kwargs():
    srs = pd.Series([1,2,3])
    typetransformdata = BooleanTransformedData(srs)
    typetransformdata._import_kwargs(threshold = 75, sample_size = 8, iterations = 3, success_count = 100)
    assert typetransformdata.threshold == 75
    assert typetransformdata.sample_size == 8
    assert typetransformdata.iterations == 3
    assert typetransformdata.success_count != 100

def test_is_my_type():
    test_df = pd.read_csv('covid_data.csv')
    type_series =
    index = 0
    for col in test_df:
        srs = test_df[col]
        true_count = 0
        boolean_object = BooleanTransformedData(srs)
        if boolean_object.is_my_type() == True:
            true_count +=1
            series_type = boolean_object.data_type
        numeric_object = NumericTransformedData(srs)
        if numeric_object.is_my_type() == True:
            true_count +=1
            series_type = numeric_object.data_type
        category_object = CategoryTransformedData(srs)
        if category_object.is_my_type() == True:
            true_count +=1
            series_type = category_object.data_type
        datetime_object = DateTimeTransformedData(srs)
        if datetime_object.is_my_type() == True:
            true_count +=1
            series_type = datetime_object.data_type
        if true_count == 0:
            string_object = StringTransformedData(srs)
            if string_object.is_my_type() == True:
                series_type = string_object.data_type
                true_count +=1
        index +=1
        assert type_series[index] == series_type
        assert true_count == 1
