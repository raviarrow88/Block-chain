from flask import  Flask
from flask import  request

node = Flask(__name__)

current_node_transactions = []

@node.route('/txion',methods=['POST'])

def transaction():
    if request.method == 'POST':
        new_txion = request.get_json()

        current_node_transactions.append(new_txion)
        print "New Transaction"
        print "From: {}".format(new_txion['from'])
        print "To: {}".format(new_txion['to'])
        print "AMOUNT: {}\n".format(new_txion['amount'])
        return "Transaction submission successful\n"


node.run()


