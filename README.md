# subwritle

This is a bad package that parses YouTube SRTs and turns them into a single readable file.

I made and use it to quickly search for content from press conferences and stuff like that in combination with [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Setup

Install `srt` with `pip`

```sh
pip install srt
```

## Usage

```sh
python3 -m subwritle 'file1.srt' 'file2.srt' 'file3.srt' -o 'output/'
```
