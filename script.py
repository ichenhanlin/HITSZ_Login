__all__ = ['script']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['s', 'xEncode', 'json', 'l'])
@Js
def PyJsHoisted_json_(d, this, arguments, var=var):
    var = Scope({'d':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['d'])
    return var.get('JSON').callprop('stringify', var.get('d'))
PyJsHoisted_json_.func_name = 'json'
var.put('json', PyJsHoisted_json_)
@Js
def PyJsHoisted_xEncode_(str, key, this, arguments, var=var):
    var = Scope({'str':str, 'key':key, 'this':this, 'arguments':arguments}, var)
    var.registers(['z', 'str', 'd', 'q', 'y', 'c', 'p', 'k', 'e', 'key', 'v', 'm', 'n'])
    if (var.get('str')==Js('')):
        return Js('')
    var.put('v', var.get('s')(var.get('str'), Js(True)))
    var.put('k', var.get('s')(var.get('key'), Js(False)))
    if (var.get('k').get('length')<Js(4.0)):
        var.get('k').put('length', Js(4.0))
    var.put('n', (var.get('v').get('length')-Js(1.0)))
    var.put('z', var.get('v').get(var.get('n')))
    var.put('y', var.get('v').get('0'))
    var.put('c', (Js(2248228889)|Js(406206880)))
    var.put('q', var.get('Math').callprop('floor', (Js(6.0)+(Js(52.0)/(var.get('n')+Js(1.0))))))
    var.put('d', Js(0.0))
    while (Js(0.0)<(var.put('q',Js(var.get('q').to_number())-Js(1))+Js(1))):
        var.put('d', ((var.get('d')+var.get('c'))&(Js(2363546047)|Js(1931421248))))
        var.put('e', (PyJsBshift(var.get('d'),Js(2.0))&Js(3.0)))
        #for JS loop
        var.put('p', Js(0.0))
        while (var.get('p')<var.get('n')):
            try:
                var.put('y', var.get('v').get((var.get('p')+Js(1.0))))
                var.put('m', (PyJsBshift(var.get('z'),Js(5.0))^(var.get('y')<<Js(2.0))))
                var.put('m', ((PyJsBshift(var.get('y'),Js(3.0))^(var.get('z')<<Js(4.0)))^(var.get('d')^var.get('y'))), '+')
                var.put('m', (var.get('k').get(((var.get('p')&Js(3.0))^var.get('e')))^var.get('z')), '+')
                var.put('z', var.get('v').put(var.get('p'), ((var.get('v').get(var.get('p'))+var.get('m'))&(Js(4021866800)|Js(273100495)))))
            finally:
                    (var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1))
        var.put('y', var.get('v').get('0'))
        var.put('m', (PyJsBshift(var.get('z'),Js(5.0))^(var.get('y')<<Js(2.0))))
        var.put('m', ((PyJsBshift(var.get('y'),Js(3.0))^(var.get('z')<<Js(4.0)))^(var.get('d')^var.get('y'))), '+')
        var.put('m', (var.get('k').get(((var.get('p')&Js(3.0))^var.get('e')))^var.get('z')), '+')
        var.put('z', var.get('v').put(var.get('n'), ((var.get('v').get(var.get('n'))+var.get('m'))&(Js(3141076802)|Js(1153890493)))))
    return var.get('l')(var.get('v'), Js(False))
PyJsHoisted_xEncode_.func_name = 'xEncode'
var.put('xEncode', PyJsHoisted_xEncode_)
@Js
def PyJsHoisted_l_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'c', 'b', 'i', 'd', 'm'])
    var.put('d', var.get('a').get('length'))
    var.put('c', ((var.get('d')-Js(1.0))<<Js(2.0)))
    if var.get('b'):
        var.put('m', var.get('a').get((var.get('d')-Js(1.0))))
        if ((var.get('m')<(var.get('c')-Js(3.0))) or (var.get('m')>var.get('c'))):
            return var.get(u"null")
        var.put('c', var.get('m'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('d')):
        try:
            var.get('a').put(var.get('i'), var.get('String').callprop('fromCharCode', (var.get('a').get(var.get('i'))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(8.0))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(16.0))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(24.0))&Js(255))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if var.get('b'):
        return var.get('a').callprop('join', Js('')).callprop('substring', Js(0.0), var.get('c'))
    else:
        return var.get('a').callprop('join', Js(''))
PyJsHoisted_l_.func_name = 'l'
var.put('l', PyJsHoisted_l_)
@Js
def PyJsHoisted_s_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'c', 'b', 'i', 'v'])
    var.put('c', var.get('a').get('length'))
    var.put('v', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('c')):
        try:
            var.get('v').put((var.get('i')>>Js(2.0)), (((var.get('a').callprop('charCodeAt', var.get('i'))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(1.0)))<<Js(8.0)))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(2.0)))<<Js(16.0)))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(3.0)))<<Js(24.0))))
        finally:
                var.put('i', Js(4.0), '+')
    if var.get('b'):
        var.get('v').put(var.get('v').get('length'), var.get('c'))
    return var.get('v')
PyJsHoisted_s_.func_name = 's'
var.put('s', PyJsHoisted_s_)
pass
pass
pass
pass
pass


# Add lib to the module scope
script = var.to_python()