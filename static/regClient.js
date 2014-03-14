/*
Adds additional CourseForms to CourseFormSet when #addMore is clicked.
http://stackoverflow.com/questions/501719/dynamically-adding-a-form-to-a-django-formset-with-ajax
*/
function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}

// Function to prepare possible dropdown options for MajorForm using var majorDict
function getDropdownOptions(){
    for (var key in majorDict) {
        colleges[key] = key;
        
        var majors = majorDict[key];
        var majorsTemp = {};
        for (var i = 0; i < majors.length; i++) {
            var majorName = majors[i];
            majorsTemp[majorName] = majorName;
        }
        majorsAll[key] = majorsTemp;
    };
}


$(document).ready(function(){

// Listener hooking cloneMore() to #addMore to add additional forms.
$('#addMore').click(function() {
        cloneMore('div.addCourseForm:last', 'form');

});

// Populates MajorForm.college dropdown with all colleges in DB
$.each(colleges, function(val, text) {
    $('#id_college').append(
        $('<option></option>').val(val).html(text)
    );
});


/*
Dynamically change MajorForm.major dropdown depending on MajorForm.college selection
http://stackoverflow.com/questions/16707850/3-dropdown-populate-based-on-selection-in-another-cascading-dropdown
*/
$('#id_college').change(function() {
    var firstkey = $(this).val();
    $('#id_major').empty();

    $('#id_major').append($("<option>").
        attr("value", -1).
        text('Please select a college and major')); 

    for (var prop in majorsAll[firstkey]) {
        var second = prop;
        $('#id_major').append($("<option>"). // Add options
        attr("value", second).
        text(second));
    }
    $('#id_major').change();
}).change(); 
