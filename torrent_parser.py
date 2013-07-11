import re

class parser:
    def __init__(self, path_to_file, path_to_result):
        try:
            with open(path_to_file) as file:
                self.string = file.read()
            self.seek = 0
            self.pattern = r'^\d'
        except:
            print 'Couldn\'t open file'
        self.result = self.__decode()
        self.__deinit(path_to_result)
    def __decode(self):
        if   self.string[0] == 'd': return self.__di()
        elif self.string[0] == 'i': return self.__int()
        elif self.string[0] == 'l': return self.__li()
        elif re.search(self.pattern, self.string[0]): return self.__str()
        elif self.string          : print 'Can\'t decode'
    def __di(self, key=None):
        di = {}
        self.string = self.string[1:]
        while self.string[0] != 'e' :
            key = self.__decode()
            di[key] = self.__decode()
        self.string = self.string[1:]
        return di
    def __str(self):
        try:
            a = self.string.index(':')
            b = int(self.string[:a])
        except:
            print 'Can\'t decode'
            return None
        str = self.string[a+1:a+1+b]
        self.string = self.string[a+b+1:]
        print str
        return str
    def __int(self):
        try:
            a = self.string.index('e')
            b = int(self.string[1:a])
        except:
            print 'Can\'t encode'
            return None
        self.string = self.string[a+1:]
        return b
    def __deinit(self, path_to_result = 'result2'):
        print self.result
        with open(path_to_result,'w') as result:
            result.write("Hi")

a = parser('1.torrent', 'result1')


