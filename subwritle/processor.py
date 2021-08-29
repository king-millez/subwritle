import srt
from typing import List


def parse(filepath: str) -> List:
    def clear_text(text: str) -> str:
        return text.strip().replace('\n', ' ').strip()

    with open(filepath, 'r') as f:
        sub_data = list(srt.parse(f.read()))
        no_dupes = []
        for index, subtitle in enumerate(sub_data):
            text = clear_text(subtitle.content)
            try:
                if text in clear_text(sub_data[index + 1].content):
                    if text not in no_dupes:
                        no_dupes.append(text)
            except IndexError:
                if text not in no_dupes:
                    no_dupes.append(text)

    final_text = ''
    for text_fragment in no_dupes:
        final_text += text_fragment + ' '

    return final_text
