import xlrd

def count(comval, val):
    #comval = 'Pop'
    cnt = 0
    #for i in range(l):
    if(val == comval):
        cnt= cnt +1
    return cnt


def main():
    loc = 'List.xlsx'
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0)
    comval = input("Enter the genre to Search: ")
    cnt = 0
    for i in range(sheet.nrows):
            for j in range(sheet.ncols):
                cnt += count(comval, sheet.cell_value(i, j))
                #print(sheet.cell_value(i,0), type(sheet.cell_value(i,0)))

    #cnt = count(comval, sheet.nrows,sheet.nrows)
    print(comval,': ', cnt)


if __name__=='__main__':
    main()
