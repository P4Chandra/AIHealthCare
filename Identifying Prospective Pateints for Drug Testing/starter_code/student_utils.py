import pandas as pd
import numpy as np
import os
import tensorflow as tf
import functools
####### STUDENTS FILL THIS OUT ######
#Question 3
def reduce_dimension_ndc(df, ndc_code_df):
    '''
    df: pandas dataframe, input dataset
    ndc_df: pandas dataframe, drug code dataset used for mapping in generic names
    return:
        df: pandas dataframe, output dataframe with joined generic drug name
    '''
    new_ndc=ndc_code_df[['NDC_Code','Non-proprietary Name']]
    reduce_dim_df=pd.merge(df,new_ndc, how="left", left_on='ndc_code',right_on='NDC_Code')
    reduce_dim_df.rename(columns={"Non-proprietary Name": "generic_drug_name"},inplace=True)
    reduce_dim_df.drop(columns=['NDC_Code'],inplace=True)
    return reduce_dim_df

#Question 4
def select_first_encounter(df):
    '''
    df: pandas dataframe, dataframe with all encounters
    return:
        first_encounter_df: pandas dataframe, dataframe with only the first encounter for a given patient
    '''
    first_encounter_df = df.copy()
    first_encounter_df = first_encounter_df.sort_values('encounter_id')
    first_encounter_df = (first_encounter_df.drop_duplicates(subset=['encounter_id'], keep='first').drop_duplicates(subset=['patient_nbr'], keep='first'))
    return first_encounter_df


#Question 6
def patient_dataset_splitter(df, key='patient_nbr'):
    '''
    df: pandas dataframe, input dataset that will be split
    patient_key: string, column that is the patient id

    return:
     - train: pandas dataframe,
     - validation: pandas dataframe,
     - test: pandas dataframe,
    '''
    train_percentage=0.6
    test_percentage=0.2
    
    df = df.iloc[np.random.permutation(len(df))]
    unique_values = df[key].unique()
    total_values = len(unique_values)
    sample_size = round(total_values * (train_percentage ))
    test_sample_size=round(total_values *(1-train_percentage)*test_percentage)
    
    train = df[df[key].isin(unique_values[:sample_size])].reset_index(drop=True)
    test = df[df[key].isin(unique_values[sample_size:sample_size+test_sample_size])].reset_index(drop=True)
    validation=df[df[key].isin(unique_values[sample_size+test_sample_size:])].reset_index(drop=True)
    print("Total number of unique patients in train = " +str(len(train[key].unique())))
    print("Total number of unique patients in test = " +str(len(test[key].unique())))
    print("Total number of unique patients in validation = "+str(len(validation[key].unique())))
    print("Training partition has a shape = " +str(train.shape) )
    print("Test partition has a shape = "+str(test.shape) )
    print("Validation partition has a shape = "+str(validation.shape) )
    return train, validation, test

#Question 7

def create_tf_categorical_feature_cols(categorical_col_list,
                              vocab_dir='./diabetes_vocab/'):
    '''
    categorical_col_list: list, categorical field list that will be transformed with TF feature column
    vocab_dir: string, the path where the vocabulary text files are located
    return:
        output_tf_list: list of TF feature columns
    '''
    output_tf_list = []
    for c in categorical_col_list:
        vocab_file_path = os.path.join(vocab_dir,  c + "_vocab.txt")
        '''
        Which TF function allows you to read from a text file and create a categorical feature
        You can use a pattern like this below...
        tf_categorical_feature_column = tf.feature_column.......

        '''
        tf_categorical_feature_column = tf.feature_column.categorical_column_with_vocabulary_file(
                    key=c,vocabulary_file = vocab_file_path, num_oov_buckets=1)
        
        tf_categorical_feature_column = tf.feature_column.indicator_column(tf_categorical_feature_column)

        output_tf_list.append(tf_categorical_feature_column)
    return output_tf_list

#Question 8
def normalize_numeric_with_zscore(col, mean, std):
    '''
    This function can be used in conjunction with the tf feature column for normalization
    '''
    return (col - mean)/std



def create_tf_numeric_feature(col, MEAN, STD, default_value=0):
    '''
    col: string, input numerical column name
    MEAN: the mean for the column in the training data
    STD: the standard deviation for the column in the training data
    default_value: the value that will be used for imputing the field

    return:
        tf_numeric_feature: tf feature column representation of the input field
    '''
        
    normalizer = functools.partial(normalize_numeric_with_zscore, mean=MEAN, std=STD)
    tf_numeric_feature = tf.feature_column.numeric_column(key=col, default_value = default_value, normalizer_fn=normalizer, dtype=tf.float64)
    return tf_numeric_feature

#Question 9
def get_mean_std_from_preds(diabetes_yhat):
    '''
    diabetes_yhat: TF Probability prediction object
    '''
    m = diabetes_yhat.mean()
    s = diabetes_yhat.stddev() 
    return m, s

# Question 10
def get_student_binary_prediction(df, col):
    '''
    df: pandas dataframe prediction output dataframe
    col: str,  probability mean prediction field
    return:
        student_binary_prediction: pandas dataframe converting input to flattened numpy array and binary labels
    '''
    binary_prediction=df.copy()
    binary_prediction["FinalResult"] = binary_prediction[col].apply(lambda x: 1 if x >=5 else 0)
     
    return binary_prediction["FinalResult"]
