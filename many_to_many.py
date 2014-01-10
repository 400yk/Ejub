# This file builds the many-to-many relationship between SkillsList, JobsList as well as CoursesList, JobsList

from ej.models import SkillsList, CoursesList, JobsList


def add_foreign_key(course, c_info):
    for skill in skills:
        skill_name = skill.skill.lower()

       # The skill keyword from SkillsList appears in 
        # the description or title field in course
        '''
        To correctly pick out the matched skills, require that both characters 
        surrounding the skill_name have to be non-alphabetic. i.g. " accounting,"
        For example, "C" in "...people. Consider that" does not
        count. 
        '''
        pos = c_info.find(skill_name)
        pos_end = pos + len(skill_name)
        if pos != -1:
            # Special case: if the skill_name is the first or the last word in c_info
            if pos == 0:
                # Note: c_info[pos_end] is the next character after the matched skill_name
                # pos_end + 1 == len(c_info) means c_info[pos_end] is the last character
                if pos_end + 1 <= len(c_info) and not c_info[pos_end].isalpha():
                    course.skillsLists.add(skill)
                    c_info = c_info.replace(skill_name, ' ')
                # In this case the c_info only contains that skill
                elif pos_end + 1 > len(c_info): 
                    course.skillsLists.add(skill)
                    c_info = c_info.replace(skill_name, ' ')

            elif pos_end == len(c_info):
                if pos >= 1 and not c_info[pos-1].isalpha():
                    course.skillsLists.add(skill)
                    c_info = c_info.replace(skill_name, ' ')

            # The general case, skill_name is somewhere in the middle of c_info
            else:
                if not c_info[pos-1].isalpha() and not c_info[pos_end].isalpha():
                    course.skillsLists.add(skill)
                    c_info = c_info.replace(skill_name, ' ')


if __name__ == '__main__':
    skills = SkillsList.objects.all()
    # Sort the list of skill by the length, and we take the longer one as the matched
    # skill instead of the short one if there's any. For example, take "project management" 
    # instead of "management"
    skills = sorted(skills, key = lambda x: len(x.skill), reverse = True)

    for course in CoursesList.objects.all():
        # Here we ignore the case
        c_info = course.coursetitle.lower()
        c_des = course.coursedescription.lower()
        # In case some course doesn't have a description, on the other hand every course
        # should have a title 
        if c_des:
            c_info += " "
            c_info += c_des

        add_foreign_key(course, c_info)


    for job in JobsList.objects.all():
        j_info = job.skills.lower()
        add_foreign_key(job, j_info)
