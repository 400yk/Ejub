$(document).ready(function() {
    var course_id;
    course_id = $("#div-course-detail").attr('course_id');
    $.get('/ej/quick_ref_course_detail/', {course_id: course_id}, function(data) {
        $("#quick-ref").html(data);

        $(".quick_ref_related_jobs").mouseenter(function() {
            $(".quick_ref_related_jobs").removeClass('hovered_skills');
            $(this).addClass('hovered_skills');
        });

        $(".quick_ref_related_jobs").mouseleave(function() {
            $(".quick_ref_related_jobs").removeClass('hovered_skills');
        });

        $(".quick_ref_related_jobs").click(function() {
            var field;
            field = $(this).attr("view-by");
            var course_id;
            course_id = $(this).attr("course-id");
            var the_field_set = [];
            var sub_field_set = [];
            $(".related_jobs_filter_select").each(function() {
                the_field_set.push($(this).attr('thefield'));
                sub_field_set.push($(this).attr('subfield'));
            });
            $.get('/ej/get_jobs/', {field: field, course_id: course_id, the_field_set: the_field_set, sub_field_set: sub_field_set}, function(data) {
                $("#quick-ref-related-jobs").html(data);
            });
        });
   });
});
