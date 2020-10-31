from token_manager.app.app_factory import create_app


if __name__ == '__main__':
    token_app = create_app()
    token_app.run(host='0.0.0.0', port=8001)
