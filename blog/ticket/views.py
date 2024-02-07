from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Ticket
from .forms import AddTicketForm

# class MyView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('classes django')
#
#
# class MyTemplateView(TemplateView):  # специальная вьюха для работы с шаблонами
#     template_name = 'ticket/addticket.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MyTemplateView, self).get_context_data(**kwargs)
#         context['text'] = 'Hello world!'
#         return context


class AddTicket(CreateView):
    """
    Добавление тикета
    """
    model = Ticket
    form_class = AddTicketForm
    template_name = 'ticket/addticket.html'

    # переопределям этот метод только из-за того, что
    # нужно получить юзера
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()  # добавление инфы из заполненной формы в бд
        return redirect('/ticket/add_ticket/')

    def success_url(self):
        return redirect('/add_ticket/')


class ListTicket(ListView):
    """Список тикетов пользователя"""
    model = Ticket
    #queryset = Ticket.objects.all()
    context_object_name = 'tickets'
    template_name = 'ticket/list_ticket.html'

    def get_queryset(self):  # в списке тикетов выдаем только тикеты текущего авторизованного юзера
        return Ticket.objects.filter(user=self.request.user)


class UpdateTicket(UpdateView):
    """Редактирование тикета"""
    model = Ticket
    form_class = AddTicketForm
    template_name = 'ticket/update_ticket.html'

    def get_success_url(self):
        return reverse('list_ticket')