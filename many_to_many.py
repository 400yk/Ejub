# This file builds the many-to-many relationship between SkillsList, JobsList as well as CoursesList, JobsList

from ej.models import SkillsList, CoursesList, JobsList

if __name__ == '__main__':
    skills = SkillsList.objects.filter(pk__gt = 8505)

    for skill in skills:
        for course in CoursesList.objects.all():
            # The skill keyword from SkillsList appears in 
            # the description or title field in course
            if skill.skill in course.coursetitle or skill.skill in course.coursedescription:
               course.skillsLists.add(skill)


        for job in JobsList.objects.all():
            if skill.skill in job.skills:
                job.skillsLists.add(skill)


