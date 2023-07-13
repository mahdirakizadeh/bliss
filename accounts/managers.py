from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, full_name, password):
        if not email:
            raise ValueError("you must enter an email")
        if not phone_number:
            raise ValueError("you must enter a phone number")
        if not full_name:
            raise ValueError("you must enter a full name")

        user = self.model(email=self.normalize_email(email), phone_number=phone_number, full_name=full_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, phone_number, full_name, password):
        user = self.create_user(email, phone_number, full_name, password)
        user.is_admin = True
        user.save(using=self.db)
        return user
