def p_decorate(func):
   def func_wrapper(name, age):
       return "<p>{0}</p>".format(func(name, age))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name, age):
        return "<strong>{0}</strong>".format(func(name, age))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name, age):
        return "<div>{0}</div>".format(func(name, age))
    return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def get_text(name, age):
   return "lorem ipsum, {0} dolor sit amet {1} . ".format(name, age)

print(get_text("Orest", "23"))
