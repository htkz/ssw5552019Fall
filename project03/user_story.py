import iden
import unittest
ind_list = iden.read_ind_info('project03.ged')

fam_list = iden.read_fam_info('project03.ged')


# return list of family id that divorced before married
# Author Mo Sun
def us_04(fam_list):
    res = []
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
    return res

# Author Yiming Xu
def user_story_5(test_ind_list,test_fam_list):
    res = None
    for i in test_ind_list:
        id = i.id
        death = i.death
        for item in test_fam_list:
            if item.husband_id == id and item.married < death:
                print('Marriage before death')
                res = 'Marriage before death'
            if item.husband_id == id and item.married > death:
                print("ERROR: FAMILY: US05: %s: Marriage %s after Husband's death %s" %(item.id,item.married,death))
                res = "ERROR: FAMILY: US05: %s: Marriage %s after Husband's death %s" % (item.id, item.married, death)
            if item.wife_id == id and item.married < death:
                print('Marriage before death')
                res='Marriage before death'
            if item.wife_id == id and item.married > death:
                print("ERROR: FAMILY: US05: %s: Marriage %s after Wife's death %s" %(item.id,item.married,death))
                res = "ERROR: FAMILY: US05: %s: Marriage %s after Wife's death %s" %(item.id,item.married,death)
    return res


def user_story_07(test_ind_list):
    res = None
    for i in test_ind_list:
        id = i.id
        if i.age > 150:
            print("ERROR: INDIVIDUAL: US07: %s: More than 150 years old - Birth date %s " %(id,i.birthday))
            res = "ERROR: INDIVIDUAL: US07: %s: More than 150 years old - Birth date %s " %(id,i.birthday)
        if i.age<150:
            print('Less than 150 years old')
            res = 'Less than 150 years old'
    return res

# Author Yiming Xu
def user_story_08(test_ind_list,test_fam_list):
    res = None
    for i in test_ind_list:
        id = i.id
        birth = i.birthday
        for item in test_fam_list:
            if id in item.children and item.married > birth:
                print('ANOMALY: FAMILY: US08: %s: Child %s born before marriage on %s' %(item.ID,id,item.married))
                res = 'ANOMALY: FAMILY: US08: %s: Child %s born before marriage on %s' %(item.ID,id,item.married)
            if id in item.children and item.married < birth:
                print('Birth before marriage of parents')
                res = 'Birth before marriage of parents'
    return res

user_story_08(ind_list,fam_list)

