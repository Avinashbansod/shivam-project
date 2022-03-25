from flask import Blueprint
from controllers.ManagementConsole import index , searchGuards, createGuard, renderCreateGuardForm, updateGuard
management_console = Blueprint('management_console', __name__)
management_console.route('/', methods=['GET'])(index)
management_console.route('/search-guards', methods=['get'])(searchGuards)
management_console.route('/register-new-guard', methods=['POST'])(createGuard)
management_console.route('/register-new-guard', methods=['GET'])(renderCreateGuardForm)
management_console.route('/update-guard', methods=['GET','POST'])(updateGuard)
# management_console.route('/<int:user_id>', methods=['DELETE'])(destroy)