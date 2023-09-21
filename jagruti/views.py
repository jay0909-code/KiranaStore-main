from django.shortcuts import render, redirect
from django.http import HttpResponse
from jagruti.models import *
import datetime
from django.db.models import Q


# Create your views here.
def IndexPage(request):
    a = Category.objects.all()
    b = Product.objects.all()
    return render(request, "jagruti/index.html", {'data': a, 'products': b})


def ProductPage(request):
    a = Product.objects.all()
    return render(request, "jagruti/product.html", {'data': a})


def ProductFilter(request, pk):
    if 'email' in request.session:
        a = Product.objects.filter(category=pk)
        return render(request, "jagruti/product.html", {'data': a})
    else:
        return redirect('loginpage')


def ProductDetails(request, pk):
    a = Product.objects.get(pk=pk)
    return render(request, "jagruti/product_details.html", {'data': a})


def RegisterPage(request):
    return render(request, "jagruti/register.html")


def RegisterUser(request):
    if request.POST:
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        number = request.POST['mnumber']
        address = request.POST['address']
        password = request.POST['password']
        Cpassword = request.POST['cpassword']

        user = Userregister.objects.filter(Email=email)

        if user:
            message = "User already exist."
            return render(request, "jagruti/register.html", {'msg': message})
        else:
            Userregister.objects.create(Firstname=fname, Lastname=lname, Email=email, MobileNumber=number,Address=address,
                                        Password=password, CPassword=Cpassword)
            return redirect('qpage')

def qpage(request):
    return render(request,"jagruti/questionpage.html")

def question(request):
    a = Question()
    a.question1 = request.POST['question1']
    a.question2 = request.POST['question2']
    a.question3 = request.POST['question3']
    a.contact = request.POST['contact']
    a.save()
    return redirect('loginpage')

def LoginPage(request):
    return render(request, "jagruti/login.html")


def LoginUser(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        user = Userregister.objects.get(Email=email)

        if user:
            if user.Password == password:
                request.session['firstname'] = user.Firstname
                request.session['lastname'] = user.Lastname
                request.session['email'] = user.Email
                request.session['id'] = user.id
                return redirect('index')
            else:
                message = "Password doesn't match."
                return render(request, "jagruti/login.html", {'msg': message})
        else:
            message = "User doesn't exist."
            return render(request, "jagruti/register.html", {'msg': message})


def ContactPage(request):
    return render(request, "jagruti/contact.html")

def for_pass_page(request):
    return render(request,"jagruti/forgotquestionpage.html")

def check_quest(request):
    questiona = request.POST['question1']
    questionb = request.POST['question2']
    questionc = request.POST['question3']
    contact = request.POST['contact']

    a = Userregister.objects.all()

    for i in a:
        b = Question.objects.get(contact=i.MobileNumber)
        request.session['contact'] = b.contact
        if b.question1 == questiona and b.question2 == questionb and b.question3 == questionc:
            return render(request,"jagruti/forgotpassword.html")
        else:
            message = "You give wrong answer or contact n.o. .So,please give right answer."
            return render(request,"jagruti/questionpage.html",{'msg':message})

def ForgotPassword(request):
    password = request.POST['password']

    user = Userregister.objects.get(MobileNumber=request.session['contact'])

    if user:
        user.Password = password
        user.save()
        return redirect('loginpage')

def DeleteUser(request):
    del request.session['email']
    del request.session['id']
    return redirect('index')


def ProfilePage(request, pk):
    user = Userregister.objects.get(pk=pk)
    return render(request, "jagruti/profile.html", {'user': user})


def ProfileUpdate(request, pk):
    user = Userregister.objects.get(pk=pk)

    # user.Firstname = request.POST['firstname']
    # user.Lastname = request.POST['lastname']
    user.MobileNumber = request.POST['mobilenumber']
    user.Address = request.POST['address']
    user.save()
    url = f'/profilepage/{pk}'
    return redirect(url)


def Ordersuccesspage(request):
    return render(request, "jagruti/order_sucess.html")


def buynow(request):
    if request.POST:
        a = Order()
        a.userid = str(request.session['id'])
        a.productid = request.POST['productid']
        prodata = Product.objects.get(id=a.productid)
        a.quantity = "1"
        a.price = str(int(a.quantity) * int(prodata.Price))
        a.save()
        return render(request, "jagruti/order_sucess.html")


def OrderTable(request):
    if 'email' in request.session:
        orderdata = Order.objects.filter(userid=request.session['id'])
        productlist = []
        for i in orderdata:
            productdict = {}
            productdata = Product.objects.get(id=i.productid)
            username = Userregister.objects.get(id = i.userid)
            productdict['image'] = productdata.Image
            productdict['name'] = productdata.Productname
            productdict['quantity'] = i.quantity
            productdict['price'] = i.price
            productdict['date'] = i.datetime
            productdict['username'] = username.Firstname
            productlist.append(productdict)
        cartdata = Cart.objects.filter(userid=request.session['id'])
        prolist = []
        for j in cartdata:
            prodict = {}
            producdata = Product.objects.get(id=j.productid)
            users = shipping.objects.filter(id=j.orderid)
            prodict['image'] = producdata.Image
            prodict['name'] = producdata.Productname
            prodict['qty'] = j.quantity
            prodict['price'] = j.totalprice
            prodict['date'] = j.datetime
            for user in users:
                prodict['username'] = user.firstname

            prolist.append(prodict)
        return render(request, 'jagruti/ordertable.html', {'productlist': productlist, 'prolist': prolist})


# import razorpay
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponseBadRequest


# def buynow(request):
#     if 'email' in request.session:
#         a = Userregister.objects.get(Email=request.session['email'])
#         if request.method == "POST":
#             request.session['productid'] = request.POST['productid']
#             productdata = Product.objects.get(id=request.POST['productid'])
#             request.session['quantity'] = "1"
#             request.session['price'] = str(int(request.session['quantity']) * productdata.Price)
#             request.session['payment'] = "razorpay"
#             return redirect('razorpayView')
#     else:
#         return redirect('login')


# RAZOR_KEY_ID = 'rzp_test_RWTi1ylD8WcKaS'
# RAZOR_KEY_SECRET = 'npP6IpBMdtn7uZYlr9CIIYGt'
# client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))


# def razorpayView(request):
#     currency = 'INR'
#     amount = int(request.session['price']) * 100
#     # Create a Razorpay Order
#     razorpay_order = client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
#     # order id of newly created order.
#     razorpay_order_id = razorpay_order['id']
#     callback_url = 'http://127.0.0.1:8000/paymenthandler/'
#     # we need to pass these details to frontend.
#     context = {}
#     context['razorpay_order_id'] = razorpay_order_id
#     context['razorpay_merchant_key'] = RAZOR_KEY_ID
#     context['razorpay_amount'] = amount
#     context['currency'] = currency
#     context['callback_url'] = callback_url
#     return render(request, 'jagruti/razorpayDemo.html', context=context)


# @csrf_exempt
# def paymenthandler(request):
#     # only accept POST request.
#     if request.method == "POST":
#         # try:
#         # get the required parameters from post request.
#         payment_id = request.POST.get('razorpay_payment_id', '')
#         razorpay_order_id = request.POST.get('razorpay_order_id', '')
#         signature = request.POST.get('razorpay_signature', '')

#         params_dict = {
#             'razorpay_order_id': razorpay_order_id,
#             'razorpay_payment_id': payment_id,
#             'razorpay_signature': signature
#         }

#         # verify the payment signature.
#         result = client.utility.verify_payment_signature(
#             params_dict)

#         amount = int(request.session['price']) * 100  # Rs. 200
#         # capture the payemt
#         client.payment.capture(payment_id, amount)

#         # Order Save Code
#         orderModel = Order()
#         orderModel.userid = request.session['id']
#         if 'name' in request.session:
#             orderModel.name = request.session['name']
#             orderModel.email = request.session['email']
#             orderModel.number = request.session['number']
#             orderModel.address = request.session['address']
#             orderModel.price = request.session['price']
#             orderModel.paymentmethod = request.session['payment']
#             orderModel.transactionid = payment_id
#             orderModel.save()
#             orderdata = Order.objects.latest('id')
#             data = Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0")
#             for i in data:
#                 productdata = Product.objects.get(id=i.productid)

#                 i.orderid = orderdata.pk
#                 i.save()
#                 productdata.save()
#             del request.session['name']
#             del request.session['email']
#             del request.session['number']
#             del request.session['address']
#             del request.session['price']
#             del request.session['payment']
#             # render success page on successful caputre of payment
#             return redirect('ordersuccesspage')
#         else:
#             orderModel.productid = request.session['productid']
#             orderModel.quantity = request.session['quantity']
#             orderModel.price = request.session['price']
#             orderModel.paymentmethod = request.session['payment']
#             orderModel.transactionid = payment_id
#             productdata = Product.objects.get(id=request.session['productid'])
#             productdata.save()
#             orderModel.save()
#             del request.session['productid']
#             del request.session['quantity']
#             del request.session['price']
#             del request.session['payment']
#             # render success page on successful caputre of payment
#             return redirect('ordersuccesspage')
#     #     except:
#     #         print("Hello")
#     #         # if we don't find the required parameters in POST data
#     #         return HttpResponseBadRequest()
#     # else:
#     #     print("Hello1")
#     #    # if other than POST request is made.
#     #     return HttpResponseBadRequest()


def VendorLoginPage(request):
    return render(request, "jagruti/vendorlogin.html")


def VendorLogin(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "jay" and password == "jay":
        request.session['username'] = username
        request.session['password'] = password
        return redirect('index')
    else:
        message = "Passoword is incorrect."
        return render(request,"jagruti/vendorlogin.html",{'msg':message})


def VendorLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('index')


def addcategory(request):
    if request.POST and request.FILES:
        cat = Category()
        cat.Categoryname = request.POST['name']
        cat.Image = request.FILES['img']
        cat.save()
    return render(request, "jagruti/addcart.html")


def addcatpage(request):
    return render(request, "jagruti/addcart.html")


def AddProduct(request):
    a = Category.objects.all()
    if request.POST and request.FILES:
        pro = Product()
        pro.Productname = request.POST['name']
        pro.Price = request.POST['price']
        pro.Quantity = request.POST['quantity']
        pro.Description = request.POST['desc']
        pro.Image = request.FILES['img']
        cat = Category.objects.get(id=request.POST['category'])
        pro.category = cat
        pro.save()
    return render(request, "jagruti/addproduct.html", {'data': a})


def VendorCart(request):
    orderdata = Order.objects.all()
    productlist = []
    for i in orderdata:
        productdict = {}
        productdata = Product.objects.get(id=i.productid)
        username = Userregister.objects.get(id=i.userid)
        productdict['image'] = productdata.Image
        productdict['name'] = productdata.Productname
        productdict['quantity'] = i.quantity
        productdict['price'] = i.price
        productdict['date'] = i.datetime
        productdict['username'] = username.Firstname
        productlist.append(productdict)
    cartdata = Cart.objects.all()
    prolist = []
    for j in cartdata:
        prodict = {}
        producdata = Product.objects.get(id=j.productid)
        users = shipping.objects.filter(id=j.orderid)
        prodict['image'] = producdata.Image
        prodict['name'] = producdata.Productname
        prodict['qty'] = j.quantity
        prodict['price'] = j.totalprice
        prodict['date'] = j.datetime
        for user in users:
            prodict['username'] = user.firstname

        prolist.append(prodict)
    return render(request, 'jagruti/ordertable.html', {'productlist': productlist, 'prolist': prolist})


def AddCart(request):
    if 'email' in request.session:
        if request.method == "POST":
            data = Cart()
            data.orderid = "0"
            data.userid = request.session['id']
            data.productid = request.POST['productid']
            x = request.POST['productid']
            data.quantity = request.POST['quantity']
            a = Product.objects.get(id=request.POST['productid'])
            data.productprice = a.Price
            data.totalprice = str(int(a.Price) * int(data.quantity))
            s = Cart.objects.filter(productid=x) and Cart.objects.filter(orderid="0")
            if len(s) == 0:
                data.save()
                return redirect('productdetails', x)
            else:
                return redirect('productdetails', x)
    else:
        return redirect('loginpage')


def CartPage(request):
    data = Cart.objects.filter(userid=request.session['id'], orderid="0")
    p = []
    final = 0
    for i in data:
        final += int(i.totalprice)
        pro = {}
        prodata = Product.objects.get(id=i.productid)
        pro['name'] = prodata.Productname
        pro['img'] = prodata.Image
        pro['price'] = prodata.Price
        pro['id'] = i.pk
        pro['quantity'] = i.quantity
        pro['totalprice'] = i.totalprice
        p.append(pro)
    return render(request, "jagruti/cart.html", {'productlist': p, 'no': len(p), 'final': final})


def removeitem(request, pk):
    item = Cart.objects.get(pk=pk)

    item.delete()
    return redirect('cartpage')


def removeall(request):
    item = Cart.objects.all() and Cart.objects.filter(orderid="0")
    item.delete()
    return redirect('cartpage')


# def ShippingPage(request):
#     userdata = Userregister.objects.get(id=request.session['id'])
#     data = Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0")
#     p = []
#     final = 0
#     for i in data:
#         final += int(i.totalprice)
#     if request.POST:
#         request.session['name'] = request.POST['name']
#         request.session['email'] = request.POST['email']
#         request.session['address'] = request.POST['address']
#         request.session['number'] = request.POST['number']
#         request.session['price'] = final
#         request.session['paymentmethod'] = "Razorpay"
#         return redirect('razorpayView')
#     return render(request, "jagruti/shiping.html", {'final': final, 'userdata': userdata})

# def shippage(request):
#     userdata = Userregister.objects.get(id=request.session['id'])
#     data = Cart.objects.filter(userid=userdata,orderid="0")
#     p=0
#     for i in data:
#         p += int(i.totalprice)
#     return render(request,"jagruti/shiping.html",{'c':data,'userdata':userdata,'p':p})
def shippage(request):
    userdata = Userregister.objects.get(id=request.session['id'])
    # a = []
    data = Cart.objects.filter(userid=request.session['id'], orderid="0")
    p = 0
    for i in data:
        p += int(i.totalprice)
        a = Product.objects.get(id=i.productid)
        # b= {'c':p}
        # a.append(b)
    return render(request, "jagruti/shiping.html", {'c': data, 'p': p, 'userdata': userdata, 'data': a})


def ships(request):
    userdata = Userregister.objects.get(id=request.session['id'])
    data = Cart.objects.filter(userid=request.session['id'], orderid="0")
    #    order = "0"
    p = []
    #    final = 0
    #    for i in data:
    #         final+=int(i.totalprice)

    if request.POST:
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        address = request.POST['address']
        contact = request.POST['contact']
        price = request.POST['price']
        pro = request.POST['productid']
        for i in data:
            # proid = i.productid
            id = i.pk
            id_dict = {'i': id}
            p.append(id_dict)

        ships = shipping.objects.create(userid=userdata.pk, firstname=fname, lastname=lname, email=email,
                                        contact=contact, address=address, price=price, productid=pro)
        for j in data:
            j.orderid = ships.pk
            j.save()
        return render(request, "jagruti/order_sucess.html")


def your_view(request):
    current_year = datetime.datetime.now().year
    return render(request, 'jagruti/base.html', {'current_year': current_year})


def search(request):
    word = request.GET.get('search')
    wordspilit = word.split(" ")
    for i in wordspilit:
        a = Product.objects.filter(Q(category__Categoryname__icontains=i) | Q(Productname__icontains=i))
    return render(request, "jagruti/product.html", {'data': a})

def error_page(request, exception):
    return render(request,'jagruti/404.html')