from collections import namedtuple, defaultdict
import re


Claim = namedtuple('Claim', ['claim_id', 'left', 'top', 'width', 'height'])


def read_claims(filename):
    claime_re = re.compile(
        '(?P<claim_id>\d+) @ (?P<left>\d+),(?P<top>\d+): (?P<width>\d+)x(?P<height>\d+)'
    )
    claims = []
    with open(filename, 'rt') as input_file:
        for line in input_file:
            match = claime_re.search(line)
            if match:
                groupdict = match.groupdict()
                claims.append(Claim(**{key: int(value) for key, value in groupdict.items()}))
    return claims


def build_fabric_usage(claims):
    fabric_usage = defaultdict(int)
    for claim in claims:
        for x in range(claim.left, claim.left + claim.width):
            for y in range(claim.top, claim.top + claim.height):
                fabric_usage[(x, y)] += 1
    return fabric_usage


def count_reused_fabric(fabric_usage):
    return sum(1 for usage_count in fabric_usage.values() if usage_count > 1)


def find_sole_usage_claim(fabric_usage, claims):

    def check_claim_is_sole_usage(claim):
        return all(
            fabric_usage[(x, y)] == 1
            for x in range(claim.left, claim.left + claim.width)
            for y in range(claim.top, claim.top + claim.height)
        )

    for claim in claims:
        if check_claim_is_sole_usage(claim):
            return claim

def main():
    filename = 'input/day03.txt'
    claims = read_claims(filename)
    fabric_usage = build_fabric_usage(claims)

    print(count_reused_fabric(fabric_usage))
    print(find_sole_usage_claim(fabric_usage, claims))


if __name__ == '__main__':
    main()
