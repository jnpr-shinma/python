import gevent

MILLION = 1000 * 1000


def foo():
    for i in range(20 * MILLION):
        if not i % MILLION:
            # Yield to the Gevent hub.
            print gevent.getcurrent(), i
            gevent.sleep(0)


def bar():
    for i in range(10 * MILLION):
        if not i % MILLION:
            print gevent.getcurrent(), i
            gevent.sleep(0)


def launch():
    foo_greenlet = gevent.spawn(foo)
    bar_greenlet = gevent.spawn(bar)
    foo_greenlet.join()
    bar_greenlet.join()

if __name__ == '__main__':
    launch()