# Recursive Directory Inventory
## Brief
This repository contains a reader contents of directory, but read contants directory inside directory and show all data, directory size and other things.
It can simplify to show direcory contents or help you to create a Tree View.


## Future versions
Inventory directory tree using asynchronous functions, but this can speedup this reader?

More file details.

Warn permission error instead rise exception.


## Usage
```Python
from directoryInventory import DirectoryInventory

dir_in = DirectoryInventory("C:\\temp\\") # Use you directory here!
dir_dict = dir_in.as_dict() # Show you directory inventory as dictionary.
print(f"{dir_dict}") # Show you directory structure with files.
```
