===================
github-contributors
===================

Get the github url of contributors ::

    $ github-contributors
    12 user1 https://github.com/github_user1
    23 user2 https://github.com/github_user2

I like use the command::

    git shortlog -s -n

but with shortlog, I don't obtain the real github user account.

With this is more easy edit the contributors section in the readme file.

Install
=======

::

    pip install github-contributors

Usage
=====

Show as markdown

::

    github-contributors -m
    [user1](https://github.com/github_user1)

Show as rst

::
    github-contributors -s
    `user1 <https://github.com/github_user1>`_
