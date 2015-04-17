__author__ = 'milo'


import logging


from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy import ForeignKey
from sqlalchemy.engine.reflection import Inspector


from ckan import model

from ckan.model.meta import metadata, mapper, Session, engine
from ckan.model.types import make_uuid
from ckan.model.domain_object import DomainObject

log = logging.getLogger(__name__)

material_event_table = None
material_node_table = None
tess_event_table = None

def setup():
    log.debug("In the setup...")
    if material_event_table is None:
        define_tables()

        if not tess_event_table.exists():
            log.debug("Creating events table.")
            tess_event_table.create()

        if not material_event_table.exists():
           log.debug("Creating material <-> event table.")
           material_event_table.create()

        if not material_node_table.exists():
            log.debug("Creating material <-> node table.")
            material_node_table.create()




def define_tables():
    log.debug("Defining tables")
    global material_event_table
    global material_node_table
    global tess_event_table
    global tess_dataset_table
    global tess_group_table

    # Attempt to gain access to the group table
    tess_group_table = Table('group',metadata,extend_existing=True)
    mapper(TessGroup, tess_group_table)

    tess_dataset_table = Table('package',metadata,extend_existing=True)
    mapper(TessDataset, tess_dataset_table)


    # First attempt at events, with minimal information.
    tess_event_table = Table('tess_events', metadata,
                             Column('id',types.UnicodeText, primary_key=True),
                             Column('url', types.UnicodeText, default=u''),
                             )

    mapper(TessEvents,tess_event_table)

    material_event_table = Table('material_event', metadata,
                                Column('id',types.UnicodeText, primary_key=True, default=make_uuid),
                                Column('material_id', types.UnicodeText, ForeignKey('package.id')),
                                Column('event_id', types.UnicodeText, ForeignKey('tess_events.id')),
                            )
    # ForeignKey('harvest_object.id')

    mapper(TessMaterialEvent, material_event_table)

    material_node_table = Table('material_node', metadata,
                                Column('id',types.UnicodeText, primary_key=True, default=make_uuid),
                                Column('material_id', types.UnicodeText, ForeignKey('package.id')),
                                Column('node_id', types.UnicodeText, ForeignKey('group.id')),
                            )

    mapper(TessMaterialNode, material_node_table)





class TessRelation(DomainObject):
    # This is a separate class from which the others inherit in case we need some
    # stuff here (e.g. for searching) later.
    pass

class TessMaterialEvent(TessRelation):
    pass

class TessMaterialNode(TessRelation):
    pass

# Group table with group type set to 'node'
class TessGroup(DomainObject):
    pass

# Event table
class TessEvents(DomainObject):
    pass

# Datasets, i.e. training materials
class TessDataset(DomainObject):
    pass
