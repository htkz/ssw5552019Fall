from iden import *
from user_story import *


if __name__ == '__main__':
    ind_list = read_ind_info('project.ged')
    ind_table = create_ind_table(ind_list)
    print(ind_table)

    fam_list = read_fam_info('project.ged')
    fam_table = creat_fam_table(fam_list)
    print(fam_table)

    ind_list = iden.read_ind_info('project.ged')
    ind_table = iden.create_ind_table(ind_list)
    fam_list = iden.read_fam_info('project.ged')
    fam_table = iden.creat_fam_table(fam_list)

    with open('output.txt', 'w') as file:
        file.write(str(ind_table))
        file.write('\n')
        file.write(str(fam_table))
        file.write('\n')


        def writedowm(res_error):
            for i in res_error:
                file.write(str(i) + '\n')


        writedowm(user_story_01(ind_list, fam_list)[1])
        writedowm(us_02(ind_list, fam_list)[1])
        writedowm(us_03(ind_list)[1])
        writedowm(us_04(fam_list)[1])
        writedowm(user_story_5(ind_list, fam_list)[1])
        writedowm(user_story_6(ind_list, fam_list)[1])
        writedowm(user_story_7(ind_list)[1])
        writedowm(user_story_8(ind_list, fam_list)[1])
        writedowm(user_story_9(ind_list)[1])
        writedowm(user_story_10(ind_list, fam_list)[1])
        writedowm(user_story_11(ind_list, fam_list)[1])
        writedowm(user_story_12(ind_list)[1])
        writedowm(user_story_13(ind_list, fam_list)[1])
        writedowm(user_story_14(ind_list, fam_list)[1])
        writedowm(user_story_15(fam_list)[1])
        writedowm(user_story_16(ind_list, fam_list)[1])
        writedowm(user_story_17(fam_list)[1])
        writedowm(user_story_18(fam_list)[1])
        writedowm(user_story_19(ind_list, fam_list)[1])
        writedowm(user_story_20(fam_list)[1])
        writedowm(user_story_21(ind_list, fam_list)[1])
        writedowm(user_story_22(ind_list, fam_list)[1])
        writedowm(user_story_23(ind_list)[1])
        writedowm(user_story_24(fam_list)[1])
        writedowm(user_story_25(ind_list, fam_list)[1])
        writedowm(user_story_29(ind_list)[1])
        writedowm(user_story_30(ind_list, fam_list)[1])
        writedowm(user_story_31(ind_list, fam_list)[1])
        writedowm(user_story_32(ind_list)[1])
        writedowm(user_story_33(ind_list, fam_list)[1])
        writedowm(user_story_35(ind_list)[1])
        writedowm(user_story_36(ind_list)[1])