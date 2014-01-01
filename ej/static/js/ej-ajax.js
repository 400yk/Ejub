$(document).ready(function() {
    $("#query-course-title").keyup(function() {
        var query_title;
        query_title = $(this).val();
        var query_dept;
        query_dept = $("#query-course-deptcode").val();
        var query_uid;
        query_uid = $("#query-course-uid").val();
        $.get('/ej/course_search/', {search_coursetitle: query_title, search_departmentcode: query_dept, search_courseuid: query_uid}, function(data) {
            $("#course-suggestions").html(data);
        });
    });

    $("#query-course-deptcode").keyup(function() {
        var query_title;
        query_title = $("#query-course-title").val();
        var query_dept;
        query_dept = $(this).val();
        var query_uid;
        query_uid = $("#query-course-uid").val();
        $.get('/ej/course_search/', {search_coursetitle: query_title, search_departmentcode: query_dept, search_courseuid: query_uid}, function(data) {
            $("#course-suggestions").html(data);
        });
    });

    $("#query-course-uid").keyup(function() {
        var query_title;
        query_title = $("#query-course-title").val();
        var query_dept;
        query_dept = $("#query-course-deptcode").val();
        var query_uid;
        query_uid = $(this).val();
        $.get('/ej/course_search/', {search_coursetitle: query_title, search_departmentcode: query_dept, search_courseuid: query_uid}, function(data) {
            $("#course-suggestions").html(data);
        });
    });

    $("#query-job-title").keyup(function() {
        var query_title;
        query_title = $(this).val();
        var query_company;
        query_company = $("#query-job-company").val();
        var query_country;
        query_country = $("#query-job-country").val();
        var query_city;
        query_city = $("#query-job-city").val();

        $.get('/ej/job_search/', {search_title: query_title, search_company: query_company, search_country: query_country, search_city: query_city}, function(data) {
            $("#job-suggestions").html(data);
        });
    });

    $("#query-job-company").keyup(function() {
        var query_title;
        query_title = $("#query-job-title").val();
        var query_company;
        query_company = $(this).val();
        var query_country;
        query_country = $("#query-job-country").val();
        var query_city;
        query_city = $("#query-job-city").val();

        $.get('/ej/job_search/', {search_title: query_title, search_company: query_company, search_country: query_country, search_city: query_city}, function(data) {
            $("#job-suggestions").html(data);
        });
    });

    $("#query-job-country").keyup(function() {
        var query_title;
        query_title = $("#query-job-title").val();
        var query_company;
        query_company = $("#query-job-company").val();
        var query_country;
        query_country = $(this).val();
        var query_city;
        query_city = $("#query-job-city").val();

        $.get('/ej/job_search/', {search_title: query_title, search_company: query_company, search_country: query_country, search_city: query_city}, function(data) {
            $("#job-suggestions").html(data);
        });
    });

    $("#query-job-city").keyup(function() {
        var query_title;
        query_title = $("#query-job-title").val();
        var query_company;
        query_company = $("#query-job-company").val();
        var query_country;
        query_country = $("#query-job-country").val();
        var query_city;
        query_city = $(this).val();

        $.get('/ej/job_search/', {search_title: query_title, search_company: query_company, search_country: query_country, search_city: query_city}, function(data) {
            $("#job-suggestions").html(data);
        });
    });

    // Hover over a skill will show the classes that trains it
    $(".job-required-skills").mouseenter(function() {
        $(".job-required-skills").removeClass('hovered_skills');
        $(this).addClass('hovered_skills');
    });

    $(".job-required-skills").mouseleave(function() {
        $(".job-required-skills").removeClass('hovered_skills');
    });
    
    var all_required_skills;

    $("li.job-required-skills").click(function() {
        $.get('/ej/from_skill_find_courses/', {skill_id: $(this).attr('skill_id')}, function(data) { 
            // Save the html to variable 
            if (all_required_skills == null) { 
                all_required_skills = $("#job-related-courses").html();
            };
            $("#job-related-courses").html(data);
        });
    });

    $("h4.job-required-skills").click(function() {
        if (all_required_skills !== null) {
            $("#job-related-courses").html(all_required_skills);
            all_required_skills = null;
        };
    });

});

