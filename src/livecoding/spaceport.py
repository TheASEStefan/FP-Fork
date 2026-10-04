# Hello world!
def check_sum(landing_code: int) -> int:
    code_sum = 0
    while (landing_code):
        last_digit = landing_code % 10
        code_sum += last_digit
        landing_code = landing_code // 10

    return code_sum

# Suspicious Transmission - 2
digits = [0] * 10
def count_each_digit(landing_code: int) -> list[int]:
    while(landing_code):
        digit = landing_code % 10
        digits[digit] += 1
        landing_code //= 10

    return digits


def landing_status(checksum: int) -> str:
    check_code = checksum % 3
    if (check_code == 0):
        return "CLEARED"
    elif (check_code == 1):
        return "MANUAL_CHECK"
    else:
        return "HOLD"

def make_report(flight_code: int, check_sum_dict: int, landing_status_code: str) -> dict:
    return {"code": flight_code, "checksum": check_sum_dict, "status": landing_status_code}

# Basic Python variable readings.
operator_name = input("Operator name: ")
print("Welcome to Spaceport Control, " + operator_name + "!")
# landing_code = input("Landing code (non-negative integer): ")
# print("Received landing code: " + landing_code)
# inspection_status = input("Inspection is not yet available.")
# Print operations!

'''
print(operator_name)
print(landing_code)
print(landing_code_status)
print(inspection_status)
'''

'''
if landing_code.isdigit():
    check_operator_sum = check_sum(int(landing_code))
    print(check_operator_sum)
    landing_code_status = landing_status(check_operator_sum)
    print(landing_code_status)
    inspection_report = make_report(int(landing_code), check_operator_sum, landing_code_status)
'''


flight_reports_list = []

while True:
    print()
    print("1. Read landing code information")
    print("2. Show the flight log")
    print("3. Exit")
    option = input("Choose an option from above: ")
    if option == "1":
        landing_code = input("Landing code (non-negative integer): ")
        # Safer console - 3 ->>>
        while not landing_code.isdigit():
            print("Invalid landing code! Make sure to type in a positive integer!!")
            landing_code = input("Landing code (non-negative integer): ")
        landing_code_int = int(landing_code)
        check_sum_code = check_sum(landing_code_int)
        landing_code_status = landing_status(check_sum_code)
        flight_report = make_report(landing_code_int, check_sum_code, landing_code_status)
        print(flight_report)
        flight_reports_list.append(flight_report)
        print(f"Flight with code {landing_code} has checksum {check_sum_code} and status {landing_code_status}")
    elif option == "2":
        flight_reports_length = len(flight_reports_list)
        if flight_reports_length == 0:
            print("No spaceships inspected yet.")
        else:
            print(flight_reports_length)
            for flight_report in flight_reports_list:
                print(flight_report)
    elif option == "3":
        break
    else:
        # None of the valid options
        print("Invalid option. Aliens !!??")



# Traffic summary - 1
print()
flight_count_per_code = [0] * 3
for flight_report in flight_reports_list:
    flight_code = flight_report["checksum"] % 3
    flight_count_per_code[flight_code] += 1
for flight_status in range(3):
    flight_status_land = landing_status(flight_status)
    flight_status_report_count = str(flight_count_per_code[flight_status])
    print("Status: " + flight_status_land + " has " + flight_status_report_count + " reports.")




