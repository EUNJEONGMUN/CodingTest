import sys
input = sys.stdin.readline


def parse_div(content):
    location_p = [idx for idx in range(0, len(
        content)-6) if content[idx:idx+3] == "<p>" or content[idx:idx+3] == "/p>"]
    print_title(content)
    for i in range(0, len(location_p), 2):
        print(parse_p(content[location_p[i]:location_p[i+1]+3]))


def print_title(content):
    title = ""
    for c in content[12:]:
        if c != '"':
            title += c
        else:
            break
    print("title :", title)


def parse_p(content):
    new = ""
    flag = False
    for c in content:
        if c == "<":
            flag = True
        elif c == ">":
            flag = False
        else:
            if flag:
                continue
            new += c
    return delete_space(new)


def delete_space(content):
    content = content.strip()
    content = ' '.join(content.split())
    return content


s = input().strip()
div_location = [idx for idx in range(6, len(s)-12) if s[idx:idx+11]
                == "<div title=" or s[idx:idx+6] == "</div>"]
for i in range(0, len(div_location), 2):
    parse_div(s[div_location[i]:div_location[i+1]+6])
