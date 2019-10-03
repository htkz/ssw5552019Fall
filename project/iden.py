from prettytable import PrettyTable
import calendar
import string


class Individual:
    def __init__(self, id, name, gender, birthday, age, alive, death, child, spouse):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.age = age
        self.alive = alive
        self.death = death
        self.child = child
        self.spouse = spouse


class Family:
    def __init__(self, id, married, divorced, husband_id, husband_name, wife_id, wife_name, children):
        self.id = id
        self.married = married
        self.divorced = divorced
        self.husband_id = husband_id
        self.husband_name = husband_name
        self.wife_id = wife_id
        self.wife_name = wife_name
        self.children = children


# get individual info from file
# return list(Individual.obj)
def read_ind_info(path):
    res = []
    with open(path) as f:
        list1 = []
        for idx, line in enumerate(f):
            a = line.strip()
            b = a.split(' ')
            list1.append(b)

        for idx, item in enumerate(list1):
            if len(item) > 2 and item[2] == 'INDI':
                id = item[1]

                # print(id)

                Name = ''
                if list1[idx + 1][1] == 'NAME':
                    for i in list1[idx + 1][2:]:
                        Name += str(i)
                else:
                    Name = 'NA'
                # print(Name)
                if list1[idx + 5][1] == 'SEX':

                    Gender = list1[idx + 5][2]
                else:
                    Gender = 'NA'

                # print(Gender)

                Birthday = list1[idx + 7][4] + '-' + str(
                    list(calendar.month_abbr).index(string.capwords(list1[idx + 7][3]))) + '-' + \
                           list1[idx + 7][2]

                # print(Birthday)
                if list1[idx + 8][1] == 'DEAT':
                    Age = int(list1[idx + 9][4]) - int(list1[idx + 7][4])
                    Alive = False
                    Death = list1[idx + 9][4] + '-' + str(
                        list(calendar.month_abbr).index(string.capwords(list1[idx + 9][3]))) + '-' + list1[idx + 9][2]
                else:
                    Age = 2019 - int(list1[idx + 7][4])
                    Alive = True
                    Death = 'NA'

                # print(Age)

                # if list1[idx + 8][1] == 'DEAT':
                #     Alive = False
                #     Death = list1[idx + 9][4] + '-' + str(
                #         list(calendar.month_abbr).index(string.capwords(list1[idx + 9][3]))) + '-' + list1[idx + 9][2]
                # else:
                #     Alive = True
                #     Death = 'NA'

                list2 = []
                spouse = ''
                famid = ''
                if list1[idx + 8][1] == 'DEAT':
                    if list1[idx + 10][1] == 'FAMS':
                        famid += list1[idx + 10][2]

                elif list1[idx + 8][1] == 'FAMS':
                    famid += list1[idx + 8][2]
                    # print(famid)

                for index, items in enumerate(list1):
                    if items[1] == famid:
                        Index = index + 3
                        while list1[Index][1] == 'CHIL':
                            list2.append(list1[Index][2].strip('@'))
                            Index += 1

                Child = ''
                if list2 != []:
                        Child = set(list2)

                else:
                    Child = 'NA'

                spouse = []
                for index, items in enumerate(list1):
                    if items[1] == famid:
                        if list1[index + 1][2] == id:
                            spouse.append(list1[index + 2][2].strip('@'))
                        if list1[index + 2][2] == id:
                            spouse.append(list1[index + 1][2].strip('@'))
                if spouse != []:
                    Spouse = set(spouse)
                else:
                    Spouse = 'NA'

                indi = Individual(id.strip('@'), Name, Gender, Birthday, Age, Alive, Death, Child, Spouse)
                res.append(indi)

    return res


# create pretty table from ind_list
def create_ind_table(ind_list):
    table = PrettyTable(field_names=['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
    table.padding_width = 1
    for ind in ind_list:
        table.add_row(
            [ind.id, ind.name, ind.gender, ind.birthday, ind.age, ind.alive, ind.death, ind.child, ind.spouse])
    return table


# get family info from file
# return list(Family.obj)
def read_fam_info(path):
    res = []
    with open(path) as f:
        list1 = []
        for idx, line in enumerate(f):
            a = line.strip()
            b = a.split(' ')
            list1.append(b)

        for idx, item in enumerate(list1):
            ID = ''
            if len(item) > 2 and item[2] == 'FAM':
                ID = item[1]

            for index, items in enumerate(list1):
                Married = ''
                Divorced = ''
                if items[1] == ID:
                    Index = index + 3
                    while list1[Index][1] != 'MARR':
                        Index += 1
                    Married = list1[Index + 1][4] + '-' + str(
                        list(calendar.month_abbr).index(string.capwords(list1[Index + 1][3]))) + '-' + \
                              list1[Index + 1][2]
                    if list1[Index + 2][1] == 'DIV':
                        Divorced = list1[Index + 3][4] + '-' + str(
                            list(calendar.month_abbr).index(string.capwords(list1[Index + 3][3]))) + '-' + \
                                   list1[Index + 3][2]
                    else:
                        Divorced = 'NA'
                    HusbandID = list1[index + 1][2]
                    WifeID = list1[index + 2][2]
                    HusbandName = ''
                    for num, thing in enumerate(list1):
                        if thing[1] == HusbandID:
                            for i in list1[num + 1][2:]:
                                HusbandName += str(i)
                    WifeName = ''
                    for num, thing in enumerate(list1):
                        if thing[1] == WifeID:
                            for i in list1[num + 1][2:]:
                                WifeName += str(i)
                    list2 = []
                    for num, thing in enumerate(list1):
                        if thing[1] == ID:
                            Num = num + 3
                            while list1[Num][1] == 'CHIL':
                                list2.append(list1[Num][2].strip('@'))
                                Num += 1

                    if list2 != []:
                        Child = set(list2)

                    else:
                        Child = 'NA'
                    res.append(
                        Family(ID.strip('@'), Married, Divorced, HusbandID.strip('@'), HusbandName, WifeID.strip('@'),
                               WifeName, Child))
    return res


# create pretty table from fam_list
def creat_fam_table(fam_list):
    table = PrettyTable(
        field_names=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
    table.padding_width = 1
    for fam in fam_list:
        table.add_row([fam.id, fam.married, fam.divorced, fam.husband_id, fam.husband_name, fam.wife_id, fam.wife_name,
                       fam.children])
    return table


if __name__ == '__main__':
    ind_list = read_ind_info('project03.ged')
    ind_table = create_ind_table(ind_list)
    print(ind_table)

    fam_list = read_fam_info('project03.ged')
    fam_table = creat_fam_table(fam_list)
    print(fam_table)

    # a = printIndTable()
    # b = printFamTable()
    # print(a)
    # print(b)
    #
    # with open('output.txt', 'w') as file:
    #     file.write(str(a))
    #     file.write(str(b))
