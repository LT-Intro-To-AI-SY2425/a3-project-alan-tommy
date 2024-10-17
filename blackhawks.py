from movies import hockey_db
from blackhawks import match

def get_points(blackHawk: Tuple[str, str, int, List[str]]) -> str:
    return blackHawk[0]

def get_height(blackHawk: Tuple[str, str, int, List[str]]) -> str:
    return blackHawk[1]


def get_weight(blackHawk: Tuple[str, str, int, List[str]]) -> int:
    return blackHawk[2]


def get_number(blackHawk: Tuple[str, str, int, List[str]]) -> List[str]:
    return blackHawk[3]


