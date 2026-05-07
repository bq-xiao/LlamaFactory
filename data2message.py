import json

def data2message(in_file, out_file):
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
    data = {
        "messages": messages
    }
    #msg = json.dumps(data)
    #print(msg)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))

data2message('multi_test.jsonl', 'qwen_train_test.json')