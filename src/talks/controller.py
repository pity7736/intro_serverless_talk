from .models import Talk


def create_talk(data):
    talk = Talk(**data)
    talk.save()


def get_talks():
    talks = Talk.scan()
    result = []
    for talk in talks:
        result.append(talk.get_json_serializable())
    return result
