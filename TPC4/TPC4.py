import re
import json

def converter_csv_json(src: str, dest:str):
        
    er1 = r'^(?P<num>\d+),(?P<nome>[^,]+),(?P<curso>[^,]+),(?P<notas>(?:\d+,)*\d+),*$'
    er2 = r'^(?P<num>\d+),(?P<nome>[^,]+),(?P<curso>[^,]+)$'
    param_list = []
    header = []
    with open(src,"r",encoding='utf8') as f:
        for line in f.readlines():
            header = re.findall(r"(\w+(?:\{\d+(?:,\d+)?\}(?:::\w+)?)?)",line,re.UNICODE)
            match = re.match(er1, line)
            if match:
                param_list.append(match.groupdict())
            elif match:= re.match(er2, line):
                param_list.append(match.groupdict())
    
    for dict in param_list:
        if "notas" in dict:
            lst = dict["notas"].split(',')
            dict["notas"] = []
            dict["notas"] = lst

    if re.search("media",header[3]):
        for dict in param_list:
            res = [int(i) for i in lst] 
            dict["notas"] = sum(res)/len(res)

    elif re.search("sum",header[3]):
        for dict in param_list:
            res = [int(i) for i in lst] 
            dict["notas"] = sum(res)

    
    with open(dest,"w",encoding='utf8') as file:
        json.dump(param_list, file,indent = 4,separators=(',', ':'),ensure_ascii=False)


converter_csv_json("alunos1.csv","alunos1.json")
converter_csv_json("alunos2.csv","alunos2.json")
converter_csv_json("alunos3.csv","alunos3.json")
converter_csv_json("alunos4.csv","alunos4.json")
converter_csv_json("alunos5.csv","alunos5.json")