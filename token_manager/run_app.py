import os
from token_manager.app.app_factory import create_app


if __name__ == '__main__':
    token_app = create_app()
    ssl_context = (os.path.join('certs', 'cert.pem'), os.path.join('certs', 'key.pem'))
    token_app.run(host='0.0.0.0', port=8001, ssl_context=ssl_context)
