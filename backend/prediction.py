import joblib
import pandas as pd
import get_wallet_features

model = joblib.load("../aiml/model/wallets_dataset/RFModel_Wallets.pkl")
# with open("../aiml/model/wallets_dataset/RF.pkl", encoding = "cp437") as f:
#     model = pickle.load(f)

def results(walletid):
    X = ['first_sent_block','fees_max','first_block_appeared_in','fees_median','fees_mean','last_block_appeared_in','blocks_btwn_txs_max','blocks_btwn_output_txs_max','blocks_btwn_output_txs_mean']
    feature_values = get_wallet_features.get_wallet_feat(walletid)
    input_features = pd.DataFrame([feature_values],columns = X)
    y = model.predict(input_features)[0]
    if y == 0:
        prediction = "legal"
    else:
        prediction = "illegal"
    return prediction

print(results("111112TykSw72ztDN2WJger4cynzWYC5w"))