from string import Template  # For Template Strings

# String formatting
name = 'Jiwook'
print('Hello, {}'.format(name))  # 'Hello, Jiwook'

# You can refer to your variable substitutions by name
# and use them in any order
errno = 1
print('Hey {name}, there is a 0x{errno:x} error!'.format(
    name=name, errno=errno))  # 'Hey Jiwook, there is a 0x1 error!'

# String Interpolation / f-Strings (Python 3.6+) [Preferred]
a = 5
b = 10
# 'Five plus ten is 15 and not 30.'
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')

print(f"Hey {name}, there's a {errno:#x} error!")
# "Hey Jiwook, there's a 0x1error!"

# Template Strings(Standard Library) [Preferred when the variable is user provided]
t = Template('Hey, $name!')
print(t.substitute(name=name))  # 'Hey, Jiwook!'

templ_string = 'Hey $name, there is a $error error!'
print(Template(templ_string).substitute(name=name, error=hex(errno)))
# 'Hey Jiwook, there is a 0x1 error!'
