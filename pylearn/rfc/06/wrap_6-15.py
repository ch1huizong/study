
def wrap(func):
    def call(*args, **kwargs):
        return func(*args, **kwargs)
    call.__doc__ == func.__doc__
    call.__name__ == func.__name__
    call.__dict__.update(func.__dict__)
    return call
