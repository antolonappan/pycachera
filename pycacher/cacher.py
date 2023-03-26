import os
import numpy as np
from hashlib import md5
import pickle as pl
from numpy import ndarray
import pandas as pd

        
class Cache(object):
    """
    This is a decorator class, used for caching functions.
    
    cachefolder(optional): Folder for caching; if not found, it makes one
    
    If the args of a function are of different data types,
    the artibute 'cachekey_gen' trys to create a unique key depanding on
    few properties of the args. Currently it cannot handle a complex args,
    but still it does a pretty good job
    
    cachekey(optional): You can override the above method by giving a 
    particular human readable key(str) for example: 'This is a function
    with fknee is 5, and alpha is 3'
    
    Verbose(optional): Just to know what's happening inside
    """
    
    def __init__(self,cachefolder=None,extrarg=None,cachekey=None,verbose=False,Cobject="class"):

        if cachefolder is None:
            cachefolder = os.path.join(os.getcwd(),'.cache')

        if not os.path.exists(cachefolder):
            if verbose: print("PyCache: No cache folder found")
            os.makedirs(cachefolder)
            if verbose: print(f"PyCache: Setting '{cachefolder}' as Cache folder")
        
        self.cachefolder = cachefolder
        self.Cobject = Cobject
        self.extrarg = extrarg
        
        if cachekey == None:
            self.cachekey = None
        else:
            self.cachekey = md5(cachekey.enconde()).hexdigest()
        self.verbose=verbose
        
    def __call__(self, func):
        def decorator(*args):
            if self.Cobject=="class":
                fileprefix = f"""{self.cachefolder}/{str(args[0].__class__).split(".")[-1].split("'")[0]}_{func.__name__}"""
            elif self.Cobject=="function":
                fileprefix = f"{self.cachefolder}/{func.__name__}"
            
            if not os.path.exists(fileprefix):
                os.makedirs(fileprefix)
            

        
            if self.cachekey is None:
                hash_arg = self.cachekey_gen(args)
            else:
                hash_arg = self.cachekey
            
            cachefile = f"{fileprefix}/{hash_arg}"
                
            if os.path.isfile(cachefile):
                if self.verbose: print("CACHE WARNING: Returning Cached value")
                return self.file_reader(cachefile)
            else:
                if self.verbose: print(f"CACHE INFO: Caching {func.__name__} with a key:{hash_arg}")
                cache = func(*args)
                self.file_writer(cachefile, cache)
                return cache
        return decorator
        
    def cachekey_gen(self, arg):
        """
        Generates a unique key for a function, depending on the args
        """
        if self.Cobject == "class":
            Earg = []
            if self.extrarg is not None:
                for earg in self.extrarg:
                    Earg.append(getattr(arg[0], earg))
        elif self.Cobject == "function":
            Earg = []
        
        a = ''
        for tag in list(arg) + Earg:
            if type(tag) == list:
                a += ''.join(map(str,tag))

            if type(tag) == str:
                a += tag

            if (type(tag) == int) or (type(tag)== float):
                a += str(tag)
            
            if isinstance(tag, np.integer):
                a +=str(tag)
                
            if isinstance(tag, np.float64):
                a +=str(tag)

            if type(tag) == dict:
                a += ''.join(map(str,list(tag.keys())))
                
            if isinstance(tag, ndarray):
                a += ''.join(map(str,tag.flatten()))
                
            if type(tag) == bool:
                if tag:
                    a += str(1)
                else:
                    a += str(0)
            
            if type(tag) == pd.DataFrame:
                a += ''.join(map(str,list(tag.columns)))
                a += f'{len(tag)}'
        return md5(a.encode()).hexdigest()
    
    def file_writer(self,name,data):
        """
        Writes data to a file
        """
        with open(name, 'wb') as writ:
            pl.dump(data, writ)
            
    def file_reader(self,name):
        """
        Reads data from a file
        """
        with open(name, 'rb') as rea:
            data = pl.load(rea)
        return data

