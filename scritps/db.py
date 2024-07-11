import uuid
import ujson
import scritps.settings as settings

def create_resume(**kwargs) -> str:
    id_ = str(uuid.uuid4())
    _write(id_, **kwargs)
    print(id_)
    return id_

def _write(id_: str, **kwargs) -> None:
    with open(f'{settings.BASE_DB_FOLDER}/asdf.json', 'w') as file:
        file.write(ujson.dumps(kwargs))

