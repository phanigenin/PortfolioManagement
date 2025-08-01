from flask import Flask,render_template,request
from middletier.positions import calc_pos_asof_bizdate
from middletier.equity.transactions import register_transaction
from datetime import datetime

app = Flask(__name__,static_url_path='',
        static_folder='templates/static',
        template_folder='templates')

@app.route('/insert_trn', methods=['GET', 'POST'])
def insert_trn():

    print(request.method)

    if request.method == 'POST':
        print(request.form)
        # Get the values from the submitted form
        symbol    = request.form['Symbol']
        price     = float(request.form['Price'])
        qty       = float(request.form['Qty'])
        strt      = request.form['Strategy']
        biz_date  = datetime.strptime(request.form['BizDate'],'%Y-%m-%d').date()
        trn_buysell = "B" if "buysell" not in request.form else "S"
        print(symbol,price,qty,strt,biz_date)
        #url = request.form['ArticleURL']
        register_transaction(symbol,
                             trn_payload={"trn_buysell": trn_buysell, "trn_price": price, "trn_qty": qty, "trn_date": biz_date,"strategy": strt})
        msg = 'Submitted: {0} {1} {2}'.format(symbol,price,qty)
        #msg = "blah"
        return render_template('register_transaction.html',message=msg)

    else:
        msg = 'Please submit transaction'
        return render_template('register_transaction.html',message=msg)

@app.route('/calc_pos', methods=['GET', 'POST'])
def calc_pos():
    if request.method == 'POST':
        print(request.form)

        biz_date  = datetime.strptime(request.form['BizDate'],'%Y-%m-%d').date()
        calc_pos_asof_bizdate(biz_date=biz_date)
        msg = "Calc Positions submitted !"
        return render_template('calc_positions.html',message=msg)

    else:
        msg = 'Please submit date'
        return render_template('calc_positions.html',message=msg)

if __name__ == '__main__':
    app.run(debug=True,port=5002)