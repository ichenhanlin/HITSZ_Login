__all__ = ['sha1']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['a', 'r', 'c', 'f', 'p', 'o', 'e', 'sha1', 'i', 't', 's', 'n', 'u', 'h'])
@Js
def PyJsHoisted_t_(t, this, arguments, var=var):
    var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['t'])
    def PyJs_LONG_1_(var=var):
        def PyJs_LONG_0_(var=var):
            return var.get('f').put('0', var.get('f').put('16', var.get('f').put('1', var.get('f').put('2', var.get('f').put('3', var.get('f').put('4', var.get('f').put('5', var.get('f').put('6', var.get('f').put('7', var.get('f').put('8', var.get('f').put('9', var.get('f').put('10', var.get('f').put('11', var.get('f').put('12', var.get('f').put('13', var.get('f').put('14', var.get('f').put('15', Js(0.0))))))))))))))))))
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma((PyJsComma(PyJs_LONG_0_(),var.get(u"this").put('blocks', var.get('f'))) if var.get('t') else var.get(u"this").put('blocks', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))),var.get(u"this").put('h0', Js(1732584193.0))),var.get(u"this").put('h1', Js(4023233417.0))),var.get(u"this").put('h2', Js(2562383102.0))),var.get(u"this").put('h3', Js(271733878.0))),var.get(u"this").put('h4', Js(3285377520.0))),var.get(u"this").put('block', var.get(u"this").put('start', var.get(u"this").put('bytes', var.get(u"this").put('hBytes', Js(0.0)))))),var.get(u"this").put('finalized', var.get(u"this").put('hashed', Js(1.0).neg()))),var.get(u"this").put('first', Js(0.0).neg()))
    PyJs_LONG_1_()
PyJsHoisted_t_.func_name = 't'
var.put('t', PyJsHoisted_t_)
pass
var.put('h', (var.get('window') if (Js('object')==var.get('window',throw=False).typeof()) else Js({})))
var.put('s', (((var.get('h').get('JS_SHA1_NO_NODE_JS').neg() and (Js('object')==var.get('process',throw=False).typeof())) and var.get('process').get('versions')) and var.get('process').get('versions').get('node')))
(var.get('s') and var.put('h', var.get('global')))
var.put('i', ((var.get('h').get('JS_SHA1_NO_COMMON_JS').neg() and (Js('object')==var.get('module',throw=False).typeof())) and var.get('module').get('exports')))
var.put('e', ((Js('function')==var.get('define',throw=False).typeof()) and var.get('define').get('amd')))
var.put('r', Js('0123456789abcdef').callprop('split', Js('')))
var.put('o', Js([(-Js(2147483648.0)), Js(8388608.0), Js(32768.0), Js(128.0)]))
var.put('n', Js([Js(24.0), Js(16.0), Js(8.0), Js(0.0)]))
var.put('a', Js([Js('hex'), Js('array'), Js('digest'), Js('arrayBuffer')]))
var.put('f', Js([]))
@Js
def PyJs_anonymous_2_(h, this, arguments, var=var):
    var = Scope({'h':h, 'this':this, 'arguments':arguments}, var)
    var.registers(['h'])
    @Js
    def PyJs_anonymous_3_(s, this, arguments, var=var):
        var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['s'])
        return var.get('t').create(Js(0.0).neg()).callprop('update', var.get('s')).callprop(var.get('h'))
    PyJs_anonymous_3_._set_name('anonymous')
    return PyJs_anonymous_3_
PyJs_anonymous_2_._set_name('anonymous')
var.put('u', PyJs_anonymous_2_)
@Js
def PyJs_anonymous_4_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'i', 'h'])
    var.put('h', var.get('u')(Js('hex')))
    @Js
    def PyJs_anonymous_5_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('t').create()
    PyJs_anonymous_5_._set_name('anonymous')
    @Js
    def PyJs_anonymous_6_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get('h').callprop('create').callprop('update', var.get('t'))
    PyJs_anonymous_6_._set_name('anonymous')
    PyJsComma(PyJsComma((var.get('s') and var.put('h', var.get('p')(var.get('h')))),var.get('h').put('create', PyJs_anonymous_5_)),var.get('h').put('update', PyJs_anonymous_6_))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('a').get('length')):
        try:
            var.put('e', var.get('a').get(var.get('i')))
            var.get('h').put(var.get('e'), var.get('u')(var.get('e')))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    return var.get('h')
PyJs_anonymous_4_._set_name('anonymous')
var.put('c', PyJs_anonymous_4_)
@Js
def PyJs_anonymous_7_(t, this, arguments, var=var):
    var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['s', 't', 'i', 'h'])
    var.put('h', var.get('eval')(Js("require('crypto')")))
    var.put('s', var.get('eval')(Js("require('buffer').Buffer")))
    @Js
    def PyJs_anonymous_8_(i, this, arguments, var=var):
        var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['i'])
        if (Js('string')==var.get('i',throw=False).typeof()):
            return var.get('h').callprop('createHash', Js('sha1')).callprop('update', var.get('i'), Js('utf8')).callprop('digest', Js('hex'))
        if PyJsStrictEq(var.get('i').get('constructor'),var.get('ArrayBuffer')):
            var.put('i', var.get('Uint8Array').create(var.get('i')))
        else:
            if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('i').get('length')):
                return var.get('t')(var.get('i'))
        return var.get('h').callprop('createHash', Js('sha1')).callprop('update', var.get('s').create(var.get('i'))).callprop('digest', Js('hex'))
    PyJs_anonymous_8_._set_name('anonymous')
    var.put('i', PyJs_anonymous_8_)
    return var.get('i')
PyJs_anonymous_7_._set_name('anonymous')
var.put('p', PyJs_anonymous_7_)
def PyJs_LONG_41_(var=var):
    @Js
    def PyJs_anonymous_9_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'o', 'e', 'i', 't', 's', 'r'])
        if var.get(u"this").get('finalized').neg():
            var.put('s', (Js('string')!=var.get('t',throw=False).typeof()))
            ((var.get('s') and PyJsStrictEq(var.get('t').get('constructor'),var.get('h').get('ArrayBuffer'))) and var.put('t', var.get('Uint8Array').create(var.get('t'))))
            #for JS loop
            var.put('r', Js(0.0))
            var.put('o', (var.get('t').get('length') or Js(0.0)))
            var.put('a', var.get(u"this").get('blocks'))
            while (var.get('r')<var.get('o')):
                def PyJs_LONG_10_(var=var):
                    return PyJsComma(PyJsComma(var.get(u"this").put('hashed', Js(1.0).neg()),var.get('a').put('0', var.get(u"this").get('block'))),var.get('a').put('16', var.get('a').put('1', var.get('a').put('2', var.get('a').put('3', var.get('a').put('4', var.get('a').put('5', var.get('a').put('6', var.get('a').put('7', var.get('a').put('8', var.get('a').put('9', var.get('a').put('10', var.get('a').put('11', var.get('a').put('12', var.get('a').put('13', var.get('a').put('14', var.get('a').put('15', Js(0.0))))))))))))))))))
                if PyJsComma((var.get(u"this").get('hashed') and PyJs_LONG_10_()),var.get('s')):
                    #for JS loop
                    var.put('e', var.get(u"this").get('start'))
                    while ((var.get('r')<var.get('o')) and (var.get('e')<Js(64.0))):
                        try:
                            var.get('a').put((var.get('e')>>Js(2.0)), (var.get('t').get(var.get('r'))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')
                        finally:
                                var.put('r',Js(var.get('r').to_number())+Js(1))
                else:
                    #for JS loop
                    var.put('e', var.get(u"this").get('start'))
                    while ((var.get('r')<var.get('o')) and (var.get('e')<Js(64.0))):
                        try:
                            def PyJs_LONG_13_(var=var):
                                def PyJs_LONG_11_(var=var):
                                    return PyJsComma(PyJsComma(var.get('a').put((var.get('e')>>Js(2.0)), ((Js(224.0)|(var.get('i')>>Js(12.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|'),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|((var.get('i')>>Js(6.0))&Js(63.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|(Js(63.0)&var.get('i')))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|'))
                                def PyJs_LONG_12_(var=var):
                                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('i', (Js(65536.0)+(((Js(1023.0)&var.get('i'))<<Js(10.0))|(Js(1023.0)&var.get('t').callprop('charCodeAt', var.put('r',Js(var.get('r').to_number())+Js(1))))))),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(240.0)|(var.get('i')>>Js(18.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|((var.get('i')>>Js(12.0))&Js(63.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|((var.get('i')>>Js(6.0))&Js(63.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|(Js(63.0)&var.get('i')))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|'))
                                return (PyJsComma(var.get('a').put((var.get('e')>>Js(2.0)), ((Js(192.0)|(var.get('i')>>Js(6.0)))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|'),var.get('a').put((var.get('e')>>Js(2.0)), ((Js(128.0)|(Js(63.0)&var.get('i')))<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|')) if (var.get('i')<Js(2048.0)) else (PyJs_LONG_11_() if ((var.get('i')<Js(55296.0)) or (var.get('i')>=Js(57344.0))) else PyJs_LONG_12_()))
                            (var.get('a').put((var.get('e')>>Js(2.0)), (var.get('i')<<var.get('n').get((Js(3.0)&(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))), '|') if (var.put('i', var.get('t').callprop('charCodeAt', var.get('r')))<Js(128.0)) else PyJs_LONG_13_())
                        finally:
                                var.put('r',Js(var.get('r').to_number())+Js(1))
                def PyJs_LONG_14_(var=var):
                    return PyJsComma(PyJsComma(var.get(u"this").put('lastByteIndex', var.get('e')),var.get(u"this").put('bytes', (var.get('e')-var.get(u"this").get('start')), '+')),(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('block', var.get('a').get('16')),var.get(u"this").put('start', (var.get('e')-Js(64.0)))),var.get(u"this").callprop('hash')),var.get(u"this").put('hashed', Js(0.0).neg())) if (var.get('e')>=Js(64.0)) else var.get(u"this").put('start', var.get('e'))))
                PyJs_LONG_14_()
            
            return PyJsComma(((var.get(u"this").get('bytes')>Js(4294967295.0)) and PyJsComma(var.get(u"this").put('hBytes', ((var.get(u"this").get('bytes')/Js(4294967296.0))<<Js(0.0)), '+'),var.get(u"this").put('bytes', (var.get(u"this").get('bytes')%Js(4294967296.0))))),var.get(u"this"))
    PyJs_anonymous_9_._set_name('anonymous')
    @Js
    def PyJs_anonymous_15_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['h', 't'])
        if var.get(u"this").get('finalized').neg():
            var.get(u"this").put('finalized', Js(0.0).neg())
            var.put('t', var.get(u"this").get('blocks'))
            var.put('h', var.get(u"this").get('lastByteIndex'))
            def PyJs_LONG_17_(var=var):
                def PyJs_LONG_16_(var=var):
                    return PyJsComma(PyJsComma((var.get(u"this").get('hashed') or var.get(u"this").callprop('hash')),var.get('t').put('0', var.get(u"this").get('block'))),var.get('t').put('16', var.get('t').put('1', var.get('t').put('2', var.get('t').put('3', var.get('t').put('4', var.get('t').put('5', var.get('t').put('6', var.get('t').put('7', var.get('t').put('8', var.get('t').put('9', var.get('t').put('10', var.get('t').put('11', var.get('t').put('12', var.get('t').put('13', var.get('t').put('14', var.get('t').put('15', Js(0.0))))))))))))))))))
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('16', var.get(u"this").get('block')),var.get('t').put((var.get('h')>>Js(2.0)), var.get('o').get((Js(3.0)&var.get('h'))), '|')),var.get(u"this").put('block', var.get('t').get('16'))),((var.get('h')>=Js(56.0)) and PyJs_LONG_16_())),var.get('t').put('14', ((var.get(u"this").get('hBytes')<<Js(3.0))|PyJsBshift(var.get(u"this").get('bytes'),Js(29.0))))),var.get('t').put('15', (var.get(u"this").get('bytes')<<Js(3.0)))),var.get(u"this").callprop('hash'))
            PyJs_LONG_17_()
    PyJs_anonymous_15_._set_name('anonymous')
    @Js
    def PyJs_anonymous_18_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'o', 'e', 'i', 't', 's', 'n', 'h'])
        var.put('s', var.get(u"this").get('h0'))
        var.put('i', var.get(u"this").get('h1'))
        var.put('e', var.get(u"this").get('h2'))
        var.put('r', var.get(u"this").get('h3'))
        var.put('o', var.get(u"this").get('h4'))
        var.put('n', var.get(u"this").get('blocks'))
        #for JS loop
        var.put('t', Js(16.0))
        while (var.get('t')<Js(80.0)):
            try:
                PyJsComma(var.put('h', (((var.get('n').get((var.get('t')-Js(3.0)))^var.get('n').get((var.get('t')-Js(8.0))))^var.get('n').get((var.get('t')-Js(14.0))))^var.get('n').get((var.get('t')-Js(16.0))))),var.get('n').put(var.get('t'), ((var.get('h')<<Js(1.0))|PyJsBshift(var.get('h'),Js(31.0)))))
            finally:
                    var.put('t',Js(var.get('t').to_number())+Js(1))
        #for JS loop
        var.put('t', Js(0.0))
        while (var.get('t')<Js(20.0)):
            try:
                def PyJs_LONG_21_(var=var):
                    def PyJs_LONG_20_(var=var):
                        def PyJs_LONG_19_(var=var):
                            return (var.put('h', ((var.put('o', (((((var.put('h', ((var.get('s')<<Js(5.0))|PyJsBshift(var.get('s'),Js(27.0))))+((var.get('i')&var.get('e'))|((~var.get('i'))&var.get('r'))))+var.get('o'))+Js(1518500249.0))+var.get('n').get(var.get('t')))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('o'),Js(27.0))))+((var.get('s')&var.put('i', ((var.get('i')<<Js(30.0))|PyJsBshift(var.get('i'),Js(2.0)))))|((~var.get('s'))&var.get('e'))))
                        return var.put('e', (((((var.put('h', ((var.put('r', ((((PyJs_LONG_19_()+var.get('r'))+Js(1518500249.0))+var.get('n').get((var.get('t')+Js(1.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('r'),Js(27.0))))+((var.get('o')&var.put('s', ((var.get('s')<<Js(30.0))|PyJsBshift(var.get('s'),Js(2.0)))))|((~var.get('o'))&var.get('i'))))+var.get('e'))+Js(1518500249.0))+var.get('n').get((var.get('t')+Js(2.0))))<<Js(0.0)))
                    return (var.put('h', ((var.put('i', (((((var.put('h', ((PyJs_LONG_20_()<<Js(5.0))|PyJsBshift(var.get('e'),Js(27.0))))+((var.get('r')&var.put('o', ((var.get('o')<<Js(30.0))|PyJsBshift(var.get('o'),Js(2.0)))))|((~var.get('r'))&var.get('s'))))+var.get('i'))+Js(1518500249.0))+var.get('n').get((var.get('t')+Js(3.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('i'),Js(27.0))))+((var.get('e')&var.put('r', ((var.get('r')<<Js(30.0))|PyJsBshift(var.get('r'),Js(2.0)))))|((~var.get('e'))&var.get('o'))))
                PyJsComma(var.put('s', ((((PyJs_LONG_21_()+var.get('s'))+Js(1518500249.0))+var.get('n').get((var.get('t')+Js(4.0))))<<Js(0.0))),var.put('e', ((var.get('e')<<Js(30.0))|PyJsBshift(var.get('e'),Js(2.0)))))
            finally:
                    var.put('t', Js(5.0), '+')
        #for JS loop
        
        while (var.get('t')<Js(40.0)):
            try:
                def PyJs_LONG_24_(var=var):
                    def PyJs_LONG_23_(var=var):
                        def PyJs_LONG_22_(var=var):
                            return (((var.put('h', ((var.put('o', (((((var.put('h', ((var.get('s')<<Js(5.0))|PyJsBshift(var.get('s'),Js(27.0))))+((var.get('i')^var.get('e'))^var.get('r')))+var.get('o'))+Js(1859775393.0))+var.get('n').get(var.get('t')))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('o'),Js(27.0))))+((var.get('s')^var.put('i', ((var.get('i')<<Js(30.0))|PyJsBshift(var.get('i'),Js(2.0)))))^var.get('e')))+var.get('r'))+Js(1859775393.0))
                        return var.put('h', ((var.put('e', (((((var.put('h', ((var.put('r', ((PyJs_LONG_22_()+var.get('n').get((var.get('t')+Js(1.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('r'),Js(27.0))))+((var.get('o')^var.put('s', ((var.get('s')<<Js(30.0))|PyJsBshift(var.get('s'),Js(2.0)))))^var.get('i')))+var.get('e'))+Js(1859775393.0))+var.get('n').get((var.get('t')+Js(2.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('e'),Js(27.0))))
                    return ((var.put('h', ((var.put('i', (((((PyJs_LONG_23_()+((var.get('r')^var.put('o', ((var.get('o')<<Js(30.0))|PyJsBshift(var.get('o'),Js(2.0)))))^var.get('s')))+var.get('i'))+Js(1859775393.0))+var.get('n').get((var.get('t')+Js(3.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('i'),Js(27.0))))+((var.get('e')^var.put('r', ((var.get('r')<<Js(30.0))|PyJsBshift(var.get('r'),Js(2.0)))))^var.get('o')))+var.get('s'))
                PyJsComma(var.put('s', (((PyJs_LONG_24_()+Js(1859775393.0))+var.get('n').get((var.get('t')+Js(4.0))))<<Js(0.0))),var.put('e', ((var.get('e')<<Js(30.0))|PyJsBshift(var.get('e'),Js(2.0)))))
            finally:
                    var.put('t', Js(5.0), '+')
        #for JS loop
        
        while (var.get('t')<Js(60.0)):
            try:
                def PyJs_LONG_27_(var=var):
                    def PyJs_LONG_26_(var=var):
                        def PyJs_LONG_25_(var=var):
                            return (var.put('h', ((var.put('o', (((((var.put('h', ((var.get('s')<<Js(5.0))|PyJsBshift(var.get('s'),Js(27.0))))+(((var.get('i')&var.get('e'))|(var.get('i')&var.get('r')))|(var.get('e')&var.get('r'))))+var.get('o'))-Js(1894007588.0))+var.get('n').get(var.get('t')))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('o'),Js(27.0))))+(((var.get('s')&var.put('i', ((var.get('i')<<Js(30.0))|PyJsBshift(var.get('i'),Js(2.0)))))|(var.get('s')&var.get('e')))|(var.get('i')&var.get('e'))))
                        return ((((var.put('h', ((var.put('r', ((((PyJs_LONG_25_()+var.get('r'))-Js(1894007588.0))+var.get('n').get((var.get('t')+Js(1.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('r'),Js(27.0))))+(((var.get('o')&var.put('s', ((var.get('s')<<Js(30.0))|PyJsBshift(var.get('s'),Js(2.0)))))|(var.get('o')&var.get('i')))|(var.get('s')&var.get('i'))))+var.get('e'))-Js(1894007588.0))+var.get('n').get((var.get('t')+Js(2.0))))
                    return ((var.put('i', (((((var.put('h', ((var.put('e', (PyJs_LONG_26_()<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('e'),Js(27.0))))+(((var.get('r')&var.put('o', ((var.get('o')<<Js(30.0))|PyJsBshift(var.get('o'),Js(2.0)))))|(var.get('r')&var.get('s')))|(var.get('o')&var.get('s'))))+var.get('i'))-Js(1894007588.0))+var.get('n').get((var.get('t')+Js(3.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('i'),Js(27.0)))
                PyJsComma(var.put('s', (((((var.put('h', PyJs_LONG_27_())+(((var.get('e')&var.put('r', ((var.get('r')<<Js(30.0))|PyJsBshift(var.get('r'),Js(2.0)))))|(var.get('e')&var.get('o')))|(var.get('r')&var.get('o'))))+var.get('s'))-Js(1894007588.0))+var.get('n').get((var.get('t')+Js(4.0))))<<Js(0.0))),var.put('e', ((var.get('e')<<Js(30.0))|PyJsBshift(var.get('e'),Js(2.0)))))
            finally:
                    var.put('t', Js(5.0), '+')
        #for JS loop
        
        while (var.get('t')<Js(80.0)):
            try:
                def PyJs_LONG_30_(var=var):
                    def PyJs_LONG_29_(var=var):
                        def PyJs_LONG_28_(var=var):
                            return (((var.put('h', ((var.put('o', (((((var.put('h', ((var.get('s')<<Js(5.0))|PyJsBshift(var.get('s'),Js(27.0))))+((var.get('i')^var.get('e'))^var.get('r')))+var.get('o'))-Js(899497514.0))+var.get('n').get(var.get('t')))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('o'),Js(27.0))))+((var.get('s')^var.put('i', ((var.get('i')<<Js(30.0))|PyJsBshift(var.get('i'),Js(2.0)))))^var.get('e')))+var.get('r'))-Js(899497514.0))
                        return var.put('h', ((var.put('e', (((((var.put('h', ((var.put('r', ((PyJs_LONG_28_()+var.get('n').get((var.get('t')+Js(1.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('r'),Js(27.0))))+((var.get('o')^var.put('s', ((var.get('s')<<Js(30.0))|PyJsBshift(var.get('s'),Js(2.0)))))^var.get('i')))+var.get('e'))-Js(899497514.0))+var.get('n').get((var.get('t')+Js(2.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('e'),Js(27.0))))
                    return ((var.put('h', ((var.put('i', (((((PyJs_LONG_29_()+((var.get('r')^var.put('o', ((var.get('o')<<Js(30.0))|PyJsBshift(var.get('o'),Js(2.0)))))^var.get('s')))+var.get('i'))-Js(899497514.0))+var.get('n').get((var.get('t')+Js(3.0))))<<Js(0.0)))<<Js(5.0))|PyJsBshift(var.get('i'),Js(27.0))))+((var.get('e')^var.put('r', ((var.get('r')<<Js(30.0))|PyJsBshift(var.get('r'),Js(2.0)))))^var.get('o')))+var.get('s'))
                PyJsComma(var.put('s', (((PyJs_LONG_30_()-Js(899497514.0))+var.get('n').get((var.get('t')+Js(4.0))))<<Js(0.0))),var.put('e', ((var.get('e')<<Js(30.0))|PyJsBshift(var.get('e'),Js(2.0)))))
            finally:
                    var.put('t', Js(5.0), '+')
        def PyJs_LONG_31_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('h0', ((var.get(u"this").get('h0')+var.get('s'))<<Js(0.0))),var.get(u"this").put('h1', ((var.get(u"this").get('h1')+var.get('i'))<<Js(0.0)))),var.get(u"this").put('h2', ((var.get(u"this").get('h2')+var.get('e'))<<Js(0.0)))),var.get(u"this").put('h3', ((var.get(u"this").get('h3')+var.get('r'))<<Js(0.0)))),var.get(u"this").put('h4', ((var.get(u"this").get('h4')+var.get('o'))<<Js(0.0))))
        PyJs_LONG_31_()
    PyJs_anonymous_18_._set_name('anonymous')
    @Js
    def PyJs_anonymous_32_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'i', 't', 's', 'h'])
        var.get(u"this").callprop('finalize')
        var.put('t', var.get(u"this").get('h0'))
        var.put('h', var.get(u"this").get('h1'))
        var.put('s', var.get(u"this").get('h2'))
        var.put('i', var.get(u"this").get('h3'))
        var.put('e', var.get(u"this").get('h4'))
        def PyJs_LONG_37_(var=var):
            def PyJs_LONG_36_(var=var):
                def PyJs_LONG_35_(var=var):
                    def PyJs_LONG_34_(var=var):
                        def PyJs_LONG_33_(var=var):
                            return (((((((var.get('r').get(((var.get('t')>>Js(28.0))&Js(15.0)))+var.get('r').get(((var.get('t')>>Js(24.0))&Js(15.0))))+var.get('r').get(((var.get('t')>>Js(20.0))&Js(15.0))))+var.get('r').get(((var.get('t')>>Js(16.0))&Js(15.0))))+var.get('r').get(((var.get('t')>>Js(12.0))&Js(15.0))))+var.get('r').get(((var.get('t')>>Js(8.0))&Js(15.0))))+var.get('r').get(((var.get('t')>>Js(4.0))&Js(15.0))))+var.get('r').get((Js(15.0)&var.get('t'))))
                        return (((((((PyJs_LONG_33_()+var.get('r').get(((var.get('h')>>Js(28.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(24.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(20.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(16.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(12.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(8.0))&Js(15.0))))+var.get('r').get(((var.get('h')>>Js(4.0))&Js(15.0))))
                    return ((((((((PyJs_LONG_34_()+var.get('r').get((Js(15.0)&var.get('h'))))+var.get('r').get(((var.get('s')>>Js(28.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(24.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(20.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(16.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(12.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(8.0))&Js(15.0))))+var.get('r').get(((var.get('s')>>Js(4.0))&Js(15.0))))
                return ((((((((PyJs_LONG_35_()+var.get('r').get((Js(15.0)&var.get('s'))))+var.get('r').get(((var.get('i')>>Js(28.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(24.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(20.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(16.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(12.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(8.0))&Js(15.0))))+var.get('r').get(((var.get('i')>>Js(4.0))&Js(15.0))))
            return ((((((((PyJs_LONG_36_()+var.get('r').get((Js(15.0)&var.get('i'))))+var.get('r').get(((var.get('e')>>Js(28.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(24.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(20.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(16.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(12.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(8.0))&Js(15.0))))+var.get('r').get(((var.get('e')>>Js(4.0))&Js(15.0))))
        return (PyJs_LONG_37_()+var.get('r').get((Js(15.0)&var.get('e'))))
    PyJs_anonymous_32_._set_name('anonymous')
    @Js
    def PyJs_anonymous_38_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'i', 't', 's', 'h'])
        var.get(u"this").callprop('finalize')
        var.put('t', var.get(u"this").get('h0'))
        var.put('h', var.get(u"this").get('h1'))
        var.put('s', var.get(u"this").get('h2'))
        var.put('i', var.get(u"this").get('h3'))
        var.put('e', var.get(u"this").get('h4'))
        return Js([((var.get('t')>>Js(24.0))&Js(255.0)), ((var.get('t')>>Js(16.0))&Js(255.0)), ((var.get('t')>>Js(8.0))&Js(255.0)), (Js(255.0)&var.get('t')), ((var.get('h')>>Js(24.0))&Js(255.0)), ((var.get('h')>>Js(16.0))&Js(255.0)), ((var.get('h')>>Js(8.0))&Js(255.0)), (Js(255.0)&var.get('h')), ((var.get('s')>>Js(24.0))&Js(255.0)), ((var.get('s')>>Js(16.0))&Js(255.0)), ((var.get('s')>>Js(8.0))&Js(255.0)), (Js(255.0)&var.get('s')), ((var.get('i')>>Js(24.0))&Js(255.0)), ((var.get('i')>>Js(16.0))&Js(255.0)), ((var.get('i')>>Js(8.0))&Js(255.0)), (Js(255.0)&var.get('i')), ((var.get('e')>>Js(24.0))&Js(255.0)), ((var.get('e')>>Js(16.0))&Js(255.0)), ((var.get('e')>>Js(8.0))&Js(255.0)), (Js(255.0)&var.get('e'))])
    PyJs_anonymous_38_._set_name('anonymous')
    @Js
    def PyJs_anonymous_39_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['h', 't'])
        var.get(u"this").callprop('finalize')
        var.put('t', var.get('ArrayBuffer').create(Js(20.0)))
        var.put('h', var.get('DataView').create(var.get('t')))
        def PyJs_LONG_40_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('h').callprop('setUint32', Js(0.0), var.get(u"this").get('h0')),var.get('h').callprop('setUint32', Js(4.0), var.get(u"this").get('h1'))),var.get('h').callprop('setUint32', Js(8.0), var.get(u"this").get('h2'))),var.get('h').callprop('setUint32', Js(12.0), var.get(u"this").get('h3'))),var.get('h').callprop('setUint32', Js(16.0), var.get(u"this").get('h4'))),var.get('t'))
        return PyJs_LONG_40_()
    PyJs_anonymous_39_._set_name('anonymous')
    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').get('prototype').put('update', PyJs_anonymous_9_),var.get('t').get('prototype').put('finalize', PyJs_anonymous_15_)),var.get('t').get('prototype').put('hash', PyJs_anonymous_18_)),var.get('t').get('prototype').put('hex', PyJs_anonymous_32_)),var.get('t').get('prototype').put('toString', var.get('t').get('prototype').get('hex'))),var.get('t').get('prototype').put('digest', PyJs_anonymous_38_)),var.get('t').get('prototype').put('array', var.get('t').get('prototype').get('digest'))),var.get('t').get('prototype').put('arrayBuffer', PyJs_anonymous_39_))
PyJs_LONG_41_()
var.put('sha1', var.get('c')())
pass


# Add lib to the module scope
sha1 = var.to_python()