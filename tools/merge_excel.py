'''
========================
test.py
========================
Created on Oct.9, 2019
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module used for merge excel data to support financial report.
@Reference: 
'''

import pandas as pd
import numpy as np

def xlsread(filepath, sheetName='Sheet1', is_dropNaN=False):
	'''
	Function: Read data from excel
	@arguments: 
	(in)  filepath:   		input file path
	(in)  dataRange:   		data range
	(in)  is_dropNaN:   	remove rows containing NaN
	(out) ls_dataset:   	return line list object
	'''

	# if( dataRange==[] ):
	data_df = pd.read_excel(filepath, sheet_name=sheetName)

	# if(is_dropNaN):
	# 	data_df = data_df.dropna()
	data_matrix=data_df.as_matrix()
	print(data_matrix.shape)
	# print(data_matrix[0])

	# print(df[df.columns[0:2]])
	# print(dataset[0:10])
	return data_matrix





if __name__ == "__main__":
	file1="Expenses-Payroll-Vacation.xls"
	file2="HOP 2 & TVL November 2019  Reconciliation Final.xlsx"
	merged_file="Merge-Payroll-Vacation-Expenses.xlsx"

	data_matrix1 = xlsread(file1, 'Compensation')

	data_matrix2 = xlsread(file2, 'Nov Compensation Hop 2 & TVL')

	for row_data in data_matrix1:
		if(isinstance(row_data[1], str)):
			tmp_name_list = row_data[1].split()
			if(len(tmp_name_list)==2):
				tmp_name1=tmp_name_list[0] + ' ' + tmp_name_list[1]
				tmp_name2=tmp_name_list[1] + ' ' + tmp_name_list[0]
			else:
				tmp_name1=''
				tmp_name1=''
			k = np.where( (data_matrix2[:, 0] == row_data[1]) | (data_matrix2[:, 0] == tmp_name1) | (data_matrix2[:, 0] == tmp_name2 ) )
		else:
			k = np.where( data_matrix2[:, 0] == row_data[1] )
		if(len(k[0])!=0):
			# print(k[0])
			data_matrix2[k[0],7]=row_data[8] 
	pd_frame=pd.DataFrame(data_matrix2)
	pd_frame.to_excel(merged_file, sheet_name='Sheet1')
	# print(data_matrix2[:,7])
