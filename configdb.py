from configparser import ConfigParser 

def config(filename='db.ini', section='postgresql'): 
    """ 
    configures the db by providing the access keys 
    """

    # parser object
    parser = ConfigParser()

    # read the ini file
    parser.read(filename)

    # inputs for psycopy2 driver
    db = {}
    # check if the inputs are related to postgres
    if parser.has_section(section):
        # creating a list of lists with the values from the .ini file 
        # eg [['hostname', 'port'], ['dbuser', 'username']]
        params = parser.items(section)

        for param in params:
            # populating the db dictionary
            # converting the list of lists inti
            db[param[0]] = param[1]
    else:
        raise Exception('Requirements for {0} not found in file {1}'. format(section, filename))

    #return the  dictionary with the desired values 
    return db 
