import os
from app import create_app, db
from app.models import User


# 创建app实例
app = create_app(os.getenv('FLASK_CONFIG') or 'default')


# shell 上下文
@app.shell_context_processor
def make_shell():
    return dict(User=User)


# 测试命令
@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run()
