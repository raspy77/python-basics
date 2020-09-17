


s ="""
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""


indexbegin = 0
while True:
    indexbegin = s.find('<', indexbegin)
    if indexbegin == -1:
        break
    indexend = s.find('>')
    if indexend != -1:
        s = s[:indexbegin] + s[indexend + 1:]
    else:
        indexend += 1

print(s)