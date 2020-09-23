__all__ = ['base64']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['_encode', '_getbyte64', '_getbyte', '_decode', '_VERSION', '_setAlpha', '_PADCHAR', '_ALPHA'])
@Js
def PyJsHoisted__getbyte64_(s, i, this, arguments, var=var):
    var = Scope({'s':s, 'i':i, 'this':this, 'arguments':arguments}, var)
    var.registers(['idx', 'i', 's'])
    var.put('idx', var.get('_ALPHA').callprop('indexOf', var.get('s').callprop('charAt', var.get('i'))))
    if PyJsStrictEq(var.get('idx'),(-Js(1.0))):
        PyJsTempException = JsToPyException(Js('Cannot decode base64'))
        raise PyJsTempException
    return var.get('idx')
PyJsHoisted__getbyte64_.func_name = '_getbyte64'
var.put('_getbyte64', PyJsHoisted__getbyte64_)
@Js
def PyJsHoisted__setAlpha_(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['s'])
    var.put('_ALPHA', var.get('s'))
PyJsHoisted__setAlpha_.func_name = '_setAlpha'
var.put('_setAlpha', PyJsHoisted__setAlpha_)
@Js
def PyJsHoisted__decode_(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['b10', 'i', 'pads', 's', 'imax', 'x'])
    var.put('pads', Js(0.0))
    var.put('imax', var.get('s').get('length'))
    var.put('x', Js([]))
    var.put('s', var.get('String')(var.get('s')))
    if PyJsStrictEq(var.get('imax'),Js(0.0)):
        return var.get('s')
    if PyJsStrictNeq((var.get('imax')%Js(4.0)),Js(0.0)):
        PyJsTempException = JsToPyException(Js('Cannot decode base64'))
        raise PyJsTempException
    if PyJsStrictEq(var.get('s').callprop('charAt', (var.get('imax')-Js(1.0))),var.get('_PADCHAR')):
        var.put('pads', Js(1.0))
        if PyJsStrictEq(var.get('s').callprop('charAt', (var.get('imax')-Js(2.0))),var.get('_PADCHAR')):
            var.put('pads', Js(2.0))
        var.put('imax', Js(4.0), '-')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('imax')):
        try:
            var.put('b10', ((((var.get('_getbyte64')(var.get('s'), var.get('i'))<<Js(18.0))|(var.get('_getbyte64')(var.get('s'), (var.get('i')+Js(1.0)))<<Js(12.0)))|(var.get('_getbyte64')(var.get('s'), (var.get('i')+Js(2.0)))<<Js(6.0)))|var.get('_getbyte64')(var.get('s'), (var.get('i')+Js(3.0)))))
            var.get('x').callprop('push', var.get('String').callprop('fromCharCode', (var.get('b10')>>Js(16.0)), ((var.get('b10')>>Js(8.0))&Js(255.0)), (var.get('b10')&Js(255.0))))
        finally:
                var.put('i', Js(4.0), '+')
    while 1:
        SWITCHED = False
        CONDITION = (var.get('pads'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            var.put('b10', (((var.get('_getbyte64')(var.get('s'), var.get('i'))<<Js(18.0))|(var.get('_getbyte64')(var.get('s'), (var.get('i')+Js(1.0)))<<Js(12.0)))|(var.get('_getbyte64')(var.get('s'), (var.get('i')+Js(2.0)))<<Js(6.0))))
            var.get('x').callprop('push', var.get('String').callprop('fromCharCode', (var.get('b10')>>Js(16.0)), ((var.get('b10')>>Js(8.0))&Js(255.0))))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            var.put('b10', ((var.get('_getbyte64')(var.get('s'), var.get('i'))<<Js(18.0))|(var.get('_getbyte64')(var.get('s'), (var.get('i')+Js(1.0)))<<Js(12.0))))
            var.get('x').callprop('push', var.get('String').callprop('fromCharCode', (var.get('b10')>>Js(16.0))))
            break
        SWITCHED = True
        break
    return var.get('x').callprop('join', Js(''))
PyJsHoisted__decode_.func_name = '_decode'
var.put('_decode', PyJsHoisted__decode_)
@Js
def PyJsHoisted__getbyte_(s, i, this, arguments, var=var):
    var = Scope({'s':s, 'i':i, 'this':this, 'arguments':arguments}, var)
    var.registers(['s', 'x', 'i'])
    var.put('x', var.get('s').callprop('charCodeAt', var.get('i')))
    if (var.get('x')>Js(255.0)):
        PyJsTempException = JsToPyException(Js('INVALID_CHARACTER_ERR: DOM Exception 5'))
        raise PyJsTempException
    return var.get('x')
PyJsHoisted__getbyte_.func_name = '_getbyte'
var.put('_getbyte', PyJsHoisted__getbyte_)
@Js
def PyJsHoisted__encode_(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['b10', 'i', 's', 'imax', 'x'])
    if PyJsStrictNeq(var.get('arguments').get('length'),Js(1.0)):
        PyJsTempException = JsToPyException(Js('SyntaxError: exactly one argument required'))
        raise PyJsTempException
    var.put('s', var.get('String')(var.get('s')))
    var.put('x', Js([]))
    var.put('imax', (var.get('s').get('length')-(var.get('s').get('length')%Js(3.0))))
    if PyJsStrictEq(var.get('s').get('length'),Js(0.0)):
        return var.get('s')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('imax')):
        try:
            var.put('b10', (((var.get('_getbyte')(var.get('s'), var.get('i'))<<Js(16.0))|(var.get('_getbyte')(var.get('s'), (var.get('i')+Js(1.0)))<<Js(8.0)))|var.get('_getbyte')(var.get('s'), (var.get('i')+Js(2.0)))))
            var.get('x').callprop('push', var.get('_ALPHA').callprop('charAt', (var.get('b10')>>Js(18.0))))
            var.get('x').callprop('push', var.get('_ALPHA').callprop('charAt', ((var.get('b10')>>Js(12.0))&Js(63.0))))
            var.get('x').callprop('push', var.get('_ALPHA').callprop('charAt', ((var.get('b10')>>Js(6.0))&Js(63.0))))
            var.get('x').callprop('push', var.get('_ALPHA').callprop('charAt', (var.get('b10')&Js(63.0))))
        finally:
                var.put('i', Js(3.0), '+')
    while 1:
        SWITCHED = False
        CONDITION = ((var.get('s').get('length')-var.get('imax')))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            var.put('b10', (var.get('_getbyte')(var.get('s'), var.get('i'))<<Js(16.0)))
            var.get('x').callprop('push', (((var.get('_ALPHA').callprop('charAt', (var.get('b10')>>Js(18.0)))+var.get('_ALPHA').callprop('charAt', ((var.get('b10')>>Js(12.0))&Js(63.0))))+var.get('_PADCHAR'))+var.get('_PADCHAR')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            var.put('b10', ((var.get('_getbyte')(var.get('s'), var.get('i'))<<Js(16.0))|(var.get('_getbyte')(var.get('s'), (var.get('i')+Js(1.0)))<<Js(8.0))))
            var.get('x').callprop('push', (((var.get('_ALPHA').callprop('charAt', (var.get('b10')>>Js(18.0)))+var.get('_ALPHA').callprop('charAt', ((var.get('b10')>>Js(12.0))&Js(63.0))))+var.get('_ALPHA').callprop('charAt', ((var.get('b10')>>Js(6.0))&Js(63.0))))+var.get('_PADCHAR')))
            break
        SWITCHED = True
        break
    return var.get('x').callprop('join', Js(''))
PyJsHoisted__encode_.func_name = '_encode'
var.put('_encode', PyJsHoisted__encode_)
var.put('_PADCHAR', Js('='))
var.put('_ALPHA', Js('LVoJPiCN2R8G90yg+hmFHuacZ1OWMnrsSTXkYpUq/3dlbfKwv6xztjI7DeBE45QA'))
var.put('_VERSION', Js('1.0'))
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
base64 = var.to_python()