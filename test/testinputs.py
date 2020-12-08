day1input = list(map(int, "1721 979 366 299 675 1456".split(' ')))

day2input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split('\n')

day3input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split('\n')

day4input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".split('\n\n')

day4invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""".split('\n\n')

day4valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a
ecl:blu byr:1944 eyr:2021 pid:093154719""".split('\n\n')

day5input = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL""".split('\n')

day5pairs = list(zip(day5input, [567, 119, 820]))

day6input = """abc

a
b
c

ab
ac

a
a
a
a

b""".split('\n\n')
day6anypairs = list(zip([x.split('\n') for x in day6input], [3, 3, 3, 1, 1]))
day6everypairs = list(zip([x.split('\n') for x in day6input], [3, 0, 1, 1, 1]))
