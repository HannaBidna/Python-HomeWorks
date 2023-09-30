class String(str):
    def __add__(self, other):
        self = str(self) + str(other)
        return self

    def __sub__(self, other):
        index = str(self).find(str(other))
        result = String('')
        if index == -1:
            return self
        else:
            len_other = len(str(other))
            for i in range(0, index):
                result = result + self[i]
            for i in range(index + len_other, len(str(self))):
                result = result + self[i]
            return String(result)

