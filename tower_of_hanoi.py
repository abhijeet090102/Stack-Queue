class tower_h:

    def toh(self,size,beg,end,aux):
        if size > 1:
            self.toh(size - 1, beg, aux, end)
            #self.end = self.beg
            print(f'{beg}->{end}')
            self.toh(size - 1, aux, end, beg)
        else:
            print(f'{beg}->{end}')

am = tower_h()
am.toh(3, 'B', 'E', 'A')

