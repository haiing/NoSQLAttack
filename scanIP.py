import  shodan

def scanMongoDBIP():
    SHODAN_API_KEY = "9kwHl4vdqoXjeKl7iXOHMvXGT3ny85Ig";
    api = shodan.Shodan(SHODAN_API_KEY);
    print 'Start Scanning.....'
    try:
        results = api.search('mongoDB')

        print 'Results found:%s' % results['total']
        for result in results['matches']:
            print 'IP:%s' % result['ip_str']
            #print result['data']
            #print 'hostnames:' % result['hostnames'];
            #print ' '
    except shodan.APIError, e:
        print 'Error:%s' % e
#if __name__ == "__main__":
#    scanMongoDBIP()
