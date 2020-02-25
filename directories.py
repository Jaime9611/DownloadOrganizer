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
            route.mkdir()

        return dirs

    def organize(self):

        # for category, suffixes in self.categories.items():
        #     for file in self.files:
        #         if file.suffix in suffixes:
        
        pass
    
    def move_file(self, category, file):
        pass

if __name__ == '__main__':
    d = Downloads('~/Downloads')
    print(d.dirs)