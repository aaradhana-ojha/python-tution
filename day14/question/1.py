def convert_date_format(date_str):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    mm, dd, yyyy = date_str.split('/')
    month_name = months[int(mm) - 1]
    return month_name + " " + str(int(dd)) + ", " + yyyy

date_input = input("Enter a date in mm/dd/yyyy format: ")
print(convert_date_format(date_input))
