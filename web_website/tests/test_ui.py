# -*- coding: utf-8 -*-
# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo.tests import common


class TestUI(common.HttpCase):

    at_install = True
    post_install = True

    def test_ui(self):
        # FIXME: we cannot use demo user to test, because with no other modules
        # installed there is no menu but Website which redirects to homepage
        user = self.env.user  # admin
        user.company_id = self.env.ref('base.main_company').id
        user.groups_id = [(4, self.env.ref('web_website.group_multi_website').id)]

        menu = self.env.ref('website.menu_website_configuration')
        tour = 'web_website.tour'
        self.phantom_js(
            '/web#menu_id=%i' % menu.id,
            "odoo.__DEBUG__.services['web_tour.tour']"
            ".run('%s')" % tour,

            "odoo.__DEBUG__.services['web_tour.tour']"
            ".tours['%s'].ready" % tour,

            login='admin',
        )
