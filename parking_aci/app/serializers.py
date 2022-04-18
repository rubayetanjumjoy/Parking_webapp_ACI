from rest_framework import serializers

from .models import *
from common.serializers import CustomSerializer
from .models import Entry
from .models import Exit
from .models import History

class EntrySerializer(CustomSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class RegiSerializer(CustomSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class ExitSerializer(CustomSerializer):
    class Meta:
        model = Exit
        fields = '__all__'

class HistroySerializer(CustomSerializer):
    class Meta:
        model = History
        fields = '__all__'

