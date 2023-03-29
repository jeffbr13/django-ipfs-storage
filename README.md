django-ipfs-storage
===================

Store [Django file-uploads](https://docs.djangoproject.com/en/4.0/topics/files/)
on the [Interplanetary File System](https://ipfs.io/).

Uploads are added and pinned to the configured IPFS node,
which returns the IPFS Content ID (a hash of the contents).
This hash is the name that is saved to your database.
Duplicate content will also have the same address,
saving disk space.

Because of this, only file creation and reading is supported.

Other IPFS users access and reseed a piece of content
through its unique content ID.
Differently-distributed (i.e. normal HTTP) users
can access the uploads through an HTTP→IPFS gateway.


Installation
------------

```bash
pip install django-ipfs-storage
```
It uses the only Python maintained library for IPFS (as of March 2023) [IPFS-Toolkit](https://github.com/emendir/IPFS-Toolkit-Python)

Configuration
-------------

By default `ipfs_storage` adds and pins content to an IPFS daemon running on localhost
and returns URLs pointing to the public <https://ipfs.io/ipfs/> HTTP Gateway

To customise this, set the following variables in your `settings.py`:

- `IPFS_STORAGE_API_URL`: defaults to `'/ip4/0.0.0.0/tcp/5001'`.
- `IPFS_GATEWAY_API_URL`: defaults to `'/ip4/0.0.0.0/tcp/8080'`.


Usage
-----

There are two ways to use a Django storage backend.

### As default backend

Use IPFS as [Django's default file storage backend](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-DEFAULT_FILE_STORAGE):

```python
# settings.py

DEFAULT_FILE_STORAGE = 'ipfs_storage.InterPlanetaryFileSystemStorage'

IPFS_STORAGE_API_URL = '/ip4/localhost/tcp/5001'

IPFS_STORAGE_GATEWAY_URL = '/ip4/localhost/tcp/8080'
IPFS_STORAGE_GATEWAY_API_URL = 'http://localhost:8080/ipfs'
```


### For a specific FileField

Alternatively, you may only want to use the IPFS storage backend for a single field:

```python
from django.db import models

from ipfs_storage import InterPlanetaryFileSystemStorage


class MyModel(models.Model):
    # …
    file_stored_on_ipfs = models.FileField(storage=InterPlanetaryFileSystemStorage())
    other_file = models.FileField()  # will still use DEFAULT_FILE_STORAGE
```

Don't forget the brackets to instantiate `InterPlanetaryFileSystemStorage()` with the default arguments!


FAQ
---

### Why IPFS?

Not my department. See <https://ipfs.io/#why>.

### How do I ensure my uploads are always available?

I don't know. Maybe look into using [ipfs-cluster](https://github.com/ipfs/ipfs-cluster)
to spread it across a few nodes?
Or perhaps you could integrate [Eternum](https://www.eternum.io)'s hosted pinning service.

### How do I backup my uploads?

See above.

### How do I delete an upload?

Because of the distributed nature of IPFS, anyone who accesses a piece
of content keeps a copy, and reseeds it for you automatically until it's
evicted from their node's local cache. Yay bandwidth costs! Boo censorship!

Unfortunately, if you're trying to censor yourself (often quite necessary),
this means the best we can do is unpin the piece of content from your own IPFS node(s)
and hope nobody else has pinned it.

### How do I securely expose my IPFS daemon's API to connect remotely?

Someone please tell me.

### How do I securely expose my own IPFS←HTTP Gateway?

Again, see above.
