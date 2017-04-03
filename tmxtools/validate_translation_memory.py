
import os
import xml.etree.ElementTree as ElementTree
HEAD = 0
BODY = 1


def is_tmx_valid(filepath):
    return filepath_exists(filepath)  and has_header_and_body(filepath) and only_contains_tu_elements(filepath)


def filepath_exists(filepath):
    return os.path.exists(filepath)


def has_header_and_body(filepath):
    """
    Does this tmx file only contain a <header> and <body> tag?

    :param filepath: path to TMX file
    :return: True iff root of file only has a <header> and <body> tag
    """
    tree = ElementTree.parse(filepath)
    root = tree.getroot()
    if len(root) != 2:
        return False
    if root[HEAD].tag != 'header':
        return False
    if root[BODY].tag != 'body':
        return False
    return True


def only_contains_tu_elements(filepath):
    """
    Does the <body> of a file only contain <tu> elements?
    :param filepath: path to TMX file
    :return: True iff <body> tag only contains <tu> elements
    """

    tree = ElementTree.parse(filepath)
    root = tree.getroot()
    for element in root[BODY]:
        if element.tag != 'tu':
            return False
    return True

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("tmxfile", help="path to tmxfile you want to know is valid or not")
    args = parser.parse_args()

    print("%s is valid: %s" % (args.tmxfile, is_tmx_valid(args.tmxfile)))

