__author__ = 'milo'

import logging


from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import types

from ckan import model

from ckan.model.meta import metadata, mapper
from ckan.model.types import make_uuid
from ckan.model.domain_object import DomainObject

log = logging.getLogger(__name__)

# http://docs.sqlalchemy.org/en/rel_0_8/orm/extensions/declarative.html
#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()

material_event_table = None
material_node_table = None

def setup():
    if material_event_table is None:
        define_tables()

        if not material_event_table: #.exists() # Blows up
           log.debug("Creating material <-> event table.")
           material_event_table.create()

        if not material_node_table: #.exists() # Blows up
            log.debug("Creating material <-> node table.")
            material_node_table.create()
    '''
    if not TessMaterialEvent.__table__.exists():
        log.debug("Creating material <-> event table.")
        TessMaterialEvent.__table__.create()
    '''


def define_tables():
    log.debug("Defining tables")
    global material_event_table
    global material_node_table

    # It seems that CKAN stores datasets ("training materials") in the "package" table, with a uuid
    # as the primary key. I don't know yet about events &c.
    material_event_table = (Table, 'material_event', metadata,
                                Column('id',types.UnicodeText, primary_key=True, default=make_uuid),
                                Column('material_id', types.UnicodeText, default=u''),
                                Column('event_id', types.UnicodeText, default=u''),
                            )

    log.debug("Table: " + str(material_event_table))

    # Blows up here...
    #mapper(TessMaterialEvent, material_event_table)

    material_node_table = (Table, 'material_node', metadata,
                                Column('id',types.UnicodeText, primary_key=True, default=make_uuid),
                                Column('material_id', types.UnicodeText, default=u''),
                                Column('node_id', types.UnicodeText, default=u''),
                            )

    #mapper(TessMaterialNode, material_node_table)


class TessRelation(DomainObject):
    # This is a separate class from which the others inherit in case we need some
    # stuff here (e.g. for searching) later.
    pass



class TessMaterialEvent(TessRelation):
    pass

class TessMaterialNode(TessRelation):
    pass

'''
class TessMaterialEvent(Base):
    __tablename__ = "materials_events"
    id = Column('id',types.UnicodeText, primary_key=True, default=make_uuid),
    material_id = Column(types.UnicodeText, primary_key=u'')
    event_id = Column(types.UnicodeText, default=u'')

class TessMaterialNode(Base):
    __tablename__ = "materials_nodes"
    id = Column(types.UnicodeText, primary_key=True, default=make_uuid),
    material_id = Column(types.UnicodeText, default=u'')
    node_id = Column(types.UnicodeText, default=u'')
'''
