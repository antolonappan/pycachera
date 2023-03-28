======
Manual
======

To cache a funtion or class attribute, you can use the ``pycachera.cache()`` decorator:


.. py:function:: cache(cachefolder=None,extrarg=None,cachekey=None,verbose=False,Cobject="class",recache=False)

   To Cache a funtion

   :param str cachefolder: The person sending the message
   :param list extrarg: The recipient of the message
   :param str cachekey: The body of the message
   :param bool verbose: The priority of the message, can be a number 1-5
   :param str Cobject: The priority of the message, can be a number 1-5
   :param bool recache: The priority of the message, can be a number 1-5
   
   :return: the message id
   :rtype: int
   :raises ValueError: if the message_body exceeds 160 characters
   :raises TypeError: if the message_body is not a basestring


