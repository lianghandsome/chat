#讀取檔案
def read_file(filename):
    list = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            list.append(line.strip())
    return list

def convert(list):
    new = []
    person = None
    for line in list:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' +line)
    return new

#寫入檔案
def write_file(filename, list):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in list:
            f.write(i + '\n')

def main():
    list = read_file('input.txt')
    list = convert(list)
    write_file('output_2.txt', list)

main()