import json
import datetime

def lambda_handler(event, context):
    # Get the current date and calculate the time delta since your birthday
    birthday = datetime.datetime(1977, 9, 22)
    today = datetime.datetime.now()
    delta = today - birthday

    # Calculate the number of years, days, hours, minutes, and seconds in the delta
    years = delta.days // 365
    days = delta.days % 365
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Create a response dictionary with the time components
    response = {
        'years_since_birthday': years,
        'days_since_birthday': days,
        'hours_since_birthday': hours,
        'minutes_since_birthday': minutes,
        'seconds_since_birthday': seconds
    }

    # Return the response as JSON
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(response)
    }
