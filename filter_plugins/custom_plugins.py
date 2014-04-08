__author__ = 'pvh@sanbi.ac.za'

def append_string_to_each(*args):
    ''' appends a string to each element of value, coercing to string as we go
    '''
    # for i,arg in enumerate(args):
    #     print "arg",i,"type", type(arg), "val", arg
    value = args[0]
    extra = args[1]
    if not isinstance(value, list):
        raise ValueError('Expected a list value, got %s' % (type(value)))
    return [ unicode(x) + unicode(extra) for x in value ]

class FilterModule(object):

    def filters(self):
        ''' FilterModule objects return a dict mapping filter names to filter functions:
                @rtype: dict'''
        return dict(append_string_to_each=append_string_to_each)

