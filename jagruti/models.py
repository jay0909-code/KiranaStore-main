from django.db import models


# Create your models here.
class Userregister(models.Model):
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    MobileNumber = models.IntegerField()
    Address = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    CPassword = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Firstname) + " " + str(self.Lastname)


class Category(models.Model):
    Categoryname = models.CharField(max_length=200)
    Image = models.ImageField(upload_to="categoryimage")

    def __str__(self):
        return self.Categoryname


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Productname = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    Quantity = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Image = models.ImageField(upload_to="productimage")


class Order(models.Model):
    userid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    address = models.TextField()
    productid = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_created=True, auto_now=True)
    paymentmethod = models.CharField(max_length=200)
    transactionid = models.CharField(max_length=200)


class Cart(models.Model):
    userid = models.CharField(max_length=200)
    productid = models.CharField(max_length=200)
    orderid = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    productprice = models.CharField(max_length=200)
    totalprice = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_created=True, auto_now=True)


class shipping(models.Model):
    userid = models.CharField(max_length=200)
    productid = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

class Question(models.Model):
    userid = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    question1 = models.CharField(max_length=200)
    question2 = models.CharField(max_length=200)
    question3 = models.CharField(max_length=200)