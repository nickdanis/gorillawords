import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_lg")

"""
Script that will generate the lemmatization of all of the hints
This takes a really long time to run, don't run unless you really want to

Created 2 csv files

1) hint words that are present in each year from 1994-2020

to load properly do this:
pd.read_csv("hints_common.csv", index_col=[0])

2) all hint words 
pd.read_csv("hints_all.csv", index_col=[0])


"""

# Nick's csv file
xword = pd.read_csv("nick-xword-big.csv", converters={'Answer' : str, 'Hint' : str}, encoding='latin-1')

# --------------------------------------

def get_hint_dict(df):
    """Returns a dictionary of unique hint words and their occurences in dataframe"""
    hint_dict = {}
    for hint in df['Hint'].values:
        doc = nlp(hint)
        for token in doc:
            if token.lemma_ in hint_dict.keys():
                hint_dict[token.lemma_] += 1
            else:
                hint_dict[token.lemma_] = 1
    return hint_dict




# -----------------------------------------------------------
# Make the lemmatization on each year

"""Who needs for loops??"""

print("1994")
hints_1994 = get_hint_dict(xword.loc[xword['Year'] == 1994])

print("1995")
hints_1995 = get_hint_dict(xword.loc[xword['Year'] == 1995])

print("1996")
hints_1996 = get_hint_dict(xword.loc[xword['Year'] == 1996])

print("1997")
hints_1997 = get_hint_dict(xword.loc[xword['Year'] == 1997])

print("1998")
hints_1998 = get_hint_dict(xword.loc[xword['Year'] == 1998])

print("1999")
hints_1999 = get_hint_dict(xword.loc[xword['Year'] == 1999])

print("2000")
hints_2000 = get_hint_dict(xword.loc[xword['Year'] == 2000])

print("2001")
hints_2001 = get_hint_dict(xword.loc[xword['Year'] == 2001])

print("2002")
hints_2002 = get_hint_dict(xword.loc[xword['Year'] == 2002])

print("2003")
hints_2003 = get_hint_dict(xword.loc[xword['Year'] == 2003])

print("2004")
hints_2004 = get_hint_dict(xword.loc[xword['Year'] == 2004])

print("2005")
hints_2005 = get_hint_dict(xword.loc[xword['Year'] == 2005])

print("2006")
hints_2006 = get_hint_dict(xword.loc[xword['Year'] == 2006])

print("2007")
hints_2007 = get_hint_dict(xword.loc[xword['Year'] == 2007])

print("2008")
hints_2008 = get_hint_dict(xword.loc[xword['Year'] == 2008])

print("2009")
hints_2009 = get_hint_dict(xword.loc[xword['Year'] == 2009])

print("2010")
hints_2010 = get_hint_dict(xword.loc[xword['Year'] == 2010])

print("2011")
hints_2011 = get_hint_dict(xword.loc[xword['Year'] == 2011])

print("2012")
hints_2012 = get_hint_dict(xword.loc[xword['Year'] == 2012])

print("2013")
hints_2013 = get_hint_dict(xword.loc[xword['Year'] == 2013])

print("2014")
hints_2014 = get_hint_dict(xword.loc[xword['Year'] == 2014])

print("2015")
hints_2015 = get_hint_dict(xword.loc[xword['Year'] == 2015])

print("2016")
hints_2016 = get_hint_dict(xword.loc[xword['Year'] == 2016])

print("2017")
hints_2017 = get_hint_dict(xword.loc[xword['Year'] == 2017])

print("2018")
hints_2018 = get_hint_dict(xword.loc[xword['Year'] == 2018])

print("2019")
hints_2019 = get_hint_dict(xword.loc[xword['Year'] == 2019])

print("2020")
hints_2020 = get_hint_dict(xword.loc[xword['Year'] == 2020])







# ------------------------------------------------------------

hints_1994_df = pd.DataFrame.from_dict(hints_1994, orient='index', columns=[1994])

hints_1995_df = pd.DataFrame.from_dict(hints_1995, orient='index', columns=[1995])
hints_1996_df = pd.DataFrame.from_dict(hints_1996, orient='index', columns=[1996])
hints_1997_df = pd.DataFrame.from_dict(hints_1997, orient='index', columns=[1997])
hints_1998_df = pd.DataFrame.from_dict(hints_1998, orient='index', columns=[1998])
hints_1999_df = pd.DataFrame.from_dict(hints_1999, orient='index', columns=[1999])

hints_2000_df = pd.DataFrame.from_dict(hints_2000, orient='index', columns=[2000])
hints_2001_df = pd.DataFrame.from_dict(hints_2001, orient='index', columns=[2001])
hints_2002_df = pd.DataFrame.from_dict(hints_2002, orient='index', columns=[2002])
hints_2003_df = pd.DataFrame.from_dict(hints_2003, orient='index', columns=[2003])
hints_2004_df = pd.DataFrame.from_dict(hints_2004, orient='index', columns=[2004])

hints_2005_df = pd.DataFrame.from_dict(hints_2005, orient='index', columns=[2005])
hints_2006_df = pd.DataFrame.from_dict(hints_2006, orient='index', columns=[2006])
hints_2007_df = pd.DataFrame.from_dict(hints_2007, orient='index', columns=[2007])
hints_2008_df = pd.DataFrame.from_dict(hints_2008, orient='index', columns=[2008])
hints_2009_df = pd.DataFrame.from_dict(hints_2009, orient='index', columns=[2009])

hints_2010_df = pd.DataFrame.from_dict(hints_2010, orient='index', columns=[2010])
hints_2011_df = pd.DataFrame.from_dict(hints_2011, orient='index', columns=[2011])
hints_2012_df = pd.DataFrame.from_dict(hints_2012, orient='index', columns=[2012])
hints_2013_df = pd.DataFrame.from_dict(hints_2013, orient='index', columns=[2013])
hints_2014_df = pd.DataFrame.from_dict(hints_2014, orient='index', columns=[2014])

hints_2015_df = pd.DataFrame.from_dict(hints_2015, orient='index', columns=[2015])
hints_2016_df = pd.DataFrame.from_dict(hints_2016, orient='index', columns=[2016])
hints_2017_df = pd.DataFrame.from_dict(hints_2017, orient='index', columns=[2017])
hints_2018_df = pd.DataFrame.from_dict(hints_2018, orient='index', columns=[2018])
hints_2019_df = pd.DataFrame.from_dict(hints_2019, orient='index', columns=[2019])

hints_2020_df = pd.DataFrame.from_dict(hints_2020, orient='index', columns=[2020])






# --------------------------------------------------------------------

hints_1994_df.to_csv("hints_1994.csv")

hints_1995_df.to_csv("hints_1995.csv")
hints_1996_df.to_csv("hints_1996.csv")
hints_1997_df.to_csv("hints_1997.csv")
hints_1998_df.to_csv("hints_1998.csv")
hints_1999_df.to_csv("hints_1999.csv")

hints_2000_df.to_csv("hints_2000.csv")
hints_2001_df.to_csv("hints_2001.csv")
hints_2002_df.to_csv("hints_2002.csv")
hints_2003_df.to_csv("hints_2003.csv")
hints_2004_df.to_csv("hints_2004.csv")

hints_2005_df.to_csv("hints_2005.csv")
hints_2006_df.to_csv("hints_2006.csv")
hints_2007_df.to_csv("hints_2007.csv")
hints_2008_df.to_csv("hints_2008.csv")
hints_2009_df.to_csv("hints_2009.csv")

hints_2010_df.to_csv("hints_2010.csv")
hints_2011_df.to_csv("hints_2011.csv")
hints_2012_df.to_csv("hints_2012.csv")
hints_2013_df.to_csv("hints_2013.csv")
hints_2014_df.to_csv("hints_2014.csv")

hints_2015_df.to_csv("hints_2015.csv")
hints_2016_df.to_csv("hints_2016.csv")
hints_2017_df.to_csv("hints_2017.csv")
hints_2018_df.to_csv("hints_2018.csv")
hints_2019_df.to_csv("hints_2019.csv")

hints_2020_df.to_csv("hints_2020.csv")





# --------------------------------------------------------------
# Concatenate all data frames with index=words columns=year

hints_all_df = pd.concat([hints_1994_df, hints_1995_df, hints_1996_df, hints_1997_df, hints_1998_df, hints_1999_df,
                          hints_2000_df, hints_2001_df, hints_2002_df, hints_2003_df, hints_2004_df,
                          hints_2005_df, hints_2006_df, hints_2007_df, hints_2008_df, hints_2009_df,
                          hints_2010_df, hints_2011_df, hints_2012_df, hints_2013_df, hints_2014_df,
                          hints_2015_df, hints_2016_df, hints_2017_df, hints_2018_df, hints_2019_df, 
                          hints_2020_df], axis=1)


hints_all_df.to_csv("hints_all.csv")







# ------------------------------------------------------------
# Keep only the words that are present in every year

set_1994 = set(hints_1994_df.index)

set_1995 = set(hints_1995_df.index)
set_1996 = set(hints_1996_df.index)
set_1997 = set(hints_1997_df.index)
set_1998 = set(hints_1998_df.index)
set_1999 = set(hints_1999_df.index)

set_2000 = set(hints_2000_df.index)
set_2001 = set(hints_2001_df.index)
set_2002 = set(hints_2002_df.index)
set_2003 = set(hints_2003_df.index)
set_2004 = set(hints_2004_df.index)

set_2005 = set(hints_2005_df.index)
set_2006 = set(hints_2006_df.index)
set_2007 = set(hints_2007_df.index)
set_2008 = set(hints_2008_df.index)
set_2009 = set(hints_2009_df.index)

set_2010 = set(hints_2010_df.index)
set_2011 = set(hints_2011_df.index)
set_2012 = set(hints_2012_df.index)
set_2013 = set(hints_2013_df.index)
set_2014 = set(hints_2014_df.index)

set_2015 = set(hints_2015_df.index)
set_2016 = set(hints_2016_df.index)
set_2017 = set(hints_2017_df.index)
set_2018 = set(hints_2018_df.index)
set_2019 = set(hints_2019_df.index)

set_2020 = set(hints_2020_df.index)

common_words = set_1994.intersection(set_1995, set_1996, set_1997, set_1998, set_1999,
                                     set_2000, set_2001, set_2002, set_2003, set_2004,
                                     set_2005, set_2006, set_2007, set_2008, set_2009,
                                     set_2010, set_2011, set_2012, set_2013, set_2014,
                                     set_2015, set_2016, set_2017, set_2018, set_2019, set_2020)

all_words = set_1994.union(set_1995, set_1996, set_1997, set_1998, set_1999,
                                     set_2000, set_2001, set_2002, set_2003, set_2004,
                                     set_2005, set_2006, set_2007, set_2008, set_2009,
                                     set_2010, set_2011, set_2012, set_2013, set_2014,
                                     set_2015, set_2016, set_2017, set_2018, set_2019, set_2020)

hints_common_df = hints_all_df.loc[common_words]
hints_common_df

hints_common_df.to_csv("hints_common.csv")