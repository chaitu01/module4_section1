[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Module 4 : Data Preparation Basics  
Module 4 is on preparing your data for machine learning.
This module consists of 
* data type identification
* formatting
* filling missing data
* encoding categorical variables
* scaling
* creating pipelines

We have introduced sections to this module to make it easier to follow.
This project is for Section 1.

## License
This code is hosted in a private repository to regulate access to Module 4. You can share this under MIT license.
After completing the module host the end product in an open repository.  

## Section 1 : Data Type Identification
Data scientists often have to deal with raw data. 
In fact many data scientists insist on raw data to make sure that third party transforms has not interfered with the original information.

You may receive original data in many different formats such as csv, Excel, database tables.
Based on the way data have been generated or as a result of data imports, data types in your Pandas data frame may not be correct.
Therefore we identify data types in the beginning of our analysis. 

This section is focused on:
 * studying ways to identify data types
 * writing a tool to automatically identify data types and transform


### Study
1. Study the most common data types
    1. Numeric that includes integer and float
    1. Boolean
    1. Categorical
    1. Date time formats
    1. String

For raw data, Pandas data types may be confusing. 
In addition to that the values may consists of missing data represented by various characters, strings or null value forms. 
How do you identify the best data type for each column?
    
Discuss how you differentiate each data type. What are the key characteristics of the following?
- Numeric that includes integer and float
- Boolean
- Categorical
- Date time formats
- String

## Application
Note: You have to implement as described in TODO sections in the source.
1. Complete the functions in DateTimeTransforms of [meta_data.py](./meta_data.py).
   Read TODO sections in each function.
1. Write pytests for the implemented methods of DateTimeTransforms in [test_meta_data.py](./test_meta_data.py)
1. Implement the classes: BooleanTransformedData, NumericTransformedData, CategoryTransformedData, 
DateTimeTransformedData and StringTransformedData in [type_transforms.py](./type_transforms.py).
   Follow TODO.
1. Write pytests for the implemented classes and methods in [test_type_transforms.py](./test_type_transforms.py)
1. Write a document for future use. That should include your ideas and the following.
    1. There are many other data types that we need to explore in data science.
        1. Apart from the studied data types, what are the other interesting data types? 
        1. Why are they important?
        1. What are the examples? 
    1. What are the suggested improvements to
        1. Function in DateTimeTransforms
        1. BooleanTransformedData
        1. NumericTransformedData
        1. CategoryTransformedData
        1. DateTimeTransformedData
        1. StringTransformedData        
    1. What are the drawbacks of our approach? 
    1. How can we improve this python module?

### Data Sets for Testing
Use the following 15 data sets for testing
1. https://archive.ics.uci.edu/ml/datasets/iris
1. https://archive.ics.uci.edu/ml/datasets/Automobile
1. https://archive.ics.uci.edu/ml/datasets/Sports+articles+for+objectivity+analysis
1. https://archive.ics.uci.edu/ml/datasets/Air+Quality
1. https://archive.ics.uci.edu/ml/datasets/Real-time+Election+Results%3A+Portugal+2019
1. https://www.kaggle.com/mrmorj/hospital-bed-capacity-and-covid19
1. https://www.kaggle.com/andrewmvd/udemy-courses
1. https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data
1. https://www.kaggle.com/lakshmilovemysoul/psychometric-data/data
1. https://www.kaggle.com/osmi/mental-health-in-tech-survey
1. https://www.kaggle.com/jboysen/mri-and-alzheimers
1. The data set used in Module 2
1. Three additional data sets of your choice

- Some data sets have more than one file. Use all the files.
- How do you automate the testing across number of different data sets?
- How do you extract data from different formats?
             

## Quality Standard of Your Work
1. Code should follow PEP8 Standard
1. Docstrings of the classes and methods should be written
1. Code should work as described in TODO sections in the original source
1. Host your code on your GitHub in a public or private repository as you prefer. 
- If it is a public repository, send the link for us to evaluate.
- If it is a private repository, share (view only) with our GitHub usernames [DataDisca](https://github.com/DataDisca) and/or [mbtl-datadisca](https://github.com/mbtl-datadisca).

	Send us a notification to start the evaluation.
	We evaluate your code for your technical progress.

 
			


    


      
 
 
