s1 = {2,3,1}
s2 = {'b','a','c'}
s3 = list(zip(s1,s2))
print("Original list: ", s1,s2)
print("Lists after zipping : ", s3 )

list1 = [10,20,30,40,50]
list2 = [100,200,300,400,500]

print("original lists : ",list1, list2)
for i,j in zip(list1,list2):
    print(i,j)

#comment
phones = ['IPhone', 'Samsung', 'OnePlus']
prices = [10000,7000,5000]

newdict = {phones: prices for phones, prices in zip(phones,prices)}
print("\n{}".format(newdict))
