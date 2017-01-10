
class Tournee(object):

    def __init__(self, name):
        self.name = name
        self.display_filenames = []

    @staticmethod
    def init_with_data(tab, content):
        t = Tournee(tab)
        for i in range(0, len(content)):
            row = content[i]
            if (len(row) < 3):
                raise RuntimeError, "Page %s non conforme" % tab
            t.display_filenames.append(row[2])
            for df in [d for d in row[3:] if d is not None]:
                t.display_filenames.append(df)

        return t

    def __repr__(self):
        return "[%s: %s]" % (self.name, self.display_filenames)
