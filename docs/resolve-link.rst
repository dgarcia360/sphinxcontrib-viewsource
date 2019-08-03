============
Resolve Link
============

The ``viewsource_resolve_link`` function set in ``config.py`` is editable to fit your documentation needs.

.. py:function:: viewsource_resolve_link(file_path, language=None)

   Defines the link resolution strategy for each code of block.

   :param file_path: Contains the path of the file included.
   :type file_path: string
   :param language: Contains the name of the highlighting language if set.
   :type language: string
   :return: URL pointing to the file as string

Here there are some popular configurations that you can use to set up the link resolution strategy.

Point to an internal file
=========================

.. code:: python

  viewsource_title = 'Get the Code'
  def viewsource_resolve_link(file_path, language=None):
    snippets_folder = '/snippets/'
    # get the name of the file
    path_split = file_path.split('/')
    file = path_split[len(path_split)-1]
    return snippets_folder + file

Point to an external file
=========================

.. code:: python

      viewsource_title = 'Edit on Github'

      def viewsource_resolve_link(file_path, language=None):
        base_url = 'https://github.com/dgarcia360/sphinxcontrib-viewsource/blob/master/docs/snippets/'
        # get the name of the file
        path_split = file_path.split('/')
        file = path_split[len(path_split)-1]
        return base_url + file

Resolution strategy per language
================================

.. code:: python

  viewsource_title = 'Edit on Github'

  def viewsource_resolve_link(file_path, language=None):
    # get the name of the file
    path_split = file_path.split('/')
    file = path_split[len(path_split)-1]

    url = 'https://github.com/dgarcia360/sphinxcontrib-viewsource/blob/master/docs/python/%s' % file
    if language == 'java':
        return 'https://github.com/dgarcia360/sphinxcontrib-viewsource/blob/master/docs/java/src/%s' % file
    return url