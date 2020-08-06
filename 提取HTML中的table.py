def table_Excel(content):  # Content 为html内容
    # print('123'*99)
    # print(type(content))
    if content.find('Original')>-1:
        content = content.split('Original')[0]  # 以Original作为分隔，只提取邮件中最新回复

    soup = BeautifulSoup(content, 'html.parser')
    try:
        tables = soup.find_all('table')  # 查看当前html页面所有table 元素<可能含有多个>
        file_name = MAIL_TABLE_PATH.format(time.time())  # 导出文件名 MAIL_TABLE_PATH
        # ExcelWriter is the class for writing DataFrame objects into excel sheets.
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')  # Excel 写操作对象
        workbook = writer.book  # 创建工作簿
        for idx, table in enumerate(tables):
            table_title = 'Table-' + str(idx)
            df_table = pd.read_html(str(table), header=0, flavor='bs4')[0]
            df_table.dropna(how='all', inplace=True)  # 当一整行都是nan时，去掉该行
            # print(df_table)
            df_table.to_excel(writer, index=False, sheet_name=table_title)  # 将df对象转换成Excel表格

            worksheet = writer.sheets[table_title] # 添加该子表
            # 对工作簿添加样式
            header_fmt = workbook.add_format({'font_size': 14, 'bold': True, 'fg_color': '#D7E4BC', 'border': 1})
            # 对子表的第一行的字段设置样式
            for col_num, value in enumerate(df_table.columns.values):
                worksheet.write(0, col_num, value, header_fmt)
            # 设置工作簿列宽
            worksheet.set_column('A:Z', 25)
        # # Close the Pandas Excel writer and output the Excel file.
        writer.save()
    except:
        print('Export Failed')
    else:
        print('Export End!')
    return file_name
