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

});

