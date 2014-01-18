$(document).ready(function() {

    // In case user use back button, it should check the input and search automatically
    var query_title = $("#query-course-title").val();
    var query_dept = $("#query-course-deptcode").val();
    var query_uid = $("#query-course-uid").val();
    if (query_title != null && query_dept != null && query_uid != null) {
        if (query_title != "" || query_dept != "" || query_uid != "") {
    $.get('/ej/course_search/', {search_coursetitle: query_title, search_departmentcode: query_dept, search_courseuid: query_uid}, function(data) {
        $("#course-suggestions").html(data);
    });
        } else {
            $("#course-suggestions").html("Suggested courses");
        }
    }

$("#query-course-title").keyup(function() {
    var query_title;
    query_title = $(this).val();
    var query_dept;
    query_dept = $("#query-course-deptcode").val();
    var query_uid;
    query_uid = $("#query-course-uid").val();
    if (query_title != "" || query_dept != "" || query_uid != "") {
        $.get('/ej/course_search/', {search_coursetitle: query_title, search_departmentcode: query_dept, search_courseuid: query_uid}, function(data) {
            $("#course-suggestions").html(data);
        });
    } else {
        $("#course-suggestions").html("Suggested courses");
    }
});

$("#query-course-deptcode").keyup(function() {
    var query_title;
    query_title = $("#query-course-title").val();
    var query_dept;
    query_dept = $(this).val();
    var query_uid;
    query_uid = $("#query-course-uid").val();
    if (query_title != "" || query_dept != "" || query_uid != "") {
        $.get('/ej/course_search/', {search_coursetitle: query_title, search_departmentcode: query_dept, search_courseuid: query_uid}, function(data) {
            $("#course-suggestions").html(data);
        });
    } else {
        $("#course-suggestions").html("Suggested courses");
    }
});

$("#query-course-uid").keyup(function() {
    var query_title;
    query_title = $("#query-course-title").val();
    var query_dept;
    query_dept = $("#query-course-deptcode").val();
    var query_uid;
    query_uid = $(this).val();
    if (query_title != "" || query_dept != "" || query_uid != "") {
        $.get('/ej/course_search/', {search_coursetitle: query_title, search_departmentcode: query_dept, search_courseuid: query_uid}, function(data) {
            $("#course-suggestions").html(data);
        });
    } else {
        $("#course-suggestions").html("Suggested courses");
    }
});

var job_query_title = $("#query-job-title").val();
var job_query_company = $("#query-job-company").val();
var job_query_country = $("#query-job-country").val();
var job_query_city = $("#query-job-city").val();
if (job_query_title != null && job_query_company != null && job_query_country != null && job_query_city != null) {
if (job_query_title != "" || job_query_company != "" || job_query_country != "" || job_query_city != "") {

    $.get('/ej/job_search/', {search_title: job_query_title, search_company: job_query_company, search_country: job_query_country, search_city: job_query_city}, function(data) {
        $("#job-suggestions").html(data);
    });

} else {
    $("#job-suggestions").html("Suggested jobs");
}
}

$("#query-job-title").keyup(function() {
    var query_title;
    query_title = $(this).val();
    var query_company;
    query_company = $("#query-job-company").val();
    var query_country;
    query_country = $("#query-job-country").val();
    var query_city;
    query_city = $("#query-job-city").val();
    if (query_title != "" || query_company != "" || query_country != "" || query_city != "" ) {
        $.get('/ej/job_search/', {search_title: query_title, search_company: query_company, search_country: query_country, search_city: query_city}, function(data) {
            $("#job-suggestions").html(data);
        });
    } else {
        $("#job-suggestions").html("Suggested jobs");
    }
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
    if (query_title != "" || query_company != "" || query_country != "" || query_city != "" ) {

        $.get('/ej/job_search/', {search_title: query_title, search_company: query_company, search_country: query_country, search_city: query_city}, function(data) {
            $("#job-suggestions").html(data);
        });
    } else {
        $("#job-suggestions").html("Suggested jobs");
    }
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
    if (query_title != "" || query_company != "" || query_country != "" || query_city != "" ) {

        $.get('/ej/job_search/', {search_title: query_title, search_company: query_company, search_country: query_country, search_city: query_city}, function(data) {
            $("#job-suggestions").html(data);
        });
    } else {
        $("#job-suggestions").html("Suggested jobs");
    }
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
    if (query_title != "" || query_company != "" || query_country != "" || query_city != "" ) {

        $.get('/ej/job_search/', {search_title: query_title, search_company: query_company, search_country: query_country, search_city: query_city}, function(data) {
            $("#job-suggestions").html(data);
        });
    } else {
        $("#job-suggestions").html("Suggested jobs");
    }
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

