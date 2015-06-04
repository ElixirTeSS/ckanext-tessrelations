=============
ckanext-tessrelations
=============

OBSOLETE: Now merged into ckanext-tess.

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


Here are the various keys in the new objects:

| Object            | Primary Key | Other keys            |
|-------------------|-------------|-----------------------|
| TessMaterialNode  | id (auto)   | material_id, node_id  |
| TessMaterialEvent | id (auto)   | material_id, event_id |
| TessEvent         | id (auto)   | url                   |

As for the existing tables which are referenced from this code, the schemas are:

                     Table "public.group" (TessGroup)
|     Column      |            Type             |   Modifiers   |
|-----------------|-----------------------------|---------------|
| id              | text                        | not null      |
| name            | text                        | not null      |
| title           | text                        |               | 
| description     | text                        |               | 
| created         | timestamp without time zone |               | 
| state           | text                        |               | 
| revision_id     | text                        |               | 
| type            | text                        | not null      |
| approval_status | text                        |               | 
| image_url       | text                        |               | 
| is_organization | boolean                     | default false |

                     Table "public.package" (TessDataset)
|      Column       |            Type             |   Modifiers   |
|-------------------|-----------------------------|---------------|
| id                | text                        | not null      |
| name              | character varying(100)      | not null      |
| title             | text                        |               | 
| version           | character varying(100)      |               | 
| url               | text                        |               |   
| notes             | text                        |               |  
| license_id        | text                        |               |  
| revision_id       | text                        |               |  
| author            | text                        |               |  
| author_email      | text                        |               |  
| maintainer        | text                        |               |  
| maintainer_email  | text                        |               |  
| state             | text                        |               |  
| type              | text                        |               |  
| owner_org         | text                        |               |  
| private           | boolean                     | default false |
| metadata_modified | timestamp without time zone |               |  
| creator_user_id   | text                        |               |  

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
