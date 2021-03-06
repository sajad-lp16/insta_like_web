from django.views import generic
from django.contrib.auth import login, get_user_model
from . import forms

User = get_user_model()


class RegisterView(generic.FormView):
    form_class    = forms.RegistrationForm
    template_name = 'register.html'
    success_url   = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(generic.FormView):
    form_class    = forms.LoginForm
    template_name = 'login.html'
    success_url   = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)


class ProfileUpdateView(generic.UpdateView):
    model         = User
    form_class    = forms.UpdateForm
    template_name = 'profile_update.html'
    success_url   = '/'

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailView(generic.DetailView):
    model               = User
    slug_field          = 'username'
    slug_url_kwarg      = 'username'
    context_object_name = 'user'
    template_name       = 'profile.html'

    def get_context_data(self, **kwargs):
        context                = super(ProfileDetailView, self).get_context_data(**kwargs)
        user                   = self.get_object()
        followers              = user.followers.all()
        context['posts_count'] = user.posts.count()
        context['followers']   = followers.count()
        context['followings']  = user.followings.count()
        context['is_followed'] = followers.filter(from_user=self.request.user, to_user=user).exists()
        return context
