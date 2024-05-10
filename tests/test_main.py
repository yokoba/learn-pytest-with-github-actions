from src.learn_pytest_with_github_actions.main import add


def test_add():
    assert add(1, 2) == 3
