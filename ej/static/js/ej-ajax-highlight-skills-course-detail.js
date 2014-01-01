$(document).ready(function() {
    $(".related-jobs-list").mouseenter(function() {
        var job_id = $(this).attr('jobid');
        $(".course-detail-each-skill").removeClass('hovered_skills');
        $.getJSON('/ej/from_job_get_skill.json',{job_id: job_id}, function(data) {
            var skills_id = data.skills_id;
            $(".course-detail-each-skill").each(function() {
                for (var i = 0; i < skills_id.length; i++) {
                    if ($(this).attr('skillid') == skills_id[i]) {
                        $(this).addClass('hovered_skills');
                        break;
                    }
                }
            });
        });
    });

    $(".related-jobs-list").mouseleave(function() {
        $(".course-detail-each-skill").removeClass('hovered_skills');
    });

})
