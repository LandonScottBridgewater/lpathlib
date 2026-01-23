from pathlib import Path, PosixPath, WindowsPath
import sys

class Script:
    def __init__(self, file=__file__):
        self.path = lPath(file).resolve()
        self.parent = self.path.parent

class lPath(type(Path())):
    def get_siblings(self):
        if not self.exists():
            return []
        return [p for p in self.parent.iterdir() if p != self]

    def get_children(self):
        return list(self.iterdir()) if self.is_dir() else []

    def get_descendants(self):
        return list(self.rglob('*')) if self.is_dir() else []

    def is_descendant_of(self, ancestor):
        try:
            self.relative_to(ancestor)
            return True
        except ValueError:
            return False

    def get_child(self, filename: str):
        if not self.is_dir():
            return None
        for child in self.iterdir():
            if child.name == filename:
                return child
        return None

    def get_sibling(self, filename: str):
        sibling = self.parent / filename
        return sibling if sibling.exists() else None

    def get_matching_descendants(self, filename: str):
        if not self.is_dir():
            return []
        return [p for p in self.rglob('*') if p.name == filename]
