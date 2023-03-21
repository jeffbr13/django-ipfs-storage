from unittest import mock

from django.conf import settings
from django.core.files.base import ContentFile

from ipfs_storage import InterPlanetaryFileSystemStorage


def test_storage_save(ipfs_client):
    name = "test_storage_save.txt"
    content = ContentFile(b"new content")
    storage = InterPlanetaryFileSystemStorage()
    storage.save(name, content)

    assert ipfs_client.add_bytes.called
    assert ipfs_client.pin.add.called


def test_storage_open(ipfs_client):
    storage = InterPlanetaryFileSystemStorage()
    name = "test_storage_open.txt"
    ipfs_client.cat = mock.MagicMock(return_value=b"new content")
    storage.open(name)

    assert ipfs_client.cat.called
    assert ipfs_client.cat.call_args[0][0] == name


def test_storage_delete(ipfs_client):
    storage = InterPlanetaryFileSystemStorage()
    name = "test_storage_open.txt"
    storage.delete(name)
    assert ipfs_client.pin.rm.called
    assert ipfs_client.pin.rm.call_args[0][0] == name


def test_storage_size(ipfs_client):
    storage = InterPlanetaryFileSystemStorage()
    name = "test_storage_save.txt"
    content = ContentFile(b"new content")
    ipfs_client.object.stat.return_value = {"CumulativeSize": 100}
    size = storage.size(name)
    assert ipfs_client.object.stat.called
    assert size == 100


def test_storage_url(ipfs_client):
    storage = InterPlanetaryFileSystemStorage()
    cid = "QmQU6KTY5w4uuxQkLYKNXSJ89naNnkmkJhtne4f1yBquzv"
    url = storage.url(cid)
    assert f"{settings.IPFS_STORAGE_GATEWAY_API_URL}/ipfs/{cid}" == url
