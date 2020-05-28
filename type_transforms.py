"""
Purpose: Data type transforms

Contributors:
<Include Your Name/Names>

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""

import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from meta_data  import DataTypes, DateTimeTransforms
from fractions import Fraction
import datetime
from dateutil.parser import parse



class TypeTransformedData(ABC):

    def __init__(self, srs: pd.Series, run: bool = True, **kwargs):

        self.data_type: int = None
        self.srs_out: pd.Series = None
        self.success_count: float = None
        self.percentage: float = None
        self.threshold: float = 80
        self.sample_size: float = 5
        self.iterations: int = 3

        self.srs: pd.Series = srs
        self.run: bool = self.run if run is None else run

        self._import_kwargs(**kwargs)
        if self.run:
            self.is_my_type()

    def _import_kwargs(self, **kwargs):
        accepted_keys: set = {'threshold', 'sample_size', 'iterations'}
        self.__dict__.update((key, value) for key, value in kwargs.items() if key in accepted_keys)

    @abstractmethod
    def is_my_type(self) -> bool:
        """
        :return: True if self.percentage >= self.threshold else False

        TODO:
            Identify if the series is of my type
            Set the following parameters of the object
                srs_out : transformed data to my type
                success_count: number of successfully transformed values to my type
                percentage: number of successfully transformed values to my type
                set type as given in the constants in the DataTypes class if self.percentage >= self.threshold
        """


class BooleanTransformedData(TypeTransformedData):

    def is_my_type(self) -> bool:
        """

        :return: True if self.percentage >= self.threshold else False

        TODO:
            Check if the given column is boolean.
            The series can be of any type originally.
            You can identify boolean fields by looking at data, when the pandas data type is misleading.
            Use the following criterion for the first version.
                string or boolean data {true, false}
                string or any numeric data {0,1}
                string {'yes','no'}
            -
            In string types the values are not case sensitive
            Read the the abstract method notes

        """
        self.success_count = 0
        self.srs_out = self.srs
        for index, value in self.srs.items():
            if pd.isnull(value):
                continue
            if type(value) == str:
                value = str.lower(value)
            if value in ['yes', '1', 'true', 1, True]:
                value = True
                self.success_count += 1
            elif value in ['no', '0', 'false', 0, False]:
                value = False
                self.success_count += 1
            self.srs_out.loc[index] = value

        self.percentage = (self.success_count/self.srs_out.size)*100
        if self.percentage >= self.threshold:
            self.data_type = 1
            return True
        else:
            return False






class NumericTransformedData(TypeTransformedData):

    def is_my_type(self) -> bool:
        """

        :return: True if self.percentage >= self.threshold else False

        TODO:
            Check if the given column is numeric.
            The column may already be numeric or the numeric values may be:
            1. Included in quotations eg: '534', "534"
            2. May be leading or trailing spaces there eg: " 534"
            3. Original data may have meaningful decorators eg: $, %, l, kg, 3/5.
            identify the best type: integer or float
            set the corresponding type {'INTEGER','FLOAT'} as in DataTypes
            set the number of decimal points you observe as self.precision
            Read the the abstract method notes

        """
        self.success_count = 0
        self.srs_out = self.srs
        float_count = 0
        convert_to_type = int
        for value in self.srs:
            if type(value) == float:
                float_count +=1
        if (float_count/self.srs.size) >= 0.10:
            convert_to_type = float

        for index, value in self.srs.items():
            if pd.isnull(value):
                continue
            if type(value) == int and convert_to_type == float:
                self.srs_out.loc[index] = float(value)
                self.success_count +=1
            elif type(value) == float and convert_to_type == int:
                self.srs_out.loc[index] = int(value)
                self.success_count +=1
            elif type(value) == str:
                value = value.strip()
                if not(value.isnumeric):
                    if value[0] == '.':
                        value = '0' + value
                    elif not(value[0].isnumeric()):
                        value = value[1:]
                    elif not(value[-1].isnumeric()):
                        value = value[:-1]
                    else:
                        try:
                            value = float(Fraction(value))
                            if convert_to_type == int:
                                self.srs_out.loc[index] = int(value)
                            else:
                                self.srs_out.loc[index] = value
                            self.success_count +=1
                            continue
                        except:
                            pass
                try:
                    value = int(value)
                except:
                    try:
                        value = float(value)
                    except:
                        continue
                self.srs_out.loc[index] = value
                self.success_count += 1




        self.percentage = (self.success_count/self.srs_out.size)*100
        if self.percentage >= self.threshold:
            if convert_to_type == float:
                self.data_type = 3
            else:
                self.data_type = 2
            return True
        else:
            return False


class CategoryTransformedData(TypeTransformedData):

    def __init__(self, srs: pd.Series, run: bool = True, **kwargs):
        self.category_threshold: float = kwargs['category_threshold'] if 'category_threshold' in kwargs.keys() else 10
        super(CategoryTransformedData, self).__init__(srs=srs, run=run, **kwargs)

    def is_my_type(self) -> bool:
        """

        :return: True if self.percentage >= self.threshold else False

        TODO:
            Check if the given column is categorical.
            The values may :
            1. Small number of numeric or string options relative to the length of the series
                i.e  number of unique values <= self.category_threshold which is a parameter you can pass
            2. May be leading or trailing spaces there eg: " 534"
            Read the the abstract method notes

        """
        self.success_count = 0
        self.srs_out = self.srs
        for index, value in self.srs.items():
            if pd.isnull(value):
                continue
            if type(value) == int:
                self.srs_out.loc[index] = str(float(value))
                self.success_count +=1
            elif type(value) == float:
                self.srs_out.loc[index] = str(value)
                self.success_count +=1
            if type(value) == str:
                value = value.strip()
                try:
                    self.srs_out.loc[index] = str(float(value))
                    self.success_count +=1
                except:
                    self.srs_out.loc[index] = value
        if self.srs_out.unique().size <= self.category_threshold:
            self.percentage = (self.success_count/self.srs_out.size)*100
            if self.percentage >= self.threshold:
                self.data_type = 5
                return True
            else:
                return False
        else:
            self.percentage = 0
            self.success_count = 0
            return False



class DateTimeTransformedData(TypeTransformedData):

    def __init__(self, srs: pd.Series, run: bool = True, **kwargs):
        self.original_format: float = None
        super(DateTimeTransformedData, self).__init__(srs=srs, run=run, **kwargs)

    def is_my_type(self) -> bool:
        """

        :return: True if self.percentage >= self.threshold else False

        TODO:
            Check if the given column is date time. The original series data may be datetime, string or any other type
            eg: "2020-05-17 15:12:23", "2020-May-17 05:12:23PM", "17/05/2020" , "13:12",  datetime(2016, 3
            , 13, 5, tzinfo=timezone.utc)
            Refer the following links for non-exhaustive lists of different formats
            https://www.ibm.com/support/knowledgecenter/bg/SSLVMB_23.0.0/spss/base/syn_date_and_time_date_time_formats.html
            There can be all combination of the date time formats:
                https://docs.python.org/3/library/datetime.html
            Programmatically identify the best for series you have then transform
            #
            set the identified original format in self.original_format
            #  reading https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
            convert data to date time format
            Read the the abstract method notes

        """
        self.success_count = 0
        self.srs_out = self.srs
        time_format_count = 0
        datetime_format_count = 0
        date_format_count = 0
        short_time_format_count = 0
        short_date_time_format_count = 0
        for index, value in self.srs.items():
            if pd.isnull(value):
                continue
            if type(value) == datetime.datetime:
                datetime_format_count +=1
                self.success_count +=1
                continue
            else:
                if type(value) == datetime.time:
                    time_format_count +=1
                elif type(value) == datetime.date:
                    date_format_count +=1
                value = str(value)
                value = value.strip()
                try:
                    value = parse(value)
                    value = value.strftime('%d/%m/%Y %H:%M:%S')
                    value = datetime.datetime.strptime(value, '%d/%m/%Y %H:%M:%S')
                    self.success_count +=1
                    self.srs_out.loc[index] = value
                except:
                    pass

        self.percentage = (self.success_count/self.srs_out.size)*100
        if self.percentage >= self.threshold:
            self.data_type = 8
            return True
        else:
            return False


class StringTransformedData(TypeTransformedData):

    def is_my_type(self) -> bool:
        """

        :return: True if self.percentage >= self.threshold else False

        TODO:
            Check if the given column is string or sting convertible.
            You will see almost everything is string convertible.
            We use this method as the last resort.
            Read the the abstract method notes
        """
        self.success_count = 0
        self.srs_out = self.srs
        for index, value in self.srs.items():
            if pd.isnull(value):
                continue
            if type(value) == str:
                value = value.strip()
                self.success_count +=1
            else:
                try:
                    value = str(value)
                    value = value.strip()
                    self.success_count +=1
                except:
                    continue
            self.srs_out.loc[index] = value

        self.percentage = (self.success_count/self.srs_out.size)*100
        if self.percentage >= self.threshold:
            self.data_type = 4
            return True
        else:
            return False

if __name__ == "__main__":
    # btd = CategoryTransformedData(pd.Series([1, 2, 3]))
    btd = CategoryTransformedData(pd.Series([1, 2, 3]), False, **{'sample_size': 1000, 'category_threshold': 50})
    x = btd.is_my_type()
    print(btd.category_threshold)
    print(btd.sample_size)
