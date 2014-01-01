$(document).ready(function() {
    $(".related-jobs-filter").mouseenter(function() {
        $(".related-jobs-filter").removeClass('hovered_skills');
        $(this).addClass('hovered_skills');
    });

    $(".related-jobs-filter").mouseleave(function() {
        $(".related-jobs-filter").removeClass('hovered_skills');
    });

    $(".related-jobs-filter").click(function() {
        var sub_field = $(this).attr("sub-field");
        var course_id = $(this).attr("course-id");
        var the_field = $(this).attr("the-field");

        $("#quick-ref-related-jobs").html("");
        // If sub_field is "Other": let user input the sub-field

        // Show the selected filter 
        $("#selected-filter-"+the_field).html(the_field+": "+sub_field);
        document.getElementById("selected-filter-"+the_field).style.display = 'block';
        $("#selected-filter-"+the_field).addClass('related_jobs_filter_select');
        // Add sub_field attr to the li
        $("#selected-filter-"+the_field).attr('subfield', sub_field);
        var the_field_set = [];
        var sub_field_set = [];
        $(".related_jobs_filter_select").each(function() {
            the_field_set.push($(this).attr('thefield'));
            sub_field_set.push($(this).attr('subfield'));
        });

        $.get('/ej/filter_jobs/', {sub_field_set: sub_field_set, the_field_set: the_field_set, course_id: course_id}, function(data) {
            $("#course-related-jobs").html(data);
        });
    });

    // Clicked on selected filter to cancel the filter
    $(".selected-related-jobs-filter").click(function() {
        $(this).removeClass('related_jobs_filter_select');
        $(this).removeAttr('subfield');
        var the_field = $(this).attr('thefield');
        var course_id = $(this).attr('course-id');
        document.getElementById("selected-filter-"+the_field).style.display = 'none';
        var the_field_set = [];
        var sub_field_set = [];
        $(".related_jobs_filter_select").each(function() {
            the_field_set.push($(this).attr('thefield'));
            sub_field_set.push($(this).attr('subfield'));
        });

        $.get('/ej/filter_jobs/', {sub_field_set: sub_field_set, the_field_set: the_field_set, course_id: course_id}, function(data) {
            $("#course-related-jobs").html(data);
        });
    });
});
