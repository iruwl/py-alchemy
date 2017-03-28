import os
import sys
import transaction
from sqlalchemy import select
from sqlalchemy.schema import CreateSchema

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
# from ..models import MyModel


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def create_schema(engine, schema):
    sql = select([('schema_name')]).\
          select_from('information_schema.schemata').\
          where("schema_name = '%s'" % schema)
    q = engine.execute(sql)
    if not q.fetchone():
        engine.execute(CreateSchema(schema))

def create_schemas(engine):
    for schema in ['app', 'bphtb']:
        create_schema(engine, schema)

def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    create_schemas(engine)
    Base.metadata.create_all(engine)

    # session_factory = get_session_factory(engine)
    #
    # with transaction.manager:
    #     dbsession = get_tm_session(session_factory, transaction.manager)
    #
    #     model = MyModel(name='one', value=1)
    #     dbsession.add(model)
