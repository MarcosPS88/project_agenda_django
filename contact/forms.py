from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
                    widget=forms.TextInput(
                        attrs = {
                                    'placeholder': 'Digite o primeiro nome',
                                    
                                                      },
                    ),
                        label= 'Nome'
        )

    last_name = forms.CharField(
                    widget=forms.TextInput(
                        attrs = {
                                    'placeholder': 'Digite o sobrenome',
                                                      },
                    ),
                        label= 'Sobrenome',
                        help_text= 'Texto de ajuda'
        )
    phone = forms.CharField(
                    widget=forms.TextInput(
                        attrs = {
                                    'placeholder': 'Digite o telefone',
                        },
                    ),
                        label= 'Telefone'
        )
    
    email = forms.CharField(
                    widget=forms.TextInput(
                        attrs = {
                                        'placeholder': 'Digite o e-mail',
                                                      },
                    ),
                        label= 'E-mail'
        )
    
    description = forms.CharField(
        widget=forms.Textarea(
            attrs= {
                'placeholder': 'Digite uma descrição para o contato',
            }
        ),
        label = 'Descrição'
    )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        description = self.cleaned_data.get('description')
        category = self.cleaned_data.get('category')

        if first_name == last_name:
        
            msg =   ValidationError(
                    'Primeiro nome não pode ser igual ao sobrenome',
                    code='invalid'
                )
            
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        
        if len(description) < 5:
            msg = msg =   ValidationError(
                    'A descrição deve ter mais do que 5 caracteres',
                    code='invalid'
                )
            self.add_error('description', msg)

        if category is None:
            msg = msg =   ValidationError(
                    'Escolha uma categoria para o contato.',
                    code='invalid'
                )
            self.add_error('category', msg)

        print(self.cleaned_data)
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(field='first_name',
                           error= ValidationError(
                                'Primeiro nome não pode ser ABC',
                                code='invalid'
                             )
            )
        return first_name
    

    class Meta:
        model = Contact


        fields = ('first_name',
                  'last_name',
                  'phone', 
                  'email', 
                  'description', 
                  'category',
                  'picture'
        )    


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3
    )

    last_name = forms.CharField(
        required=True,
         min_length=3
    )

    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email',
                           ValidationError('Endereço de e-mail já cadastrado!',
                                           code='invalid'))
        return email