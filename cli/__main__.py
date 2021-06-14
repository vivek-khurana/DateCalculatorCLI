import argparse

from .date import get_days_difference, get_date_obj, is_date_valid


def main():
    my_parser = argparse.ArgumentParser(description='Calculate days difference with provided dates')

    # Arguments for Argparse CLI
    my_parser.add_argument('start_date', type=str, help='Please provide start date in format DD/MM/YYYY')
    my_parser.add_argument('end_date', type=str, help='Please provide end date in format DD/MM/YYYY')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    if is_date_valid(args.start_date) and is_date_valid(args.end_date):
        days_difference = get_days_difference(get_date_obj(args.start_date),
                                              get_date_obj(args.end_date))
        # Days difference will include start day count, so we need to subtract it by 1
        # in order to exclude partial start day and end day. Negative values will be shown as 0 as well
        print(f'Days between start date-{args.start_date} and end date-{args.end_date} is '
              f'{days_difference - 1 if days_difference > 0 else 0}')
    else:
        print('Start date or end date is invalid! Please provide date in format DD/MM/YYYY '
              'and range 01/01/1901-31/12/2999')


if __name__ == '__main__':
    main()
