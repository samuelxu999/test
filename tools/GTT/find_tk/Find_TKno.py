'''
========================
test.py
========================
Created on Oct.9, 2019
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module used for functions test.
@Reference: 
'''

import pandas as pd
import numpy as np
import xlrd

def getSheetName(filepath):
	xls = xlrd.open_workbook(filepath, on_demand=True)
	return xls.sheet_names()

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
	data_matrix=data_df.values
	print(data_matrix.shape)
	# print(data_matrix[0])

	# print(df[df.columns[0:2]])
	# print(dataset[0:10])
	return data_matrix


if __name__ == "__main__":
	source_file="TEMFQQ+statement+11142019-01232020.xls"
	target_file="TEMFQQ+05202020.xls"
	result_file="Checked-TEMFQQ.xlsx"

	# get all sheet names in source_file
	sheetnames = getSheetName(source_file)[:-1]
	print( "Sheet names: {}".format(len(sheetnames)) )

	# load data in target_file
	target_matrix = xlsread(target_file, 'coicas')
	target_titno_column = target_matrix[:,5:6]
	print( len(target_titno_column) )

	# build a new column to save results
	results_col = np.zeros((target_titno_column.shape[0],target_titno_column.shape[1]))
	print("results_col shape: {}".format(results_col.shape))

	# for each sheet to check tktno in target_file
	for sheetname in sheetnames:
		print("check sheet: {}".format(sheetname))
		data_matrix = xlsread(source_file, sheetname)
		# get TKTNO column
		tktno_pos = np.where(data_matrix == 'TKTNO')
		# print(tktno_pos)

		# get tktno column data
		titno_column = data_matrix[ tktno_pos[0][0]+1:,tktno_pos[1][0]:tktno_pos[1][0]+1]
		# check tktno in target_file
		for titkno_data in titno_column:
			if(titkno_data[0]==0):
				continue
			# search tktno position
			check_tktno_pos = np.where(target_titno_column == titkno_data[0])
			if(len(check_tktno_pos[0])==0):
				continue
			# print("{} : {}".format(titkno_data[0], check_tktno_pos[0]) ) 

			# Set 1 to results_col
			for pos_index in check_tktno_pos[0]:
				results_col[pos_index][0]=1
		# break
	# append results_col and output new data
	results_matrix = np.append(target_matrix, results_col, 1)
	pd_frame=pd.DataFrame(results_matrix)
	pd_frame.to_excel(result_file, sheet_name='tktno_total')
