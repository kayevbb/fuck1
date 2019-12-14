
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from .forms import FieldCreateForm, FieldImageCreateForm
from .models import Pole, PoleImage, Reservation
from django.views.generic.edit import FormView


from django.urls import reverse_lazy


class AboutPostView(ListView):
    model = Pole
    template_name = 'about.html'



class TeamPostView(ListView):
    model = Pole
    template_name = 'team.html'

    def get_queryset(self):
        return Pole.objects.exclude(status=False)


class NewsPostView(ListView):
    model = Pole
    template_name = 'news.html'


class BlogPostView(ListView):
    model = Pole
    template_name = 'blog.html'


class ContactPostView(ListView):
    model = Pole
    template_name = 'contact.html'


class PoleListView(ListView):
    model = Pole
    template_name = 'index.html'

    def get_queryset(self):
        return Pole.objects.exclude(status=False)



class ProfileView(ListView):
    model = Reservation
    template_name = 'profile.html'

    def get_queryset(self):
        return Reservation.objects.exclude(status=False)


class PoleDetailView(FormView, DetailView):
    model = Pole
    form_class = FieldImageCreateForm
    template_name = 'single-blog.html'

    def get_success_url(self):
        return reverse('pole_detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return form_invalid(form)

    def form_valid(self, form):
        poleimage = form.save(commit=False)
        poleimage.pole = self.get_object()
        poleimage.save()
        return super(PoleDetailView, self).form_valid(form)


class PoleUpdateView(LoginRequiredMixin, UpdateView):
    model = Pole
    fields = ('title', 'body',)
    template_name = 'pole_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PoleDeleteView(LoginRequiredMixin, DeleteView):
    model = Pole
    template_name = 'pole_delete.html'
    success_url = reverse_lazy('pole_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PoleCreateView(LoginRequiredMixin,CreateView):
    template_name = 'pole_new.html'
    form_class = FieldCreateForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# class PoleCreateImageView(LoginRequiredMixin, CreateView):
#     model = PoleImage
#     form_class = FieldImageCreateForm
#     template_name = 'pole_image.html'
#     success_url = reverse_lazy('pole_list')


def to_rezerv(request):
    table = Pole.objects.get(pk=1)
    print(request)
    if request.method == "POST":
        party = request.POST.get('hello')
        spot = request.POST.get('date')
        reserv = Reservation(table=table, party=party, spot=spot)
        reserv.save()
    return render(request, 'rezerv.html', {})



def index_detail(request, pk):
    what = Pole.objects.get(pk=pk)
    if request.method == "POST":
        party = request.POST.get('hello')
        spot = request.POST.get('date')
        reserv = Reservation(table=what, party=party, spot=spot)
        reserv.save()
    return render(request, 'single-blog.html', {'what': what})
