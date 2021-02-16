
def split_filepath(filepath):
    fplist = []
    for char in filepath:
        fplist.append(char)
    listend = len(fplist)
    print(listend)
    detect = 1
    reversedfilename = ""
    while detect != 0:
        letter = fplist[listend-1]
        if letter != "\\":
            reversedfilename += letter
            listend -= 1
        else:
            detect -= 1
    return reversedfilename[::-1]




print(split_filepath(r"C:\Users\user\PycharmProjects\pythonProject\ExcelAutomation\BulkFile.xlsx"))
