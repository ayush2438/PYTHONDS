class C:
    original_size = 10

    def shape(self):
        return self.original_size
    
cup=C()
cup.original_size=20
cup.fake_size=200
print(cup.fake_size)#this will print 200)
print(cup.shape())#this will print 20 
print(cup.original_size)#this will print 20
print(C.shape(cup))#this will print 20))

plate=C()
print(plate.shape())#this will print 10