from datetime import datetime, timedelta

def end_of_week_month_quarter(input_date):
    # Calculate End of Week (EOW)
    end_of_week = input_date + timedelta(days=(6 - input_date.weekday()))
   
    # Calculate End of Month (EOM)
    if input_date.month == 12:
        next_month_first_day = datetime(input_date.year + 1, 1, 1)
    else:
        next_month_first_day = datetime(input_date.year, input_date.month + 1, 1)
    end_of_month = next_month_first_day - timedelta(days=1)
   
    # Calculate End of Quarter (EOQ)
    current_quarter = (input_date.month - 1) // 3 + 1
    next_quarter_first_day = datetime(input_date.year + (1 if current_quarter % 4 == 0 else 0), (current_quarter % 4) * 3 + 1, 1)
    last_day_of_current_quarter = next_quarter_first_day - timedelta(days=1)
   
    # Adjust for leap year
    if last_day_of_current_quarter.month == 2 and last_day_of_current_quarter.day == 29:
        last_day_of_current_quarter = datetime(last_day_of_current_quarter.year, 2, 28)

    return end_of_week, end_of_month, last_day_of_current_quarter