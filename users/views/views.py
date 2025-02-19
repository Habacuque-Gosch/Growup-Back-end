from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib import auth, messages
from ..serializers import UserRegistrationSerializer, GetUserByToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics


# from apps.usuarios.forms import ChangePassForms, ForgetMyPassForms, SendCodeForms
# from django.core.mail import EmailMultiAlternatives
# from ..tokens import account_activation_token
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.utils.html import strip_tags
# from apps.usuarios.models import Profile
# from apps.vagas.models import Job 
# from django.core.mail import send_mail
# from django.conf import settings


# def home(request):
#     ''' Realiza o login do usuario na aplicação '''

#     user = request.user

#     # if user.is_authenticated:
#         # return redirect('index_jobs')

# def login_user(request):
#     ''' Realiza o login do usuario na aplicação '''

#     user = request.user

#     if user.is_authenticated:
#         return redirect('index_jobs')
    
#     form = LoginForms()
#     if request.method == 'POST':
#         form = LoginForms(request.POST)

#         if form.is_valid():
#             nome = form["nome_login"].value()
#             senha = form["senha_login"].value()

#             try:

#                 user_active = User.objects.get(username=nome)

#                 if user_active.is_active:

#                     usuario = auth.authenticate(
#                         request,
#                         username=nome,
#                         password=senha
#                     )
#                     if usuario is not None:
#                         auth.login(request, usuario)
#                         return redirect('index_jobs')
#                     else:
#                         messages.error(request, "usuário ou senha incorreto")
#                         return redirect('login')
                
#                 messages.error(request, "Conta desativada, entre em contato com o suporte: @habacuke14@gmail.com")
#                 return redirect('login')
        
#             except:
#                 messages.error(request, "usuário ou senha incorreto")
#                 return redirect('login')


#     return render(request, 'usuarios/login/login.html', {"form": form})

# # def send_email_welcome(request, user):

# #     print("######### SendEmailWelcome #########")

# #     user = User.objects.get(username=user)
    
# #     message = render_to_string("emails/welcome/welcome.html", {'user': user.username})
    
# #     text_content = strip_tags(message)
# #     mail_subject = 'Bem-vindo(a) à Freelaworks'
# #     email = EmailMultiAlternatives(mail_subject, text_content, settings.EMAIL_HOST_USER, [user.email])
# #     email.attach_alternative(content=message, mimetype='text/html')
# #     if email.send():
# #         messages.success(request, f'Bem vindo(a), {str(user)}')
# #     else:
# #         messages.error(
# #             request, f'Problema ao enviar e-mail para {user.email}, verifique se você digitou corretamente.')

# # def activate_account(request, uidb64, token):

# #     try:
# #         uid = force_str(urlsafe_base64_decode(uidb64))
# #         user = User.objects.get(pk=uid)
# #     except Exception:
# #         user = None

# #     if user is not None and account_activation_token.check_token(user, token):
# #         user.is_active = True
# #         user.save()
# #         send_email_welcome(request, user)
# #         messages.success(request, "Obrigado(a) pela confirmação do seu e-mail. Agora você pode fazer login na sua conta.")

# #         return redirect('login')

# #     else:
# #         messages.error(request, "O link de ativação é inválido!")

# #     return redirect('login')

# # def activateEmail(request, user, to_email):
#     mail_subject = "Confirmação de cadastro"

#     print("######### activateEmail #########")

#     message = render_to_string("emails/active_account/active_account.html", {
#         'user': user,
#         'domain': get_current_site(request).domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': account_activation_token.make_token(user),
#         "protocol": 'https' if request.is_secure() else 'http'
#     })
#     text_content = strip_tags(message)
#     email = EmailMultiAlternatives(mail_subject, text_content, settings.EMAIL_HOST_USER, [to_email])
#     email.attach_alternative(content=message, mimetype='text/html')
#     if email.send():
#         messages.success(request, f'Olá, {user}, acesse sua caixa de entrada de e-mail {to_email} e clique em \
#         link de ativação recebido para confirmar e concluir o registro. Observação: Verifique sua pasta de spam.')
#     else:
#         messages.error(
#             request, f'Problema ao enviar e-mail para {to_email}, verifique se você digitou corretamente.')

@api_view(["POST"])
def register_user(request):
    ''' Realiza o cadastro de um novo usuario no sistema '''

    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.create_user(validate_data=request.data)
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = GetUserByToken
    
    def get_queryset(self):
        # token = self.request.headers.get('key')
        token = self.kwargs.get('token')
        if token:
            # self.lookup_field = 'key'
            user_token = Token.objects.get(key=token)
            print('USER', user_token.user.id)
            user = self.queryset.filter(id=user_token.user.id)
            print('DATA', user.values())
            # print('USER', user.username)
            return user

        # return self.queryset.all()

    # form = CadastroForms()
    # if request.method == 'POST':
    #     form = CadastroForms(request.POST)
        
    #     if form.is_valid():
    #         if form["senha_cadastro"].value() != form["senha_confirma"].value():
    #             messages.error(request, "senhas não são iguais")
    #             return redirect('cadastro')

    #         nome = form["nome_cadastro"].value()
    #         email = form["email"].value()
    #         senha = form["senha_cadastro"].value()

    #         if nome:
    #             if ' ' in nome:
    #                 messages.error(request, 'O nome de usuário não pode conter espaços em branco')
    #                 return redirect('cadastro')

    #     if  User.objects.filter(username=nome).exists() or User.objects.filter(email=email).exists():
    #         messages.error(request, "Usuário já existente")
    #         return redirect('cadastro')
        
    #     usuario =  User.objects.create_user(
    #         username=nome,
    #         email=email,
    #         password=senha
    #     )

    #     usuario.is_active = False
    #     usuario.save()

        # activateEmail(request, usuario, email)
        # return redirect('login')

    # return render(request, 'usuarios/register/register.html', {"form": form})



# @login_required(login_url='login')
# def desactivate_account(request):

#     current_user = request.user

#     user_desactive = User.objects.get(user=current_user.id)

#     user_desactive.is_active = False

#     user_desactive.save()

#     return redirect('/')

@login_required(login_url='login')
def logout(request):
    ''' Realiza o logout do usuario na aplicação '''
    # messages.success(request, "Logout efetuado com sucesso")
    auth.logout(request)
    return redirect('login')

# @login_required(login_url='login')
# def change_pass(request):
#     ''' Realiza a troca de senha do usuario no sistema '''

#     current_user = request.user

#     form = ChangePassForms()
    
#     if request.method == 'POST':
#         form = ChangePassForms(request.POST)
        
#         if form.is_valid():
#             if form["senha_nova"].value() != form["senha_nova_confirma"].value():
#                 messages.error(request, "senhas não são iguais")
#                 return redirect('change_pass')

#             senha_atual = form["senha_atual"].value()
            
#             check_senha = current_user.check_password(senha_atual)

#             if check_senha == True:
#                 senha_nova = form["senha_nova"].value()

#                 usuario = User.objects.get(username=current_user)
#                 usuario.set_password(senha_nova)
#                 usuario.save()
#                 return redirect('/')

#             else:
#                 return redirect('change_pass')
            
#     context = {
#         'title':'Trocar senha',
#         "form": form
#     }

#     return render(request, 'usuarios/settings/change_pass/change_pass.html', context)
