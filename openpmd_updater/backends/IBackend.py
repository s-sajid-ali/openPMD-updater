"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

class IBackend(object):
    """An I/O file format backend.
    Used to access and modify existing files with openPMD markup.
    """
    
    @abstractmethod
    def __init__(self, filename):
        """Open a file"""
        raise NotImplementedError("File opening not implemented!")

    @abstractmethod
    def can_handle(self, filename):
        """Check if a backend can handle a file."""
        raise NotImplementedError("File handling check not implemented!")

    @abstractmethod
    def cd(self, filename):
        """Change current directory in file."""
        raise NotImplementedError("Directory change not implemented!")

    @abstractmethod    
    def list_groups(self, path):
        """Return a list of groups in a path"""
        raise NotImplementedError("Group listing not implemented!")

    @abstractmethod
    def list_attrs(self, path):
        """Return a list of attributes on a path"""
        raise NotImplementedError("Attribute listing not implemented!")

    @abstractmethod
    def list_data(self, path):
        """Return a list of datasets in a path"""
        raise NotImplementedError("Data listing not implemented!")

    @abstractmethod
    def move(self, old_path, new_path):
        """Move (rename) a group, attribute or dataset"""
        raise NotImplementedError("Move (rename) not implemented!")

    @abstractmethod    
    def delete(self, path):
        """Remove a group, attribute or dataset"""
        raise NotImplementedError("Deleting not implemented!")

    @abstractmethod
    def add_group(self, path)
        """Add a new group at path"""
        raise NotImplementedError("Group adding not implemented!")

    @abstractmethod
    def add_attr(self, path, value)
        """Add a new attribute at path"""
        raise NotImplementedError("Attribute adding not implemented!")

    @abstractmethod
    def get_attr(self, path)
        """Read an attribute"""
        raise NotImplementedError("Attribute reading not implemented!")