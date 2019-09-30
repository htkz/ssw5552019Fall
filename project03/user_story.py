import iden
import unittest
ind_list = iden.read_ind_info('project03.ged')

fam_list = iden.read_fam_info('project03.ged')


def user_story_5(test_ind_list,test_fam_list):
    for i in test_ind_list:
        id = i.id
        death = i.death
        for item in test_fam_list:
            if item.husband_id == id and item.married < death:
                print('Marriage before death')
            if item.husband_id == id and item.married > death:
                print("ERROR: FAMILY: US05: %s: Marriage %s after Husband's death %s" %(id,item.married,death))
            if item.wife_id == id and item.married < death:
                print('Marriage before death')
            if item.wife_id == id and item.married > death:
                print("ERROR: FAMILY: US05: %s: Marriage %s after Wife's death %s" %(id,item.married,death))

user_story_5(ind_list,fam_list)

