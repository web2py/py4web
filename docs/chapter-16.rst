============================
Advanced topics and examples
============================



py4web and asyncio
------------------

py4web (as bottle) is thread-based, with high speed and efficient memory usage.
Asyncio is not strictly needed, at least for most of the normal use
cases where it will add problems more than value because of its concurrency model.
On the other hand, we think py4web needs a buil-in websocket async based solution.

If you plan to play with asyncio be careful that you should also deal with all
the framework's components: in particular pydal is not asyncio compliant because
not all the adapters work with async.

