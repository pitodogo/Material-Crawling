import wikipedia
page = wikipedia.page("List_of_materials_properties")
content = page.content

last_numbers = []
import re
pattern = re.compile("\n\n\n==.*==\n")
for r in re.finditer(pattern,content):
    last_numbers.append(r.end())

properties = []
for i in range(len(last_numbers)-1):
    lists = content[last_numbers[i]:last_numbers[i+1]].split('\n')
    for l in lists:
        if(len(l)==0 or l[0]=="="):
            continue
        try:
            pos = l.index(":")
            properties.append(l[:pos])
        except:
            try:
                pos = l.index("(")
                properties.append(l[:pos])
            except:
                properties.append(l)
Properties = {}
for i in properties:
    Properties[i] = []
