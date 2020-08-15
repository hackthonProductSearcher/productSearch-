from models import User, Shop, Product
import string
import random
import binascii, hashlib, os

def generate_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

class UserService:
    def create(data):
        pass_hash = hash_password(data['password'])
        id = generate_id()
        print(id)
        pk = User.insert(
            id = id,
            name = data['name'],
            email = data['email'],
            pass_hash = pass_hash,
            is_seller = data['is_seller']
        ).execute()
        return pk
   
    def getAll():
        return User.select()
    
    def getById(id):
        return User.select().where(User.id == id)
    
    def update(data, id):
        return User.update(data).where(User.id == id)

    def delete(id):
        try:
            user = User.get(User.id == id)
            return user.delete_instance()
        except:
            return 'User not found'

class ShopService:
    def create(data):
        try:
            id = generate_id()
            owner = User.get(User.id == data['owner_id'])
            pk = User.insert(
                id = id,
                name = data['name'],
                city = data['city'],
                owner = owner
            ).execute()
            return id
        except:
            return 'DB error'
    
    def getAll():
        return Shop.select()
    
    def getById(id):
        return Shop.select().where(Shop.id == id)
    
    def update(data, id):
        return Shop.update(data).where(Shop.id == id)

    def delete(id):
        try:
            shop = Shop.get(Shop.id == id)
            return shop.delete_instance()
        except:
            return 'Shop not found'

class ProductService:
    def create(data):
        try:
            id = generate_id()
            owner = Shop.get(Shop.id == data['shop_id'])
            pk = User.insert(
                id = id,
                name = data['name'],
                city = data['city'],
                shop = shop
            ).execute()
            return id
        except:
            return 'Can\'t create product'
    
    def getAll():
        return Product.select()
    
    def getById(id):
        return Product.select().where(Product.id == id)
    
    def update(data, id):
        return Product.update(data).where(Product.id == id)

    def delete(id):
        try:
            product = Product.get(Product.id == id)
            return product.delete_instance()
        except:
            return 'Product not found'
