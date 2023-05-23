from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,password,**kwarg):
        email=self.normalize_email(email)
        user=self.model.create_user(email=email,**kwarg)
        user.set_password(password)
        user.save()
        return user


    def create_super_user(self,email,password,**kwarg):
        kwarg.setdefault('is_active',True)
        kwarg.setdefault('is_staff',False)
        kwarg.setdefault('is_superuser',True)

        if kwarg.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if kwarg.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email,password,**kwarg)