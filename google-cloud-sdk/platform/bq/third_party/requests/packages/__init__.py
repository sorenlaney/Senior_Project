#!/usr/bin/env python
'''
Debian and other distributions "unbundle" requests' vendored dependencies, and
rewrite all imports to use the global versions of ``urllib3`` and ``chardet``.
The problem with this is that not only requests itself imports those
dependencies, but third-party code outside of the distros' control too.

In reaction to these problems, the distro maintainers replaced
``requests.packages`` with a magical "stub module" that imports the correct
modules. The implementations were varying in quality and all had severe
problems. For example, a symlink (or hardlink) that links the correct modules
into place introduces problems regarding object identity, since you now have
two modules in `sys.modules` with the same API, but different identities::

    requests.packages.urllib3 is not urllib3

With version ``2.5.2``, requests started to maintain its own stub, so that
distro-specific breakage would be reduced to a minimum, even though the whole
issue is not requests' fault in the first place. See
https://github.com/kennethreitz/requests/pull/2375 for the corresponding pull
request.
'''

from __future__ import absolute_import
import sys

try:
    from . import urllib3
except ImportError:
    import urllib3

try:
    from . import chardet
except ImportError:
    import chardet

try:
    from . import idna
except ImportError:
    import idna

for package in ('urllib3', 'idna', 'chardet'):
    # This traversal is apparently necessary such that the identities are
    # preserved (requests.packages.urllib3.* is urllib3.*)
    for mod in list(sys.modules):
        if mod == package or mod.startswith(package + '.'):
            sys.modules['requests.packages.' + mod] = sys.modules[mod]
