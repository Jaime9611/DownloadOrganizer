from pathlib import Path


class Downloads:
    """Class that represents the download directory and its organization."""

    # Categories' names and the type of files they will contain.
    categories = {
        'Installers': ['.exe', '.msi'],
        'Images': ['.jpg'],
        'Books': ['.pdf', '.epub'],
        'Office': ['.docx']
    }

    def __init__(self, route):
        """
        Initialize the directory path, the files it contains and create the new 
        directories for each category.
        """

        self.route = Path(route)
        self.files = self._search_files()
        self.dirs = self._make_dirs()

    def organize(self):
        """Organize the files in their respective category"""

        for category, suffixes in self.categories.items():
            for item in self.files[:]:
                if item.suffix in suffixes:
                    self._move_file(category, item)
                    self.files.remove(item)

        # ask for any uncategorized file
        if self.files:
            for item in self.files:
                self._move_file('Others', item)

    def _search_files(self):
        """Find out what files are in the folder and return a list of them."""
        return [ x for x in self.route.iterdir() if x.is_file() ]

    def _make_dirs(self):
        """
        Create the directories for each category, and return a dict with the name and its path.
        """

        dirs = { name: self.route / name for name in self.categories }

        for route in dirs.values():
            if not route.exists():
                route.mkdir()

        others = self.route / 'Others'
        if not others.exists():
            others.mkdir() # Create the 'Others' directory

        return dirs

    def _move_file(self, category, item):
        """Move the file to the specified category."""

        if category == 'Others':
            target = self.route / category / item.name
        else:
            target = self.dirs[category] / item.name

        if not target.exists():
            item.replace(target)