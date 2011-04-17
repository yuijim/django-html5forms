# Recipe 20.17. Solving Metaclass Conflicts
# Credit: Michele Simionato, David Mertz, Phillip J. Eby, Alex Martelli, Anna Martelli Ravenscroft
# http://book.opensourceproject.org.cn/lamp/python/pythoncook2/opensource/0596007973/pythoncook2-chp-20-sect-17.html

# support 2.3, too
try: set
except NameError: from sets import Set as set
# support classic classes, to some extent
import types
def uniques(sequence, skipset):
    for item in sequence:
        if item not in skipset:
            yield item
            skipset.add(item)
import inspect
def remove_redundant(classes):
    redundant = set([types.ClassType])   # turn old-style classes to new
    for c in classes:
        redundant.update(inspect.getmro(c)[1:])
    return tuple(uniques(classes, redundant))

memoized_metaclasses_map = {  }
def _get_noconflict_metaclass(bases, left_metas, right_metas):
     # make tuple of needed metaclasses in specified order
     metas = left_metas + tuple(map(type, bases)) + right_metas
     needed_metas = remove_redundant(metas)
     # return existing confict-solving meta, if any
     try: return memoized_metaclasses_map[needed_metas]
     except KeyError: pass
     # compute, memoize and return needed conflict-solving meta
     if not needed_metas:         # whee, a trivial case, happy us
         meta = type
     elif len(needed_metas) == 1: # another trivial case
         meta = needed_metas[0]
     else:                        # nontrivial, darn, gotta work...
         # ward against non-type root metatypes
         for m in needed_metas:
             if not issubclass(m, type):
                 raise TypeError( 'Non-type root metatype %r' % m)
         metaname = '_' + ''.join([m.__name__ for m in needed_metas])
         meta = classmaker( )(metaname, needed_metas, {  })
     memoized_metaclasses_map[needed_metas] = meta
     return meta
def classmaker(left_metas=( ), right_metas=( )):
     def make_class(name, bases, adict):
         metaclass = _get_noconflict_metaclass(bases, left_metas, right_metas)
         return metaclass(name, bases, adict)
     return make_class