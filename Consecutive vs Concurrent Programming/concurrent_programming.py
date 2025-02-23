from functions import build_list_of_team_members, pre_async_request, print_member_registration, get_time_counter
import asyncio

if __name__ == "__main__":
    team = build_list_of_team_members(count=int(input("Enter the number of members to register: ")))
    start = get_time_counter()
    team = asyncio.run(main=pre_async_request(team=team))
    end = get_time_counter()
    print_member_registration(start=start, end=end, team=team)