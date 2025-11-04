This example should result in two warnings
=======

This line that contains :: in the middle should be ignored.


.. code-block:: python

    # This line should be ignored
    print("Hello, world!")  # This line should be flagged

Some more text.

    # Another code block
    int x = 5;  # This line should be flagged

.. code:: c++

    // This should be ignored
    int main() { // This line should be flagged
        return
