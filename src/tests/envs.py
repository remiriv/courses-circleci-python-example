import pytest


@pytest.fixture(scope="function")
def env_dev(monkeypatch):
    monkeypatch.setenv("ENV_NAME", "development")


@pytest.fixture(scope="function")
def env_staging(monkeypatch):
    monkeypatch.setenv("ENV_NAME", "staging")


@pytest.fixture(scope="function")
def env_default(monkeypatch):
    monkeypatch.delenv("ENV_NAME", raising=False)
