from .models import *
from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = "__all__"

    id = serializers.IntegerField(read_only = True)
    telegram = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.telegram = validated_data.get('telegram', instance.telegram)
        instance.save()
        return instance

class RecordSerializer(serializers.Serializer):
    class Meta:
        model = Record
        fields = "__all__"

    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    text = serializers.CharField()
    user = serializers.IntegerField(source='user.id')

    def create(self, validated_data):
        user_tb = User.objects.get(id=validated_data.get('user').get('id'))
        validated_data.pop('user')
        instance = Record.objects.create(user=user_tb, **validated_data)
        return instance

    def update(self, instance, validated_data):
        if self.data.get('user') == validated_data.get('user').get('id'):
            instance.title = validated_data.get('title', instance.title)
            instance.text = validated_data.get('text', instance.text)
            instance.save()
            return instance
        else:
            return self.data

class DateSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only = True)
    record = serializers.IntegerField(source='record.id')
    timer = serializers.DateField()

    class Meta:
        model = Date
        fields = "__all__"

    def create(self, validated_data):
        rec_id = Record.objects.get(id=validated_data.get('record').get('id'))
        validated_data.pop('record')
        instance = Date.objects.create(record=rec_id, **validated_data)
        return instance

    def update(self, instance, validated_data):
        rec_id = Record.objects.get(id=validated_data.get('record').get('id'))
        instance.record = rec_id
        instance.timer = validated_data.get('timer', instance.timer)
        instance.save()
        return instance
'''
class RecordSerializer2(serializers.Serializer):
    class Meta:
        model = Record
        fields = "__all__"

    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    text = serializers.CharField()
    user = serializers.CharField()

    def create(self, validated_data):
        user_tb = User.objects.get(id=validated_data.get('user'))
        validated_data.pop('user')
        instance = Record.objects.create(user=user_tb, **validated_data)
        return instance

    def update(self, instance, validated_data):
        user_tb = User.objects.get(id=validated_data.get('user'))
        validated_data.pop('user')
        instance.title = validated_data.get('title')
        instance.text = validated_data.get('text')
        instance.user = user_tb
        instance.save()
        return instance

class DateSerializer2(serializers.Serializer):

    id = serializers.IntegerField(read_only = True)
    record = serializers.CharField()
    timer = serializers.DateField()

    class Meta:
        model = Date
        fields = "__all__"
        depth = 0

    def create(self, validated_data):
        record_tb = Record.objects.get(id=validated_data.get('record'))
        validated_data.pop('record')
        instance = Date.objects.create(record=record_tb, **validated_data)
        return instance

    def update(self, instance, validated_data):
        record_tb = Record.objects.get(id=validated_data.get('record'))
        validated_data.pop('record')
        instance.record = record_tb
        instance.timer = validated_data.get('timer')
        instance.save()
        return instance'''