class Chai:
    origin="India"
    flavor="spicy"

print(Chai.origin)

Chai.is_hot=True
print(Chai.is_hot)

masal=Chai()
print(masal.origin)
print(masal.is_hot)

masal.is_hot=False
print("original class",Chai.is_hot)
print("masal",masal.is_hot)

masal.flavor="lemon"

print(Chai.flavor)  
print(masal.flavor)  # This will print "lemon" since masal has its own flavor attribute