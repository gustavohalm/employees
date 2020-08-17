from rest_framework import serializers


class EmployeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
