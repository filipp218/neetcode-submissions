class StringIterator:

    def __init__(self, compressedString: str):
        self.index_in_string = 0
        self.remind_last_char = ''
        self.last_char = ''
        self.start_char = False
        self.compressedString = compressedString


    def next(self) -> str:
        while self.index_in_string < len(self.compressedString):
            if self.compressedString[self.index_in_string].isalpha() and self.start_char:
                self.remind_last_char = int(self.remind_last_char)
                if self.remind_last_char:
                    self.remind_last_char -= 1
                    return self.last_char
                self.start_char = False
                self.remind_last_char = ''

            if self.compressedString[self.index_in_string].isalpha():
                self.last_char = self.compressedString[self.index_in_string]
                self.start_char = True
            if self.compressedString[self.index_in_string].isdigit():
                self.remind_last_char += self.compressedString[self.index_in_string]
            
            self.index_in_string += 1

    def hasNext(self) -> bool:
        if self.index_in_string == len(self.compressedString) - 1 and self.remind_last_char < 1:
            return False
        return True



        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
