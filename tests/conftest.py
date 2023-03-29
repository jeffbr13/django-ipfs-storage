from unittest import mock

import pytest

from django.conf import settings


def pytest_configure():
    settings.configure(
        IPFS_STORAGE_API_URL="/ip4/0.0.0.0/tcp/5001",
        IPFS_STORAGE_GATEWAY_URL="/ip4/0.0.0.0/tcp/8080",
        IPFS_STORAGE_GATEWAY_API_URL="http://0.0.0.0:8080",
    )


@pytest.fixture
def ipfs_client():
    """Return an ipfshttpclient.Client mock.
    Used for instantation of :class:`ipfs_storage.InterPlanetaryFileSystemStorage`.
    Introduce it in tests as a function argument `ipfs_client`.
    """
    with (
        mock.patch("ipfs_storage.storage.ipfshttpclient.connect") as ipfs_conn_mock,
        mock.patch("ipfs_storage.storage.ipfshttpclient.Client") as client_mock,
    ):
        ipfs_conn_mock.return_value = client_mock
        yield client_mock
