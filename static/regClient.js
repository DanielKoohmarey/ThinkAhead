/* 
Adds/delete CourseForms to CourseFormSet when #addForm or #deleteForm is clicked.
BUG: If page is refreshed, form indices do not reset
Adapted from:
http://stellarchariot.com/blog/2011/02/dynamically-add-form-to-formset-using-javascript-and-django/
*/
function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+-)');
    var replacement = prefix + '-' + ndx + '-';
    if ($(el).attr("for")) {
        $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    }
    if (el.id) {
        el.id = el.id.replace(id_regex, replacement);
    }
    if (el.name) {
        el.name = el.name.replace(id_regex, replacement);
    }
}

function deleteForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (formCount > 1) {
        // Delete the item/form
        $(btn).parents('.addCourseForm').remove();
        var forms = $('.addCourseForm'); // Get all the forms  
        // Update the total number of forms (1 less than before)
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        var i = 0;
        // Go through the forms and set their indices, names and IDs
        for (formCount = forms.length; i < formCount; i++) {
            $(forms.get(i)).children().each(function () {
                if ($(this).attr('type') == 'text') {updateElementIndex(this, prefix, i);
                }
            });
        }
    }
    else {
        alert("You have to enter at least one course!");
    }
    return false;
}

function addForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());

    // Clone a form (without event handlers) from the last form
    var row = $(btn).clone(false);
    // Insert it after the last form
    $(row).removeAttr('id').hide().insertAfter(".addCourseForm:last").slideDown(300);

    // Remove the bits we don't want in the new row/form
    // e.g. error messages
    $(".errorlist", row).remove();
    $(row).children().removeClass("error");

    // Relabel or rename all the relevant bits
    $(row).children().each(function () {
        updateElementIndex(this, prefix, formCount);
        //$(this).val("");
        if ($(this).attr('id') == 'deleteForm') {
            $(this).val("Delete");
        } else {
            $(this).val("");
        }
    });

    // Add an event handler for the delete item/form link 
    $(row).find(".buttonLink").click(function () {
        return deleteForm(this, prefix);
    });
    // Update the total form count
    var forms = $('.addCourseForm'); // Get all the forms
    $("#id_" + prefix + "-TOTAL_FORMS").val(forms.length);
    return false;
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

// Update/check TOTAL_FORMS
var formCount = $('.addCourseForm').length; // Get all the forms
$("#id_form-TOTAL_FORMS").val(formCount);


// Listener hooking cloneMore() to #addMore to add additional forms.
$('#addForm').click(function() {
    addForm('div.addCourseForm:nth-last-child(2)', 'form');
});

$('#deleteForm').click(function() {
    deleteForm(this, 'form');
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

});