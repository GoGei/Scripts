import os
import sys
import json
from youtube_transcript_api import YouTubeTranscriptApi


CURRENT_DIR = os.getcwd()
JSON = 'json'
TEXT = 'txt'


def get_code() -> str:
    def get_from_query_params() -> str:
        try:
            youtube_domain, query_params = url.split('?')
            params = query_params.split('&')
            code = [param for param in params if 'v=' in param]
            if not code:
                raise ValueError('Code "v={code}" not found')
            elif len(code) != 1:
                raise ValueError('Code "v={code}" found multiple times')

            code = code[0].replace('v=', '')
            return code
        except ValueError:
            return None

    def get_by_last_slash() -> str:
        try:
            params = url.split('/')
            code = params[-1]
            return code
        except IndexError:
            return None

    try:
        url = sys.argv[1]
    except IndexError:
        raise ValueError('Provide URL')

    methods = [
        get_from_query_params,
        get_by_last_slash
    ]

    for method in methods:
        code = method()
        if code:
            return code

    raise ValueError('Code not found')


def write(transcript, file_format):
    filepath = f'{CURRENT_DIR}/transcriptions/transcript.{file_format}'

    with open(filepath, 'w+') as file:
        file.seek(0)
        file.truncate()

        if file_format == JSON:
            def apply_replacers(item):
                chars_to_replace = ('\\n', '\n', ' ' * 2)
                for char in chars_to_replace:
                    item = item.replace(char, ' ')

                return ' '.join(item.split())

            transcript = [apply_replacers(item['text']) for item in transcript]
            content = json.dumps(transcript, ensure_ascii=False)
        elif file_format == TEXT:
            content = '\n'.join([item['text'] for item in transcript])
        file.write(content)


if __name__ == '__main__':
    code = get_code()

    try:
        lang = sys.argv[2]
    except IndexError:
        lang = 'ru'

    transcript = YouTubeTranscriptApi.get_transcript(code, languages=[lang])
    # print(transcript)
    write(transcript, JSON)
    write(transcript, TEXT)
