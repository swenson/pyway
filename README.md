# pyway

Dead simple database migrations using Python.

[Flyway](http://flywaydb.org/) is great, but it's seems a bit too heavy for
simple projects, especially non-JVM ones.

So I created `pyway`.

It's just a little `pyway.py` file, a few dozen lines long.
All it does is run a bunch of SQL files against your database if
it hasn't already, and it keeps track in a little table.

For now, it only supports `sqlite3`, but it would be trivial to
extend to any other SQL system that supports running SQL commands
via the command line.

You should be able to pretty easily modify it to suit your needs,
and it's liberally licensed so that you can feel free to.

## demo

```sh
python pyway.py test.db sample_migrations
```

## TODO

  * Postgres support
  * MySQL support
  * Add support for transactions around migrations?

## License

MIT:

```
The MIT License (MIT)

Copyright (c) 2014 Christopher Swenson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
