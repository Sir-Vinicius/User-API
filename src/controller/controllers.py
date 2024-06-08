from flask import request, jsonify
import uuid
from ... import db
from ..model.models import Account

# GET ALL
def list_all_accounts_controller():
    accounts = Account.query.all()
    response = [account.toDict() for account in accounts]
    return jsonify(response)

# POST
def create_account_controller():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    required_fields = ['email', 'username', 'birth_date', 'phone_number']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields in request"}), 400

    id = str(uuid.uuid4())
    new_account = Account(
        id=id,
        email=data['email'],
        username=data['username'],
        birth_date=data['birth_date'],
        phone_number=data['phone_number'],
    )
    db.session.add(new_account)
    db.session.commit()

    response = Account.query.get(id).toDict()
    return jsonify(response), 201

# GET
def retrieve_account_controller(account_id):
    account = Account.query.get(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(account.toDict())

# PUT
def update_account_controller(account_id):
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    account = Account.query.get(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404

    account.email = data.get('email', account.email)
    account.username = data.get('username', account.username)
    account.birth_date = data.get('birth_date', account.birth_date)
    account.phone_number = data.get('phone_number', account.phone_number)
    db.session.commit()

    response = account.toDict()
    return jsonify(response)

# DELETE
def delete_account_controller(account_id):
    account = Account.query.get(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404

    db.session.delete(account)
    db.session.commit()

    return jsonify({"message": f'Account with Id "{account_id}" deleted successfully!'}), 200
