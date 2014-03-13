
/* Takes a dictionary to be JSON encoded, calls the success
   function with the diction decoded from the JSON response.*/
function json_request(page, dict, success, failure) {
    $.ajax({
        type: 'POST',
        url: page,
        data: JSON.stringify(dict),
        contentType: "application/json",
        dataType: "json",
        success: success,
        error: failure
    });
}

debug_flag = false;

ERR_BAD_CREDENTIALS = (-1);
ERR_USER_EXISTS = (-2);
ERR_BAD_USERNAME = (-3);
ERR_BAD_PASSWORD  = -4;



function get_message_for_errcode(code) {
    /* "Invalid username and password combination. Please try again. " (ERR_BAD_CREDENTIALS)
       "The user name should not be empty. Please try again." (ERR_BAD_USERNAME)
       "This user name already exists. Please try again." (ERR_USER_EXISTS)
    */

    if( code == ERR_BAD_CREDENTIALS) {
        return ("Invalid username and password combination. Please try again. ");
    } else if( code == ERR_BAD_USERNAME) {
        return ("The user name should not be empty and at most 128 characters long. Please try again.");
    } else if( code == ERR_USER_EXISTS) {
        return ("This user name already exists. Please try again.");
    } else if( code == ERR_BAD_PASSWORD) {
        return ("The password should be at most 128 characters long. Please try again");
    } else {
        // This case should never happen!
        if( debug_flag ) { alert('Illegal error code encountered: ' + code); }
        return ("Unknown error occured: " + code);
   }
}
