# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:39:59 2022

@author: RajaI
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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
# print(Read_File(DATA))


# -----------------------------------------------------------------------------


# First viualisation to compare C02 Emission of different countries
def CO2BarPlot():
    '''
    Function to produce barplot comparing the C02 Emission of the  countries
    in 2014, 2015 and 2016
    '''
# Calling function Read_File(DATA) for performing data cleaning
    Read_File(DATA)

# Clean up Dataset for relavant information
# Extract 2014, 2015 and 2016  data of Countries
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
# Reset Index of Dataframe
    MyCountries = MyCountries.reset_index(drop=True)
    # print(MyCountries)
    MyCountries.plot(title='CO2 Emissions of Countries',
                     x="Country Name", kind="barh",
                     color=['black', 'red', 'green', 'blue', 'cyan'])
    plt.show()


CO2BarPlot()

# -----------------------------------------------------------------------------


# Second viualisation to compare Methane Emission of different countries
def MethaneBarPlot():
    '''
    Function to produce barplot comparing the Methane Gas Emission of the
    countries in 2014, 2015 and 2016
    '''
# Calling function Read_File(DATA) for performing data cleaning
    Read_File(DATA)

# Clean up Dataset for relavant information
# Extract 2014, 2015 and 2016 data of Countries
    MyCountries = DATA[["Country Name", "Indicator Code", "2014", "2015",
                        "2016"]]
# Methane emissions data for 8 countries
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
# Reset Index of Dataframe
    MyCountries = MyCountries.reset_index(drop=True)
    # print(MyCountries)
    MyCountries.plot(title='Methane Emissions of Countries',
                     x="Country Name", kind="barh")
    plt.show()


MethaneBarPlot()


# -----------------------------------------------------------------------------


# Heatmap visulaisation of different indicators
def heatmap():
    '''
    Function to produce heatmap of different indicators of different countries
    in order 
    '''
# Calling function Read_File(DATA) for performing data cleaning
    Read_File(DATA)

# Clean up Dataset for relavant information
# Extract 2012, 2013 and 2014 data of Countries
    MyIndicators = DATA[["Country Name", "Indicator Name", "2012", "2013",
                        "2014"]]
# Indicators data for 8 countries
    MyIndicators = MyIndicators[((MyIndicators['Indicator Name'] ==
                                'Arable land (% of land area)') |
                                 (MyIndicators['Indicator Name'] ==
                                 'Agricultural land (% of land area)') |
                                 (MyIndicators['Indicator Name'] ==
                                 'Population, total')) &
                                ((MyIndicators['Country Name'] == 'China') |
                                 (MyIndicators['Country Name'] ==
                                  'United States') |
                                 (MyIndicators['Country Name'] == 'Germany') |
                                 (MyIndicators['Country Name'] == 'India'))]

# Dropping the rows with null values
    MyIndicators = MyIndicators.dropna()
# Pivot is used to create a new derived table from the given data frame
    x = MyIndicators.pivot("Country Name", "Indicator Name", ["2012", "2013",
                                                              "2014"])
    # print(x)

    ax = plt.axes()
    sns.heatmap(x.corr(), annot=True, fmt=".1f", ax=ax)
    ax.set_title('Heatmap of CO2 Emission of Countries')
    plt.show()


heatmap()


# -----------------------------------------------------------------------------


# Fourth visulation to compare Total population and urban population of few
# countries
def Population():
    '''
    Function to analyse changes in population of countries over time using
    line graph
    '''
# Calling function Read_File(DATA) for performing data cleaning
    Read_File(DATA)

# Clean up Dataset for relavant information
# Extract 1990, 2009 and 2019 data of Countries
    MyCountries = DATA[["Country Name", "Indicator Code", "1990",
                        "2009", "2019"]]
    # Urban Population data for 8 countries
    UrbanPop = MyCountries[((MyCountries['Indicator Code'] == 'SP.URB.TOTL')) &
                           ((MyCountries['Country Name'] == 'China') |
                           (MyCountries['Country Name'] == 'United States')
                           | (MyCountries['Country Name'] == 'Germany')
                           | (MyCountries['Country Name'] == 'Japan')
                           | (MyCountries['Country Name'] == 'India')
                           | (MyCountries['Country Name'] == 'Aruba') |
                           (MyCountries['Country Name'] == 'South Africa')
                           | (MyCountries['Country Name'] == 'Zambia'))]


# Dropping the rows with null values
    UrbanPop = UrbanPop.dropna()
# Reset Index of Dataframe
    UrbanPop = UrbanPop.reset_index(drop=True)
    # print(UrbanPop)

    # Total Population data for 8 countries
    TotalPop = MyCountries[((MyCountries['Indicator Code'] == 'SP.POP.TOTL')) &
                           ((MyCountries['Country Name'] == 'China') |
                           (MyCountries['Country Name'] == 'United States')
                           | (MyCountries['Country Name'] == 'Germany')
                           | (MyCountries['Country Name'] == 'Japan')
                           | (MyCountries['Country Name'] == 'India')
                           | (MyCountries['Country Name'] == 'Aruba') |
                           (MyCountries['Country Name'] == 'South Africa')
                           | (MyCountries['Country Name'] == 'Zambia'))]


# Dropping the rows with null values
    TotalPop = TotalPop.dropna()
# Reset Index of Dataframe
    TotalPop = TotalPop.reset_index(drop=True)
    # print(UrbanPop)

    fig, (ax, ax2) = plt.subplots(ncols=2, sharey=True)
    ax.invert_xaxis()
    ax.yaxis.tick_right()

    TotalPop.plot(title='Total Population of Countries',
                  x="Country Name", kind="bar", legend=False, ax=ax)
    UrbanPop.plot(title='Urban Population of Countries',
                  x="Country Name", kind="bar", ax=ax2)
    plt.tight_layout()
    plt.show()


Population()

# -----------------------------------------------------------------------------


def skew():
    """ Function to calculates the centralised and normalised skewness of dist.
    """
    # Calling function Read_File(DATA) for performing data cleaning
    Read_File(DATA)

    # Clean up Dataset for relavant information
    # Extract 2019 data of Countries
    MyCountries = DATA[["Country Name", "Indicator Code", "2019"]]
    # Population Growth data for 8 countries
    PopGrowth = MyCountries[((MyCountries['Indicator Code'] == 'SP.POP.GROW'))
                            & ((MyCountries['Country Name'] == 'China') |
                            (MyCountries['Country Name'] == 'United State')
                            | (MyCountries['Country Name'] == 'Japan')
                            | (MyCountries['Country Name'] == 'India')
                            | (MyCountries['Country Name'] == 'Aruba')
                            | (MyCountries['Country Name'] == 'Zambia'))]

# Dropping the rows with null values
    PopGrowth = PopGrowth.dropna()
# Reset Index of Dataframe
    PopGrowth = PopGrowth.reset_index(drop=True)
    # print(PopGrowth)

    # calculates average and std dev for centralising and normalising
    aver = PopGrowth.mean(axis=1, numeric_only=True)
    std = PopGrowth.std(axis=1, numeric_only=True)

    # now calculate the skewness
    Skew = np.sum((((PopGrowth-aver) / std)**3) / len(PopGrowth), axis=1)
    # print(value)

    Skew.plot(title='Skewness of Countries')
    plt.show()


skew()


# -----------------------------------------------------------------------------


def LandBasedComparison():
    '''
    Function to comapre change in Arable and Agricultural Land of China
    and Cyrus
    '''
    # Calling function Read_File(DATA) for performing data cleaning
    Read_File(DATA)

    # Clean up Dataset for relavant information
    # Extract 2016, 2017, 2018 and 2019 data of Countries
    MyCountires = DATA[["Country Name", "Indicator Code", "2016"]]
    # Agricultural land for two countires
    ArblLand = MyCountires[(MyCountires['Indicator Code'] ==
                            'AG.LND.ARBL.ZS') &
                           ((MyCountires['Country Name'] == 'Germany') |
                           (MyCountires['Country Name'] == 'Cyprus'))]

    AgriLand = MyCountires[(MyCountires['Indicator Code'] ==
                            'AG.LND.AGRI.ZS') &
                           ((MyCountires['Country Name'] == 'Germany') |
                           (MyCountires['Country Name'] == 'Cyprus'))]

    ax = ArblLand.plot(x="Country Name", kind="bar")
    AgriLand.plot(title='Change in Arable and Agricultural land',
                  x="Country Name", kind="bar", ax=ax)
    plt.show()


LandBasedComparison()
