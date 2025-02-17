from functions import build_list_of_team_members, make_request, print_member_registration, get_time_counter

team = build_list_of_team_members(count=int(input("Enter the number of members to register: ")))
start = get_time_counter()
team = [make_request(member=member) for member in team]
end = get_time_counter()
print_member_registration(start=start, end=end, team=team)