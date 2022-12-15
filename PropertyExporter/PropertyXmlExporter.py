from bs4 import BeautifulSoup as bs
constData = "C:/rb-project-2022/rubinum-game/client/CRYPTION/source/"
def MakeUnique(uq):
    temp = ""
    temp = uq[len(constData):]
    return temp


with open('property.xml', 'r') as f:
    data = f.read()


bsData = bs(data, "xml")


b_unique = bsData.find_all("Property")



with open('prblist.txt', 'w+') as f:
    for i in b_unique:
        test = MakeUnique(i['filename'])
        f.write(test + "\n")

with open('gr2list.txt', 'w+') as f:
    for i in b_unique:
        try:
            f.write(i['buildingfile'] + "\n")
        except:
            pass

