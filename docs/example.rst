=======
Example
=======

Here is a simple example how to use `cache`:

.. code-block:: python

   from pycachera import cache

    @cache()
    def my_function(a, b):
        return a + b
    
    my_function(1, 2)  # returns 3