from enum import Enum


class MessageType(Enum):
    GROUP_MESSAGE = "GroupMessage"  # 群组形式的消息
    GROUP_ADD = "GroupAdd"  # 加群邀请事件，入群
    FRIEND_ADD = "FriendAdd"  # 加好友邀请事件
    GROUP_DEL = "GroupDel"  # 群聊踢出事件
    FRIEND_DEL = "FriendDel"  # 私聊好友删除事件
    FRIEND_MESSAGE = "FriendMessage"  # 私聊、好友等单聊消息
    OTHER_MESSAGE = "OtherMessage"  # 其他类型的消息，如系统消息等
