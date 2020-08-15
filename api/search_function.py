import sqlite3

'''
db = path to database in your computer
ct = connection to database
'''
db = 'hacks.db'
ct = sqlite3.connect(db)

'''
cs = cursor used to collect data from database
u_t = user table
u_i = user id
u_n = user name
u_e = user email
u_p = user pass hash
u_s = user is seller?
So, I collect the data and put them in above variables
'''
cs = ct.execute('select id,name,email,pass_hash,is_seller from user')
u_t = ('id','name','email','pass_hash','is_seller')
u_i,u_n,u_e,u_p,u_s = [],[],[],[],[]
tp = list(cs)
for i in tp :
    u_i.append(i[0].lower())
    u_n.append(i[1].lower())
    u_e.append(i[2].lower())
    u_p.append(i[3].lower())
    u_s.append(i[4])

'''
cs = cursor used to collect data from database
s_t = shop table
s_i = shop id
s_c = shop city
s_n = shop name
s_o = shop owner id
So, I collect the data and put them in above variables
'''
cs = ct.execute('select id,city,name,owner_id from shop')
s_t = ('id','city','name','owner_id')
s_i,s_c,s_n,s_o = [],[],[],[]
tp = list(cs)
for i in tp :
    s_i.append(i[0].lower())
    s_c.append(i[1].lower())
    s_n.append(i[2].lower())
    s_o.append(i[3].lower())

'''
cs = cursor used to collect data from database
p_t = product table
p_i = product id
p_n = product name
p_p = product price
p_s = product shop id
So, I collect the data and put them in above variables
'''
cs = ct.execute('select id,name,price,shop_id from product')
p_t = ('id','name','price','shop_id')
p_i,p_n,p_p,p_s = [],[],[],[]
tp = list(cs)
for i in tp :
    p_i.append(i[0].lower())
    p_n.append(i[1].lower())
    p_p.append(i[2])
    p_s.append(i[3].lower())

'''
This function takes shop name as input
This function prints products and prices in the shop name
'''
def search_shop(sn) :
    try :
        si = s_i[s_n.index(sn.lower())]
        o_n,o_p,k = [],[],0
        for i in p_s :
            if i == si :
                o_n.append(p_n[p_s.index(i,k)])
                o_p.append(p_p[p_s.index(i,k)])
            else : None
            k += 1
        print(o_n)
        print(o_p)
    except : print('Shop does not exist')

'''
This function takes product name as input
This function prints shop names and their cities
'''
def search_product(pn) :
    try :
        si = p_s[p_n.index(pn.lower())]
        o_n,o_c,k = [],[],0
        for i in s_i :
            if i == si :
                o_n.append(s_n[s_i.index(i,k)])
                o_c.append(s_c[s_i.index(i,k)])
            else : None
            k += 1
        print(o_n)
        print(o_c)
    except : print('Product does not exist')

'''
How to use the function
'''
# f_s('fauzan\'s shop')
# f_p('tablet')
