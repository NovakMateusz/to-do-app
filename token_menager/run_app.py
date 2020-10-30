from token_menager.app.app_factory import create_app


if __name__ == '__main__':
    token_app = create_app()
    token_app.run()
