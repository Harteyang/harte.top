---
layout: post
title: "Python Relative and Absolute Import"
date: 2013-10-07 16:54
comments: true
categories: Python
---

The [PEP 328: Absolute and Relative Imports](http://docs.python.org/2/whatsnew/2.5.html#pep-328-absolute-and-relative-imports) explans very detailed.

The `absolute_import` feature is default in `Python 3.x`. (I use `Python 2.7.x`)

<!-- more -->

Use the examples pep328 gives:

	pkg
	├── __init__.py
	├── main.py
	└── string.py

The content of string.py

```python
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	def say_hello():
		print "say hello"
```

The content of first version main.py:

```python
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	import string

	string.say_hello()
```

This will use the relative string.py module, not the Python's standard string module.

When use `absolute_import`:

From pep328:

> Once absolute imports are the default, `import string` will always find the standard library’s version.
> It’s **suggested** that users should begin using absolute imports as much as possible, so it’s preferable to begin writing `from pkg import string` in your code.

```python
	from __future__ import absolute_import

	#import string   # This is error because `import string` will use the standard string module
	from pkg import string
	string.say_hello()
```

> Relative imports are still possible by adding **a leading period** to the module name when using the `from ... import` form:

```python
	from __future__ import absolute_import

	from . import string # This is the same as `from pkg import string`
	string.say_hello()
```

or

```python
	from __future__ import absolute_import

	from .string import say_hello
	say_hello()
```

Execute code:

	# move to the parent dir of pkg
	$ python -m pkg.main
	say hello
