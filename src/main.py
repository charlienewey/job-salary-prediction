import pandas as pd

from job_description_feature_extraction import get_one_hot_encoded_words, get_rake_keywords
from contract_cleaning import get_one_hot_encoded_contract

train_raw_data_csv_file_name = '../data/Train_rev1.csv'
test_raw_data_csv_file_name = '../data/Test_rev1.csv'

if __name__ == "__main__":
    train_raw_data = pd.read_csv(train_raw_data_csv_file_name)
    test_raw_data = pd.read_csv(test_raw_data_csv_file_name)
    # Train fields
    train_description_feature = train_raw_data[['FullDescription']]
    train_con_type_feature = train_raw_data[['ContractType']]
    train_con_time_feature = train_raw_data[['ContractTime']]
    # Test fields
    test_description_feature = test_raw_data[['FullDescription']]
    test_con_type_feature = test_raw_data[['ContractType']]
    test_con_time_feature = test_raw_data[['ContractTime']]

    # Train one hot encoded features - desciption, contract-type, contract-time
    # All lists containt list of lists of features in one hot encoded format ready to append to
    # cleaned set
    # Description: consisting of 5 features existence of words below in the description:
    # 'excellent', 'graduate', 'immediate', 'junior', 'urgent'
    train_one_hot_encoded_desc_words = get_one_hot_encoded_words(train_description_feature)
    # Contract type: One hot encoded, 3 features: part time, full time, *is empty*
    train_one_hot_encoded_contract_type = get_one_hot_encoded_contract(train_con_type_feature)
    # Contract time: One hot encoded, 3 features: permanent, contract, *is empty*
    train_one_hot_encoded_contract_time = get_one_hot_encoded_contract(train_con_time_feature)

    # Test one hot encoded features - desciption, contract-type, contract-time
    test_one_hot_encoded_desc_words = get_one_hot_encoded_words(test_description_feature)
    test_one_hot_encoded_contract_type = get_one_hot_encoded_contract(test_con_type_feature)
    test_one_hot_encoded_contract_time = get_one_hot_encoded_contract(test_con_time_feature)

    keywords = get_rake_keywords(train_description_feature)
    # one_hot_encoded_features are a list of 5 lists consisting of 1s and 0s
    # If a word appears in the description, this kind of representation will
    # make it feasible for machine learning
    # We will need to append those lists on final data frame when everything is cleaned
