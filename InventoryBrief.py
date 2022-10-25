"""
Inventory Brief module.
"""
from dataclasses import dataclass, field, asdict


@dataclass(frozen=True)
class InventoryBrief:
    """
    Directory Brief metadata.
    """
    contents: list
    name: str
    path: str
    size: int

    def size_human(self):
        """
        Return size human readeble.
        :return:
        """
        return _size_file(self.size)

    def as_dict(self) -> dict:
        """
        Return directory brief as dictionary.
        :return:
        """
        return {
            "contents": [content.as_dict() for content in self.contents],
            "name": self.name,
            "path": self.path,
            "size": self.size,
            "size_human": self.size_human()
        }


@dataclass(frozen=True)
class File:
    """
    File description.
    """
    name: str
    absolute_path: str
    size: int
    type_file: str

    def size_human(self):
        """
        Return size human readeble.
        :return:
        """
        return _size_file(self.size)

    def as_dict(self):
        """
        Return this data as dictionary.
        :return:
        """
        return {
            "size": self.size,
            "size_human": self.size_human(),
            "name": self.name,
            "path": self.absolute_path,
            "type_file": self.type_file
        }


def _size_file(size: int):
    """
    Convert size in byte to human readable.

    :param size: int: Size file in byte.
    :return: str: Size file in format human readable.
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(size) < 1024.0:
            return "%3.1f%s%s" % (size, unit, "B")
        size /= 1024.0
