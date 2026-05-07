import json

def data2message(in_file, out_dir):
    i = 0
    index = 0
    messages = []
    messages.append({
        "role": "system",
        "content": "我是你的问答助手"
    })
    with open(in_file, 'r', encoding='utf-8') as file:
        for doc in file:
            if "NaN" in doc:
                doc = doc.replace("NaN", "\"？\"")
            conversations = json.loads(doc)
            for conv in conversations['conversations']:
                messages.append({
                    "role":conv['from'],
                    "content": conv['value']
                })
            if (i+1) % 2000 ==0:
                data = {
                    "messages": messages
                }
                # msg = json.dumps(data)
                # print(msg)
                out_file = out_dir + "/multi_train_" + str(index) + ".json"
                with open(out_file, 'w', encoding='utf-8') as f:
                    f.write(json.dumps(data, ensure_ascii=False))
                index = index + 1
                messages = []
                messages.append({
                    "role": "system",
                    "content": "我是你的问答助手"
                })
            i = i + 1
    if len(messages) > 0:
        messages.insert(0, {
            "role": "system",
            "content": "我是你的问答助手"
        })
        out_file = out_dir + "/multi_train_" + str(index) + ".json"
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
data2message('multi_train.jsonl', 'data')