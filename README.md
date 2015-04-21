=============
ckanext-tessrelations
=============

This extension adds several tables to CKAN and grants access via models to both those and some existing tables.

The new tables, and their associated models, are:

* TessMaterialNode, material_node_table - links ckan datasets (training materials in TeSS) with ckan groups (includes nodes).
* TessMaterialEvent, material_event_table - links events to training materials.
* TessEvents, tess_event_table - for the saving of events. At present this only has a URL field and will need to be extended.

Tables which are accessed by this plugin:

* TessGroup, tess_group_table - ckan groups.
* TessDataset, tess_dataset_table - ckan datasets.


In order to explain the confusing names for some of the fields, please refer to this table:

| Original CKAN name | New CKAN name | TeSS name              |
|--------------------|---------------|------------------------|
| package            | dataset       | training material      |


------------
Installation
------------

To install ckanext-tessrelations for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/ElixirUK/ckanext-tessrelations.git
    cd ckanext-tessrelations
    python setup.py develop
    pip install -r dev-requirements.txt

To make the models accessible in other plugins, add this to their plugin.py file:

    from ckanext.tessrelations.model.tables import TessMaterialNode, TessMaterialEvent, TessEvents, TessGroup, TessDomainObject, TessDataset


-----
Usage
-----

An example for creating an event:


    new_event = TessEvents()
    new_event.url = “http://myevent.com”
    new_event.save()

More information on searching &c. to come when I have worked it out (contributions welcome).
