import datetime
from datetime import timedelta

confdictGir = {'k06gir':'k06gir',
            'k10gir':'k10gir',
            'k09gir':'k09gir',
            'k11gir':'k11gir',
            'k05gir':'k05gir',
            'k08gir': 'k08gir',
            'k02gir':'k02gir',
            'k03gir':'k03gir',
            'k04gir':'k04gir',
            'k07gir':'k07gir',
            'k12gir':'k12gir',
            'k01gir':'k01gir',}

def dictParameter(firstDict):
    dictGir = []
    for i in firstDict:
        stringGir = f''' PATH_FROM LIKE '%{i}%' OR PATH_TO LIKE '%{i}%' '''
        dictGir.append(stringGir)

    cekJoin = 'OR'.join(dictGir)
    return cekJoin

dateLastData = datetime.date.today()
dateLastData = dateLastData.replace(month=2)

dateThirtyDays = dateLastData +timedelta(days=-30)

dataDict = dictParameter(confdictGir)
# print(dataDict)

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