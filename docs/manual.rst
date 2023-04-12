======
Manual
======

To cache a funtion or class attribute, you can use the ``pycachera.cache()`` decorator:


.. py:function:: cache(cachefolder=None,extrarg=None,cachekey=None,verbose=False,recache=False)



   :param str cachefolder: (Optional)The cache folder is set to '.cache' as default in the current working directory
   :param list extrarg: (Optional)If the function is a class method, you can give the extra arguments of the class as a list just for saving the cache
   :param str cachekey: (Optional) You can override the above method by giving a particular human readable key(str) for example: 'This is a function with fknee is 5, and alpha is 3'
   :param bool verbose: (Optional) To print the info
   :param bool recache: (Optional) If you want to recache the function, set it to True
   
 


