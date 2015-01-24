---
layout: post
title: "Python Encoding"
date: 2015-01-21 07:30
---

## Python Source File Encoding ##

```python
#!/usr/bin/env python

u = unicode('中国', 'utf-8')
```

Without specify source file encoding on the top of source file:

	$ python without-magic-comment.py
	  File "without-magic-comment.py", line 3
	  SyntaxError: Non-ASCII character '\xe2' in file without-magic-comment.py on line 5, but no encoding declared;
	  see http://www.python.org/peps/pep-0263.html for details

Because there are `non-ascii` characters in the source file, Python parser can't interpret the source code.

The error message metioned [PEP-0263](https://www.python.org/dev/peps/pep-0263/):

> This PEP proposes to introduce a syntax to declare the encoding of a Python source file. The encoding information     is then used by the Python parser to interpret the file using the given encoding.

<!-- -->

> Python will default to ASCII as standard encoding if no other encoding hints are given.

Place magic comment into the source at the top:

```python
# coding=<encoding name>
```

or:

```python
# -*- coding: <encoding name> -*-
```

or:

```python
# vim: set fileencoding=<encoding name>
```

I usual use:

```python
# -*- coding: utf-8 -*-
```

Example:

First use `iconv` to convert the source file encoding to gb2312:

	iconv -f utf-8 -t gb2312 magic_comment.py > magic_comment_gb2312.py

The source code:

	#!/usr/bin/env python
	# -*- coding: gb2312 -*-

	import chardet
	from pprint import pprint
	s = '中国'

	pprint(s)
	print chardet.detect(s)

	pprint(s.decode('gb2312'))

Output:

	$ python magic_comment_gb2312.py
	'\xd6\xd0\xb9\xfa'
	{'confidence': 0.7679697235616183, 'encoding': 'IBM855'}
	u'\u4e2d\u56fd'

---

## `unicode_literals` in `__future__` ##

[`unicode_literals`](https://docs.python.org/2/library/__future__.html) add in Python 2.6, I usual add this for uniform encoding environment and compatibility

The default string type is `str` in Python 2.x, after `from __future__ import unicode_literals`, the string type is unicode.

First, the common mode without `unicode_literals`:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint

s = ['abc', u'abc', '中国', u'中国']

for i in s:
        print(i, end=': ')
        pprint(type(i))
        print('')

print('------- decode:')
for i in s:
        try:
                print(i, end=': ')
                pprint(type(i.decode('utf-8')))
        except Exception as e:
                print(">>> error: " + str(e))
        finally:
                print('')

print('------- encode:')
for i in s:
        try:
                print(i, end=': ')
                pprint(type(i.encode('utf-8')))
        except Exception as e:
                print(">>> error: " + str(e))
        finally:
                print('')
```

Output:

	abc: <type 'str'>

	abc: <type 'unicode'>

	中国: <type 'str'>

	中国: <type 'unicode'>

	------- decode:
	abc: <type 'unicode'>


	abc: <type 'unicode'>

	中国: <type 'unicode'>

	中国: >>> error: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

	------- encode:
	abc: <type 'str'>

	abc: <type 'str'>

	中国: >>> error: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)

	中国: <type 'str'>

If add `unicode_literals`:

	abc: <type 'unicode'>

	abc: <type 'unicode'>

	中国: <type 'unicode'>

	中国: <type 'unicode'>

	------- decode:
	abc: <type 'unicode'>

	abc: <type 'unicode'>

	中国: >>> error: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

	中国: >>> error: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

	------- encode:
	abc: <type 'str'>

	abc: <type 'str'>

	中国: <type 'str'>

	中国: <type 'str'>


Use `unicode_literals`, all the string variable is unicode.

Other discuss:

* [Any gotchas using unicode_literals in Python 2.6?](http://stackoverflow.com/questions/809796/any-gotchas-using-u    nicode-literals-in-python-2-6)
* [Should I import unicode_literals?](http://python-future.org/unicode_literals.html)

