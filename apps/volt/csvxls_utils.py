class ExportClass(object):
    label = None
    file_ext = None
    content_type = None

    def __init__(self, rows):
        self.rows = rows

    def represented(self):
        def none_exception(value):
            """
            Returns a cleaned up value that can be used for csv export:

            - unicode text is encoded as such
            - None values are replaced with the given representation (default <NULL>)
            """
            if value is None:
                return '<NULL>'
            elif isinstance(value, unicodeT):
                return value.encode('utf8')
            elif isinstance(value, Reference):
                return int(value)
            elif hasattr(value, 'isoformat'):
                return value.isoformat()[:19].replace('T', ' ')
            elif isinstance(value, (list, tuple)):  # for type='list:..'
                return bar_encode(value)
            return value
        represented = []
        repr_cache = {}
        for record in self.rows:
            row = []
            for col in self.rows.colnames:
                if not self.rows.db._adapter.REGEX_TABLE_DOT_FIELD.match(col):
                    row.append(record._extra[col])
                else:
                    #(t, f) = col.split('.')
                    (t, f) = [name.strip('"') for name in col.split('.')]
                    field = self.rows.db[t][f]
                    if isinstance(record.get(t, None), (Row, dict)):
                        value = record[t][f]
                    else:
                        value = record[f]
                    if field.type == 'blob' and value is not None:
                        value = ''
                    elif field.represent:
                        if field.type.startswith('reference'):
                            if field not in repr_cache:
                                repr_cache[field] = {}
                            if value not in repr_cache[field]:
                                repr_cache[field][value] = field.represent(value, record)
                            value = repr_cache[field][value]
                        else:
                            value = field.represent(value, record)
                    row.append(none_exception(value))

            represented.append(row)
        return represented
    def export(self):
        raise NotImplementedError

class ExporterCSV(ExportClass):
    # CSV, represent == True
    label = 'CSV'
    file_ext = "csv"
    content_type = "text/csv"

    def __init__(self, rows):
        ExportClass.__init__(self, rows)

    def export(self):  # export CSV with rows.represent
        if self.rows:
            s = StringIO()
            self.rows.export_to_csv_file(s, represent=True)
            return s.getvalue()
        else:
            return None


class ExporterCSV_hidden(ExportClass):
    # pure csv, no represent.
    label = 'CSV'
    file_ext = "csv"
    content_type = "text/csv"

    def __init__(self, rows):
        ExportClass.__init__(self, rows)

    def export(self):
        if self.rows:
            return self.rows.as_csv()
        else:
            return ''

class ExporterXLS(ExportClass):
    label = 'XLS'
    file_ext = "xls"
    #content_type = ".xls"
    content_type = "application/vnd.ms-excel"
    # https://gist.github.com/brendano/22764
    # https://groups.google.com/forum/#!topic/web2py/MR_8JzzP9o4
    def __init__(self, rows):
        ExportClass.__init__(self, rows)

    def export(self):
        import xlwt, cStringIO
        if self.rows is None:
              return 'ExporterXLS: None rows-table'
        if len(self.rows) == 0:
              return 'ExporterXLS: empty rows-table'

        rows_colnames= [name.translate(None,'"') for name in self.rows.colnames ]

        (table_name, _)= rows_colnames[0].split('.')
        book = xlwt.Workbook()
        sheet = book.add_sheet(table_name)
        first_xls_row= 0

        def list2xls(row_num,line_list):
            for col_num, value in enumerate(line_list):
                 if value is None:
                     value= ''
                 elif isinstance(value, (int, long, float)):
                     value= str(value)
                 elif isinstance(value, (tuple, list)):
                     result_str= ''
                     for e in value:
                           if isinstance(e, (int, long, float)):
                                e= str(e)
                           result_str += e.decode('utf8') + ';\n'
                     value = result_str
                 elif isinstance(value, str):
                     value= value.decode('utf8')
                 elif isinstance(value,  datetime.date):
                     value= value.strftime('%d.%m.%Y')
                 elif isinstance(value, datetime.datetime):
                     value= value.strftime('%d.%m.%Y %H:%M:%S')
                 else:
                     value='### ' + str(type(value))
                 sheet.write(row_num, col_num, value)

        fields=[]; labels=[]
        # put labels to first_xls_row

        for col in rows_colnames:
             # t - table name
             # f - field name d[t][f]
            (t,f) = col.split('.')
            fields.append(f)
            labels.append( self.rows.db[t][f].label )
        list2xls(first_xls_row, labels)

        # put every table_row to xls_row
        for r_num, row in enumerate (self.rows, first_xls_row + 1):
             llist=[ row[f]  for f in fields]
             list2xls(r_num, llist)

        s = cStringIO.StringIO()
        book.save(s)
        return s.getvalue()


