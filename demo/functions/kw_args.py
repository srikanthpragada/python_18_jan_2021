# Keyword arguments
def fun(**details):
    print(details)


def toofunny(*args, **kwargs):
    print(args)
    print(kwargs)

fun(a=10, b=20, c=30)
fun(x='abc', y='bbc')
# fun(10, 20)
toofunny(10,20, name = 'xyz', email  = False)

