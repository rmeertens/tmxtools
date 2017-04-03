import xml.etree.ElementTree as ElementTree
TMX_INDEX_HEAD = 0
TMX_INDEX_BODY = 1

def get_input_output(tmxpath):
    tree = ElementTree.parse(tmxpath)
    root = tree.getroot()
    for tu in root[TMX_INDEX_BODY].findall('tu'):
        values = []
        for index, translation_value in enumerate(tu.findall('tuv')):
            segment = translation_value.find('seg')
            values.append(content(segment))
        if len(values) == 2:
            if values[0] and values[1]:
                yield values[0],values[1]

def content(tag,encoding='utf-8'):
    ending = ''.join(ElementTree.tostring(e).decode(encoding) for e in tag)
    if tag.text:
        return tag.text + ending
    return ending

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("tmxfile", help="the tmx file you want to split")
    parser.add_argument("--outputsource", default="tmxsource.in", help="the file to which to write the src sentences")
    parser.add_argument("--outputtarget", default='tmxtarget.out', help="the file to which to write the target sentences")
    args = parser.parse_args()

    with open(args.outputsource,'w') as sourcefile:
        with open(args.outputtarget,'w') as targetfile:
            for input, output in get_input_output(args.tmxfile):
                sourcefile.write(input.encode('utf-8') + "\n")
                targetfile.write(output.encode('utf-8')+ "\n")