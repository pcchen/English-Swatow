heads = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','Q','R','S','T','U','V','W','Y','Z']

for h in heads:
    with open('{}.txt'.format(h), 'r') as 輸入檔案:
        with open('{}.md'.format(h), 'w') as 輸出檔案:
            for 逝 in 輸入檔案:
                print("* " + 逝,end="")
                輸出檔案.write("* " + 逝)
