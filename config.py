from configparser import ConfigParser

def config_postgres(filename='config.ini',section='postgresql'):

    # creater a parser
    parser = ConfigParser()

    # read config file
    parser.read(filename)

    db_config = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1] # key-value
    else:
        raise Exception('Section{0} is not found in the {1} file.'.format(section, filename))

    #print(db_config)

    return db_config

def config_mysql(filename='config.ini',section='mysql'):

    # creater a parser
    parser = ConfigParser()

    # read config file
    parser.read(filename)

    db_config = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1] # key-value
    else:
        raise Exception('Section{0} is not found in the {1} file.'.format(section, filename))

    #print(db_config)

    return db_config

if __name__ == "__main__":
    
    db_config = config_mysql()
    print(db_config)