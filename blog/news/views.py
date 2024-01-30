from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comments
from .forms import CommentForm


def news_list(request):
    """Вывод всех новостей"""
    news = News.objects.all()
    return render(request, "news/news_list.html", {'news': news})


def new_single(request, pk):
    """Вывод полной статьи"""
    new = get_object_or_404(News, id=pk)
    # закоментим, чтобы выводить коменты не через views, а через шаблон
    # но это не совсем правильно!
    # правильнее всю логику обработки запросов выносить во views
    comment = Comments.objects.filter(new=pk, moderation=True)

    # если POST запрос, форму обрабатываем и сохраняем
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)  # редиректимся на страницу новости
    else:  # если GET запрос, форму создаем
        form = CommentForm()
    return render(request, 'news/new_single.html',
                  {
                      'new': new,
                      'comments': comment,
                      'form': form
                  })



