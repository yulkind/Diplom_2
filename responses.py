class Responses:
    create_order_without_ingredients = {"success": False, "message": "Ingredient ids must be provided"}
    create_existing_user = {'message': 'User already exists', 'success': False}
    create_user_without_all_fields = {"success": False, "message": "Email, password and name are required fields"}
    unauth_user = {"success": False, "message": "You should be authorised"}
    user_login_with_incorrect_data = {"success": False, "message": "email or password are incorrect"}
    user_deleted_success = {'success': True, 'message': 'User successfully removed'}
