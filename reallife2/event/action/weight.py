


@status(task="同步体重",date=date,run_only=True)
def sync_weight()->str:
    # source ~/.bash_profile ;cd /Users/zhaoxuefeng/GitHub/aiworker; .venv/bin/python script/reallife/get_weight.py

    def get_weight(date):
        url = f"http://101.201.244.227:8000/weight/{date}"
        response = requests.get(url)
        return response.json().get('weight')
    result = get_weight(date)
    x = f"""---
番茄: 14
体重: {result}
---
"""
    with open(f'/Users/zhaoxuefeng/GitHub/obsidian/工作/日记/{date}.md','a') as f:
        f.write(x)
    return 'success'

