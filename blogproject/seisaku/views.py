from django.views.generic import FormView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import BlogPost
from .forms import ContactForm

class IndexView(ListView):
    model = BlogPost
    template_name = 'seisaku/index.html'
    context_object_name = 'posts'
    ordering = ['-posted_at']
    paginate_by = 4

class AboutView(TemplateView):
    template_name = "seisaku/about.html"

class PostView(DetailView):
    model = BlogPost
    template_name = "seisaku/post.html"
    context_object_name = "post"

class ContactView(FormView):
    template_name = "seisaku/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('seisaku:contact')   # 送信後に同ページへリダイレクト

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['question_title']
        detail = form.cleaned_data['question_detail']

        subject = f'お問い合わせ：{title}'
        body = (
            f'送信者名：{name}\n'
            f'メールアドレス：{email}\n'
            f'タイトル：{title}\n'
            f'メッセージ：{detail}'
        )

        from_email = 'admin@example.com'    # settingsでDEFAULT_FROM_EMAILを使ってもOK
        to_list = ['admin@example.com']     # 宛先を必要に応じて設定

        EmailMessage(subject=subject, body=body, from_email=from_email, to=to_list).send()

        messages.success(self.request, 'お問い合わせは正常に送信されました')
        return super().form_valid(form)
