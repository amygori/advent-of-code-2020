import re


class PassportValidator:

    def __init__(self, passport):
        self.valid = True
        self.report = []

    @classmethod
    def validate(self, passport):
        self.__init__(self, passport)
        self.validate_all_the_things(self, passport)
        return self.valid

    def validate_all_the_things(self, passport):
        self.validate_byr(self, passport['byr'])
        self.validate_iyr(self, passport['iyr'])
        self.validate_eyr(self, passport['eyr'])
        self.validate_hgt(self, passport['hgt'])
        self.validate_hcl(self, passport['hcl'])
        self.validate_ecl(self, passport['ecl'])
        self.validate_pid(self, passport['pid'])

    def mark_invalid(self, key):
        self.valid = False
        self.report.append(key)

    def validate_byr(self, byr):
        """
        four digits; at least 1920 and at most 2002
        """
        if not self.valid:
            return
        if int(byr) not in range(1920, 2002):
            self.mark_invalid(self, 'byr')

    def validate_iyr(self, iyr):
        """
        four digits; at least 2010 and at most 2020
        """
        if not self.valid:
            return
        if int(iyr) not in range(2010, 2021):
            self.mark_invalid(self, 'iyr')

    def validate_eyr(self, eyr):
        """
        four digits; at least 2020 and at most 2030
        """
        if not self.valid:
            return
        if int(eyr) not in range(2020, 2031):
            self.mark_invalid(self, 'eyr')

    def validate_hgt(self, hgt):
        """
        a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
        """
        unit = hgt[-2:]
        measurement = hgt[:-2]
        if not self.valid:
            return
        if not measurement:
            self.mark_invalid(self, 'hgt')
        if unit == 'cm' and int(measurement) not in range(150, 194):
            self.mark_invalid(self, 'hgt')
        elif unit == 'in' and int(measurement) not in range(59, 77):
            self.mark_invalid(self, 'hgt')

    def validate_hcl(self, hcl):
        """
        a # followed by exactly six characters 0-9 or a-f
        """
        if not self.valid:
            return
        if not re.fullmatch("^#[0-9a-fA-F]{6}", hcl):
            self.mark_invalid(self, 'hcl')

    def validate_ecl(self, ecl):
        """
        exactly one of: amb blu brn gry grn hzl oth
        """
        if not self.valid:
            return
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            self.mark_invalid(self, 'ecl')

    def validate_pid(self, pid):
        """
        a nine-digit number, including leading zeroes.
        """
        if not self.valid:
            return
        if not re.fullmatch("^[0-9]{9}", pid):
            self.mark_invalid(self, 'pid')
