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
    srs = pd.Series([])
    assert
