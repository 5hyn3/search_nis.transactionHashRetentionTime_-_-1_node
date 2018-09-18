import requests
import json

get_transaction_by_hash_path = "/transaction/get?hash=e793f3d0c5f01b528a027a6f1a13006685ac88be9d9c67aab29c293f9efa6081"

status_ok_nodes = []
with open("node_list.json", mode='r', encoding="utf-8_sig") as f:
    nodes = json.load(f)

    for node in nodes:
        address = "http://" + node["NEM Node"] + ":" + node["Port"]
        path = address + get_transaction_by_hash_path
        print(node["#"])
        try:
            if(requests.get(path).status_code == 200):
                status_ok_nodes.append(address)
        except:
            pass

with open("result.txt", mode='w') as f:
    for node in status_ok_nodes:
        f.write(str(address) + "\n")