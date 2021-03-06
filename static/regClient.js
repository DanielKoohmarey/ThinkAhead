/* 
Adds/delete CourseForms to CourseFormSet when #addForm or #deleteForm is clicked.
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
            $(this).autocomplete({
                source: "/autocompleteCourse/",
                minLength: 2,
                change: function(event,ui) {
                    if (ui.item==null) {
                        $(this).val('');
                        $(this).focus();
                    }
                }
            });
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


// Checks all forms for non-empty and valid options selected.
function checkEmail() {
    var emailVal = $("#id_email").val()
    if (emailVal == '') {
        return false;
    } else {
        return true;
    }
}

function checkGradDate() {
    var semesterVal = $("#id_semester").val();
    var yearVal = $("#id_year").val();
    
    var now = new Date();
    var month = now.getMonth()+1;
    var year = now.getFullYear();
    
    // Check if current year is selected as GradDate that semester hasn't passed yet
    if (year == parseInt(yearVal)) {
        if (semesterVal == 'Spring') {
            // Current month needs to be in Spring
            if (month >= 1 && month <= 5) {
                return true;
            } else {
                return false;
            }
        } else if (semesterVal == 'Summer') {
            // Current month needs to be in Spring or Summer
            if (month >= 1 && month <= 8) {
                return true;
            } else {
                return false;
            }
        } else{
            return true;
        }
        return false;
    } else {
        return true;
    }
}

function checkMajor() {
    var collegeVal = $("#id_college").val();
    var majorVal = $("#id_major").val();
    if (collegeVal == 0 || collegeVal == -1) {
        return false;
    } else if (majorVal == 0 || majorVal == -1) {
        return false;
    } else {
        return true;
    }
}

function validateProfile() {
    var errors = [];
    if (!checkEmail()) {
        //return false;
        errors.push('Please submit a valid email.');
    }
    if (!checkGradDate()) {
        errors.push("Please select an intended graduation date that hasn't passed.")
        //return false;
    }
    if (!checkMajor()) {
        //return false;
        errors.push("Please select a college and major.")
    }
    //return true;
    return errors;
}


$(document).ready(function(){

// On form submit, validate forms and cancel submission if validation fails
$("form").submit(function(event) {
    var valid = validateProfile();
    if (valid.length == 0) {
        return;
    }
    var message = 'Please correct the following:';
    for (var i = 0; i < valid.length; i++) {
        message += '\n- ';
        message += valid[i];
    }
    alert(message);
    return false;
});

// Update/check TOTAL_FORMS
var formCount = $('.addCourseForm').length; // Get all the forms
$("#id_form-TOTAL_FORMS").val(formCount);


// Listener hooking cloneMore() to #addMore to add additional forms.
$('#addForm').click(function() {
    addForm('div.addCourseForm:nth-last-child(2)', 'form');
});

$('[id=deleteForm]').each(function(i) {
    $(this).click(function() {
        deleteForm(this, 'form');
    })
});

// Binds any existing CourseForms to have autocomplete
var id;
for (var i = 0; i < formCount; i++) {
    id = '#id_form-' + i.toString() + '-name';
    $(id).autocomplete({
        source: "/autocompleteCourse/",
        minLength: 2,
        change: function(event,ui) {
            if (ui.item==null) {
                $(this).val('');
                $(this).focus();
            }
        }
    });
}


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

if (undefined != selectCollege && undefined != selectMajor) {
    $("#id_college").val(selectCollege).change();
    $("#id_major").val(selectMajor);
}

});