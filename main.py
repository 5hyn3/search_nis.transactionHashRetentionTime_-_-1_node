import requests
import json

get_transaction_by_hash_path = "/transaction/get?hash=9bacb53783c5fb943797e0b1c096fd5780469734fa58832f9df558ee06427e82"

status_ok_nodes = []
with open("node_list.json", mode='r', encoding="utf-8_sig") as f:
    nodes = json.load(f)

    for node in nodes:
        address = node["NEM Node"]
        path = "http://" + address + ":7890" + get_transaction_by_hash_path
        print(node["#"])
        try:
            if(requests.get(path).status_code == 200):
                status_ok_nodes.append(address)
        except:
            pass

with open("result.txt", mode='w') as f:
    for node in status_ok_nodes:
        f.write(str(node) + "\n")