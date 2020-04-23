import string
from random import choice
def translate(string):
    dictionary = {'-':'-','а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'cz','ш':'sh','щ':'scz','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ja'}
    out = ''
    for l in string:
        out += dictionary.get(l, l)
    return out

def get_random_string(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(choice(chars) for _ in range(size))