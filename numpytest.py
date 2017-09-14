#encoding:utf-8

import numpy as np

def startMain():
    list = [[1,3,5],[2,4,6]]
    print(type(list))
    np_list = np.array(list)
    print(type(np_list))
    np_lst = np.array(list,dtype= np.float)
    print(np_lst.shape) #形状
    print(np_lst.ndim) #维数
    print(np_lst.dtype)
    print(np_lst.itemsize)
    print(np_lst.size)

    #常用数组
    print(np.zeros([2,3,4],dtype=np.int))
    print(np.ones([3,5]))
    print('Random')
    print(np.random.rand(2,4))
    print('RandomInt')
    print(np.random.randint(1,10,3))
    print('RandomN')
    print(np.random.randn(2,3))
    print('Choice')
    print(np.random.choice(list[1],3))
    print('Beta')
    print(np.random.beta(1,10,100))

    #数据操作
    print(np.arange(1,11,dtype=np.float))
    print(np.arange(1,11,dtype=np.float).reshape(2,5))
    lst = np.arange(1,11,dtype=np.float).reshape(2,5)
    print(np.exp(lst))
    print(np.exp2(lst))
    print(np.power(lst,2))
    print(np.log(lst))
    print(np.sin(lst))
    print(lst*2+1)
    lst=np.arange(1,65).reshape(4,2,8)
    print(lst)
    print('sum')
    print(lst.sum())
    print('sum axis')
    print(np.sum(lst,axis=2))
    print('max')
    print(np.max(lst,axis=2))
    print('max axis')
    print(lst.max(2))
    print('**')
    print(lst**2)
    lst = lst.reshape(-1,4)
    print('lst reshape\n',lst)
    lst2 = np.arange(1,9).reshape(4,2)
    print('dot')
    print(np.dot(lst,lst2))

    #线性方程
    import numpy.linalg
    print(np.eye(4))
    print('inv')
    lst = np.arange(1,17).reshape(2,2,2,2)
    print(np.linalg.inv(lst))
    print('T')
    print(np.transpose(lst2))
    print('Det')
    print(np.linalg.det(np.arange(1,5).reshape(2,2)))
    lst =np.array( [[1,3,4],[2,3,2],[4,5,20]])
    y =np.array( [[12],[14],[120]])
    print ('''求解
1x+3y+4z=12
2x+3y+2z=14
4x+5y+20z=120
的方程''')
    result = np.linalg.solve(lst,y)
    print(result)
    print(np.dot(lst,result))
    print(np.dot(np.linalg.inv(lst),y))

    a = np.poly1d([1,2,-3])
    print(a)
    print(a.r)




if __name__=='__main__':
    startMain()