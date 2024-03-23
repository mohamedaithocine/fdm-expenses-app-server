from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models.claim import Claim, ClaimStatus

bp = Blueprint('claims', __name__, url_prefix='/claims')


@bp.route('/', methods=["GET"])
@login_required
def get_claims():
    claims = [{'id': claim.id, 'temp': claim.temp} for claim in current_user.claims]
    return jsonify({'claims': claims}), 200


@bp.route('/<claim_id>', methods=["GET"])
@login_required
def get_claim(claim_id):
    claim = Claim.query.filter_by(id=int(claim_id)).first()

    if claim.user_id != current_user.get_id():
        return jsonify({'error': 'Unauthorised'}), 401

    return jsonify({'data': {'id': claim.id, 'temp': claim.temp}}), 200


@bp.route('/<claim_id>/review')
@login_required
def review_claim(claim_id):
    claim = Claim.query.filter_by(id=int(claim_id)).first()
    # ...
    return jsonify({'message': 'successful'}), 200


@bp.route('/managed-by')
@login_required
def get_review_claims():
    # if user is not a line manager, send error message
    # ...

    claims = []
    for employee in current_user.managed_employees:
        claims += employee.claims

    pending_claims = [{'id': claim.id, 'temp': claim.temp} for claim in claims if claim.status == ClaimStatus.PENDING]

    return jsonify({'claims': pending_claims}), 200
