import iden
import unittest



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
            if item.husband_id == id and item.divorced == 'NA':
                print(s1)

            if item.wife_id == id and item.divorced == 'NA':
                print(s1)

            if item.husband_id == id and item.married < death:
                print(s1)
                res1 = 'Marriage before death'
            if item.husband_id == id and item.married > death:
                print("ERROR: FAMILY: US05: %s: Marriage %s after Husband's death %s" %(item.id,item.married,death))
                res0 = "ERROR: FAMILY: US05: %s: Marriage %s after Husband's death %s" % (item.id, item.married, death)
                res.append(item.husband_id)
                res_error.append(res0)
            if item.wife_id == id and item.married < death:
                print(s1)

            if item.wife_id == id and item.married > death:
                print("ERROR: FAMILY: US05: %s: Marriage %s after Wife's death %s" %(item.id,item.married,death))
                res0 = "ERROR: FAMILY: US05: %s: Marriage %s after Wife's death %s" %(item.id,item.married,death)
                res.append(s1)
                res_error.append(res0)
    return res,res_error

## Author Yiming Xu and Mo Sun
## Pair Programming
def user_story_6(test_ind_list,test_fam_list):
    s1 = 'Divorce before death'
    res = []
    res_error=[]
    for i in test_ind_list:
        id = i.id
        death = i.death
        for item in test_fam_list:
            if item.husband_id == id and item.divorced == 'NA':
                print(s1)
            if item.wife_id == id and item.divorced == 'NA':
                print(s1)
            if item.husband_id == id and item.divorced < death:
                print(s1)
            if item.husband_id == id and item.divorced > death:
                print("ERROR: FAMILY: US05: %s: Divorce %s after Husband's death %s" %(item.id,item.divorce,death))
                res2 = "ERROR: FAMILY: US05: %s: Divorce %s after Husband's death %s" % (item.id, item.divorce, death)
                res.append(item.husband_id)
                res_error.append(res2)
            if item.wife_id == id and item.divorced < death:
                print(s1)
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
        if i.age<150:
            print('Less than 150 years old')
            res1 = 'Less than 150 years old'
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
                print('ANOMALY: FAMILY: US08: %s: Child %s born before marriage on %s' %(item.ID,id,item.married))
                res0 = 'ANOMALY: FAMILY: US08: %s: Child %s born before marriage on %s' %(item.ID,id,item.married)
                res_error.append(res0)
                res.append(item.id)
            if id in item.children and item.married < birth:
                print('Birth before marriage of parents')
    return res,res_error

# user_story_08(ind_list,fam_list)



if __name__ == '__main__':
    ind_list = iden.read_ind_info('project03.ged')
    ind_table = iden.create_ind_table(ind_list)
    fam_list = iden.read_fam_info('project03.ged')
    fam_table = iden.creat_fam_table(fam_list)

    # print(user_story_5(ind_list,fam_list))
    with open('output.txt', 'a') as file:
        file.write(str(ind_table))
        file.write('\n')
        file.write(str(fam_table))
        file.write('\n')
        res_error_4 = us_04(fam_list)[1]
        for i in res_error_4:

            file.write(str(i)+'\n')
        res_error_5 = user_story_5(ind_list,fam_list)[1]
        for i in res_error_5:
            file.write(str(i)+'\n')
        res_error_6 = user_story_6(ind_list,fam_list)[1]
        for i in res_error_6:
            file.write(str(i)+'\n')
        res_error_7 = user_story_7(ind_list)[1]
        for i in res_error_7:
            file.write(str(i)+'\n')
        res_error_8 = user_story_8(ind_list,fam_list)[1]
        for i in res_error_8:
            file.write(str(i)+'\n')
