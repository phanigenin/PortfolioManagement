from flask import Flask,render_template,request,jsonify

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

@app.route('/open_pos_bonds', methods=['GET'])
def open_pos_bonds():
    from middletier.bonds.bonds_api import get_all_bond_positions_detail

    res  = get_all_bond_positions_detail()
    data = res.to_dict(orient="records")
    return jsonify(data)

@app.route('/get_bond_instruments', methods=['GET'])
def get_bond_instruments():
    from middletier.bonds.bonds_api import get_bond_instruments,get_instrument_by_issuers,get_bond_instruments_by_isins

    print(get_instrument_by_issuers(["Keertana"]))
    print(get_bond_instruments_by_isins(["INE296Q07068","INE0NES07188"]))

    res  = get_bond_instruments()
    data = res.to_dict(orient="records")
    return jsonify(data)

#http://127.0.0.1:5002/open_pos_bonds
#http://127.0.0.1:5002/get_bond_instruments
if __name__ == '__main__':
    app.run(debug=True,port=5002)