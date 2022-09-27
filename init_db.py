import sys
from werkzeug.security import generate_password_hash
from users_mgt import create_user_table, add_user


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} [admin-email] [admin-password]')
        sys.exit(0)

    USER_NAME = 'admin'
    USER_EMAIL = sys.argv[1]
    USER_PASSWORD = sys.argv[2]
    USER_IS_ADMIN = True

    create_user_table()
    add_user(USER_NAME, USER_PASSWORD, USER_EMAIL, USER_IS_ADMIN)
