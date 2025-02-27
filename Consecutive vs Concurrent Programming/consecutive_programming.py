from functions import build_list_of_team_members, make_request, print_member_registration

if __name__ == "__main__":
    team = build_list_of_team_members(count=int(input("Enter the number of members to register: ")))
    team = [make_request(member=member) for member in team]
    print_member_registration(team=team)