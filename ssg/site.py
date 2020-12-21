from pathlib import Path

class Site():

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / relative_to(path)
        directory.mkdir(parents=True, exist_ok=True)
        #mkdir(directory, parents=True, exist_ok=True)

    def build():
        self.dest.mkdir(parents=True, exist_ok=True)
        
        for path in self.source.rglob("*"):
            if path.is_directory(): # TODO
                create_dir(path)