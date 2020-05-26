"""
Purpose: Data types used in DataDisca applications are defined here

Contributors:
<Include Your Name/Names>

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""


class DataTypes:
    BOOLEAN: int = 1
    INTEGER: int = 2
    FLOAT: int = 3
    STRING: int = 4
    CATEGORICAL: int = 5
    DATE: int = 6
    TIME: int = 7
    DATETIME: int = 8
    SHORT_TIME: int = 9
    SHORT_DATETIME: int = 10

    SECONDS: int = 11
    MINUTES: int = 12
    HOURS: int = 13
    DAYS: int = 14
    WEEKS: int = 15
    YEARS: int = 16
    EPOCH: int = 17


class DateTimeTransforms:
    DEFAULT_DATE_FORMAT = '%d/%m/%Y'  # Refer https://docs.python.org/3/library/datetime.html
    DEFAULT_TIME_FORMAT = '%H:%M:%S'
    DEFAULT_DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'
    DEFAULT_SHORT_TIME_FORMAT = '%H:%M'
    DEFAULT_SHORT_DATETIME_FORMAT = '%d/%m/%Y %H:%M'

    @staticmethod
    def to_date_str(my_date_time) -> str:
        """
        :return: str

        TODO: Return str in DEFAULT_DATE_FORMAT
        """
        return(my_date_time.strftime(DateTimeTransforms.DEFAULT_DATE_FORMAT))

    @staticmethod
    def to_time_str(my_date_time) -> str:
        """
        :return:

        TODO: Return str in DEFAULT_DATE_FORMAT
        """
        return(my_date_time.strftime(DateTimeTransforms.DEFAULT_TIME_FORMAT))

    @staticmethod
    def to_datetime_str(my_date_time) -> str:
        """
        :return:

        TODO: Return str in DEFAULT_DATETIME_FORMAT
        """
        return(my_date_time.strftime(DateTimeTransforms.DEFAULT_DATETIME_FORMAT))

    @staticmethod
    def to_short_time_str(my_date_time) -> str:
        """
        :return:

        TODO: Return str in DEFAULT_SHORT_TIME_FORMAT
        """
        return(my_date_time.strftime(DateTimeTransforms.DEFAULT_SHORT_TIME_FORMAT))

    @staticmethod
    def to_short_datetime_str(my_date_time) -> str:
        """
        :return:

        TODO: Return str in DEFAULT_SHORT_DATETIME_FORMAT
        """
        return(my_date_time.strftime(DateTimeTransforms.DEFAULT_SHORT_DATETIME_FORMAT))


if __name__ == "__main__":
    print(DateTimeTransforms.DEFAULT_DATE_FORMAT)
