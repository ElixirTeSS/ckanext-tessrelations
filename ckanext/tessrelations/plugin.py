import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


from ckanext.tessrelations.model.tables import setup as model_setup
from ckanext.tessrelations.model.tables import TessMaterialNode, TessMaterialEvent

log = logging.getLogger(__name__)


class TessrelationsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'tessrelations')

    #def configure(self, config):
    #    log.debug("Running configure method.")
    #    model_setup()

    def update_config(self, config):
        log.debug("Running update method.")
        model_setup()