$(document).ready(function() {
    $("#query-course-title").keyup(function() {
        var query_title;
        query_title = $(this).val();
        var query_dept;
        query_dept = $("#query-course-deptcode").val();
        $.get('/ej/course_search/', {search_coursetitle: query_title, search_departmentcode: query_dept}, function(data) {
            $("#course-suggestions").html(data);
        });
    });

    $("#query-course-deptcode").keyup(function() {
        var query_title;
        query_title = $("#query-course-title").val();
        var query_dept;
        query_dept = $(this).val();
        $.get('/ej/course_search/', {search_coursetitle: query_title, search_departmentcode: query_dept}, function(data) {
            $("#course-suggestions").html(data);
        });
    });
});
