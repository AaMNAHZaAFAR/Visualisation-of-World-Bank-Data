# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:39:59 2022

@author: RajaI
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
    plt.ylabel("Country Name")
    plt.xlabel("CO2 Emission")
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
    plt.ylabel("Country Name")
    plt.xlabel("Methane Emission")
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
# Extract 2012 data of Countries
    MyIndicators = DATA[["Country Name", "Indicator Name", "2012"]]
# Indicators data for 8 countries
    MyIndicators = MyIndicators[((MyIndicators['Indicator Name'] ==
                                'Nitrous oxide emissions (% change from 1990)')
                                 | (MyIndicators['Indicator Name'] == 'HFC '
                                    'gas.'
                                    'emissions (thousand metric tons of CO2 '
                                    'equivalent)') |
                                 (MyIndicators['Indicator Name'] ==
                                 'Population, total') |
                                 (MyIndicators['Indicator Name'] ==
                                  'CO2 emissions (kt)') |
                                 (MyIndicators['Indicator Name'] ==
                                  'Methane emissions (kt of CO2 equivalent)') |
                                 (MyIndicators['Indicator Name'] ==
                                  'Total greenhouse gas emissions (kt of CO2 '
                                  'equivalent)'))
                                &
                                ((MyIndicators['Country Name'] ==
                                  'United States') |
                                 (MyIndicators['Country Name'] == 'China') |
                                 (MyIndicators['Country Name'] == 'India'))]

# Dropping the rows with null values
    MyIndicators = MyIndicators.dropna()
    MyIndicators = MyIndicators.pivot("Country Name", "Indicator Name", ["2012"
                                                                         ])
    # print(MyIndicators)

    ax = plt.axes()
    sns.heatmap(MyIndicators.corr(), annot=True, fmt=".1f", ax=ax)
    ax.set_title('Heatmap of C02 Emission of Countries')
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


def skewandkurtosis():
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
    Skew = PopGrowth.skew(axis=0, numeric_only=True)
    Kurtosis = PopGrowth.kurtosis(axis=0, numeric_only=True)

    print(Skew)
    print(Kurtosis)


skewandkurtosis()


# -----------------------------------------------------------------------------


# Fifth visulaisation using lineplot to check GDP
def GDPPLOT(DATA2):
    '''
    Function to comapre GDP of different countries
    '''
    # slice the ‘country’ and ‘country code’ column
    countrycode = DATA2.iloc[:, 0:2]
    # print(countrycode)

    # remove columns which are not useful for further analysis
    DATA2 = DATA2.drop(columns=['Indicator Name', 'Country Code',
                                'Indicator Code', '2019'])

    # rename one column and convert the exp into the unit of millions
    GDPDATA = DATA2.melt(id_vars=['Country Name'], var_name='Year',
                         value_name='gdp')

    # rename one column and convert the gpd into the unit of millions
    GDPDATA.rename(columns={'Country Name': 'Country'}, inplace=True)
    GDPDATA['gdpMillion'] = GDPDATA['gdp'].div(1000000)

    # add the countrycode back to the dataframe
    GDPDATA_merged = GDPDATA.merge(countrycode, left_on='Country',
                                   right_on='Country Name')

    # subset the data for 8 countries after year 1980
    options = ['United States', 'India', 'Thailand', 'Japan']
    GDP = GDPDATA_merged[GDPDATA_merged.Country.isin(options)][['Year',
                                                                'Country',
                                                                'Country Code',
                                                                'gdpMillion']]
    GDP['Year'] = pd.to_datetime(GDP['Year'])
    GDP = GDP.loc[GDPDATA['Year'] > '1980']

    sns.set_style("whitegrid")
    sns.lineplot(x='Year', y='gdpMillion', hue='Country Code',
                 data=GDP,
                 marker="o")
    plt.tick_params(axis='y', which='both', labelleft='on', labelright='on')
    plt.xlabel("Year")
    plt.ylabel("GDP (Millions)")
    plt.title("GDP of Countries")
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    sns.despine(left=True, bottom=True)
    plt.tight_layout()

    plt.show()


# -----------------------------------------------------------------------------


# Sixth visulaisation using lineplot to check expenses
def ExpensesPlot(DATA2):
    '''
    Function to comapre Expenses of different countries
    '''
    # slice the ‘country’ and ‘country code’ column
    countrycode = DATA2.iloc[:, 0:2]
    # print(countrycode)

    # remove columns which are not useful for further analysis
    DATA2 = DATA2.drop(columns=['Indicator Name', 'Country Code',
                                'Indicator Code', '2019'])
    Exp_unpivoted = DATA2.melt(id_vars=['Country Name'], var_name='Year',
                               value_name='expenses')

    # rename one column and convert the exp into the unit of millions
    Exp_unpivoted.rename(columns={'Country Name': 'Country'}, inplace=True)
    Exp_unpivoted['expensesMillion'] = Exp_unpivoted['expenses'].div(1000000)

    # add the countrycode back to the dataframe
    Exp_unpivoted = Exp_unpivoted.merge(countrycode, left_on='Country',
                                        right_on='Country Name')

    # subset the data for 8 countries after year 1980
    options = ['United States', 'India', 'Thailand', 'Japan']
    Exp = Exp_unpivoted[Exp_unpivoted.Country.isin(options)][['Year',
                                                              'Country',
                                                              'Country Code',
                                                              'expensesMillion'
                                                              ]]
    Exp['Year'] = pd.to_datetime(Exp['Year'])
    Exp = Exp.loc[Exp['Year'] > '1980']

    sns.set_style("whitegrid")
    sns.lineplot(x='Year', y='expensesMillion', hue='Country Code',
                 data=Exp,
                 marker="o")
    plt.tick_params(axis='y', which='both', labelleft='on', labelright='on')
    plt.xlabel("Year")
    plt.ylabel("Expenses (Millions)")
    plt.title("Expenditures of Countries (% of GDP)")
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.show()


DATA2 = pd.read_csv('C:\\Users\\RajaI\\Desktop\\climate change\\GDP.csv')
GDPPLOT(DATA2)
DATA3 = pd.read_csv('C:\\Users\\RajaI\\Desktop\\climate change\\Expenses.csv')
ExpensesPlot(DATA3)
