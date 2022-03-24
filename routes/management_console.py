from flask import Blueprint
from controllers.ManagementConsole import index , search_Guards
management_console = Blueprint('management_console', __name__)
management_console.route('/', methods=['GET'])(index)
management_console.route('/search-guards', methods=['get'])(search_Guards)
# management_console.route('/<int:user_id>', methods=['GET'])(show)
# management_console.route('/<int:user_id>/edit', methods=['POST'])(update)
# management_console.route('/<int:user_id>', methods=['DELETE'])(destroy)