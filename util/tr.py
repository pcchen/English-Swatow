for c in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','Q','R','S','T','U','V','W','Y','Z']:
    docx檔案 = '../docx.txt/{}.docx.txt'.format(c)
    txt檔案 = '../txt/{}.txt'.format(c)
    print(docx檔案, '=>', txt檔案)

    with open(docx檔案, 'r') as 檔案:
        with open(txt檔案, 'w') as f:
            for 逝 in 檔案:
                逝 = 逝.replace("ñ2","2ñ")
                逝 = 逝.replace("ñ3","3ñ")
                逝 = 逝.replace("ñ4","4ñ")
                逝 = 逝.replace("ñ5","5ñ")
                逝 = 逝.replace("ñ6","6ñ")
                逝 = 逝.replace("ñ8","8ñ")
                逝 = 逝.replace("ñ","ⁿ")
                逝 = 逝.replace("ü","ṳ")
                逝 = 逝.replace("2","\u0302")
                逝 = 逝.replace("3","\u0301")
                逝 = 逝.replace("4","\u0300")
                逝 = 逝.replace("5","\u0303")
                逝 = 逝.replace("6","\u0304")
                逝 = 逝.replace("8","\u030D")
                # print(逝,end="")
                f.write(逝)
