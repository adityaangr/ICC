import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import pyodbc
import pandas as pd
from flask_wtf import Form
from wtforms.fields.html5 import DateField
from datetime import datetime as dt

from dao import *
# from cekDict import *
from config import *


app = Flask(__name__)
app.secret_key = 'SHH!'

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/mastergiro", methods=["POST","GET"])
def mastergiro():
    dataDict = dictParameter(confdictGir)
    cnxn = connectionSQLExpress()
    cursor = cnxn.cursor()
    stringQuerry = funcstringQuerry(dateThirtyDays,dateLastData,dataDict)
    cursor.execute(stringQuerry)
    resultQuerry = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template("mastergiro.html",menu='dataworkload', submenu='datagiro', rowTable=resultQuerry, headingTable=colNames)


@app.route("/range",methods=["POST","GET"])
def range(): 
    if request.method == 'POST':
        timing = request.form['From']
        timing2 = request.form['to']
        data = giroRange(timing,timing2)
        if data['status'] == 'F':
            return jsonify({'htmlresponse': render_template('response.html', rowTableUpdate=[],headingTableUpdate=[])})
    return jsonify({'htmlresponse': render_template('response.html', rowTableUpdate=data['result']['resultQuerryUpdate'],headingTableUpdate=data['result']['colNames'])})


@app.route("/mastersupplier", methods=["GET","POST"])
def mastersupplier():
    if request.method == "POST":
        cnxn = connectionSQLExpress()
        cursor = cnxn.cursor()
        datetimes = request.form["datetimes"]
        # print(datetimes)
        startTime, endTime = datetimes.split(' - ', 1)
        format = '%Y/%m/%d %I:%M %p'
        dtstartTime = dt.strptime(startTime, format).strftime('%Y-%m-%d %H:%M:%S.%f0')
        dtendTime = dt.strptime(endTime, format).strftime('%Y-%m-%d %H:%M:%S.%f0')
        stringQuerry = (
        f'''
            SELECT *
            FROM 
                (SELECT       
                            [iccprod].[dbo].[CC_PROCESS].[PROC_ID] as PROCESS_ID,
                            DATEADD(hour,7,[iccprod].[dbo].[CC_PROCESS].[ENDED]) AS ENDED ,
                            [iccprod].[dbo].[CC_PROCESS].[PROC_NAME] AS PROC_NAME,
                            [iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_SIZE] AS FILE_SIZE,
                            [iccprod].[dbo].[CC_FILE_TRANSFER].[DURATION] AS 'DURATION(mS)',
                            RIGHT('0' + CAST([iccprod].[dbo].[CC_FILE_TRANSFER].[DURATION] / 1000 AS VARCHAR),3) + ':'  AS 'DURATION(S)', 
                            [iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_TYPE] AS FILE_TYPE,	
                            [iccprod].[dbo].[CC_FILE_TRANSFER].[RETURN_CODE] AS RC_TRANSFER,
                            [iccprod].[dbo].[CC_FILE_TRANSFER].[TRANSFER_STATUS] AS TRANSFER_STATUS,
                            [iccprod].[dbo].[CC_PROCESS].[RETURN_CODE] AS RC_PROCESS,
                            [iccprod].[dbo].[CC_PROCESS].[PROC_STATUS] AS PROC_STATUS,
                            [iccprod].[dbo].[CC_PROCESS].[SUBMITTER] as SUBMITTER,
                            [iccprod].[dbo].[CC_PROCESS].[ORIG_NODE],
                            [iccprod].[dbo].[CC_PROCESS].[REMOTE_NODE],
                            [iccprod].[dbo].[CC_FILE_TRANSFER].[XFER_DIRECTION] AS ARAH,
                            [iccprod].[dbo].[CC_FILE_TRANSFER].[LOCAL_FILE_NAME] AS LOCAL_PATH_FILE,
                            [iccprod].[dbo].[CC_FILE_TRANSFER].[REMOTE_FILE_NAME] AS REMOTE_PATH_FILE,
                            [iccprod].[dbo].[CC_PROCESS].[LAST_MESSAGE_ID] AS CODE_MESSAGE,
                            [iccprod].[dbo].[CC_PROCESS].[LAST_MESSAGE_TEXT] AS MESSAGE
                    FROM	[iccprod].[dbo].[CC_FILE_TRANSFER] right JOIN [iccprod].[dbo].[CC_PROCESS]
                    ON		[iccprod].[dbo].[CC_FILE_TRANSFER].[PROCESS_ID]=[iccprod].[dbo].[CC_PROCESS].[PROCESS_ID] 
                ) MainQuerry
            WHERE ENDED BETWEEN '{dtstartTime}' AND '{dtendTime}'
            --and REMOTE_PATH_FILE LIKE '%K01GIR%'  
            AND TRANSFER_STATUS='success' and ORIG_NODE='CD.CD3PARTY'
            ORDER BY ENDED DESC
            '''
        )
        cursor.execute(stringQuerry)
        resultfirst = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        return render_template("mastersupplier.html",menu='dataworkload', submenu='supplier', data=resultfirst,lendata=len(resultfirst), colnames=field_names, lencolnames = len(cursor.description))
    else:
        return render_template("mastersupplier.html",menu='dataworkload', submenu='supplier')
# class ExampleForm(Form):
#     dt = DateField('DatePicker', format='%Y-%m-%d')


# @app.route('/mastersupplier', methods=['POST','GET'])
# def hello_world():
#     form = ExampleForm()
#     if form.validate_on_submit():
#         return form.dt.data.strftime('%Y-%m-%d')
#     return render_template('mastersupplier.html', form=form)


# @app.route("/masterbarang", methods=["GET","POST"])
# def masterbarang():
#     nama = request.form['nama']
#     cnxn = connectionSQLExpress()
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT * FROM [pos].[dbo].[masterbarang] where Nama={nama}", (nama))
#     all_result = cursor.fetchall()
#     return render_template('masterbarang.html', menu='master', submenu='barang', form=nama, data=all_result)

# @app.route("/mastersupplier")
# def mastersupplier():
#     return render_template('mastersupplier.html', menu='master', submenu='supplier')


@app.route("/masterpelanggan")
def masterpelanggan():
    return render_template('masterpelanggan.html', menu='master', submenu='pelanggan')

# @app.route("/formpembelian",  methods=["GET","POST"])
# def formpembelian():
#     if request.method == "POST":
#         datetimes = request.form["datetimes"]
#         print(datetimes)
#         valDate = str(datetimes)
#         return render_template('formpembelian.html', menu='pembelian', submenu='form', val=valDate)
#     else:
#         return render_template('formpembelian.html', menu='pembelian', submenu='form')

@app.route('/formpembelian'  ,methods=["GET","POST"])
def asd():
    if request.method == "POST":
        # From = request.form['From']
        # to = request.form['to']
        # print(From)
        # print(to)
        # cnxn = connectionSQLExpress()
        # cursor = cnxn.cursor()
        startTimestamp = request.form["startTimestamp"]
        datetimes = request.form["endTimestamp"]
        print(datetimes)
        # startTime, endTime = datetimes.split(' - ', 1)
        
        # format = '%Y/%m/%d %I:%M %p'
        # dtstartTime = dt.strptime(startTime, format).strftime('%Y-%m-%d %H:%M:%S.%f0')
        # dtendTime = dt.strptime(endTime, format).strftime('%Y-%m-%d %H:%M:%S.%f0')
        # stringQuerry = (
        # f'''
        #     SELECT *
        #     FROM 
        #         (SELECT       
        #                     [iccprod].[dbo].[CC_PROCESS].[PROC_ID] as PROCESS_ID,
        #                     DATEADD(hour,7,[iccprod].[dbo].[CC_PROCESS].[ENDED]) AS ENDED ,
        #                     [iccprod].[dbo].[CC_PROCESS].[PROC_NAME] AS PROC_NAME,
        #                     [iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_SIZE] AS FILE_SIZE,
        #                     [iccprod].[dbo].[CC_FILE_TRANSFER].[DURATION] AS 'DURATION(mS)',
        #                     RIGHT('0' + CAST([iccprod].[dbo].[CC_FILE_TRANSFER].[DURATION] / 1000 AS VARCHAR),3) + ':'  AS 'DURATION(S)', 
        #                     [iccprod].[dbo].[CC_FILE_TRANSFER].[FILE_TYPE] AS FILE_TYPE,	
        #                     [iccprod].[dbo].[CC_FILE_TRANSFER].[RETURN_CODE] AS RC_TRANSFER,
        #                     [iccprod].[dbo].[CC_FILE_TRANSFER].[TRANSFER_STATUS] AS TRANSFER_STATUS,
        #                     [iccprod].[dbo].[CC_PROCESS].[RETURN_CODE] AS RC_PROCESS,
        #                     [iccprod].[dbo].[CC_PROCESS].[PROC_STATUS] AS PROC_STATUS,
        #                     [iccprod].[dbo].[CC_PROCESS].[SUBMITTER] as SUBMITTER,
        #                     [iccprod].[dbo].[CC_PROCESS].[ORIG_NODE],
        #                     [iccprod].[dbo].[CC_PROCESS].[REMOTE_NODE],
        #                     [iccprod].[dbo].[CC_FILE_TRANSFER].[XFER_DIRECTION] AS ARAH,
        #                     [iccprod].[dbo].[CC_FILE_TRANSFER].[LOCAL_FILE_NAME] AS LOCAL_PATH_FILE,
        #                     [iccprod].[dbo].[CC_FILE_TRANSFER].[REMOTE_FILE_NAME] AS REMOTE_PATH_FILE,
        #                     [iccprod].[dbo].[CC_PROCESS].[LAST_MESSAGE_ID] AS CODE_MESSAGE,
        #                     [iccprod].[dbo].[CC_PROCESS].[LAST_MESSAGE_TEXT] AS MESSAGE
        #             FROM	[iccprod].[dbo].[CC_FILE_TRANSFER] right JOIN [iccprod].[dbo].[CC_PROCESS]
        #             ON		[iccprod].[dbo].[CC_FILE_TRANSFER].[PROCESS_ID]=[iccprod].[dbo].[CC_PROCESS].[PROCESS_ID] 
        #         ) MainQuerry
        #     WHERE ENDED BETWEEN '{dtstartTime}' AND '{dtendTime}'
        #     --and REMOTE_PATH_FILE LIKE '%K01GIR%'  
        #     AND TRANSFER_STATUS='success' and ORIG_NODE='CD.CD3PARTY'
        #     ORDER BY ENDED DESC
        #     '''
        # )
        # cursor.execute(stringQuerry)
        # ordersrange = cursor.fetchall()
        # field_names = [i[0] for i in cursor.description]
        return  render_template("formpembelian.html")#, ordersrange=ordersrange,lendata=len(ordersrange), colnames=field_names, lencolnames = len(cursor.description))
    else:
        return render_template("formpembelian.html",menu='pembelian', submenu='form') 

  
# @app.route("/formpembelian_render",methods=["POST","GET"])
# def range(): 
#     if request.method == 'POST':
#         From = request.form['From']
#         to = request.form['to']
#         print(From)
#         print(to)
#     return jsonify({'htmlresponse': render_template('formpembelian_render.html')})


@app.route("/datapembelian")
def maidatapembeliann():
    return render_template('datapembelian.html', menu='pembelian', submenu='data')

@app.route("/formpenjualan")
def formpenjualan():
    return render_template('formpenjualan.html', menu='penjualan', submenu='form')

@app.route("/datapenjualan")
def datapenjualan():
    return render_template('datapenjualan.html', menu='penjualan', submenu='data')

@app.route("/tes")
def datates():
    
    return jsonify({'tes':'tes'})

if __name__ == "__main__":
    app.run(debug=True)