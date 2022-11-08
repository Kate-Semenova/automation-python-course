class KeyValueStorage:
    song_name = 'hello'

    def __init__(self, path_to_file) -> None:
        lines: list
        with open(path_to_file) as f:
            for line in f:
                split = line.strip().split('=')
                if split[0][0].isdigit():
                    raise ValueError('Unacceptable attribute')
                try:
                    self.__getattribute__(split[0])
                except:
                    split__strip = split[1].strip()
                    if split__strip.isdigit():
                        split__strip = int(split__strip)
                self.__setattr__(split[0].strip(), split__strip)
        super().__init__()

    def __getitem__(self, text):
        return self.__getattribute__(text)


storage = KeyValueStorage('file.txt')
