import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import pyodbc
import pandas as pd
from flask_wtf import Form
from wtforms.fields.html5 import DateField
from datetime import datetime as dt
from config import *

def connectionSQLExpress():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=ADITYAANGR;'
                          'Database=iccprod;'
                          'UID=sa;'
                          'PWD=kudaponi69;'
                          'Trusted_Connection=no;')
    return conn


def funcstringQuerry(dateFirst, dateLast, paramsData):
    stringQuerry = (f'''
                SELECT TOP 100 *
                FROM
                            (SELECT      
                                [iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_TRANSFER_ID] AS FILE_TRANSFER_ID
                                ,[iccprod].[dbo].[CC_FILE_TRANSFER].[DURATION] AS 'DURATION(mS)'
                                ,RIGHT('0' + CAST([iccprod].[dbo].[CC_FILE_TRANSFER].[DURATION] / 1000 AS VARCHAR),3) + ':'  AS 'DURATION(S)'
                                ,[iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_SIZE] AS FILE_SIZE
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
                WHERE ({paramsData}) AND FILE_TYPE='TXT' AND  ENDED BETWEEN '{dateFirst}' AND '{dateLast}'
                ''')
    return stringQuerry

def giroRange(timing1,timing2):
    paramsData = dictParameter(confdictGir)
    try:
        cnxn = connectionSQLExpress()
        cursor = cnxn.cursor()
        stringQuerry = funcstringQuerry(timing1,timing2,paramsData)
        cursor.execute(stringQuerry)
        resultQuerryUpdate = cursor.fetchall()
        colNames = [i[0] for i in cursor.description]
        return {'status':'T','messsage':'success','result':{'resultQuerryUpdate':resultQuerryUpdate,'colNames':colNames}}
    except Exception as e:
        print(str(e))
        return {'status':'F','messsage':str(e),'result':[]}
    finally:
        cnxn.close()

    