from data_lineage.parser import visit_dml_queries


def test_parser(parse_queries_fixture):
    assert len(parse_queries_fixture) == 5


def test_visitor(save_catalog, parse_queries_fixture):
    file_catalog, catalog = save_catalog
    dml = visit_dml_queries(catalog, parse_queries_fixture)
    assert len(dml) == 5

    for d in dml:
        assert len(d.source_tables) > 0 and d.target_table is not None
