from django.contrib.auth import get_user_model

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        """specify the fields that you want to include"""
        """in serializer.These are fields that are going to"""
        """be converted to and from jason when we do HTTP post"""
        """and then we retrieve that in our view and then we want to"""
        """save it to a model"""
        """these are the fields accessible to the API  to read or right"""
        fields = ('email', 'password', 'name')
        """extra restrictions for the fields"""
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)




