def readFileContent(filename):
    countries = []
    with open(filename, 'r') as file:
        for line in file:
            countries.append(line.rstrip().split(','))
    return countries

codes = readFileContent('country.csv')
for code in codes:
    country_code = code[0]
    iso2_country_code = code[1]
    sql = "UPDATE country SET iso2_country_code = '{}' WHERE country_code = '{}'".format(iso2_country_code, country_code)
    str = "IF  @@ERROR <> 0" \
          "\n     BEGIN" \
          "\n         SET @message = 'Error updating {}'" \
          "\n         GOTO rollback_handler" \
          "\n     END".format(country_code)
    print(sql)
    print(str)