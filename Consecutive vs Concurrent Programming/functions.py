from aiolimiter import AsyncLimiter
import aiohttp
import json
import random as rand
import requests
import time

def build_list_of_team_members(count: int) -> list[dict[str, str]]:
    """
    PURPOSE: Build a random list, of size count, of names and job titles\n
    ARGUMENT: count (int): The number of members to make in the list\n
    RETURN: (list): A list of random names and job titles\n
    """
    names = ["justin", "jason", "amanda", "tracy", "destiny", "catherine", "robert", "hazel", "dillion", "matthew"]
    jobs = ["data analyst", "data engineer", "data scientist", "software developer", "software engineer", "leader", "product owner", "ai engineer", "ai developer", "solution architect"]
    return [{"name": names[rand.randint(a=0, b=len(names) - 1)], "job": jobs[rand.randint(a=0, b=len(jobs) - 1)]} for i in range(count)]

def get_time_counter() -> float:
    """
    PURPOSE: Get a float representing the current time\n
    ARGUMENT: None\n
    RETURN: (float): representation of current time\n
    """
    return time.perf_counter()

def print_member_registration(start: float, end: float, team: list[dict[str, str]]) -> None:
    """
    PURPOSE: print the member registration confirmations\n
    ARGUMENT: start (float): The start time of the request, end (float): the end time of the request, team (list): a list of api response from api\n
    RETURN: None\n
    """
    print(f"Total run time for processing {len(team)} team members is: {end - start}")
    for member in team: print(member["form"])

def make_request(member: dict[str, str]) -> json:
    """
    PURPOSE: Make request to api\n
    ARGUMENT: team (list): The team to register\n
    RETURN: (json): response from api confirming member registration\n
    """
    return requests.post(url="https://httpbin.org/post", data=member).json()

async def pre_async_request(team: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    PURPOSE: prep for async api request\n
    ARGUMENT: team (list): a list of names and job titles\n
    RETURN: (list): responses from api request\n
    """
    async with aiohttp.ClientSession() as session: 
        return [await async_request(session=session, member=member) for member in team]

async def async_request(session: aiohttp.ClientSession, member: dict[str, str]) -> json:
    """
    PURPOSE: Make async request to api\n
    ARGUMENT: session (ClientSession), person: (dict)\n
    RETURN: (json): response from api confirming member registration\n
    """
    async with AsyncLimiter(max_rate=10, time_period=60): 
        async with session.post(url="https://httpbin.org/post", data=member) as response: return await response.json()
