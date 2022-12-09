# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:39:59 2022

@author: RajaI
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def Read_File(DATA):
    '''
    Function to print countires as columns and years as columns
    DATA : Nmae of Dataset (World Bank)
   '''
# File in original Worldbank format
    YearsAsCol = DATA
# Doing the tranpose
    CountiresAsCol = DATA.set_index('Country Name').T

    return YearsAsCol, CountiresAsCol


DATA = pd.read_csv('C:\\Users\\RajaI\\Desktop\\climate change\\data.csv')
print(Read_File(DATA))


def CO2BarPlot():
    '''
    Function to produce barplot comparing the C02 Emission of the  countries
    in 2014, 2015 and 201
    '''
# Calling function Read_File(DATA) for performing data cleaning
    Read_File(DATA)

# Clean up Dataset for relavant information
# Extract 2015 and 2016 data of C02 Emission of MyCountries
    MyCountries = DATA[["Country Name", "Indicator Code", "2014", "2015",
                        "2016"]]
# CO2 emissions data for 8 countries
    MyCountries = MyCountries[(MyCountries['Indicator Code'] ==
                              'EN.ATM.CO2E.GF.ZS') &
                              ((MyCountries['Country Name'] == 'China') |
                              (MyCountries['Country Name'] == 'United States')
                              | (MyCountries['Country Name'] == 'Germany')
                              | (MyCountries['Country Name'] == 'Japan')
                              | (MyCountries['Country Name'] == 'India')
                              | (MyCountries['Country Name'] == 'Aruba') |
                              (MyCountries['Country Name'] == 'South Africa')
                              | (MyCountries['Country Name'] == 'Zambia'))]

# Dropping the rows with null values
    MyCountries = MyCountries.dropna()
#
    MyCountries.plot(title='CO2 Emissions of Top Countries',
                     x="Country Name", kind="barh")

    return MyCountries


CO2BarPlot()


def MethaneBarPlot():
    '''
    Function to produce barplot comparing the Methane Gas Emission of the
    countries in 2014, 2015 and 201
    '''
# Calling function Read_File(DATA) for performing data cleaning
    Read_File(DATA)

# Clean up Dataset for relavant information
# Extract 2015 and 2016 data of C02 Emission of MyCountries
    MyCountries = DATA[["Country Name", "Indicator Code", "2014", "2015",
                        "2016"]]
# CO2 emissions data for 8 countries
    MyCountries = MyCountries[(MyCountries['Indicator Code'] ==
                              'EN.ATM.METH.KT.CE') &
                              ((MyCountries['Country Name'] == 'China') |
                              (MyCountries['Country Name'] == 'United States')
                              | (MyCountries['Country Name'] == 'Germany')
                              | (MyCountries['Country Name'] == 'Japan')
                              | (MyCountries['Country Name'] == 'India')
                              | (MyCountries['Country Name'] == 'Aruba') |
                              (MyCountries['Country Name'] == 'South Africa')
                              | (MyCountries['Country Name'] == 'Zambia'))]

# Dropping the rows with null values
    MyCountries = MyCountries.dropna()
#
    MyCountries.plot(title='Metane Gas Emissions of Top Countries',
                     x="Country Name", kind="barh")

    return MyCountries


MethaneBarPlot()


# Heatmap visulation of C02 Emission of different countries
def heatmap():
    '''
    Function to produce heatmap to find the correlation between the columns
    '''
# Calling function Read_File(DATA) for performing data cleaning
    Read_File(DATA)

# Clean up Dataset for relavant information
# Extract 2015 and 2016 data of C02 Emission of MyCountries
    MyCountries = DATA[["Country Name", "Indicator Code", "2012", "2013",
                        "2014", "2015", "2016"]]
# CO2 emissions data for 8 countries
    MyCountries = MyCountries[((MyCountries['Indicator Code'] ==
                              'EN.ATM.CO2E.GF.ZS') |
                               (MyCountries['Indicator Code'] ==
                               'EN.ATM.CO2E.SF.ZS') |
                               (MyCountries['Indicator Code'] ==
                               'EN.ATM.CO2E.LF.ZS')) &
                              ((MyCountries['Country Name'] == 'China') |
                              (MyCountries['Country Name'] == 'United States')
                              | (MyCountries['Country Name'] == 'Germany')
                              | (MyCountries['Country Name'] == 'Japan')
                              | (MyCountries['Country Name'] == 'India')
                              | (MyCountries['Country Name'] == 'Aruba') |
                              (MyCountries['Country Name'] == 'South Africa')
                              | (MyCountries['Country Name'] == 'Zambia'))]

# Dropping the rows with null values
    MyCountries = MyCountries.dropna()

# Pivot is used to create a new derived table from the given data frame
    x = MyCountries.pivot("Country Name", "Indicator Code")
    print(x)
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(x.corr(), annot=True, fmt=".1f", center=0, ax=ax)
    plt.savefig('correlation_us.png')
    plt.show()


heatmap()
