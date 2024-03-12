# Variable scope in Python
# Local Scope
# Global Scope
# Global Keyword
# LEGB rule: local -> Enclosing -> Global -> Built-in
# local & Global
x = 100
def var_global():
    print(x)
    def var_scope_demo():
        x = 20
        print(x)
        def var_scope_demo1():
            x = 50
            print(x)
            def grand_child():
                x = 70
                print(x)
            grand_child()
        var_scope_demo1()
    var_scope_demo() 

var_global()