
def my_args(*args):
    print(args)
#print(my_args(3,5,10,20,100))
my_args(3,5,10,20,100)
print("############################")

def my_kwargs(**kwargs):
    print(kwargs)
#print(my_args(3,5,10,20,100))
my_args(3,5,10,20,100)
print("############################")
def my_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
my_args_kwargs()
