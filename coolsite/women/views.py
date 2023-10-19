from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    t = render_to_string('index.html')
    return HttpResponse(t)


def categories(request, cat_id):
    return HttpResponse(f'ffdgfhgj, {cat_id}')

def pryedmety(request, cat_id):
    if cat_id == 1:
        return HttpResponse('AAAAAAAAAAAAAAAAAAAAAAAAAAAA АЛГЕБРА<img widht=300 height=300 src="https://img01.kupiprodai.ru/112021/1641964916796.jpg">☠️☠️☠️☠️☠️</img>')
    elif cat_id == 2:
        return HttpResponse('БИОЛОГИЯ АААААА СИНТЕЗ БЕЛКОВ: <img widht=300 height=300 src="https://bibliotecapleyades.net/imagenes_ciencia3/life119_01.jpg"></img>')
    elif cat_id == 3:
        return HttpResponse('ходи оглядывайся😂😂😂😂😂😂😂😂😂<img widht=300 height=300 src="https://basket-04.wb.ru/vol449/part44963/44963985/images/big/1.jpg">👻👻👻</img>')
    elif cat_id == 4:
        return HttpResponse('география <img widht=300 height=300 src="https://mbucbs.vl.muzkult.ru/media/2023/05/29/1277919951/1674221132_gas-kvas-com-p-risunok-na-den-geografii-13.jpg">👻👻👻</img>')
    elif cat_id == 5:
        return HttpResponse('геометрия <img widht=300 height=300 src="https://main-cdn.sbermegamarket.ru/hlr-system/152/969/211/423/145/4/100048640377b0.jpg">👻👻👻 НА ЭТОТ УЧЕБНИК НЕТ ГДЗ ОНО ПЛАТНОЕ ВЕЗДЕ</img>')
    elif cat_id == 6:
        return HttpResponse('аглискиц <img widht=300 height=300 src="https://www.e-book24.ru/upload/iblock/ca4/ca4b2f4d96c4c44bdcb4426979e227ec.jpg">👻👻👻</img>')
    elif cat_id == 7:
        return HttpResponse('информатика <img widht=300 height=300 src="https://cache3.youla.io/files/images/780_780/5d/71/5d71fc254aa7e5bb0170ffc7.jpg">👻👻👻</img>')
    elif cat_id == 8:
        return HttpResponse(' истрия <img widht=300 height=300 src="https://uchebniki-shop.ru/upload/iblock/5cf/h6uhto4h2ka9pqs7a8jixfawfn2jxtcn.jpeg">👻👻👻</img>')
    elif cat_id == 9:
        return HttpResponse('<img widht=300 height=300 src="https://na-klass.ru/wp-content/uploads/2017/08/978-5-09-037553-5.jpg">👻👻👻</img>')
    elif cat_id == 10:
        return HttpResponse('😂😂😂😂😂😂😂😂😂<img widht=300 height=300 src="https://dagpravda.ru/wp-content/uploads/2022/08/o-vazhnom-e1661251752632.jpg">👻👻👻</img>')

def page_not_found(request, exception ):
    return HttpResponseNotFound('<h1>страница не найдена<h1>')
