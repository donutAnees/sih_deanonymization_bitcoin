import requests
import json

def get_all_transaction(user_hash):

    user_info_response = requests.get("https://api.blockcypher.com/v1/btc/main/addrs/" + user_hash )

    user_info_json = user_info_response.json()
    user_txs = user_info_json.get("txrefs",[])

    txs = []

    for tx in user_txs:
        tx_detail = requests.get("https://api.blockcypher.com/v1/btc/main/txs/" + tx["tx_hash"] )
        txs.append(tx_detail.json())

    data = {
        "address": user_info_json["address"],
        "total_received": user_info_json["total_received"],
        "total_sent": user_info_json["total_sent"],
        "balance": user_info_json["balance"],
        "unconfirmed_balance": user_info_json["unconfirmed_balance"],
        "final_balance": user_info_json["final_balance"],
        "n_tx": user_info_json["n_tx"],
        "unconfirmed_n_tx": user_info_json["unconfirmed_n_tx"],
        "final_n_tx": user_info_json["final_n_tx"],
        "txs" : txs,
    }

    with open("./wallets/" + user_hash + ".json" , "w") as file:
        json.dump(data,file)
    file.close()

if __name__ == "__main__":
    with open("./unknown.txt") as file:
        for wallet_id in file:
            get_all_transaction(wallet_id.strip())
    file.close()