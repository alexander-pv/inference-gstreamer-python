
import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='GStreamer samples argument parser')
    parser.add_argument('-ip', metavar='ip', type=str, default='127.0.0.1', help='str, rtsp ip address')
    parser.add_argument('-port', metavar='port', type=int, default=8554, help='int, rtsp port')
    parser.add_argument('-name', metavar='name', type=str, default='stream', help='str, rtsp address name')
    parser.add_argument('-codec', metavar='codec', type=str, default='h264', help='str, video codec')
    parser.add_argument('-debug_level', metavar='debug_level', type=int, default=0, help='str, GStreamer debug level')
    parser.add_argument('-d', action='store_true', help='bool, display pipeline output')
    return parser.parse_args()
