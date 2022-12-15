def LoadItemList():
    iconData = []
    gr2List = []
    grContent = ".gr2"

    with open("item_list.txt", "r+") as f:
        item_list = f.readlines()
        for line in item_list:
            #13	WEAPON	icon/item/00010.tga	d:/ymir work/item/weapon/00010.gr2
            lines = line.split("\t")
            if line.strip():
                for i in lines:
                    if i.startswith("icon"):
                        iconData.append(i)
                    if i.startswith("d:/ymir"):
                        gr2List.append(i)

            
    return gr2List, iconData


gr2List, iconData = LoadItemList()

with open("icons.txt", "w+") as f:
    for i in set(iconData):
        f.write(i + "\n")

with open("gr2.txt", "w+") as f:
    for i in set(gr2List):
        f.write(i + "\n")