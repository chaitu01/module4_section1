import pandas as pd
from anytree import NodeMixin, RenderTree
from abc import ABC, abstractmethod
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import numpy as np


class DataTypes:
    BOOLEAN = 1
    INTEGER = 2
    FLOAT = 3
    STRING = 4
    CATEGORICAL = 5
    DATE = 6
    TIME = 7
    DATETIME = 8
    SHORT_TIME = 9
    SHORT_DATETIME = 10

    SECONDS: float = 11
    MINUTES: float = 12
    HOURS: float = 13
    DAYS: float = 14
    WEEKS: float = 15
    YEARS: float = 16
    EPOCH: float = 17

    DEFAULT_DATE_FORMAT = '%d/%m/%Y'  # Refer https://docs.python.org/3/library/datetime.html
    DEFAULT_TIME_FORMAT = '%H:%M:%S'
    DEFAULT_DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'
    DEFAULT_SHORT_TIME_FORMAT = '%H:%M'
    DEFAULT_SHORT_DATETIME_FORMAT = '%d/%m/%Y %H:%M'

class FieldTransform(NodeMixin):
    function_name: str = None
    scalar: object = None
    scalar_type: str = None  # This can be MinMaxScaler or StandardScaler
    encoder: object = None
    encoder_type: str = None  # This can be OneHotEncoder or LabelEncoder
    from_field: str = None  # field name before transformation
    to_fields: str = []  # field names after transformation


# class TypeTransformedData(ABC):
#     data_type: int = None
#     run: bool = True
#     srs: pd.Series = None
#     srs_out: pd.Series = None
#     success_count: float = None
#     percentage: float = None
#     threshold: float = 80
#     sample_size: float = 5
#     iterations: int = 3
#
#     def __init__(self, srs: pd.Series, run: bool = True, **kwargs):
#         self.srs = srs
#         self.run = self.run if run is None else run
#         self._import_kwargs(**kwargs)
#
#     def _import_kwargs(self, **kwargs):
#         accepted_keys = set(['threshold', 'sample_size', 'iterations'])
#         self.__dict__.update((key, value) for key, value in kwargs.items() if key in accepted_keys)
#
#     @abstractmethod
#     def is_my_type(self) -> bool:
#         """
#         :return:
#
#         TODO:
#             Identify if the series is of my type
#             Set the following parameters of the object
#                 srs_out : transformed data to my type
#                 success_count: number of successfully transformed values to my type
#                 percentage: number of successfully transformed values to my type
#         """



class DataTypeIdentifier:
    srs: pd.Series = None
    data_type: int = None
    srs_out: pd.Series = None
    percentage: float = None
    explore_types: list = None
    _transformed_srs: dict = {}

    def __init__(self, srs: pd.Series, explore_types: list = None):
        self.srs = srs
        self.explore_types = explore_types if explore_types is not None else self.explore_types

    def _is_boolean(self) -> bool:
        """
        :param field_name:
        :return: true or false
        :set:

        TODO:
            Check if the given column is boolean.
            The column can be of any type originally.
            You can identify boolean fields by looking at data rather than the pandas data type.
            Use the following for the first version any of the following can be converted to boolean.
                string or boolean data {true, false}
                string or any numeric data {0,1}
                string {'yes','no'}
            .
            When string types are considered the values should not be case sensitive
            None, Nan, ' ', '-'
        """

    def _is_integer(self) -> bool:
        """
        :return: true or false

        TODO:
            Check if the given column is integer
            The interger values can be

        """



class DataSet:
    data: pd.DataFrame = None
    transformed_data: pd.DataFrame = None
    field_transforms = {}
    pipe_line = {} # This is a dictionary. There is a key for each

    def __init__(self, data:pd.DataFrame):
        self.data = data

    def identify_data_types(self):
        pass

    def standardize_missing_data(self, data: pd.DataFrame = None):
        """
        :param data:
        :param field_name:
        :return:

        The data set can consist of many empty values represented in different formats.
        Example:
        NaN,None,'','-','NA', 'N/A', \spaces, \tabs

        These can be string or in different cases

        TODO:
            Fill all missing data with NaN
            update the following:
                transformed_data

        """












