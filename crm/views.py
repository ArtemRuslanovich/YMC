from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from telegbot.SendMessage import sendTelegram

# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()

    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'form': form,
                }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone)
        return render(request, './thanks.html', {'name': name, })
    else:
        return render(request, './thanks.html')


def Page_about(request):
    return render(request, './about.html')
