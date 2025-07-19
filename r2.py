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
    Allen_world_count = 0
    Allen_sticker_count = 0
    Allen_image_count = 0
    Viki_world_count = 0
    Viki_sticker_count = 0
    Viki_image_count = 0
    for line in list:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker_count += 1
            elif s[2] == '圖片':
                Allen_image_count +=1
            else:
                for msg in s[2:]:
                    Allen_world_count += len(msg) 
        elif name == 'Viki':
            if s[2] == '貼圖':
                Viki_sticker_count += 1
            elif s[2] == '圖片':
                Viki_image_count += 1
            else:
                for msg in s[2:]:
                    Viki_world_count += len(msg) 
    print('Allen的字數', Allen_world_count,'個字')
    print('Allen傳了', Allen_sticker_count, '個貼圖')
    print('Allen傳了', Allen_image_count, '個圖片')

    print('Viki的字數', Viki_world_count, '個字')
    print('Viki傳了', Viki_sticker_count, '個貼圖')
    print('Viki傳了', Viki_image_count, '個圖片')
    return new


#寫入檔案
def write_file(filename, list):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in list:
            f.write(i + '\n')


def main():
    list = read_file('LINE-Viki.txt')
    convert(list)


main()