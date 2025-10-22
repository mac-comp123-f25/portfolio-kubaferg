betsy_info = {'Name': 'Betsy Foobar',
              'Phone': 'x8012',
              'Street': '1600 Grand Avenue',
              'City': 'Saint Paul',
              'State': 'MN',
              'Email': 'bfoobar@macalester.edu'}

tom_info = {'Name': 'Tom Riddle',
            'Phone': 'x8512',
            'Street': '1600 Grand Avenue',
            'City': 'Saint Paul',
            'State': 'MN',
            'Email': 'triddle@macalester.edu'}
kuba_info = {'Name': 'Kuba Ferguson',
            'Phone': '4172',
            'Street': '3325 Westheimer Rd',
            'City': 'Houston',
            'State': 'TX',
            'Email': 'kubaferg@gmail.com'}
amin_info = {'Name': 'Amin Alhashim',
            'Phone': '4261',
            'Street': '2115 Main Street',
            'City': 'New York City',
            'State': 'NY',
            'Email': 'amin@gmail.com'}
address_book = [ betsy_info, tom_info, kuba_info, amin_info,
                {'Name': 'Susan Fox',
                 'Phone': 'x6553',
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'} ]
def filter_by_city (city, book):
    if city in book:
        return


