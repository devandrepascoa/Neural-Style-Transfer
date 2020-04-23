import argparse
import Style_Network as NST
import os
import sys

def build_parser():
    argparser = argparse.ArgumentParser(prog="style_transfer",
                                        description="Transfer style to videos or images")


    return argparser

def main():
    parser = build_parser()
    opts = parser.parse_args()
    NST.NST_Video("Uploads/small.mp4","Downloads/result.mp4", "Uploads/style_img.jpg")


if __name__ == '__main__':
    main()