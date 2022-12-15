def Load():
    data = []
    startData = "000000"
    for i in range(6):
        startData = startData[:1] + str(i) + startData[2:]
        for j in range(6):
            newData = startData[:-1] + str(j)
            data.append(newData)
    
    return data

def LoadAtlasInfo():
    atlas = []
    with open("atlasinfo.txt", "r") as f:
        data = f.readlines()
        for i in data:
            atlas.append(i.split("\t")[0])

    return atlas


subNumericFolders = Load() # for 000001 folders
mapNames = LoadAtlasInfo() # for mapnames

folderBegin = "" # main maps folder

constNumericData = ["areaambiencedata.txt", "areadata.txt", "areaproperty.txt", "attr.attr",
    "height.raw", "minimap.dds", "shadowmap.dds", "shadowmap.raw", "title.raw", "water.wtr"]

constRawData = ["mapproperty.txt", "monsterareainfo.txt", "monsterarrange.txt", "regen.txt", "setting.txt"]

with open("list.txt", "w+") as f:

    for i in mapNames:
        for j in subNumericFolders:
            for k in constNumericData:
                f.write(folderBegin + i + "/" + j + "/" + k + "\n")
    for i in mapNames:
        for j in constRawData:
            f.write(folderBegin + i + "/" + j + "\n")
