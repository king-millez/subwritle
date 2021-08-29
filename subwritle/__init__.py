import os
import sys
import argparse


from . import processor


def main():
    USAGE_MSG = 'subwritle <Subtitle Files> -o <Output Directory>'
    parser = argparse.ArgumentParser(
        description='Easily turn subtitle files into readable text files.',
        usage=USAGE_MSG
    )
    parser.add_argument('-o', dest='output_dir', type=str,
                        help='Output directory for downloaded content.')
    args, unknown = parser.parse_known_args()

    if(not args.output_dir):
        print('Output directory (-o) is required.')
        sys.exit(USAGE_MSG)
    elif(args.output_dir[-1] == '"' or args.output_dir[-1] == "'"):
        args.output_dir = f'{args.output_dir[:-1]}/'
    elif(args.output_dir[-1] != '/' and args.output_dir[-1] != '\\'):
        args.output_dir += '/'

    if(not os.path.isdir(args.output_dir)):
        try:
            os.mkdir(args.output_dir)
        except Exception:
            sys.exit(f'Could not create directory "{args.output_dir}"')

    if len(unknown) > 0:
        no_dupes = []
        for filepath in unknown:
            if os.path.isfile(filepath):
                if os.path.splitext(filepath)[-1].lower() == '.srt':
                    if filepath not in no_dupes:
                        no_dupes.append(filepath)
                else:
                    sys.exit(
                        'The file provided is not an SRT file.\n' + USAGE_MSG)
            else:
                sys.exit(f'{filepath} is not a file path.\n{USAGE_MSG}')
        if len(no_dupes) > 0:
            for filepath in no_dupes:
                with open(os.path.join(
                    args.output_dir,
                    filepath.replace('.srt', '.txt')
                ), 'w') as f:
                    f.write(processor.parse(filepath))
    else:
        sys.exit('Please provide at least 1 file.\n' + USAGE_MSG)
