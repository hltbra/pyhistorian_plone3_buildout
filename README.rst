=======================
 Pyhistorian + Plone 3
=======================

Yes, we are trying to run pyhistorian with Plone 3!


Using this buildout
===================

::

    $ python bootstrap.py
    $ ./build.sh


Running myproduct tests::

    $ bin/instance test -s myproduct -vv



PS.: I didn't get PIL installation working properly with buildout.cfg here,
and installed both PIL and pyhistorian by hand.
