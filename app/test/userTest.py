import os
from django.utils.six import BytesIO

os.environ.update({"DJANGO_SETTINGS_MODULE": "GoogleAuthenticatorBackEnd.settings"})

import django
django.setup()

from app.models import User
from app.serializer.UserSerializer import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

user = User(userName="aa", password="aa")
# user.save()

serializer = UserSerializer(user)
print(serializer.data)

content = JSONRenderer().render(serializer.data)
stream = BytesIO(content)
data = JSONParser().parse(stream)