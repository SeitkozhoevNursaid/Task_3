from rest_framework import serializers
from music.models import Genre, Music, MusicImg
from music.tasks import music_created


class GenreSerializer(serializers.Serializer):  # ModelSerializer vs Serializer
    id = serializers.SlugField(read_only=True)
    name = serializers.CharField()

    def create(self,validated_data):
        serializer = Genre(**validated_data)
        serializer.save()
        return serializer

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class MusicImgSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicImg
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    images = MusicImgSerializer(many=True, read_only=True)

    class Meta:
        model = Music
        fields = '__all__'

    def create(self, validated_data):
        new_music = Music.objects.create(**validated_data)
        request = self.context.get('request')
        files = request.FILES
        image_objects = []
        for file in files.getlist('images'):
            image_objects.append(MusicImg(music=new_music, images=file))
        MusicImg.objects.bulk_create(image_objects)
        music_created.delay(new_music.id, new_music.name)
        return new_music
