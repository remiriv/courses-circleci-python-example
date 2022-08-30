from src.app import get_environment_name

# pylint: disable=unused-import
from src.tests.envs import (
    env_dev,
    env_staging,
    env_default,
)


def test_env_dev(env_dev):  # pylint: disable=unused-argument, redefined-outer-name
    assert get_environment_name() == "development"


def test_env_staging(
    env_staging,
):  # pylint: disable=unused-argument, redefined-outer-name
    assert get_environment_name() == "staging"


def test_env_default(
    env_default,
):  # pylint: disable=unused-argument, redefined-outer-name
    assert get_environment_name() == "default"


def test_env_inline():
    assert get_environment_name() == "Still another env"
