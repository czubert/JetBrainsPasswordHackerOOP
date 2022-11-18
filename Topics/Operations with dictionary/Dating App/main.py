def select_dates(dates):
    return ', '.join([person['name'] for person in dates if
                      person['age'] > 30 and 'art' in person['hobbies'] and person['city'] == 'Berlin'])
