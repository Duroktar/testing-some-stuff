Install
-------

First clone the repo

.. code-block:: bash

    $ https://github.com/Duroktar/testing-some-stuff.git
    $ cd testing-some-stuff

Usage
-----

**To start with fuge**

First install dependancies

.. code-block:: bash

    $ ./install.sh

Now run fuge 

.. code-block:: bash

    $ ./start.sh

Then in your browser navigate to `http://localhost:3000` or `http://localhost:3001/`

----


**To start with docker-compose**

.. code-block:: bash

    $ ./docker-up.sh

If you need to rebuild images

.. code-block:: bash

    $ ./docker-rebuild.sh

To run in the background.

.. code-block:: bash

    $ ./docker-start.sh


Then in your browser navigate to `http://localhost:3000`

Add new tasks like so `http://localhost:3001/tasks?description=Walk the dog&when=at 6:30 am`

Or use Postman and the included collection file `Tasks-Demo.postman_collection`

Then get the next upcoming task from `http://localhost:3001/tasks`
