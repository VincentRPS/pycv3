# MIT License
#
# Copyright (c) 2023 VincentRPS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys

from aiohttp import BasicAuth, ClientSession, __version__ as aiohttp_version

from .._version import __version__


class HTTPClient:
    def __init__(
        self,
        token: str | None = None,
        base_url: str = "https://discord.com/api/v10",
        proxy: str | None = None,
        proxy_auth: BasicAuth | None = None,
    ) -> None:
        self.base_url = base_url
        self._proxy = proxy
        self._proxy_auth = proxy_auth
        self._headers = {
            "User-Agent": "DiscordBot (https://pycord.dev, {0}) Python/{1[0]}.{1[1]} aiohttp/{2}".format(
                __version__, sys.version_info, aiohttp_version
            ),
        }
        if token:
            self._headers["Authorization"] = f"Bot {token}"

        self._session: None | ClientSession = None
