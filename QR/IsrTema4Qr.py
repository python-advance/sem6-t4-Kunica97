import pyqrcode
import random

r = lambda: random.randint(0,255)

print('Введите текст или вставьте ссылку:')
text = input()
url = pyqrcode.create(str(text))
url.svg('qr.svg', scale=2, background='#%02X%02X%02X' % (r(),r(),r()), module_color='#%02X%02X%02X' % (r(),r(),r()))
print(url.terminal(quiet_zone=1))