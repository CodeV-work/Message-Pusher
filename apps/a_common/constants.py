from typing import Tuple

from typing_extensions import Literal

""" 这里放一些不会改变的东西 比如类型到数字的映射关系 """

MANAGE_ROLE_PERMISSION_NAME = 'manage-user:{role_id}'


def to_choice(cls: object) -> Tuple:
    return_choice = ()
    for key, value in cls.__dict__.items():
        if not callable(getattr(cls, key)) and not key.startswith("__"):
            return_choice = return_choice + ((value, key),)
    return return_choice


def to_map(cls: object) -> dict:
    return_dict = {}
    for key, value in cls.__dict__.items():
        if not callable(getattr(cls, key)) and not key.startswith("__"):
            return_dict[value] = key
    return return_dict


class PusherType:
    TEST_WECHAT = 1
    OFFICIAL_WECHAT = 2
    EMAIL = 3
    ANDROID = 4
    WECHAT = 5
    QQ = 6


PUSHER_TYPE_LITERAL = Literal[1, 2, 3, 4, 5, 6]
PUSHER_TYPE_CHOICE = to_choice(PusherType)
PUSHER_TYPE_MAP = to_map(PusherType)
ZH_PUSHER_TYPE_MAP = {
    '微信测试号': 1,
    '企业微信': 2,
    '邮件': 3,
    '安卓': 4,
    '微信': 5,
    'QQ': 6
}
