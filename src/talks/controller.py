from .models import Talk


def create_talk(data):
    talk = Talk(**data)
    talk.save()
