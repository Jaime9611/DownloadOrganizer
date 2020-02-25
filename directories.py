from pathlib import Path


class Downloads:
    categories = {
        'Installers': ['.exe', '.msi'],
        'Images': ['.jpg'],
        'Books': ['.pdf', '.epub'],
        'Office': ['.docx']
    }

    def __init__(self, route):
        self.route = Path(r'C:\Users\Jaime\Downloads')
        self.files = self._search_files()
        self.dirs = self._make_dirs()

    def _search_files(self):
        return [ x for x in self.route.iterdir() if x.is_file() ]

    def _make_dirs(self):
        dirs = { name: self.route / name for name in self.categories }

        for route in dirs.values():
            if not route.exists():
                route.mkdir()

        others = self.route / 'Others'
        if not others.exists():
            others.mkdir() # Create the 'Others' directory

        return dirs

    def _move_file(self, category, item):
        if category == 'Others':
            target = self.route / category / item.name
        else:
            target = self.dirs[category] / item.name

        if not target.exists():
            item.replace(target)

    def organize(self):
        for category, suffixes in self.categories.items():
            for item in self.files[:]:
                if item.suffix in suffixes:
                    self._move_file(category, item)
                    self.files.remove(item)

        # ask for any uncategorized file
        if self.files:
            for item in self.files:
                self._move_file('Others', item)


if __name__ == '__main__':
    d = Downloads('..a')