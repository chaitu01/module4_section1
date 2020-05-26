"""
Purpose: Data types used in DataDisca applications are defined here

Contributors:
chaitanya anantha

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""
from datetime import datetime
import pytest
from meta_data import DateTimeTransforms

def test_to_date_str():
    my_date = datetime.strptime("2018/10/12 30:06:45", '%Y/%m/%d %M:%H:%S')
    assert DateTimeTransforms.to_date_str(my_date) == "12/10/2018"


def test_to_time_str():
    my_date = datetime.strptime("2018/10/12 30:06:45", '%Y/%m/%d %M:%H:%S')
    assert DateTimeTransforms.to_time_str(my_date) == "06:30:45"


def test_to_datetime_str():
    my_date = datetime.strptime("2018/10/12 30:06:45", '%Y/%m/%d %M:%H:%S')
    assert DateTimeTransforms.to_datetime_str(my_date) == "12/10/2018 06:30:45"


def test_to_short_time_str():
    my_date = datetime.strptime("2018/10/12 30:06:45", '%Y/%m/%d %M:%H:%S')
    assert DateTimeTransforms.to_short_time_str(my_date) == "06:30"


def test_to_short_datetime_str():
    my_date = datetime.strptime("2018/10/12 30:06:45", '%Y/%m/%d %M:%H:%S')
    assert (DateTimeTransforms.to_short_datetime_str(my_date)
            == "12/10/2018 06:30")
