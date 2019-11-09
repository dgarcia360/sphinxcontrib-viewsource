# -*- encoding: utf-8 -*-
#
# (c) 2019 David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)

from docutils import nodes, utils
from sphinx.directives.code import LiteralInclude
from sphinx.util.nodes import split_explicit_title


class ViewSource(LiteralInclude):  # type: ignore
    """
    LiteralInclude replacing the caption with a custom link.
    """

    def run(self):
        env = self.state.document.settings.env
        config = env.config
        resolve_link = config['viewsource_resolve_link']
        if callable(resolve_link):
            file_path = self.arguments[0]
            language = None if not self.options['language'] else self.options['language']
            link = resolve_link(file_path, language)
            if 'caption' not in self.options:
                self.options['caption'] = ':viewsource:`%s`' % link
        return list(LiteralInclude.run(self))


def make_link_role(label):
    def role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
        text = utils.unescape(text)
        has_set_title, title, url = split_explicit_title(text)
        node = nodes.reference(label, label, internal=None, refuri=url)
        return [node], []

    return role


def setup_link_roles(app):
    title = app.config.viewsource_title
    app.add_role('viewsource', make_link_role(title))


def setup(app):
    app.add_config_value('viewsource_resolve_link', None, '')
    app.add_config_value('viewsource_title', None, 'View the Code')
    app.connect('builder-inited', setup_link_roles)
    app.add_directive('viewsource', ViewSource)
