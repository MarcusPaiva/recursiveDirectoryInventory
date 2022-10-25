"""
Directory Inventory engine module.
"""
from InventoryBrief import InventoryBrief, File
import os
from pathlib import Path


class DirectoryInventory:
    def __init__(self, path):
        self._path = path
        self._start()

    def as_dict(self):
        """
        Return directory metadata as dict.
        :return:
        """
        return self._dir_contents.as_dict()

    def metadata(self):
        """
        Return directory as metadata instance.
        :return:
        """
        return self._dir_contents

    def _start(self):
        """
        Startup process
        """
        self._dir_contents = self._reader_recursive(self._path)

    def _reader_recursive(self, path: str) -> InventoryBrief:
        """
        Reader a directory recursively.
        :return: InventoryBrief instance.
        """
        path_metadata = Path(path)
        list_dir = [Path(os.path.join(path, file)).as_posix() for file in os.listdir(path)]
        contents = [
            File(Path(content).name, absolute_path=content, size=os.path.getsize(content), type_file=Path(content).name.split(".")[-1])
            if os.path.isfile(content)
            else self._reader_recursive(content)
            for content in list_dir
        ]
        invent_brief = InventoryBrief(
            name=path_metadata.name,
            path=path_metadata.as_posix(),
            contents=contents,
            size=sum([content.size for content in contents]))
        return invent_brief


if __name__ == '__main__':
    # dir_in = DirectoryInventory(r"C:\Users\marcu\OneDrive\Documentos\arquivos migração")
    # dir_in = DirectoryInventory(r"C:\Jogos")
    dir_in = DirectoryInventory("F:\\")
    dir_dict = dir_in.as_dict()
    print("here!")
