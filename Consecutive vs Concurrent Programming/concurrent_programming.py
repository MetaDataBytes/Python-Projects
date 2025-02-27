from functions import build_list_of_team_members, pre_async_request, print_member_registration
import asyncio

if __name__ == "__main__":
    team = build_list_of_team_members(count=int(input("Enter the number of members to register: ")))
    team = asyncio.run(main=pre_async_request(team=team))
    print_member_registration(team=team)