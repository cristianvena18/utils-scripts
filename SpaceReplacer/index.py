import pyexcel_io as pyexcel
from pyexcel_xlsx import save_data
from collections import OrderedDict

CBU_COL = 1
INDEX_COL = 0


wb_data = pyexcel.get_data('file.xlsx')
first_sheet_name = list(wb_data.keys())[0]
data = wb_data[first_sheet_name]

num_rows = len(data)

result = []

for row in range(0, num_rows):
    row_data = data[row]
    cbu = row_data[CBU_COL]
    index = row_data[INDEX_COL]

    cbu = str(cbu).replace(' ', '')
    result.append([index, cbu])

orderedDict = OrderedDict()
orderedDict.update({"Sheet 1": result})

save_data('result.xlsx', orderedDict)

