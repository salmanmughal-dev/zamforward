with open('code.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = 142003
script_open = text.rfind('<script', 0, pos_start)
print("Script tag before 142003 starts at:", script_open)
print(text[script_open:script_open+500])
