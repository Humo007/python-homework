def addunderscores(text : str):
    vowels = 'aoueiAOUEI'
    cnt = 2
    while cnt < len(text):
        if text[cnt] not in vowels:
            text = text[:cnt + 1] + '_' + text[cnt + 1:]
            vowels += text[cnt]
            cnt += 4
            continue
        else:
            cnt += 1
    if text.endswith("_"):
        text = text[:-1]
    return text




text = input("Enter the text: ")
print(addunderscores(text))
   
