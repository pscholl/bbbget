#!/bin/python
#
# script to download bbb recordings to a local ..mkv file

import argparse, urllib.parse, subprocess, sys

parser = argparse.ArgumentParser(description='downloads a public BigBlueButton recording to a local file')
parser.add_argument('url', type=urllib.parse.urlparse,
                    help='the url of the recording')
parser.add_argument('-d', '--deskshare', action="store_true",
                    help='Download deskshare')
parser.add_argument('-w', '--webcams', action="store_true",
                    help='Download webcams')
parser.add_argument('-s', '--slides', action="store_true",
                    help='Download slides')
parser.add_argument('-o', '--output', type=str, default='output.webm',
                    help='where to write the result too')
args = parser.parse_args()

try:
    meetingId = urllib.parse.parse_qs(args.url.query)['meetingId'][0]

    inputs = {}
    if args.deskshare:
        deskshare = f"{args.url.scheme}://{args.url.netloc}/presentation/{meetingId}/deskshare/deskshare.webm"
        inputs["deskshare"] = deskshare

    if args.webcams:
        webcams = f"{args.url.scheme}://{args.url.netloc}/presentation/{meetingId}/video/webcams.webm"
        inputs["webcams"] = webcams

    if args.slides:
        slides = f"{args.url.scheme}://{args.url.netloc}/presentation/{meetingId}/slides_new.xml"
        inputs["slides"] = slides

    if len(inputs.keys()) < 1: 
        sys.exit("Specify at least one input")

    cmd = f'ffmpeg'

    for inp in inputs.keys():
        cmd += f' -i {inputs[inp]}'

    cmd += f' -c copy '

    for i in range(len(inputs.keys())):
        cmd += f'-map {i}'

    cmd += f' -y'
    cmd = cmd.split()
    cmd.append( args.output )
    subprocess.run(cmd)

except KeyError:
    print("url does not contain a meetingId")
