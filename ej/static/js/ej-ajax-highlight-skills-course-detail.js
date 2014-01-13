$(document).ready(function() {
    $(".related-jobs-list").mouseenter(function() {
        var job_id = $(this).attr('jobid');
        $(".course-detail-each-skill").removeClass('hovered_skills');
        $.getJSON('/ej/from_job_get_skill.json',{job_id: job_id}, function(data) {
            var skills_id = data.skills_id;
            var other_skills_id = skills_id;
            $(".course-detail-each-skill").each(function() {
                for (var i = 0; i < skills_id.length; i++) {
                    var the_skill = skills_id[i];
                    if ($(this).attr('skillid') == the_skill){
                        $(this).addClass('hovered_skills');
                        // Remove the matched skill from the other_skills_id
                        var index = other_skills_id.indexOf(the_skill)
                        if (index != -1) {
                            other_skills_id.splice(index, 1);
                        }
                        break; 
                    } 
                }
            });

                if (other_skills_id) {
                    $.get('/ej/get_other_skills_needed/', {other_skills_id: other_skills_id}, function(data) {
                        $("#other-skills-needed").html(data);
                    });
                }
        });
    });

    $(".related-jobs-list").mouseleave(function() {
        $(".course-detail-each-skill").removeClass('hovered_skills');
        $("#other-skills-needed").html("");
    });

})
