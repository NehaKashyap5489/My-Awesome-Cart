from django.shortcuts import render
from django.http import HttpResponse
from .models import product,contact,Order,OrderUpdate
from math import ceil
import json

# Create your views here.
def index(request):
    # products=product.objects.all()
    # print(products)
    # n=len(products)
    # nslide=n//4+ceil((n/4)-(4//4))
    allprods=[]
    catprods=product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nslide=n//4+ceil((n/4)-(4//4))
        allprods.append([prod,range(1,nslide),nslide])

    #params={'product':products,'no_of_slides':nslide,'range':range(1, nslide)}
    # allprods=[[products,range(1,nslide),nslide],[products,range(1,nslide),nslide]]
    params={'allprods':allprods}
    return render(request,'shopee/index.html',params)

def about(request):
    return render(request,('shopee/about.html'))

def Contact(request):
    thank=False
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        Contact = contact(name=name,email=email,phone=phone,desc=desc)
        Contact.save()
        thank=True
    return render(request, 'shopee/contact.html',{'thank':thank})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId','')
        email = request.POST.get('email','')
        # return HttpResponse(f"{orderId} and {email}")
        try:
            order=Order.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,('shopee/tracker.html'))

def search(request):
    return render(request,('shopee/search.html'))

def prodView(request,myid):
    #Fetching the products by using id
    product1=product.objects.filter(id=myid)
    print(product1)
    return render(request,('shopee/prodView.html'),{'product':product1[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address1','')+" "+request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        order = Order(items_json=items_json,name=name,email=email,phone=phone,address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The order has been Placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request,('shopee/checkout.html'),{'thank':thank,'id':id})
    return render(request,('shopee/checkout.html'))
