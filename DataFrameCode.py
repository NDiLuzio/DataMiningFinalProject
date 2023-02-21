# Coded By Matthew Myles & Nicholas DiLuzio

import pandas as pd
import numpy as np
import ClusteringCode as CC

# Set display to show all rows and columns
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('Alzheimer_s_Disease_and_Healthy_Aging_Data.csv', header=None, index_col=False)
# Dataframe was changed and redownloaded, needed to replace cells with '.' as content for proper sorting logic


def cluster(list1, list2, graphTitle, axisLabel, clusters):
    X = np.column_stack((list1, list2))
    k = CC.KMeans(K=clusters, max_iters=200, plot_steps=True)
    k.predict(X, graphTitle, axisLabel)
    return k


# Set up columns
df.columns = ['RowId', 'YearStart', 'YearEnd', 'LocationAbbr', 'LocationDesc', 'Datasource', 'Class', 'Topic', 'Question',
              'Response', 'Data_Value_Unit', 'DataValueTypeID', 'Data_Value_Type', 'Data_Value', 'Data_Value_Alt', 'Data_Value_Footnote_Symbol',
              'Data_Value_Footnote', 'Low_Confidence_Limit', 'High_Confidence_Limit', 'Sample_Size', 'StratificationCategory1', 'Stratification1',
              'StratificationCategory2', 'Stratification2', 'StratificationCategory3', 'Stratification3', 'Geolocation', 'ClassID', 'TopicID', 'QuestionID',
              'ResponseID', 'LocationID', 'StratificationCategoryID1', 'StratificationID1', 'StratificationCategoryID2', 'StratificationID2',
              'StratificationCategoryID3', 'StratificationID3', 'Report']

# Make new dataframe without first row of column headers
data = df.iloc[1:]

# Drop unneeded columns
data = data.drop(['RowId', 'Datasource', 'Response', 'LocationAbbr', 'Data_Value_Alt', 'DataValueTypeID', 'Data_Value_Footnote_Symbol', 'Data_Value_Footnote',
                  'Sample_Size', 'StratificationCategory1', 'StratificationCategory2', 'StratificationCategory3', 'Stratification3', 'Geolocation',
                  'ClassID', 'TopicID', 'QuestionID', 'ResponseID', 'LocationID', 'StratificationCategoryID1', 'StratificationID1',
                  'StratificationCategoryID2', 'StratificationID2', 'StratificationCategoryID3', 'StratificationID3', 'Report'], axis=1)

# Create new dfs based on people overall
df_actlim_overall = data.loc[(data['Stratification1'] == "Overall") & (data['Topic'] == "Recent activity limitations in past month")]
df_actlim_overall_gendM = data.loc[(data['Stratification1'] == "Overall") & (data['Stratification2'] == "Male") & (data['Topic'] == "Recent activity limitations in past month")]
df_actlim_overall_gendF = data.loc[(data['Stratification1'] == "Overall") & (data['Stratification2'] == "Female") & (data['Topic'] == "Recent activity limitations in past month")]

df_cogdec_overall = data.loc[(data['Stratification1'] == "Overall") & (data['Class'] == "Cognitive Decline")]
df_cogdec_overall_gendM = data.loc[(data['Stratification1'] == "Overall") & (data['Stratification2'] == "Male") & (data['Class'] == "Cognitive Decline")]
df_cogdec_overall_gendF = data.loc[(data['Stratification1'] == "Overall") & (data['Stratification2'] == "Female") & (data['Class'] == "Cognitive Decline")]

df_mentdist_overall = data.loc[(data['Stratification1'] == "Overall") & (data['Topic'] == "Frequent mental distress")]
df_mentdist_overall_gendM = data.loc[(data['Stratification1'] == "Overall") & (data['Stratification2'] == "Male") & (data['Topic'] == "Frequent mental distress")]
df_mentdist_overall_gendF = data.loc[(data['Stratification1'] == "Overall") & (data['Stratification2'] == "Female") & (data['Topic'] == "Frequent mental distress")]

df_sufsleep_overall = data.loc[(data['Stratification1'] == "Overall") & (data['Topic'] == "Prevalence of sufficient sleep")]
df_sufsleep_overall_gendM = data.loc[(data['Stratification1'] == "Overall") & (data['Stratification2'] == "Male") & (data['Topic'] == "Prevalence of sufficient sleep")]
df_sufsleep_overall_gendF = data.loc[(data['Stratification1'] == "Overall") & (data['Stratification2'] == "Female") & (data['Topic'] == "Prevalence of sufficient sleep")]

# Create new dfs based on age 50-64
df_actlim_5064 = data.loc[(data['Stratification1'] == "50-64 years") & (data['Topic'] == "Recent activity limitations in past month")]
df_actlim_5064_gendM = data.loc[(data['Stratification1'] == "50-64 years") & (data['Stratification2'] == "Male") & (data['Topic'] == "Recent activity limitations in past month")]
df_actlim_5064_gendF = data.loc[(data['Stratification1'] == "50-64 years") & (data['Stratification2'] == "Female") & (data['Topic'] == "Recent activity limitations in past month")]

df_cogdec_5064 = data.loc[(data['Stratification1'] == "50-64 years") & (data['Class'] == "Cognitive Decline")]
df_cogdec_5064_gendM = data.loc[(data['Stratification1'] == "50-64 years") & (data['Stratification2'] == "Male") & (data['Class'] == "Cognitive Decline")]
df_cogdec_5064_gendF = data.loc[(data['Stratification1'] == "50-64 years") & (data['Stratification2'] == "Female") & (data['Class'] == "Cognitive Decline")]

df_mentdist_5064 = data.loc[(data['Stratification1'] == "50-64 years") & (data['Topic'] == "Frequent mental distress")]
df_mentdist_5064_gendM = data.loc[(data['Stratification1'] == "50-64 years") & (data['Stratification2'] == "Male") & (data['Topic'] == "Frequent mental distress")]
df_mentdist_5064_gendF = data.loc[(data['Stratification1'] == "50-64 years") & (data['Stratification2'] == "Female") & (data['Topic'] == "Frequent mental distress")]

df_sufsleep_5064 = data.loc[(data['Stratification1'] == "50-64 years") & (data['Topic'] == "Prevalence of sufficient sleep")]
df_sufsleep_5064_gendM = data.loc[(data['Stratification1'] == "50-64 years") & (data['Stratification2'] == "Male") & (data['Topic'] == "Prevalence of sufficient sleep")]
df_sufsleep_5064_gendF = data.loc[(data['Stratification1'] == "50-64 years") & (data['Stratification2'] == "Female") & (data['Topic'] == "Prevalence of sufficient sleep")]

# Create new dfs based on age 65+
df_actlim_65plus = data.loc[(data['Stratification1'] == "65 years or older") & (data['Topic'] == "Recent activity limitations in past month")]
df_actlim_65plus_gendM = data.loc[(data['Stratification1'] == "65 years or older") & (data['Stratification2'] == "Male") & (data['Topic'] == "Recent activity limitations in past month")]
df_actlim_65plus_gendF = data.loc[(data['Stratification1'] == "65 years or older") & (data['Stratification2'] == "Female") & (data['Topic'] == "Recent activity limitations in past month")]

df_cogdec_65plus = data.loc[(data['Stratification1'] == "50-64 years") & (data['Class'] == "Cognitive Decline")]
df_cogdec_65plus_gendM = data.loc[(data['Stratification1'] == "65 years or older") & (data['Stratification2'] == "Male") & (data['Class'] == "Cognitive Decline")]
df_cogdec_65plus_gendF = data.loc[(data['Stratification1'] == "65 years or older") & (data['Stratification2'] == "Female") & (data['Class'] == "Cognitive Decline")]

df_mentdist_65plus = data.loc[(data['Stratification1'] == "65 years or older") & (data['Topic'] == "Frequent mental distress")]
df_mentdist_65plus_gendM = data.loc[(data['Stratification1'] == "65 years or older") & (data['Stratification2'] == "Male") & (data['Topic'] == "Frequent mental distress")]
df_mentdist_65plus_gendF = data.loc[(data['Stratification1'] == "65 years or older") & (data['Stratification2'] == "Female") & (data['Topic'] == "Frequent mental distress")]

df_sufsleep_65plus = data.loc[(data['Stratification1'] == "65 years or older") & (data['Topic'] == "Prevalence of sufficient sleep")]
df_sufsleep_65plus_gendM = data.loc[(data['Stratification1'] == "65 years or older") & (data['Stratification2'] == "Male") & (data['Topic'] == "Prevalence of sufficient sleep")]
df_sufsleep_65plus_gendF = data.loc[(data['Stratification1'] == "65 years or older") & (data['Stratification2'] == "Female") & (data['Topic'] == "Prevalence of sufficient sleep")]

# Datatype for dataframe is string, not numeric, so conversion needed using pd method

# Replacements for overall category
df_actlim_overall_high = pd.to_numeric(df_actlim_overall['High_Confidence_Limit'])
df_actlim_overall_low = pd.to_numeric(df_actlim_overall['Low_Confidence_Limit'])

df_actlim_overall_gendM_low = pd.to_numeric(df_actlim_overall_gendM['Low_Confidence_Limit'])
df_actlim_overall_gendM_high = pd.to_numeric(df_actlim_overall_gendM['High_Confidence_Limit'])

df_actlim_overall_gendF_low = pd.to_numeric(df_actlim_overall_gendF['Low_Confidence_Limit'])
df_actlim_overall_gendF_high = pd.to_numeric(df_actlim_overall_gendF['High_Confidence_Limit'])

df_cogdec_overall_low = pd.to_numeric(df_cogdec_overall['Low_Confidence_Limit'])
df_cogdec_overall_high = pd.to_numeric(df_cogdec_overall['High_Confidence_Limit'])

df_cogdec_overall_gendM_low = pd.to_numeric(df_cogdec_overall_gendM['Low_Confidence_Limit'])
df_cogdec_overall_gendM_high = pd.to_numeric(df_cogdec_overall_gendM['High_Confidence_Limit'])

df_cogdec_overall_gendF_low = pd.to_numeric(df_cogdec_overall_gendF['Low_Confidence_Limit'])
df_cogdec_overall_gendF_high = pd.to_numeric(df_cogdec_overall_gendF['High_Confidence_Limit'])

df_mentdist_overall_low = pd.to_numeric(df_mentdist_overall['Low_Confidence_Limit'])
df_mentdist_overall_high = pd.to_numeric(df_mentdist_overall['High_Confidence_Limit'])

df_mentdist_overall_low_gendM = pd.to_numeric(df_mentdist_overall_gendM['Low_Confidence_Limit'])
df_mentdist_overall_high_gendM = pd.to_numeric(df_mentdist_overall_gendM['High_Confidence_Limit'])

df_mentdist_overall_low_gendF = pd.to_numeric(df_mentdist_overall_gendF['Low_Confidence_Limit'])
df_mentdist_overall_high_gendF = pd.to_numeric(df_mentdist_overall_gendF['High_Confidence_Limit'])

df_sufsleep_overall_low = pd.to_numeric(df_sufsleep_overall['Low_Confidence_Limit'])
df_sufsleep_overall_high = pd.to_numeric(df_sufsleep_overall['High_Confidence_Limit'])

df_sufsleep_overall_low_gendM = pd.to_numeric(df_sufsleep_overall_gendM['Low_Confidence_Limit'])
df_sufsleep_overall_high_gendM = pd.to_numeric(df_sufsleep_overall_gendM['High_Confidence_Limit'])

df_sufsleep_overall_low_gendF = pd.to_numeric(df_sufsleep_overall_gendF['Low_Confidence_Limit'])
df_sufsleep_overall_high_gendF = pd.to_numeric(df_sufsleep_overall_gendF['High_Confidence_Limit'])

# Replacements for ages 50-64
df_actlim_5064_high = pd.to_numeric(df_actlim_5064['High_Confidence_Limit'])
df_actlim_5064_low = pd.to_numeric(df_actlim_5064['Low_Confidence_Limit'])

df_actlim_5064_gendM_low = pd.to_numeric(df_actlim_5064_gendM['Low_Confidence_Limit'])
df_actlim_5064_gendM_high = pd.to_numeric(df_actlim_5064_gendM['High_Confidence_Limit'])

df_actlim_5064_gendF_low = pd.to_numeric(df_actlim_5064_gendF['Low_Confidence_Limit'])
df_actlim_5064_gendF_high = pd.to_numeric(df_actlim_5064_gendF['High_Confidence_Limit'])

df_cogdec_5064_low = pd.to_numeric(df_cogdec_5064['Low_Confidence_Limit'])
df_cogdec_5064_high = pd.to_numeric(df_cogdec_5064['High_Confidence_Limit'])

df_cogdec_5064_gendM_low = pd.to_numeric(df_cogdec_5064_gendM['Low_Confidence_Limit'])
df_cogdec_5064_gendM_high = pd.to_numeric(df_cogdec_5064_gendM['High_Confidence_Limit'])

df_cogdec_5064_gendF_low = pd.to_numeric(df_cogdec_5064_gendF['Low_Confidence_Limit'])
df_cogdec_5064_gendF_high = pd.to_numeric(df_cogdec_5064_gendF['High_Confidence_Limit'])

df_mentdist_5064_low = pd.to_numeric(df_mentdist_5064['Low_Confidence_Limit'])
df_mentdist_5064_high = pd.to_numeric(df_mentdist_5064['High_Confidence_Limit'])

df_mentdist_5064_low_gendM = pd.to_numeric(df_mentdist_5064_gendM['Low_Confidence_Limit'])
df_mentdist_5064_high_gendM = pd.to_numeric(df_mentdist_5064_gendM['High_Confidence_Limit'])

df_mentdist_5064_low_gendF = pd.to_numeric(df_mentdist_5064_gendF['Low_Confidence_Limit'])
df_mentdist_5064_high_gendF = pd.to_numeric(df_mentdist_5064_gendF['High_Confidence_Limit'])

df_sufsleep_5064_low = pd.to_numeric(df_sufsleep_5064['Low_Confidence_Limit'])
df_sufsleep_5064_high = pd.to_numeric(df_sufsleep_5064['High_Confidence_Limit'])

df_sufsleep_5064_low_gendM = pd.to_numeric(df_sufsleep_5064_gendM['Low_Confidence_Limit'])
df_sufsleep_5064_high_gendM = pd.to_numeric(df_sufsleep_5064_gendM['High_Confidence_Limit'])

df_sufsleep_5064_low_gendF = pd.to_numeric(df_sufsleep_5064_gendF['Low_Confidence_Limit'])
df_sufsleep_5064_high_gendF = pd.to_numeric(df_sufsleep_5064_gendF['High_Confidence_Limit'])

# Replacements for 65+
df_actlim_65plus_high = pd.to_numeric(df_actlim_65plus['High_Confidence_Limit'])
df_actlim_65plus_low = pd.to_numeric(df_actlim_65plus['Low_Confidence_Limit'])

df_actlim_65plus_gendM_low = pd.to_numeric(df_actlim_65plus_gendM['Low_Confidence_Limit'])
df_actlim_65plus_gendM_high = pd.to_numeric(df_actlim_65plus_gendM['High_Confidence_Limit'])

df_actlim_65plus_gendF_low = pd.to_numeric(df_actlim_65plus_gendF['Low_Confidence_Limit'])
df_actlim_65plus_gendF_high = pd.to_numeric(df_actlim_65plus_gendF['High_Confidence_Limit'])

df_cogdec_65plus_low = pd.to_numeric(df_cogdec_65plus['Low_Confidence_Limit'])
df_cogdec_65plus_high = pd.to_numeric(df_cogdec_65plus['High_Confidence_Limit'])

df_cogdec_65plus_gendM_low = pd.to_numeric(df_cogdec_65plus_gendM['Low_Confidence_Limit'])
df_cogdec_65plus_gendM_high = pd.to_numeric(df_cogdec_65plus_gendM['High_Confidence_Limit'])

df_cogdec_65plus_gendF_low = pd.to_numeric(df_cogdec_65plus_gendF['Low_Confidence_Limit'])
df_cogdec_65plus_gendF_high = pd.to_numeric(df_cogdec_65plus_gendF['High_Confidence_Limit'])

df_mentdist_65plus_low = pd.to_numeric(df_mentdist_65plus['Low_Confidence_Limit'])
df_mentdist_65plus_high = pd.to_numeric(df_mentdist_65plus['High_Confidence_Limit'])

df_mentdist_65plus_low_gendM = pd.to_numeric(df_mentdist_65plus_gendM['Low_Confidence_Limit'])
df_mentdist_65plus_high_gendM = pd.to_numeric(df_mentdist_65plus_gendM['High_Confidence_Limit'])

df_mentdist_65plus_low_gendF = pd.to_numeric(df_mentdist_65plus_gendF['Low_Confidence_Limit'])
df_mentdist_65plus_high_gendF = pd.to_numeric(df_mentdist_65plus_gendF['High_Confidence_Limit'])

df_sufsleep_65plus_low = pd.to_numeric(df_sufsleep_65plus['Low_Confidence_Limit'])
df_sufsleep_65plus_high = pd.to_numeric(df_sufsleep_65plus['High_Confidence_Limit'])

df_sufsleep_65plus_low_gendM = pd.to_numeric(df_sufsleep_65plus_gendM['Low_Confidence_Limit'])
df_sufsleep_65plus_high_gendM = pd.to_numeric(df_sufsleep_65plus_gendM['High_Confidence_Limit'])

df_sufsleep_65plus_low_gendF = pd.to_numeric(df_sufsleep_65plus_gendF['Low_Confidence_Limit'])
df_sufsleep_65plus_high_gendF = pd.to_numeric(df_sufsleep_65plus_gendF['High_Confidence_Limit'])

# Pre-Processing: Handle NaNs by dropping
df_actlim_overall_low, df_actlim_overall_high = df_actlim_overall_low.dropna(), df_actlim_overall_high.dropna()
df_actlim_overall_gendM_low, df_actlim_overall_gendM_high = df_actlim_overall_gendM_low.dropna(), df_actlim_overall_gendM_high.dropna()
df_actlim_overall_gendF_low, df_actlim_overall_gendF_high = df_actlim_overall_gendF_low.dropna(), df_actlim_overall_gendF_high.dropna()

df_actlim_5064_low, df_actlim_5064_high = df_actlim_5064_low.dropna(), df_actlim_5064_high.dropna()
df_actlim_5064_gendM_low, df_actlim_5064_gendM_high = df_actlim_5064_gendM_low.dropna(), df_actlim_5064_gendM_high.dropna()
df_actlim_5064_gendF_low, df_actlim_5064_gendF_high = df_actlim_5064_gendF_low.dropna(), df_actlim_5064_gendF_high.dropna()

df_actlim_65plus_low, df_actlim_65plus_high = df_actlim_65plus_low.dropna(), df_actlim_65plus_high.dropna()
df_actlim_65plus_gendM_low, df_actlim_65plus_gendM_high = df_actlim_65plus_gendM_low.dropna(), df_actlim_65plus_gendM_high.dropna()
df_actlim_65plus_gendF_low, df_actlim_65plus_gendF_high = df_actlim_65plus_gendF_low.dropna(), df_actlim_65plus_gendF_high.dropna()

df_cogdec_overall_low, df_cogdec_overall_high = df_cogdec_overall_low.dropna(), df_cogdec_overall_high.dropna()
df_cogdec_overall_gendM_low, df_cogdec_overall_gendM_high = df_cogdec_overall_gendM_low.dropna(), df_cogdec_overall_gendM_high.dropna()
df_cogdec_overall_gendF_low, df_cogdec_overall_gendF_high = df_cogdec_overall_gendF_low.dropna(), df_cogdec_overall_gendF_high.dropna()

df_cogdec_5064_low, df_cogdec_5064_high = df_cogdec_5064_low.dropna(), df_cogdec_5064_high.dropna()
df_cogdec_5064_gendM_low, df_cogdec_5064_gendM_high = df_cogdec_5064_gendM_low.dropna(), df_cogdec_5064_gendM_high.dropna()
df_cogdec_5064_gendF_low, df_cogdec_5064_gendF_high = df_cogdec_5064_gendF_low.dropna(), df_cogdec_5064_gendF_high.dropna()

df_cogdec_65plus_low, df_cogdec_65plus_high = df_cogdec_65plus_low.dropna(), df_cogdec_65plus_high.dropna()
df_cogdec_65plus_gendM_low, df_cogdec_65plus_gendM_high = df_cogdec_65plus_gendM_low.dropna(), df_cogdec_65plus_gendM_high.dropna()
df_cogdec_65plus_gendF_low, df_cogdec_65plus_gendF_high = df_cogdec_65plus_gendF_low.dropna(), df_cogdec_65plus_gendF_high.dropna()

df_mentdist_overall_low, df_mentdist_overall_high = df_mentdist_overall_low.dropna(), df_mentdist_overall_high.dropna()
df_mentdist_overall_low_gendM, df_mentdist_overall_high_gendM = df_mentdist_overall_low_gendM.dropna(), df_mentdist_overall_high_gendM.dropna()
df_mentdist_overall_low_gendF, df_mentdist_overall_high_gendF = df_mentdist_overall_low_gendF.dropna(), df_mentdist_overall_high_gendF.dropna()

df_mentdist_5064_low, df_mentdist_5064_high = df_mentdist_5064_low.dropna(), df_mentdist_5064_high.dropna()
df_mentdist_5064_low_gendM, df_mentdist_5064_high_gendM = df_mentdist_5064_low_gendM.dropna(), df_mentdist_5064_high_gendM.dropna()
df_mentdist_5064_low_gendF, df_mentdist_5064_high_gendF = df_mentdist_5064_low_gendF.dropna(), df_mentdist_5064_high_gendF.dropna()

df_mentdist_65plus_low, df_mentdist_65plus_high = df_mentdist_65plus_low.dropna(), df_mentdist_65plus_high.dropna()
df_mentdist_65plus_low_gendM, df_mentdist_65plus_high_gendM = df_mentdist_65plus_low_gendM.dropna(), df_mentdist_65plus_high_gendM.dropna()
df_mentdist_65plus_low_gendF, df_mentdist_65plus_high_gendF = df_mentdist_65plus_low_gendF.dropna(), df_mentdist_65plus_high_gendF.dropna()

df_sufsleep_overall_low, df_sufsleep_overall_high = df_sufsleep_overall_low.dropna(), df_sufsleep_overall_high.dropna()
df_sufsleep_overall_low_gendM, df_sufsleep_overall_high_gendM = df_sufsleep_overall_low_gendM.dropna(), df_sufsleep_overall_high_gendM.dropna()
df_sufsleep_overall_low_gendF, df_sufsleep_overall_high_gendF = df_sufsleep_overall_low_gendF.dropna(), df_sufsleep_overall_high_gendF.dropna()

df_sufsleep_5064_low, df_sufsleep_5064_high = df_sufsleep_5064_low.dropna(), df_sufsleep_5064_high.dropna()
df_sufsleep_5064_low_gendM, df_sufsleep_5064_high_gendM = df_sufsleep_5064_low_gendM.dropna(), df_sufsleep_5064_high_gendM.dropna()
df_sufsleep_5064_low_gendF, df_sufsleep_5064_high_gendF = df_sufsleep_5064_low_gendF.dropna(), df_sufsleep_5064_high_gendF.dropna()

df_sufsleep_65plus_low, df_sufsleep_65plus_high = df_sufsleep_65plus_low.dropna(), df_sufsleep_65plus_high.dropna()
df_sufsleep_65plus_low_gendM, df_sufsleep_65plus_high_gendM = df_sufsleep_65plus_low_gendM.dropna(), df_sufsleep_65plus_high_gendM.dropna()
df_sufsleep_65plus_low_gendF, df_sufsleep_65plus_high_gendF = df_sufsleep_65plus_low_gendF.dropna(), df_sufsleep_65plus_high_gendF.dropna()


# Run algorithm to  show plot

def clusterActOver():
    return cluster(df_actlim_overall_low.values.tolist(), df_actlim_overall_high.values.tolist(), "Activity Limitations In Past Month Overall", "Mean Number Of Days", 6)


def clusterActOver_M():
    return cluster(df_actlim_overall_gendM_low.values.tolist(), df_actlim_overall_gendM_high.values.tolist(), "Activity Limitations In Past Month Males Overall", "Mean Number Of Days", 6)


def clusterActOver_F():
    return cluster(df_actlim_overall_gendF_low.values.tolist(), df_actlim_overall_gendF_high.values.tolist(), "Activity Limitations In Past Month Females Overall", "Mean Number Of Days", 6)


def clusterAct5064():
    return cluster(df_actlim_5064_low.values.tolist(), df_actlim_5064_high.values.tolist(), "Activity Limitations In Past Month For All 50-64 Years", "Mean Number Of Days", 6)


def clusterAct5064_M():
    return cluster(df_actlim_5064_gendM_low.values.tolist(), df_actlim_5064_gendM_high.values.tolist(), "Activity Limitations In Past Month For All Males 50-64 Years", "Mean Number Of Days", 6)


def clusterAct5064_F():
    return cluster(df_actlim_5064_gendF_low.values.tolist(), df_actlim_5064_gendF_high.values.tolist(), "Activity Limitations In Past Month For All Females 50-64 Years", "Mean Number Of Days", 6)


def clusterAct65():
    return cluster(df_actlim_65plus_low.values.tolist(), df_actlim_65plus_high.values.tolist(), "Activity Limitations In Past Month For All 65+ Years", "Mean Number Of Days", 6)


def clusterAct65_M():
    return cluster(df_actlim_65plus_gendM_low.values.tolist(), df_actlim_65plus_gendM_high.values.tolist(), "Activity Limitations In Past Month For All Males 65+ Years", "Mean Number Of Days", 6)


def clusterAct65_F():
    return cluster(df_actlim_65plus_gendF_low.values.tolist(), df_actlim_65plus_gendF_high.values.tolist(), "Activity Limitations In Past Month For All Females 65+ Years", "Mean Number Of Days", 6)


def clusterCogOver():
    return cluster(df_cogdec_overall_low.values.tolist(), df_cogdec_overall_high.values.tolist(), "Adults Reporting Cognitive Issues", "Percentage of Adults", 6)


def clusterCogOver_M():
    return cluster(df_cogdec_overall_gendM_low.values.tolist(), df_cogdec_overall_gendM_high.values.tolist(), "Male Adults Reporting Cognitive Issues", "Percentage of Adults", 6)


def clusterCogOver_F():
    return cluster(df_cogdec_overall_gendF_low.values.tolist(), df_cogdec_overall_gendF_high.values.tolist(), "Female Adults Reporting Cognitive Issues", "Percentage of Adults", 6)


def clusterCog5064():
    return cluster(df_cogdec_5064_low.values.tolist(), df_cogdec_5064_high.values.tolist(), "Adults 50-64 Years Old Reporting Cognitive Issues", "Percentage of Adults", 6)


def clusterCog5064_M():
    return cluster(df_cogdec_5064_gendM_low.values.tolist(), df_cogdec_5064_gendM_high.values.tolist(), "Male Adults 50-64 Years Old Reporting Cognitive Issues", "Percentage of Adults", 6)


def clusterCog5064_F():
    cluster(df_cogdec_5064_gendF_low.values.tolist(), df_cogdec_5064_gendF_high.values.tolist(), "Female Adults 50-64 Years Old Reporting Cognitive Issues", "Percentage of Adults", 6)


def clusterCog65():
    return cluster(df_cogdec_65plus_low.values.tolist(), df_cogdec_65plus_high.values.tolist(), "Adults 65+ Years Old Reporting Cognitive Issues", "Percentage of Adults", 6)


def clusterCog65_M():
    return cluster(df_cogdec_65plus_gendM_low.values.tolist(), df_cogdec_65plus_gendM_high.values.tolist(), "Male Adults 65+ Years Old Reporting Cognitive Issues", "Percentage of Adults", 6)


def clusterCog65_F():
    return cluster(df_cogdec_65plus_gendF_low.values.tolist(), df_cogdec_65plus_gendF_high.values.tolist(), "Female Adults 65+ Years Old Reporting Cognitive Issues", "Percentage of Adults", 6)


def clusterMentOver():
    return cluster(df_mentdist_overall_low.values.tolist(), df_mentdist_overall_high.values.tolist(), "Adults Reporting Frequent Mental Distress", "Percentage of Adults", 6)


def clusterMentOver_M():
    return cluster(df_mentdist_overall_low_gendM.values.tolist(), df_mentdist_overall_high_gendM.values.tolist(), "Adult Males Reporting Frequent Mental Distress", "Percentage of Males", 6)


def clusterMentOver_F():
    return cluster(df_mentdist_overall_low_gendF.values.tolist(), df_mentdist_overall_high_gendF.values.tolist(), "Adults Females Reporting Frequent Mental Distress", "Percentage of Females", 6)


def clusterMent5064():
    return cluster(df_mentdist_5064_low.values.tolist(), df_mentdist_5064_high.values.tolist(), "Adults ages 50-64 Reporting Frequent Mental Distress", "Percentage of Adults", 6)


def clusterMent5064_M():
    return cluster(df_mentdist_5064_low_gendM.values.tolist(), df_mentdist_5064_high_gendM.values.tolist(), "Adult Males ages 50-64 Reporting Frequent Mental Distress", "Percentage of Males", 6)


def clusterMent5064_F():
    return cluster(df_mentdist_5064_low_gendF.values.tolist(), df_mentdist_5064_high_gendF.values.tolist(), "Adults Females ages 50-64 Reporting Frequent Mental Distress", "Percentage of Females", 6)


def clusterMent65():
    return cluster(df_mentdist_65plus_low.values.tolist(), df_mentdist_65plus_high.values.tolist(), "Adults ages 65+ Reporting Frequent Mental Distress", "Percentage of Adults", 6)


def clusterMent65_M():
    return cluster(df_mentdist_65plus_low_gendM.values.tolist(), df_mentdist_65plus_high_gendM.values.tolist(), "Adult Males ages 65+ Reporting Frequent Mental Distress", "Percentage of Males", 6)


def clusterMent65_F():
    return cluster(df_mentdist_65plus_low_gendF.values.tolist(), df_mentdist_65plus_high_gendF.values.tolist(), "Adults Females ages 65+ Reporting Frequent Mental Distress", "Percentage of Females", 6)


def clusterSleepOver():
    return cluster(df_sufsleep_overall_low.values.tolist(), df_sufsleep_overall_high.values.tolist(), "Adults Reporting sufficient sleep (>6 hours)", "Percentage of Adults", 6)


def clusterSleepOver_M():
    return cluster(df_sufsleep_overall_low_gendM.values.tolist(), df_sufsleep_overall_high_gendM.values.tolist(), "Adult Males Reporting sufficient sleep (>6 hours)", "Percentage of Males", 6)


def clusterSleepOver_F():
    return cluster(df_sufsleep_overall_low_gendF.values.tolist(), df_sufsleep_overall_high_gendF.values.tolist(), "Adult Females Reporting sufficient sleep (>6 hours)", "Percentage of Females", 6)


def clusterSleep5064():
    return cluster(df_sufsleep_5064_low.values.tolist(), df_sufsleep_5064_high.values.tolist(), "Adults ages 50-64 Reporting sufficient sleep (>6 hours)", "Percentage of Adults", 6)


def clusterSleep5064_M():
    return cluster(df_sufsleep_5064_low_gendM.values.tolist(), df_sufsleep_5064_high_gendM.values.tolist(), "Adult Males ages 50-64 Reporting sufficient sleep (>6 hours)", "Percentage of Males", 6)


def clusterSleep5064_F():
    cluster(df_sufsleep_5064_low_gendF.values.tolist(), df_sufsleep_5064_high_gendF.values.tolist(), "Adults Females ages 50-64 Reporting sufficient sleep (>6 hours)", "Percentage of Females", 6)


def clusterSleep65():
    return cluster(df_sufsleep_65plus_low.values.tolist(), df_sufsleep_65plus_high.values.tolist(), "Adults ages 65+ Reporting sufficient sleep (>6 hours)", "Percentage of Adults", 6)


def clusterSleep65_M():
    return cluster(df_sufsleep_65plus_low_gendM.values.tolist(), df_sufsleep_65plus_high_gendM.values.tolist(), "Adult Males ages 65+ Reporting sufficient sleep (>6 hours)", "Percentage of Males", 6)


def clusterSleep65_F():
    return cluster(df_sufsleep_65plus_low_gendF.values.tolist(), df_sufsleep_65plus_high_gendF.values.tolist(), "Adults Females ages 65+ Reporting sufficient sleep (>6 hours)", "Percentage of Females", 6)
