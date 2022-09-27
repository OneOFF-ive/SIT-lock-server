from urllib.parse import urlencode
import asyncio
from WebAPI.lib.config import LockConfig


class LockUrlBuilder:
    def __init__(self):
        self.base_url = None
        self.card_id = None
        self.mac_id = None
        self.laboratory_id = None
        self.method = None

    async def build(self, path: str = ''):
        full_dict = {
            'Method': self.method,
            'ShiYanShiID': self.laboratory_id,
            'KaHao': self.card_id,
            'MacID': self.mac_id,
        }
        # 去除所有的值为None的参数
        selected_dict = {k: v for (k, v) in full_dict.items() if v is not None}
        query = urlencode(selected_dict)
        return f'{self.base_url}{path}?{query}'


async def build_shuaka_liu_cheng_url_by_config(config: LockConfig):
    builder = LockUrlBuilder()
    builder.base_url = config.base_url
    builder.card_id = config.card_id
    builder.mac_id = config.mac_id
    builder.method = 'ShuaKaLiuCheng'
    return await builder.build(path='/HCommon.ashx')


async def build_remote_open_door_url_by_config(config: LockConfig):
    builder = LockUrlBuilder()
    builder.base_url = config.base_url
    builder.card_id = config.card_id
    builder.mac_id = config.mac_id
    builder.method = 'SaveRemoteOpenDoor'
    builder.laboratory_id = ''
    return await builder.build(path='/HShiYanShi.ashx')


__all__ = [
    "build_shuaka_liu_cheng_url_by_config",
    "build_remote_open_door_url_by_config",
    "LockUrlBuilder",
]
