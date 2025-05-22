from ..serializers import RegisterSerializer, UserSerializer, EmailTokenObtainPairSerializer, ProfileSerializer
# from ..models import Profile
# from ..permissions import IsSuperuser
# from rest_framework import permissions
# from rest_framework.authtoken.models import Token
# from rest_framework import generics
from rest_framework.decorators import action
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()




class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get', 'patch'], url_path='me')
    def me(self, request):
        user = request.user

        try:

            if request.method == 'GET':
                serializer = UserSerializer(user)
                return Response(serializer.data)

            elif request.method == 'PATCH':
                serializer = UserSerializer(user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except get_user_model().DoesNotExist:
            return Response({"detail":"Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomEmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


# def send_email_welcome(request, user):

#     print("######### SendEmailWelcome #########")

#     user = User.objects.get(username=user)
    
#     message = render_to_string("emails/welcome/welcome.html", {'user': user.username})
    
#     text_content = strip_tags(message)
#     mail_subject = 'Bem-vindo(a) à Freelaworks'
#     email = EmailMultiAlternatives(mail_subject, text_content, settings.EMAIL_HOST_USER, [user.email])
#     email.attach_alternative(content=message, mimetype='text/html')
#     if email.send():
#         messages.success(request, f'Bem vindo(a), {str(user)}')
#     else:
#         messages.error(
#             request, f'Problema ao enviar e-mail para {user.email}, verifique se você digitou corretamente.')

# def activate_account(request, uidb64, token):

#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except Exception:
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         send_email_welcome(request, user)
#         messages.success(request, "Obrigado(a) pela confirmação do seu e-mail. Agora você pode fazer login na sua conta.")

#         return redirect('login')

#     else:
#         messages.error(request, "O link de ativação é inválido!")

#     return redirect('login')

# def activateEmail(request, user, to_email):
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
