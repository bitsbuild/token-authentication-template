from rest_framework.serializers import ModelSerializer,CharField
from django.contrib.auth.models import User
class UserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    class Meta:
        model = User
        fields = [
                    'username',
                    'email',
                    'password',
                    'confirm_password'
                 ]
        extra_kwargs = {
            'password': {
                'write_only':True
                        }
        }
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
