import datetime
from datetime import timedelta

confdictGir = {'K06GIR':'K06GIR',
            'K10GIR':'K10GIR',
            'K09GIR':'K09GIR',
            'K11GIR':'K11GIR',
            'K05GIR':'K05GIR',
            'K08GIR': 'K08GIR',
            'K02GIR':'K02GIR',
            'K03GIR':'K03GIR',
            'K04GIR':'K04GIR',
            'K07GIR':'K07GIR',
            'K12GIR':'K12GIR',
            'K01GIR':'K01GIR',}

def dictWhere(firstDict):
    dictGir = []
    for i in firstDict:
        stringGir = f''' PATH_FROM LIKE '%{i}%' OR PATH_TO LIKE '%{i}%' '''
        dictGir.append(stringGir)
    keyJoin = 'OR'.join(dictGir)
    return keyJoin

def dictCase(firstDict):
    dictGir = []
    for i in firstDict:
        stringGir = f''' WHEN PATH_TO LIKE '%{i}%' THEN '{i}' '''
        dictGir.append(stringGir)
    keyJoin = ''.join(dictGir)
    return keyJoin

def dtypesFloat(dataframe):
    colFloat = []
    for col in dataframe.select_dtypes(include=['float64']):
        colFloat.append(col)
    return colFloat

dateLastData = datetime.date.today()
dateLastData = dateLastData.replace(month=2, day=25)

dateThirtyDays = dateLastData +timedelta(days=-30)

keyWhereGir = dictWhere(confdictGir)
keyCaseGir = dictCase(confdictGir)


# testJson = {
#         "labels": ['Jan 2021', 'Feb 2021'],
#         "data":

# }
# print(keyCaseGir)

# def stringQuerrydef(dateFirst, dateLast, paramsData):
#     stringQuerry = (f'''
#                 SELECT TOP 100 *
#                 FROM
#                             (SELECT      
#                                 [iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_TRANSFER_ID] AS FILE_TRANSFER_ID
#                                 ,[iccprod].[dbo].[CC_FILE_TRANSFER].[DURATION] AS 'DURATION(mS)'
#                                 ,RIGHT('0' + CAST([iccprod].[dbo].[CC_FILE_TRANSFER].[DURATION] / 1000 AS VARCHAR),3) + ':'  AS 'DURATION(S)'
#                                 ,[iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_SIZE] AS FILE_SIZE
#                                 ,[iccprod].[dbo].[CC_PROCESS].[PROC_NAME] AS PROC_NAME
#                                 ,[iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_TYPE] AS FILE_TYPE
#                                 ,DATEADD(hour,7,[iccprod].[dbo].[CC_PROCESS].[ENDED]) AS ENDED
#                                 ,[iccprod].[dbo].[CC_PROCESS].[PROC_ID] as PROCESS_ID
#                                 ,[iccprod].[dbo].[CC_FILE_TRANSFER].[RETURN_CODE] AS RC_TRANSFER
#                                 ,[iccprod].[dbo].[CC_PROCESS].[RETURN_CODE] AS RC_PROCESS
#                                 ,[iccprod].[dbo].[CC_FILE_TRANSFER].[TRANSFER_STATUS] AS TRANSFER_STATUS
#                                 ,[iccprod].[dbo].[CC_PROCESS].[PROC_STATUS] AS PROC_STATUS
#                                 ,[iccprod].[dbo].[CC_PROCESS].[SUBMITTER] as SUBMITTER
#                                 ,[iccprod].[dbo].[CC_PROCESS].[ORIG_NODE] AS FROM_NODE
#                                 ,[iccprod].[dbo].[CC_PROCESS].[REMOTE_NODE] AS TO_NODE
#                                 ,[iccprod].[dbo].[CC_FILE_TRANSFER].[XFER_DIRECTION] AS ARAH
#                                 ,[iccprod].[dbo].[CC_FILE_TRANSFER].[REMOTE_FILE_NAME] AS PATH_FROM
#                                 ,[iccprod].[dbo].[CC_FILE_TRANSFER].[LOCAL_FILE_NAME] AS PATH_TO
#                                 ,[iccprod].[dbo].[CC_PROCESS].[LAST_MESSAGE_ID] AS CODE_MESSAGE
#                                 ,[iccprod].[dbo].[CC_PROCESS].[LAST_MESSAGE_TEXT] AS MESSAGE
#                                 FROM  [iccprod].[dbo].[CC_FILE_TRANSFER]
#                                 right JOIN [iccprod].[dbo].[CC_PROCESS]
#                                 ON [iccprod].[dbo].[CC_FILE_TRANSFER].[PROCESS_ID]=[iccprod].[dbo].[CC_PROCESS].[PROCESS_ID] 
#                             ) A
#                 WHERE ({paramsData}) AND FILE_TYPE='TXT' AND  ENDED BETWEEN '{dateFirst}' AND '{dateLast}'
#                 ''')
#     return stringQuerry
    
# print(stringQuerrydef(dateThirtyDays,dateLastData,dataDict))

# dateLastData = dateLastData.replace(day=25)

# print(dateLastData)
# print(dateThirtyDays)

# listGiro = [{'giro': 'E:\\GIRO\\K10GIRH_300121_030704.TXT'}, 
# {'giro': 'E:\\GIRO\\K10GIRM_300121_030705.TXT'}, 
# {'giro': 'E:\\GIRO\\K10GIRX_300121_030707.TXT'}, 
# {'giro': 'E:\\GIRO\\K10GIRH_300121_042011.TXT'}, 
# {'giro': 'E:\\GIRO\\K10GIRM_300121_042013.TXT'}, 
# {'giro': 'E:\\GIRO\\K10GIRX_300121_042014.TXT'}, 
# {'giro': 'E:\\GIRO\\K10GIRH_300121_051900.TXT'}, 
# {'giro': 'E:\\GIRO\\K10GIRM_300121_051901.TXT'},
#  {'giro': 'E:\\GIRO\\K06GIRH_300121_015318.TXT'}, 
#  {'giro': 'E:\\GIRO\\K06GIRM_300121_015319.TXT'}, 
#  {'giro': 'E:\\GIRO\\MK06GIR_300121_034543.TXT'}, 
#  {'giro': 'E:\\GIRO\\MK10GIR_300121_034545.TXT'}, 
#  {'giro': 'E:\\GIRO\\WK10GIR_300121_034603.TXT'}, 
#  {'giro': 'E:\\GIRO\\WK06GIR_300121_034604.TXT'},
#   {'giro': 'E:\\GIRO\\K04GIRH_020221_011049.TXT'}, 
#   {'giro': 'E:\\GIRO\\K09GIRH_020221_011520.TXT'}, 
#   {'giro': 'E:\\GIRO\\K12GIRM_020221_011521.TXT'}, 
#   {'giro': 'E:\\GIRO\\K06GIRM_020221_011522.TXT'}, 
#   {'giro': 'E:\\GIRO\\K05GIRM_020221_011524.TXT'}, 
#   {'giro': 'E:\\GIRO\\K06GIRH_020221_011525.TXT'}, 
#   {'giro': 'E:\\GIRO\\K09GIRM_020221_011526.TXT'}]

# for dt in listGiro:
#     dataListSplitBackSlash = dt['giro'].split('\\')
#     dataListSplitUnderLine = dataListSplitBackSlash[2].split('_')
#     dt['result'] = dataListSplitUnderLine[0][:-1]

# print(listGiro)
