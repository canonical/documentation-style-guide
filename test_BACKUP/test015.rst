This example should result in two warnings
=======

This line that contains :: in the middle should be ignored.

.. code-block:: python
    print("Hello, world!")
    # This line should be ignored
    $ This line should be flagged
    %> This line should be flagged
