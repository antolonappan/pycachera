======
Manual
======

To cache a funtion or class attribute, you can use the ``pycacher.cache()`` decorator:

.. py:function:: pycacher.cache(cachefolder=None,extrarg=None,cachekey=None,verbose=False,Cobject="class",recache=False)
   :param cachefolder: (Optional) If None, the cache folder is set to '.cache' in the current working directory
   :type kind: str
   :param extrarg: Optional-If the function is a class method, you can give the extra arguments of the class as a list just for saving the cache