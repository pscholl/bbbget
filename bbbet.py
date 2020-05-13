#!/bin/python
#
# script to download bbb recordings to a local ..mkv file

import argparse, urllib.parse, subprocess

parser = argparse.ArgumentParser(description='downloads a public BigBlueButton recording to a local file')
parser.add_argument('url', type=urllib.parse.urlparse,
                    help='the url of the recording')
parser.add_argument('-o', '--output', type=str, default='output.mkv',
                    help='where to write the result too')
args = parser.parse_args()

try:
    meetingId = urllib.parse.parse_qs(args.url.query)['meetingId'][0]

    deskshare = f"{args.url.scheme}://{args.url.netloc}/presentation/{meetingId}/deskshare/deskshare.webm"
    webcams = f"{args.url.scheme}://{args.url.netloc}/presentation/{meetingId}/video/webcams.webm"
    slides = f"{args.url.scheme}://{args.url.netloc}/presentation/{meetingId}/slides_new.xml"

    cmd = f'ffmpeg -i {deskshare} -i {webcams} -c copy -map 0 -map 1 -f matroska -y'.split()
    cmd.append( args.output )
    subprocess.run(cmd)
except KeyError:
    print("url does not contain a meetingId")
