import iden
import collections
from datetime import datetime, timedelta, date


# user_story_1: Dates before current date
# Author: Shaopeng Ge
def record_error(id,message,res,res_error):
    print(message)
    res.append(id)
    res_error.append(message)

def user_story_01(ind_list,fam_list):
    res = []
    res_error= []
    today = str(date.today())
    #check ind's birthday and death date
    for i in ind_list:
        birthday = i.birthday
        death = i.death
        id = i.id
        #check birthday of ind
        if birthday > today:
            message = "ERROR: INDIVIDUAL: US01: " + id + ": birthday " + birthday + " is before current date " + today
            record_error(id,message,res,res_error)
        #check death date of ind
        if death != "NA" and death > today:
            message = "ERROR: INDIVIDUAL: US01: " + id + ": death date " + death + " is before current date " + today
            record_error(id,message,res,res_error)


    #check fam's marriage date and divorce date
    for i in fam_list:
        id = i.id
        married = i.married
        divorced = i.divorced
        #check marriage date
        if married != "NA" and married > today:
            message = "ERROR: FAMILY: US01: " + id + ": marriage date " + married + " is before current date " + today
            record_error(id,message,res,res_error)
        #check divorce date
        if divorced != "NA" and divorced > today:
            message = "ERROR: FAMILY: US01: " + id + ": divorce date " + married + " is before current date " + today
            record_error(id,message,res,res_error)
    return res,res_error


# Author Qizhan Liu
def us_02(ind_list, fam_list):
    prompt = "Birth before marriage"
    res = []
    res_error = []
    for fam in fam_list:
        for ind in ind_list:
            if fam.husband_name == ind.name or fam.wife_name == ind.name:
                birthday = ind.birthday
                marriage = fam.married
                birthday = birthday.split('-')
                marriage = marriage.split('-')
                wrong = False
                for i in range(3):
                    if int(marriage[i]) > int(birthday[i]):
                        # print(prompt)
                        break
                    if int(marriage[i]) < int(birthday[i]):
                        wrong = True
                        break
                if wrong:
                    print("ERROR: INDIVIDUAL: US02: " + ind.id + ": Married "
                          + fam.married + " before born " + ind.birthday)
                    res.append(ind.id)
                    res_error.append("ERROR: INDIVIDUAL: US02: " + ind.id + ": Married "
                                     + fam.married + " before born " + ind.birthday)
    return res, res_error


# Author Qizhan Liu and Shaopeng Ge
def us_03(ind_list):
    res = []
    res_error = []
    for ind in ind_list:
        birthday = ind.birthday
        death = ind.death
        if death != 'NA':
            birthday = birthday.split('-')
            death = death.split('-')
            wrong = False
            for i in range(3):
                if int(birthday[i]) <= int(death[i]):
                    continue
                if int(birthday[i]) > int(death[i]):
                    wrong = True
                    break
            if wrong:
                print("ERROR: INDIVIDUAL: US03: " + ind.id + ": Died " + ind.death + " before born" + ind.birthday)
                res.append(ind.id)
                res_error.append("ERROR: INDIVIDUAL: US03: " + ind.id + ": Died "
                                 + ind.death + " before born" + ind.birthday)
    return res, res_error


# return list of family id that divorced before married
# Author Mo Sun
def us_04(fam_list):
    res = []
    res_error= []
    for fam in fam_list:
        married = fam.married
        divorced = fam.divorced
        if divorced != 'NA':
            married = married.split('-')
            divorced = divorced.split('-')
            wrong = False
            for i in range(3):
                if int(married[i]) < int(divorced[i]):
                    break
                if int(married[i]) > int(divorced[i]):
                    wrong = True
                    break
            if wrong:
                print("ERROR: FAMILY: US04: " + fam.id + ": Divorced " + fam.divorced + " before married " + fam.married)
                res.append(fam.id)
                res_error.append("ERROR: FAMILY: US04: " + fam.id + ": Divorced " + fam.divorced + " before married " + fam.married)
    return res,res_error

# Author Yiming Xu
def user_story_5(test_ind_list,test_fam_list):
    s1 = 'Marriage before death'
    res = []
    res_error = []
    for i in test_ind_list:
        id = i.id
        death = i.death
        for item in test_fam_list:
            if item.husband_id == id and item.married > death:
                print("ERROR: FAMILY: US05: %s: Marriage %s after Husband's death %s" %(item.id,item.married,death))
                res0 = "ERROR: FAMILY: US05: %s: Marriage %s after Husband's death %s" % (item.id, item.married, death)
                res.append(item.husband_id)
                res_error.append(res0)

            if item.wife_id == id and item.married > death:
                print("ERROR: FAMILY: US05: %s: Marriage %s after Wife's death %s" %(item.id,item.married,death))
                res0 = "ERROR: FAMILY: US05: %s: Marriage %s after Wife's death %s" %(item.id,item.married,death)
                res.append(s1)
                res_error.append(res0)
    return res,res_error

## Author Yiming Xu and Mo Sun
## Pair Programming
def user_story_6(test_ind_list,test_fam_list):
    res = []
    res_error=[]
    for i in test_ind_list:
        id = i.id
        death = i.death
        for item in test_fam_list:
            if item.husband_id == id and item.divorced > death:
                print("ERROR: FAMILY: US06: %s: Divorce %s after Husband's death %s" %(item.id,item.divorced,death))
                res2 = "ERROR: FAMILY: US06: %s: Divorce %s after Husband's death %s" % (item.id, item.divorced, death)
                res.append(item.husband_id)
                res_error.append(res2)
            if item.wife_id == id and item.divorced > death:
                print("ERROR: FAMILY: US05: %s: Divorce %s after Wife's death %s" %(item.id,item.divorced,death))
                res4 = "ERROR: FAMILY: US05: %s: Divorce %s after Wife's death %s" %(item.id,item.divorced,death)
                res.append(item.wife_id)
                res_error.append(res4)
    return res,res_error

## Author Yiming Xu
def user_story_7(test_ind_list):
    res = []
    res_error = []
    for i in test_ind_list:
        id = i.id
        if i.age > 150:
            print("ERROR: INDIVIDUAL: US07: %s: More than 150 years old - Birth date %s " %(id,i.birthday))
            res1 = "ERROR: INDIVIDUAL: US07: %s: More than 150 years old - Birth date %s " %(id,i.birthday)
            res.append(id)
            res_error.append(res1)
    return res,res_error

# Author Yiming Xu
def user_story_8(test_ind_list,test_fam_list):
    res = []
    res_error = []
    for i in test_ind_list:
        id = i.id
        birth = i.birthday
        for item in test_fam_list:
            if id in item.children and item.married > birth:
                res0 = 'ANOMALY: FAMILY: US08: %s: Child %s born before parents marriage on %s' %(item.id,id,item.married)
                print(res0)
                res_error.append(res0)
                res.append(item.id)
    return res,res_error

# Author Shaopeng Ge
def user_story_9(ind_list):
    res = []
    res_error = []
    for ind in ind_list:
        if ind.death != 'NA' and ind.child != 'NA':
            death = ind.death
            for kid in ind.child:
                for i in ind_list:
                    if i.id == kid:
                        birthday = i.birthday 
                        if ind.gender == 'M':
                            if (datetime.strptime(birthday, '%Y-%m-%d') > (datetime.strptime(death, '%Y-%m-%d') + timedelta(days=270))):
                                message = "ERROR: INDIVIDUAL: US09: " + i.id + ": birthday " + birthday + " is not before 9 months after father's death " + death
                                record_error(i.id,message,res,res_error)
                        else:
                            if death < birthday:
                                message = "ERROR: INDIVIDUAL: US09: " + i.id + ": birthday " + birthday + " is after mother's death " + death
                                record_error(i.id,message,res,res_error)
    return res, res_error
                            
# Author Shaopeng Ge
def user_story_10(ind_list,fam_list):
    res = []
    res_error = []
    for fam in fam_list:
        if fam.married != 'NA':
            marriage = fam.married
            Husband = fam.husband_id
            Wife = fam.wife_id
            for ind in ind_list:
                if ind.id == Husband:
                    birthday = ind.birthday
                    if (datetime.strptime(marriage, '%Y-%m-%d') < (datetime.strptime(birthday, '%Y-%m-%d') + timedelta(days=14*365))):
                        message = "ERROR: INDIVIDUAL: US10: " + ind.id + ": marriage " + marriage + " before 14 years old"
                        record_error(ind.id,message,res,res_error)
                if ind.id == Wife:
                    birthday = ind.birthday
                    if (datetime.strptime(marriage, '%Y-%m-%d') < (datetime.strptime(birthday, '%Y-%m-%d') + timedelta(days=14*365))):
                        message = "ERROR: INDIVIDUAL: US10: " + ind.id + ": marriage " + marriage + " before 14 years old"
                        record_error(ind.id,message,res,res_error)
    return res, res_error

# Author Qizhan Liu
def user_story_11(ind_list,fam_list):
    res = []
    res_error = []
    for fam in fam_list:
        if fam.divorced != 'NA':
            divorced = fam.divorced
            husband_id = fam.husband_id
            wife_id = fam.wife_id
            for ind in ind_list:
                if ind.id == husband_id:
                    spouse_id = ind.spouse.pop()
                    if spouse_id != wife_id:
                        for fam2 in fam_list:
                            if fam2.wife_id == spouse_id:
                                if fam2.married < divorced:
                                    message = "ERROR: FAMILY: US011: in " + fam.id + ", "+ ind.id + " remarriage " + fam2.married + " before divorce "+ divorced
                                    record_error(ind.id,message,res,res_error)
                                    break
                if ind.id == wife_id:
                    spouse_id = ind.spouse.pop()
                    if spouse_id != husband_id:
                        for fam2 in fam_list:
                            if fam2.husband_id == spouse_id:
                                if fam2.married < divorced:
                                    message = "ERROR: FAMILY: US011: in " + fam.id + ", "+ ind.id + " remarriage " + fam2.married + " before divorce "+ divorced
                                    record_error(ind.id,message,res,res_error)
    return res, res_error

# Author Qizhan Liu
def user_story_12(ind_list):
    res = []
    res_error = []
    for ind in ind_list:
        if ind.child != 'NA':
            for kid in ind.child:
                for i in ind_list:
                    if i.id == kid:
                        if ind.gender == 'F':
                            if ((datetime.strptime(i.birthday, '%Y-%m-%d') - datetime.strptime(ind.birthday, '%Y-%m-%d')) > timedelta(days=365*60)):
                                message = "ERROR: INDIVIDUAL: US012: " + ind.id + " is more than 60 years older than her child " + i.id
                                record_error(ind.id,message,res,res_error)
                        else:
                            if ((datetime.strptime(i.birthday, '%Y-%m-%d') - datetime.strptime(ind.birthday, '%Y-%m-%d')) > timedelta(days=365*80)):
                                message = "ERROR: INDIVIDUAL: US012: " + ind.id + " is more than 80 years older than his child " + i.id
                                record_error(ind.id,message,res,res_error)
    return res, res_error


# Author Mo Sun
def user_story_13(ind_list,fam_list):
    res = []
    res_error = []
    for fam in fam_list:
        if fam.children != 'NA':
            children = []
            birthday = []
            for child in fam.children:
                for ind in ind_list:
                    if ind.id == child:
                        children.append(ind.id)
                        birthday.append(ind.birthday)
            if len(birthday) > 1:
                for i in range(len(birthday)-1):
                    for j in range(i+1,len(birthday)):
                        datedif1 = (abs(datetime.strptime(birthday[i], '%Y-%m-%d') - datetime.strptime(birthday[j], '%Y-%m-%d')) >= timedelta(days=2))
                        datedif2 = (abs(datetime.strptime(birthday[i], '%Y-%m-%d') - datetime.strptime(birthday[j], '%Y-%m-%d')) < timedelta(days=240))
                        if datedif1 and datedif2 :
                            message = "ERROR: FAMILY: US013: in " + fam.id + ", Siblings spacing between " + children[i] + " and " + children[j] + " are wrong"
                            record_error(fam.id,message,res,res_error)
    return res, res_error

# Author Mo Sun
def user_story_14(ind_list,fam_list):
    res = []
    res_error = []
    for fam in fam_list:
        if fam.children != 'NA':
            children = []
            birthday = []
            find = False
            for child in fam.children:
                for ind in ind_list:
                    if ind.id == child:
                        children.append(ind.id)
                        birthday.append(ind.birthday)
            if len(birthday) > 5:
                for i in range(len(birthday)-4):
                    if find == True:
                        break
                    count = 1
                    for j in range(i+1,len(birthday)):
                        if (datetime.strptime(birthday[i], '%Y-%m-%d') == datetime.strptime(birthday[j], '%Y-%m-%d')):
                            count += 1
                        if count > 5:
                            message = "ERROR: FAMILY: US014: in " + fam.id + ", more than five siblings borned at the same time " + birthday[i]
                            record_error(fam.id,message,res,res_error)
                            find = True  
                            break              
    return res, res_error

# Author Yiming Xu
def user_story_15(fam_list):
    res = []
    res_error = []
    for fam in fam_list:
        if len(fam.children) >= 15:
            message = "ERROR: FAMILY: US015: in " + fam.id + ", more than 14 siblings in a family"
            record_error(fam.id,message,res,res_error)
    return res, res_error

# Author Yiming Xu
def user_story_16(ind_list,fam_list):
    res = []
    res_error = []
    for fam in fam_list:
        familyName = fam.husband_name.split('/')[1]
        for ind in ind_list:
            if ind.id in fam.children and ind.gender == "M":
                if ind.name.split('/')[1] != familyName:
                    message = "ERROR: FAMILY: US016: in " + fam.id + ", not all male members of a family have the same last name"
                    record_error(fam.id,message,res,res_error)
                    break
    return res, res_error


# Parents should not marry any of their children
def user_story_17(fam_list):
    error_ids = []
    error_messages = []
    for fam in fam_list:
        if fam.children and fam.children != 'NA':
            if fam.husband_id in fam.children:
                message = "ERROR: FAMILY: US017: in %s, wife (%s) married with her children" % (fam.id, fam.wife_id)
                record_error(fam.id, message, error_ids, error_messages)
            if fam.wife_id in fam.children:
                message = "ERROR: FAMILY: US017: in %s, husband (%s) married with his children" % (fam.id, fam.husband_id)
                record_error(fam.id, message, error_ids, error_messages)

    return error_ids, error_messages


# Siblings should not marry
def user_story_18(fam_list):
    error_ids = []
    error_messages = []
    children_list = []
    for fam in fam_list:
        if fam.children and fam.children != 'NA':
            children_list.append(fam.children)

    for fam in fam_list:
        for children in children_list:
            if fam.husband_id in children and fam.wife_id in children:
                message = 'ERROR: FAMILY: US018: in %s, husband (%s) and wife (%s) are siblings' \
                          % (fam.id, fam.husband_id, fam.wife_id)
                record_error(fam.id, message, error_ids, error_messages)

    return error_ids, error_messages


# First cousins should not marry one another
def user_story_19(ind_list, fam_list):
    error_ids = []
    error_messages = []
    for fam in fam_list:
        if fam.children and len(fam.children) >= 2:
            children_list = []
            for sibling in fam.children:
                for ind in ind_list:
                    if ind.id == sibling and ind.child != 'NA':
                        children_list.append(ind.child)

            if len(children_list) < 2:
                continue

            for fam2 in fam_list:
                husband_index, wife_index = -1, -1
                for index, chidren in enumerate(children_list):
                    if fam2.husband_id in chidren:
                        husband_index = index
                    if fam2.wife_id in chidren:
                        wife_index = index

                if husband_index >= 0 and wife_index >= 0 and husband_index != wife_index:
                    message = 'ERROR: FAMILY: US019: in %s, husband (%s) and wife (%s) are first cousins' \
                              % (fam2.id, fam2.husband_id, fam2.wife_id)
                    record_error(fam2.id, message, error_ids, error_messages)

    return error_ids, error_messages


# Aunts and uncles should not marry their nieces or nephews
def user_story_20(fam_list):
    error_ids = []
    error_messages = []
    for fam in fam_list:
        if fam.children and fam.children != 'NA':
            if fam.husband_id in fam.children:
                for fam2 in fam_list:
                    if fam2.husband_id != fam.husband_id and fam.husband_id in fam2.children:
                        message = "ERROR: FAMILY: US020: in %s, aunts (%s) married with her children" % (fam.id, fam.wife_id)
                        record_error(fam.id, message, error_ids, error_messages)
            if fam.wife_id in fam.children:
                for fam2 in fam_list:
                    if fam2.wife_id == fam.wife_id and fam.wife_id in fam2.children:
                        message = "ERROR: FAMILY: US020: in %s, uncles (%s) married with his children" % (fam.id, fam.husband_id)
                        record_error(fam.id, message, error_ids, error_messages)

    return error_ids, error_messages


# Husband in family should be male and wife in family should be female
def user_story_21(ind_list, fam_list):
    error_ids = []
    error_messages = []

    for fam in fam_list:
        for ind in ind_list:
            if fam.husband_id == ind.id and ind.gender != 'M':
                message = "ERROR: FAMILY: US021: in %s, husband (%s) is not male" % (fam.id, fam.husband_id)
                record_error(fam.id, message, error_ids, error_messages)
            if fam.wife_id == ind.id and ind.gender != 'F':
                message = "ERROR: FAMILY: US021: in %s, wife (%s) is not female" % (fam.id, fam.wife_id)
                record_error(fam.id, message, error_ids, error_messages)

    return error_ids, error_messages


# All individual IDs should be unique and all family IDs should be unique
def user_story_22(ind_list, fam_list):
    error_ids = []
    error_messages = []

    ind_ids = [ind.id for ind in ind_list]
    fam_ids = [fam.id for fam in fam_list]
    duplicate_inds = [item for item, count in collections.Counter(ind_ids).items() if count > 1]
    duplicate_fams = [item for item, count in collections.Counter(fam_ids).items() if count > 1]

    for id in duplicate_inds:
        message = "ERROR: INDIVIDUAL: US022: Individual id (%s) duplicates" % id
        record_error(id, message, error_ids, error_messages)
    for id in duplicate_fams:
        message = "ERROR: FAMILY: US022: Family id (%s) duplicates" % id
        record_error(id, message, error_ids, error_messages)

    return error_ids, error_messages


# No more than one individual with the same name and birth date should appear in a GEDCOM file
def user_story_23(ind_list):
    error_ids = []
    error_messages = []

    names = [ind.name for ind in ind_list]
    duplicate_names = [item for item, count in collections.Counter(names).items() if count > 1]

    for name in duplicate_names:
        message = "ERROR: INDIVIDUAL: US023: Individual name (%s) duplicates" % name
        record_error(name, message, error_ids, error_messages)

    return error_ids, error_messages


if __name__ == '__main__':
    ind_list = iden.read_ind_info('project.ged')
    ind_table = iden.create_ind_table(ind_list)
    fam_list = iden.read_fam_info('project.ged')
    fam_table = iden.creat_fam_table(fam_list)

    print(ind_table)
    print(fam_table)

    with open('output.txt', 'w') as file:
        file.write(str(ind_table))
        file.write('\n')
        file.write(str(fam_table))
        file.write('\n')

        def writedowm(res_error):
            for i in res_error:
                file.write(str(i) + '\n')

        writedowm(user_story_01(ind_list,fam_list)[1])
        writedowm(us_02(ind_list, fam_list)[1])
        writedowm(us_03(ind_list)[1])
        writedowm(us_04(fam_list)[1])
        writedowm(user_story_5(ind_list,fam_list)[1])
        writedowm(user_story_6(ind_list,fam_list)[1])
        writedowm(user_story_7(ind_list)[1])
        writedowm(user_story_8(ind_list,fam_list)[1])
        writedowm(user_story_9(ind_list)[1])
        writedowm(user_story_10(ind_list,fam_list)[1])
        writedowm(user_story_11(ind_list,fam_list)[1])
        writedowm(user_story_12(ind_list)[1])
        writedowm(user_story_13(ind_list,fam_list)[1])
        writedowm(user_story_14(ind_list,fam_list)[1])
        writedowm(user_story_15(fam_list)[1])
        writedowm(user_story_16(ind_list,fam_list)[1])
        writedowm(user_story_17(fam_list)[1])
        writedowm(user_story_18(fam_list)[1])
        writedowm(user_story_19(ind_list, fam_list)[1])
        writedowm(user_story_20(fam_list)[1])
        writedowm(user_story_21(ind_list, fam_list)[1])
        writedowm(user_story_22(ind_list, fam_list)[1])
        writedowm(user_story_23(ind_list)[1])