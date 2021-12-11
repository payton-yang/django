from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        to_sb = request.POST.get('to_sb')
        money = request.POST.get('money')
        # 打印一下转账结果
        print('%s给%s转了%s元' % (user, to_sb, money))
        return HttpResponse('转账成功')

    return render(request, 'index.html')


def hacker(request):
    return render(request, 'hacker.html')
