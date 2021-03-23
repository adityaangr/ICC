confdictGir = {'k06gir':'k06gir',
            'k07gir': 'k07gir'}


def dictParameter(firstDict):
    dictGir = []
    for i in firstDict:
        stringGir = f''' PATH_FROM LIKE '%{i}%' OR PATH_TO LIKE '%{i}%' '''
        dictGir.append(stringGir)

    cekJoin = 'OR'.join(dictGir)
    return cekJoin

dataDict = dictParameter(confdictGir)

stringQuerry = f'''
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
                WHERE ('''+dataDict+''') AND  FILE_TYPE='TXT' AND ENDED BETWEEN '2021-01-05' AND '2021-01-06'  
                '''
print(stringQuerry)
# dataDict = dictParameter(confdictGir)
# print(dataDict)
# dataDict = dictParameter(confdictGir)

# print(cekJoin)
# for key, value in confdictGir.items():
