from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexPage, name="index"),
    path("productfilter/<int:pk>", views.ProductFilter, name="productfilter"),
    path("productpage/", views.ProductPage, name="productpage"),
    path("productget/<int:pk>", views.ProductDetails, name="productdetails"),
    path("registerpage/", views.RegisterPage, name="registerpage"),
    path("registeruser/", views.RegisterUser, name="registeruser"),
    path("loginpage/", views.LoginPage, name="loginpage"),
    path("loginuser/", views.LoginUser, name="loginuser"),
    path("contact/", views.ContactPage, name="contact"),
    path("deleteuser/", views.DeleteUser, name="deleteuser"),
    path("profilepage/<int:pk>", views.ProfilePage, name="profilepage"),
    path("profileupdate/<int:pk>", views.ProfileUpdate, name="profileupdate"),
    path("ordersuccesspage/", views.Ordersuccesspage, name="ordersuccesspage"),
    path("buynow/", views.buynow, name="buynow"),
    path("ordertable/", views.OrderTable, name="orderSuccessView"),
    # path("paymenthandler/", views.paymenthandler, name="paymenthandler"),
    # path("razorpayveiw/", views.razorpayView, name="razorpayView"),
  
    path("addcart/", views.AddCart, name="addcart"),
    path("cartpage/", views.CartPage, name="cartpage"),
    path("removeitem/<int:pk>", views.removeitem, name="removeitem"),
    path("remaoveall/", views.removeall, name="removeall"),
    # path("shipingpage/", views.ShippingPage, name="shipingpage"),
    path("search/",views.search,name="search"),
    path("youview/",views.your_view,name="yv"),
    path("spage/",views.shippage,name="spage"),
    path("ship/",views.ships,name="ship"),
    path("qpage/",views.qpage,name="qpage"),
    path("question/",views.question,name="question"),
    path("fgp/",views.for_pass_page,name="fgp"),
    path("cq",views.check_quest,name="cq"),
    path("fp/",views.ForgotPassword,name="fp"),

    #################################################### Vendor #########################################################################
    path("vendorloginpage/", views.VendorLoginPage, name="vendorloginpage"),
    path("vendorregister/", views.VendorLogin, name="vendorregister"),
    path("deletevendor/", views.VendorLogout, name="deletevendor"),
    path("addproduct/", views.AddProduct, name="addproduct"),
    path("vendorcart/",views.VendorCart,name="vcart"),
    path("addcpage/",views.addcatpage,name="acpage"),
    path("addcategory/",views.addcategory,name="ac"),
    

]
