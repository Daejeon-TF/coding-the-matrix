# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[x] for x in keylist]

def list2dict(L, keylist): return {k:v for (k,v) in zip(keylist, L)}

def listrange2dict(L): return {k:v for (k,v) in zip(range(len(L)), L)}
 'Mary': {5, 7, 35, 45},'By': {5, 10, 11, 13, 19, 20, 21, 25, 26, 37, 39, 41},
  'offering': {1, 5, 13},
