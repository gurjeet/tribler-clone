import pytest

from tribler_core.components.base import Session
from tribler_core.components.ipv8.ipv8_component import Ipv8Component
from tribler_core.components.key.key_component import KeyComponent
from tribler_core.components.libtorrent.libtorrent_component import LibtorrentComponent
from tribler_core.components.metadata_store.metadata_store_component import MetadataStoreComponent
from tribler_core.components.socks_servers.socks_servers_component import SocksServersComponent
from tribler_core.components.tag.tag_component import TagComponent
from tribler_core.components.torrent_checker.torrent_checker_component import TorrentCheckerComponent


# pylint: disable=protected-access
@pytest.mark.asyncio
@pytest.mark.no_parallel
async def test_torrent_checker_component(tribler_config):
    components = [SocksServersComponent(), LibtorrentComponent(), KeyComponent(),
                  Ipv8Component(), TagComponent(), MetadataStoreComponent(), TorrentCheckerComponent()]
    async with Session(tribler_config, components).start():
        comp = TorrentCheckerComponent.instance()
        assert comp.started_event.is_set() and not comp.failed
        assert comp.torrent_checker
