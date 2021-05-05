import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import pyodbc
import pandas as pd
from flask_wtf import Form
from wtforms.fields.html5 import DateField
from datetime import datetime as dt
from config import *
import json
pd.options.mode.chained_assignment = None
def connectionSQLExpress():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=ADITYAANGR;'
                          'Database=iccprod;'
                          'UID=sa;'
                          'PWD=kudaponi69;'
                          'Trusted_Connection=no;')
    return conn


def funcstringQuerry(dateFirst, dateLast, keyWhereGir, keyCaseGir):
    stringQuerry = (f'''
SELECT (CONVERT(CHAR(4), ENDED, 100) + CONVERT(CHAR(4), ended, 120)) AS PERIODE, ENDED, KEY_GIR,KEY_GIR_CODE, 1 AS COUNT_KEY_GIR, FILE_SIZE, TRANSFER_STATUS, PATH_TO, PATH_FROM

from(
  SELECT CASE
                        when PATH_TO LIKE '%K01GIRH%' then 'K01GIRH'
						when PATH_TO LIKE '%K01GIRM%' then 'K01GIRM'
						when PATH_TO LIKE '%K01GIRX%' then 'K01GIRX'
						
						when PATH_TO LIKE '%K02GIRH%' then 'K02GIRH'
						when PATH_TO LIKE '%K02GIRM%' then 'K02GIRM'
						when PATH_TO LIKE '%K02GIRX%' then 'K02GIRX'

						when PATH_TO LIKE '%K03GIRH%' then 'K03GIRH'
						when PATH_TO LIKE '%K03GIRM%' then 'K03GIRM'
						when PATH_TO LIKE '%K03GIRX%' then 'K03GIRX'

						when PATH_TO LIKE '%K04GIRH%' then 'K04GIRH'
						when PATH_TO LIKE '%K04GIRM%' then 'K04GIRM'
						when PATH_TO LIKE '%K04GIRX%' then 'K04GIRX'
						
						when PATH_TO LIKE '%K05GIRH%' then 'K05GIRH'
						when PATH_TO LIKE '%K05GIRM%' then 'K05GIRM'
						when PATH_TO LIKE '%K05GIRX%' then 'K05GIRX'

						when PATH_TO LIKE '%K06GIRH%' then 'K06GIRH'
						when PATH_TO LIKE '%K06GIRM%' then 'K06GIRM'
						when PATH_TO LIKE '%K06GIRX%' then 'K06GIRX'

						when PATH_TO LIKE '%K07GIRH%' then 'K07GIRH'
						when PATH_TO LIKE '%K07GIRM%' then 'K07GIRM'
						when PATH_TO LIKE '%K07GIRX%' then 'K07GIRX'
						
						when PATH_TO LIKE '%K08GIRH%' then 'K08GIRH'
						when PATH_TO LIKE '%K08GIRM%' then 'K08GIRM'
						when PATH_TO LIKE '%K08GIRX%' then 'K08GIRX'

						when PATH_TO LIKE '%K09GIRH%' then 'K09GIRH'
						when PATH_TO LIKE '%K09GIRM%' then 'K09GIRM'
						when PATH_TO LIKE '%K09GIRX%' then 'K09GIRX'

						when PATH_TO LIKE '%K10GIRH%' then 'K10GIRH'
						when PATH_TO LIKE '%K10GIRM%' then 'K10GIRM'
						when PATH_TO LIKE '%K10GIRX%' then 'K10GIRX'

						when PATH_TO LIKE '%K11GIRH%' then 'K11GIRH'
						when PATH_TO LIKE '%K11GIRM%' then 'K11GIRM'
						when PATH_TO LIKE '%K11GIRX%' then 'K11GIRX'

						when PATH_TO LIKE '%K12GIRH%' then 'K12GIRH'
						when PATH_TO LIKE '%K12GIRM%' then 'K12GIRM'
						when PATH_TO LIKE '%K12GIRX%' then 'K12GIRX'
                END AS KEY_GIR_CODE, *
  FROM (
    SELECT CASE {keyCaseGir}
		END AS KEY_GIR, *
		FROM 
(
SELECT *
                FROM
                            (SELECT
                                [iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_TRANSFER_ID] AS FILE_TRANSFER_ID
                                ,[iccprod].[dbo].[CC_FILE_TRANSFER].[DURATION] AS 'DURATION(mS)'
                                ,RIGHT('0' + CAST([iccprod].[dbo].[CC_FILE_TRANSFER].[DURATION] / 1000 AS VARCHAR),3) + ':'  AS 'DURATION(S)'
                                ,RIGHT(CAST([iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_SIZE] / 1024 AS int), 20) as FILE_SIZE
                                ,[iccprod].[dbo].[CC_PROCESS].[PROC_NAME] AS PROC_NAME
                                ,[iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_TYPE] AS FILE_TYPE
                                ,DATEADD(hour,7,[iccprod].[dbo].[CC_PROCESS].[ENDED]) AS ENDED
                                ,[iccprod].[dbo].[CC_PROCESS].[PROC_ID] as PROCESS_ID
                                ,[iccprod].[dbo].[CC_FILE_TRANSFER].[RETURN_CODE] AS RC_TRANSFER
                                ,[iccprod].[dbo].[CC_PROCESS].[RETURN_CODE] AS RC_PROCESS
                                ,[iccprod].[dbo].[CC_FILE_TRANSFER].[TRANSFER_STATUS] AS TRANSFER_STATUS
                                ,[iccprod].[dbo].[CC_PROCESS].[PROC_STATUS] AS PROC_STATUS
                                ,[iccprod].[dbo].[CC_PROCESS].[SUBMITTER] as SUBMITTER
                                ,[iccprod].[dbo].[CC_PROCESS].[ORIG_NODE] AS FROM_NODE
                                ,[iccprod].[dbo].[CC_PROCESS].[REMOTE_NODE] AS TO_NODE
                                ,[iccprod].[dbo].[CC_FILE_TRANSFER].[XFER_DIRECTION] AS ARAH
                                ,[iccprod].[dbo].[CC_FILE_TRANSFER].[REMOTE_FILE_NAME] AS PATH_FROM
                                ,[iccprod].[dbo].[CC_FILE_TRANSFER].[LOCAL_FILE_NAME] AS PATH_TO
                                ,[iccprod].[dbo].[CC_PROCESS].[LAST_MESSAGE_ID] AS CODE_MESSAGE
                                ,[iccprod].[dbo].[CC_PROCESS].[LAST_MESSAGE_TEXT] AS MESSAGE
                                FROM  [iccprod].[dbo].[CC_FILE_TRANSFER]
                                right JOIN [iccprod].[dbo].[CC_PROCESS]
                                ON [iccprod].[dbo].[CC_FILE_TRANSFER].[PROCESS_ID]=[iccprod].[dbo].[CC_PROCESS].[PROCESS_ID]
                            ) A
                WHERE ({keyWhereGir}) AND FILE_TYPE='TXT' AND  ENDED BETWEEN '{dateFirst}' AND '{dateLast}') A) A)A
               
                ''')
    return stringQuerry

# def giroRange(timing1,timing2):
#     paramsData = dictParameter(confdictGir)
#     try:
#         cnxn = connectionSQLExpress()
#         cursor = cnxn.cursor()
#         stringQuerry = funcstringQuerry(timing1,timing2,paramsData)
#         cursor.execute(stringQuerry)
#         resultQuerryUpdate = cursor.fetchall()
#         colNames = [i[0] for i in cursor.description]
#         return {'status':'T','messsage':'success','result':{'resultQuerryUpdate':resultQuerryUpdate,'colNames':colNames}}
#     except Exception as e:
#         print(str(e))
#         return {'status':'F','messsage':str(e),'result':[]}
#     finally:
#         cnxn.close()

def giroDefault(timing1,timing2):
    try:
        cnxn = connectionSQLExpress()
        stringQuerry = funcstringQuerry(timing1,timing2,keyWhereGir,keyCaseGir)
        # df kasar
        dfMaster = pd.read_sql(sql=stringQuerry, con=cnxn)
        # datatable
        resultTable = dfMaster.to_json(orient="split")
        resultTable = json.loads(resultTable)
        # start create datacharting
        #chart countkeygir
        pd.to_datetime(dfMaster['PERIODE'], format='%b %Y')
        resultChart = dfMaster.groupby(by=["PERIODE","KEY_GIR"]).sum('COUNT_KEY_GIR').reset_index().sort_values(by=['PERIODE'], ascending=False)
        uniqPeriod = resultChart.PERIODE.unique()
        uniqKeyGir = resultChart.KEY_GIR.unique()
        zeroValue = [0]
        dummyDataframe = pd.MultiIndex.from_product([uniqPeriod, uniqKeyGir,zeroValue], names = ["PERIODE", "KEY_GIR","COUNT_KEY_GIR_DUMMY"])
        dummyDataframe = pd.DataFrame(index = dummyDataframe).reset_index()
        dfnotfinalchart =pd.merge(resultChart, dummyDataframe,how="right", on=["PERIODE", "KEY_GIR"]).fillna(0).drop(columns=['COUNT_KEY_GIR_DUMMY']).astype({'COUNT_KEY_GIR':int})
        dfPiv = dfnotfinalchart.pivot('PERIODE','KEY_GIR', 'COUNT_KEY_GIR').reset_index().fillna(0)
        dfPiv[dtypesFloat(dfPiv)] = dfPiv[dtypesFloat(dfPiv)].astype(int)
        dfPiv = dfPiv.sort_values(by='PERIODE',ascending=False)
        dfPiv.insert(0, "Dummy", [99]*len(dfPiv), True)
        dfPivFinal = dfPiv.groupby('Dummy').agg(lambda x: tuple(x)).set_index('PERIODE')#.drop('Dummy',axis=1)

        #chart file size
        dfLowest = dfMaster[['PERIODE','KEY_GIR_CODE','COUNT_KEY_GIR','FILE_SIZE']]#.set_index('KEY_GIR_CODE')
        listInt = ['COUNT_KEY_GIR','FILE_SIZE']
        dfLowest[listInt] = dfLowest[listInt].astype(int)
        dfLowestGrp = dfLowest.dropna().groupby(['PERIODE','KEY_GIR_CODE']).sum().reset_index()
        dfLowestPiv = dfLowestGrp.pivot('PERIODE','KEY_GIR_CODE', 'FILE_SIZE').reset_index().fillna(0)
        dfLowestPiv[dtypesFloat(dfLowestPiv)] = dfLowestPiv[dtypesFloat(dfLowestPiv)].astype(int)
        dfLowestPiv = dfLowestPiv.set_index('PERIODE')
        dfLowestFinal = dfLowestPiv.sum(axis=0).sort_values(ascending=True).head(5).index
        dfLowestFinal = dfLowestPiv[dfLowestFinal].sort_values(by='PERIODE',ascending=False).reset_index()

        dfLowestFinal.insert(0, "Dummy", [99]*len(dfLowestFinal), True)
        dfLowestFinal = dfLowestFinal.groupby('Dummy').agg(lambda x: tuple(x)).set_index('PERIODE')#.drop('Dummy',axis=1)

        resultChartCount = dfPivFinal.to_json(orient="split")
        resultChartCount = json.loads(resultChartCount)
        resultChartFileSize = dfLowestFinal.to_json(orient="split")
        resultChartFileSize = json.loads(resultChartFileSize)
        return {'status':'T','messsage':'success','resultTable':{'resultRow':resultTable['data'],'resultCol':resultTable["columns"]},
                'resultChartCKG':{'dataChartCKG':resultChartCount}, 'resultChartFileSize':{'dataChartFileSize':resultChartFileSize}}
    except Exception as e:
        # print(str(e))
        return {'status':'F','messsage':str(e),'resultTable':[],'resultChart':[],'resultChartFileSize':[]}
    finally:
        cnxn.close()

# data = giroDefault('2021-01-01','2021-03-30')
# print(data)




def giroRange(timing1,timing2):
    try:
        cnxn = connectionSQLExpress()
        stringQuerry = funcstringQuerry(timing1,timing2,keyWhereGir,keyCaseGir)
        resultDataframe = pd.read_sql(sql=stringQuerry, con=cnxn)
        
        # with pd.option_context('display.max_rows',None, 'display.max_columns', None): 
        #     print(resultDataframe)
        return {'status':'T','messsage':'success','result':{'resultQuerryUpdate':list(resultDataframe.values.tolist()),'colNames':resultDataframe.columns.values}}
    except Exception as e:
        print(str(e))
        return {'status':'F','messsage':str(e),'result':[]}
    finally:
        cnxn.close()

def giroRangeChart(timing1,timing2):
    try:
        cnxn = connectionSQLExpress()
        stringQuerry = funcstringQuerry(timing1,timing2,keyWhereGir,keyCaseGir)
        resultDataframe = pd.read_sql(sql=stringQuerry, con=cnxn)
        resultDataFrameChart = resultDataframe.groupby(by=["PERIODE","KEY_GIR"]).sum('COUNT_KEY_GIR').reset_index()
        # with pd.option_context('display.max_rows',None, 'display.max_columns', None): 
        #     print(resultDataframe1)
        return {'status':'T','messsage':'success','result':{'resultQuerryUpdate':list(resultDataframe.values.tolist()),'colNames':resultDataframe.columns.values},
                'resultChart':{'valChart':list(resultDataFrameChart.values.tolist()),'colChart':resultDataFrameChart.columns.values}}
    except Exception as e:
        print(str(e))
        return {'status':'F','messsage':str(e),'result':[],'resultChart':[]}
    finally:
        cnxn.close()


# print(giroRange('2021-01-01','2021-02-28',keyWhereGir,keyCaseGir))