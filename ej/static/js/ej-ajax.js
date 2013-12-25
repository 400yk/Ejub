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


});

